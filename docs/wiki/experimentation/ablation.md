---
id: ablation
title: "Ablação e atribuição de contribuição"
type: method
domain: experimentation
summary: "Ablação estima a contribuição de um componente substituindo-o por um substituto de referência declarado, mantidas as demais condições do experimento."
links:
  depends_on: [research-question-to-evidence]
  evaluates: [progressive-autonomy]
  related: [experimental-environments, observability-and-provenance]
references: [Meyes2019, LiptonSteinhardt2018, Montgomery2017]
---
# Ablação e atribuição de contribuição

> Ablação estima a contribuição de um componente substituindo-o por um substituto de
> referência declarado, mantidas as demais condições do experimento.

## Por que importa

Sistemas de automação e de inteligência artificial combinam vários componentes:
aquisição e qualificação de dados, predição, diagnóstico, planejamento, coordenação e
verificação. Quando o sistema completo supera uma linha de base, esse resultado não
indica qual componente produziu o ganho. Atribuir o desempenho ao componente mais
visível — um modelo aprendido, um agente adicional — sem isolar sua contribuição é uma
falha recorrente identificada na literatura de aprendizado de máquina (Lipton e
Steinhardt, 2018).

O termo provém da neurociência, em que a remoção de uma região permite inferir sua
função; a prática foi transposta para redes neurais artificiais e, de modo geral, para
sistemas compostos (Meyes *et al.*, 2019).

A ablação é uma **premissa metodológica**, não um objetivo de pesquisa. Ela é condição
para que uma alegação do tipo "o componente X melhora o resultado Y" seja testável, e
só é praticável quando o sistema foi projetado com componentes separáveis.

## Modelo conceitual

Seja $S$ um sistema composto pelos componentes $c_1, \dots, c_n$ e $M$ uma métrica de
desempenho medida sob um cenário fixo. A contribuição estimada do componente $c_i$ é

$$
\Delta_i = M(S) - M\big(S[c_i \leftarrow r_i]\big)
$$

em que $S[c_i \leftarrow r_i]$ denota o mesmo sistema com $c_i$ substituído por seu
**substituto de referência** $r_i$. As duas medições compartilham cenário, carga,
recursos e procedimento de medição; $\Delta_i$ tem a unidade de $M$.

| Elemento | Definição |
| --- | --- |
| Componente | Parte do sistema com interface definida, cuja contribuição se deseja estimar. |
| Substituto de referência | Implementação mínima e declarada que preserva a interface e mantém o sistema funcional: previsão por persistência no lugar de um modelo, sequência fixa no lugar de um planejador, decisões independentes no lugar da coordenação. |
| Configuração completa | Sistema com todos os componentes, ponto de partida das substituições. |
| Invariantes | Partes nunca removidas, como autorização, verificação de segurança e registro de auditoria. Removê-las para medir efeito alteraria o objeto de estudo e o risco do experimento. |

Remover sem substituir costuma produzir um sistema que falha ou deixa de responder; a
diferença medida, nesse caso, reflete a quebra da interface, não a contribuição do
componente. Por isso o substituto integra a definição do experimento.

### Estratégias

| Estratégia | Procedimento | Limitação |
| --- | --- | --- |
| Remoção individual (*leave-one-out*) | A partir do sistema completo, substitui um componente por vez. | Não revela interações entre componentes. |
| Construção incremental (*add-one-in*) | A partir da linha de base, acrescenta componentes em sequência. | O efeito atribuído a cada componente depende da ordem de inclusão. |
| Fatorial | Combina presença e ausência de vários componentes em desenho fatorial completo ou fracionado. | O número de configurações cresce exponencialmente; desenhos fracionados confundem interações de ordem alta (Montgomery, 2017). |

Quando os componentes interagem, as contribuições individuais não são aditivas: a soma
dos $\Delta_i$ pode diferir do ganho total do sistema. A remoção individual é adequada
a uma primeira campanha; interações são estudadas depois, em desenho fatorial limitado
aos componentes que mostraram efeito.

### Ablação de capacidade, ablação de informação e comparação de arquiteturas

Substituir um componente difere de retirar uma entrada. Retirar uma fonte de dados de
um componente que permanece ativo mede o valor da informação, não o valor do
componente. As duas intervenções são identificadas separadamente; misturá-las atribui
ao componente um efeito que pertence à informação disponível.

A ablação também difere da comparação entre arquiteturas alternativas. Comparar um
fluxo centralizado com um conjunto de agentes coordenados exige que ambos recebam as
mesmas observações, modelos, ações permitidas e orçamento de recursos; caso contrário,
a diferença medida incorpora as discrepâncias de informação ou de recurso.

## Relação com a plataforma

Na plataforma, a ablação sustenta qualquer alegação de que um componente de automação
ou de análise contribui para um resultado: a configuração completa é comparada com a
configuração em que o componente é trocado por seu substituto de referência, sob o
mesmo cenário. Esta página descreve o método; não relata estudos nem resultados.

## Como avaliar

- Declarar, antes da campanha, os componentes avaliados, seus substitutos, a métrica
  primária e o efeito mínimo de interesse.
- Tratar a execução completa como unidade experimental; mensagens ou amostras de uma
  mesma execução não são repetições independentes.
- Parear as configurações pelo mesmo cenário, carga e semente, e aleatorizar a ordem de
  execução.
- Estimar o número de repetições a partir da variabilidade observada em piloto, não por
  convenção.
- Relatar o efeito absoluto com intervalo de confiança e o custo de cada componente
  (tempo, memória, mensagens), além do efeito relativo.
- Preservar resultados nulos e negativos: a ausência de contribuição é informação para
  simplificar o sistema.
- Registrar a configuração efetiva de cada execução, para que a comparação seja
  reproduzível, conforme [Observabilidade e proveniência](../data-and-evidence/observability-and-provenance.md).

## Limites de interpretação

- $\Delta_i$ é condicional ao sistema, ao cenário e ao substituto escolhidos. Um
  substituto deliberadamente fraco infla a contribuição estimada.
- Componentes redundantes podem compensar a remoção de um deles: um $\Delta_i$ próximo
  de zero não prova que o componente seja dispensável em outras configurações. A
  redundância de representações foi observada experimentalmente em redes neurais
  (Meyes *et al.*, 2019).
- A ablação estima contribuição, não mecanismo: indica que o componente importa naquele
  contexto, não por que importa.
- Resultados obtidos em ambiente simulado ou emulado não se transferem automaticamente
  para medição física; ver [Ambientes experimentais](experimental-environments.md).

## Conceitos relacionados

- [Da pergunta à evidência](research-question-to-evidence.md)
- [Ambientes experimentais](experimental-environments.md)
- [Observabilidade e proveniência](../data-and-evidence/observability-and-provenance.md)
- [Automação progressiva](../intelligence/progressive-autonomy.md)

## Referências

Consulte `Meyes2019`, `LiptonSteinhardt2018` e `Montgomery2017` em
[`bibliography.bib`](../../bibliography.bib).
