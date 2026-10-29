#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Gera o mapa de conceitos da base de conhecimento a partir dos metadados das notas.

Cada nota em docs/wiki/<domínio>/<id>.md declara, no front matter YAML, seu tipo,
domínio, resumo, ligações tipadas e chaves bibliográficas. Este script valida esses
metadados e escreve docs/wiki/concept-map.md (diagrama Mermaid + índice).

Uso:
    python docs/assets/src/render_concept_map.py            # regenera o mapa
    python docs/assets/src/render_concept_map.py --check    # falha se o mapa estiver desatualizado
    python docs/assets/src/render_concept_map.py --strict   # avisos também falham

Dependência: PyYAML.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
WIKI = ROOT / "docs" / "wiki"
BIB = ROOT / "docs" / "bibliography.bib"
OUT = WIKI / "concept-map.md"

DOMAINS = {
    "foundations": "Fundamentos",
    "experimentation": "Experimentação",
    "data-and-evidence": "Dados e evidência",
    "intelligence": "Inteligência e autonomia",
    "networking": "Redes",
    "security": "Segurança",
}

# Tipo da nota -> (abertura, fechamento) da forma Mermaid e rótulo da legenda.
TYPES = {
    "overview": ("(", ")", "Panorama de um domínio"),
    "concept": ("[", "]", "Conceito"),
    "method": ("([", "])", "Método"),
    "technology": ("[[", "]]", "Tecnologia"),
}

# Tipo de ligação -> (seta Mermaid, rótulo, simétrica, leitura na legenda).
LINKS = {
    "depends_on": ("-->", "pressupõe", False, "A pressupõe B: compreender A exige B."),
    "part_of": ("-->", "parte de", False, "A é componente de B."),
    "specializes": ("-->", "é um tipo de", False, "A é caso particular de B."),
    "evaluates": ("==>", "avalia", False, "O método A é usado para avaliar B."),
    "alternative_to": ("<-->", "alternativa a", True, "A e B resolvem o mesmo problema por caminhos distintos."),
    "related": ("-.-", "relaciona-se", True, "Relação fraca, sem semântica adicional."),
}

REQUIRED = ("id", "title", "type", "domain", "summary")
MD_LINK = re.compile(r"\]\(([^)#\s]+\.md)(?:#[^)]*)?\)")


