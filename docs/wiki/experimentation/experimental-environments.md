# Ambientes físicos, virtuais, emulados e simulados

> O ambiente experimental determina quais mecanismos estão presentes, quais são
> representados por modelos e até onde uma conclusão pode ser generalizada.

## Quatro formas de execução

| Ambiente | O que executa | Principal força | Limite típico |
| --- | --- | --- | --- |
| Físico | Equipamentos, meios e fenômenos reais | Realismo dos mecanismos presentes | Custo, escala e menor controle ambiental |
| Virtual | Software real sobre recursos computacionais abstraídos | Repetição e flexibilidade | Não reproduz por si só o meio físico |
| Emulado | Componentes reais interagem com efeitos impostos | Controle de atraso, perda, carga ou falha | Fidelidade depende do modelo e do emulador |
| Simulado | Modelos calculam o comportamento do sistema | Escala e exploração de hipóteses | Resultado depende das abstrações e da calibração |

Um experimento **híbrido** compõe dois ou mais desses ambientes. A palavra não indica
automaticamente maior fidelidade: as interfaces entre as partes e o sincronismo
podem introduzir novos erros.

## Fidelidade não é uma escala única

Um ambiente pode ser fiel em um aspecto e abstrato em outro. Uma simulação pode
representar detalhadamente filas e propagação, mas simplificar aplicações. Uma
execução física pode usar rádios reais e, ainda assim, não representar vegetação,
interferência ou distâncias de campo.

Por isso, a fidelidade deve ser declarada em relação ao fenômeno estudado. As
perguntas centrais são:

1. Quais mecanismos relevantes estão presentes?
2. Quais são substituídos por modelos?
3. De onde vieram os parâmetros desses modelos?
4. Contra quais observações o comportamento foi verificado?
5. Em que domínio de condições a comparação é válida?

## Calibração, verificação e validação

**Calibrar** ajusta parâmetros do modelo a partir de dados de referência.
**Verificar** examina se a implementação resolve o modelo pretendido corretamente.
**Validar** avalia se o modelo representa o fenômeno real com adequação ao uso
pretendido. Uma boa coincidência com os dados usados na calibração não basta para
validar o modelo; é preciso avaliar condições ou amostras independentes e quantificar
o erro relevante.

## Sombra digital e gêmeo digital

Uma representação digital pode receber dados do sistema físico sem atuar sobre ele;
nesse caso, é útil tratá-la como **sombra digital**. Um **gêmeo digital de rede**
pressupõe uma relação operacional mais forte entre representação e sistema,
incluindo mapeamento interativo e uso da representação para analisar, diagnosticar,
emular ou orientar o comportamento da rede.

Nem todo painel, modelo ou simulador é um gêmeo digital. O nome deve ser reservado
para uma capacidade demonstrável, com identidade entre entidades, sincronização,
modelo declarado, avaliação de erro e governança da interação.

## Relação com a plataforma

A plataforma permite formular uma pergunta uma vez e executá-la, quando apropriado,
em ambientes distintos. A comparação pode revelar quais efeitos pertencem ao modelo,
à implementação ou ao fenômeno físico. Cada resultado deve carregar o tipo de
ambiente e seus limites; resultados de ambientes diferentes não são combinados como
se fossem observações homogêneas.

## Exemplo conceitual

Uma hipótese sobre congestionamento pode ser explorada em grande escala por
simulação, exercitada com aplicações reais sob emulação de enlace e finalmente
avaliada em uma rede física. As etapas não formam uma escada obrigatória. Cada uma
responde a uma parte da pergunta e produz evidência de natureza diferente.

## Conceitos relacionados

- [Da pergunta à evidência](research-question-to-evidence.md)
- [Qualidade de rede](../networking/network-quality.md)
- [Observabilidade e proveniência](../data-and-evidence/observability-and-provenance.md)

## Referências

Consulte as entradas `Cintuglu2017`, `Smadi2021`, `HELICS2024`, `GridLABD2024`,
`AmarisoftDigitalTwin2024`, `ITUY3090` e `ITUY3093` em
[`bibliography.bib`](../../bibliography.bib).