def read_front_matter(path: Path) -> tuple[dict | None, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text
    return yaml.safe_load(text[4:end]) or {}, text[end + 5:]


def bib_keys() -> set[str]:
    return set(re.findall(r"^@\w+\{([^,\s]+),", BIB.read_text(encoding="utf-8"), re.M))


def load_notes(errors: list[str]) -> dict[str, dict]:
    notes: dict[str, dict] = {}
    for path in sorted(WIKI.glob("*/*.md")):
        rel = path.relative_to(ROOT).as_posix()
        meta, body = read_front_matter(path)
        if meta is None:
            errors.append(f"{rel}: sem front matter")
            continue
        missing = [k for k in REQUIRED if not meta.get(k)]
        if missing:
            errors.append(f"{rel}: campos obrigatórios ausentes: {', '.join(missing)}")
            continue
        if meta["id"] != path.stem:
            errors.append(f"{rel}: id '{meta['id']}' difere do nome do arquivo")
        if meta["domain"] != path.parent.name:
            errors.append(f"{rel}: domínio '{meta['domain']}' difere da pasta")
        if meta["domain"] not in DOMAINS:
            errors.append(f"{rel}: domínio '{meta['domain']}' não registrado em DOMAINS")
        if meta["type"] not in TYPES:
            errors.append(f"{rel}: tipo '{meta['type']}' fora do vocabulário {sorted(TYPES)}")
        if meta["id"] in notes:
            errors.append(f"{rel}: id duplicado '{meta['id']}'")
        meta["_path"], meta["_body"] = path, body
        notes[meta["id"]] = meta
    return notes


def validate(notes: dict[str, dict], errors: list[str], warnings: list[str]) -> list[tuple[str, str, str]]:
    keys = bib_keys()
    by_path = {n["_path"].resolve(): nid for nid, n in notes.items()}
    edges: set[tuple[str, str, str]] = set()
    declared: dict[str, set[str]] = {nid: set() for nid in notes}
    for nid, note in notes.items():
        rel = note["_path"].relative_to(ROOT).as_posix()
        for kind, targets in (note.get("links") or {}).items():
            if kind not in LINKS:
                errors.append(f"{rel}: tipo de ligação '{kind}' fora do vocabulário {sorted(LINKS)}")
                continue
            for target in targets or []:
                if target == nid:
                    errors.append(f"{rel}: ligação para si mesma ({kind})")
                elif target not in notes:
                    errors.append(f"{rel}: ligação {kind} para nota inexistente '{target}'")
                else:
                    declared[nid].add(target)
                    a, b = (nid, target) if not LINKS[kind][2] else tuple(sorted((nid, target)))
                    edges.add((a, kind, b))
        for key in note.get("references") or []:
            if key not in keys:
                warnings.append(f"{rel}: referência '{key}' ausente de docs/bibliography.bib")
    # Toda ligação declarada aparece no texto; um link no texto basta estar declarado
    # em qualquer sentido, para que a nota de destino possa apontar de volta.
    for nid, note in notes.items():
        rel = note["_path"].relative_to(ROOT).as_posix()
        in_body = {
            by_path[p]
            for m in MD_LINK.finditer(note["_body"])
            if (p := (note["_path"].parent / m.group(1)).resolve()) in by_path and by_path[p] != nid
        }
        for target in sorted(declared[nid] - in_body):
            warnings.append(f"{rel}: ligação para '{target}' declarada nos metadados, mas sem link no texto")
        for target in sorted(t for t in in_body - declared[nid] if nid not in declared[t]):
            warnings.append(f"{rel}: link no texto para '{target}' sem ligação tipada em nenhum sentido")
    return sorted(edges)


def node_ref(nid: str) -> str:
    return nid.replace("-", "_")


def label(text: str) -> str:
    return text.replace('"', "#quot;")


def render(notes: dict[str, dict], edges: list[tuple[str, str, str]]) -> str:
    out = [
        "<!-- Gerado por docs/assets/src/render_concept_map.py a partir dos metadados das notas. Não editar manualmente. -->",
        "# Mapa de conceitos",
        "",
        "> Grafo das notas da base de conhecimento e de suas ligações tipadas. O mapa é",
        "> derivado dos metadados de cada nota; para alterá-lo, edite a nota e regenere.",
        "",
        "```mermaid",
        "flowchart LR",
    ]
    for domain, title in DOMAINS.items():
        members = sorted(nid for nid, n in notes.items() if n["domain"] == domain)
        if not members:
            continue
        out.append(f'    subgraph {node_ref(domain)}["{label(title)}"]')
        for nid in members:
            opening, closing, _ = TYPES[notes[nid]["type"]]
            out.append(f'        {node_ref(nid)}{opening}"{label(notes[nid]["title"])}"{closing}')
        out.append("    end")
    for a, kind, b in edges:
        arrow, text, _, _ = LINKS[kind]
        out.append(f"    {node_ref(a)} {arrow}|{text}| {node_ref(b)}")
    out += ["```", "", "## Legenda", "", "| Forma | Tipo de nota |", "| --- | --- |"]
    shapes = {"overview": "contorno arredondado", "concept": "retângulo", "method": "cápsula", "technology": "retângulo de borda dupla"}
    out += [f"| {shapes[t]} | {TYPES[t][2]} |" for t in TYPES]
    out += ["", "| Ligação | Leitura |", "| --- | --- |"]
    out += [f"| `{k}` — {v[1]} | {v[3]} |" for k, v in LINKS.items()]
    out += ["", "## Índice", "", "| Nota | Tipo | Domínio | Resumo |", "| --- | --- | --- | --- |"]
    for domain, title in DOMAINS.items():
        for nid in sorted(nid for nid, n in notes.items() if n["domain"] == domain):
            n = notes[nid]
            summary = " ".join(str(n["summary"]).split())
            out.append(f"| [{n['title']}]({domain}/{nid}.md) | {TYPES[n['type']][2]} | {title} | {summary} |")
    return "\n".join(out) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="não escreve; falha se o mapa estiver desatualizado")
    parser.add_argument("--strict", action="store_true", help="trata avisos como erros")
    args = parser.parse_args()
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")

    errors: list[str] = []
    warnings: list[str] = []
    notes = load_notes(errors)
    edges = validate(notes, errors, warnings)
    for w in warnings:
        print(f"aviso: {w}", file=sys.stderr)
    for e in errors:
        print(f"erro: {e}", file=sys.stderr)
    if errors or (args.strict and warnings):
        return 1

    content = render(notes, edges)
    current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
    if args.check:
        if current != content:
            print(f"erro: {OUT.relative_to(ROOT).as_posix()} desatualizado; regenere o mapa", file=sys.stderr)
            return 1
        print(f"ok: {len(notes)} notas, {len(edges)} ligações")
        return 0
    OUT.write_text(content, encoding="utf-8", newline="\n")
    print(f"escrito {OUT.relative_to(ROOT).as_posix()}: {len(notes)} notas, {len(edges)} ligações, {len(warnings)} avisos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
