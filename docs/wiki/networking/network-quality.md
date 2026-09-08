# Qualidade de rede: atraso, variação, perda e disponibilidade

> Qualidade de comunicação é a adequação mensurável da rede a uma função, sob
> condições e período definidos.

## Atraso fim a fim

O atraso de uma mensagem pode ser decomposto, conceitualmente, em:

$$
d_{fim-a-fim} = d_{processamento} + d_{fila} + d_{transmissao} + d_{propagacao}
$$

O processamento inclui inspeção e tratamento nos nós. A fila depende da contenção e
do escalonamento. A transmissão é aproximadamente o tamanho da unidade de dados
dividido pela taxa do enlace. A propagação depende do meio e da distância. Em redes
sem fio, retransmissões, acesso ao meio, codificação e adaptação de enlace também
podem contribuir significativamente.

O tempo de ida e volta (RTT) inclui os caminhos de ida e retorno e o processamento
no destino. Ele não deve ser dividido por dois para estimar atraso unidirecional sem
demonstrar simetria entre os caminhos e os relógios envolvidos.

## Distribuições, não apenas médias

O atraso varia entre mensagens. Essa variação é frequentemente chamada de *jitter*,
mas o cálculo exato deve ser declarado. Para funções sensíveis a prazos, percentis e
máximos condicionados são geralmente mais informativos que a média. Um percentil
alto, contudo, continua ocultando as amostras além dele; resultados devem informar
tamanho da amostra, janela e perdas.

## Perda, erro e entrega útil

Perda de pacotes mede unidades esperadas que não chegam ao ponto de observação. Taxa
de erro de pacotes (PER) costuma representar unidades recebidas com erro em uma
camada específica. Retransmissões podem esconder erros do enlace e aumentar atraso.
Por isso, medições em camadas diferentes respondem a perguntas diferentes.

Vazão (*throughput*) mede dados transferidos por tempo; vazão útil (*goodput*) exclui
sobrecarga e retransmissões conforme a definição adotada. Capacidade nominal do
enlace não equivale a vazão da aplicação.

## Disponibilidade e confiabilidade

Disponibilidade é a proporção de tempo em que um serviço atende a uma condição
definida. Ela depende tanto da frequência quanto da duração das interrupções. Uma
estimativa observada por poucas horas não sustenta, sozinha, uma alegação anual.

Confiabilidade descreve a probabilidade de operar sem falha durante um intervalo e
sob condições definidas. Resiliência acrescenta a capacidade de absorver,
recuperar-se e adaptar-se a perturbações. Os três termos estão relacionados, mas não
são sinônimos.

## QoS e prioridade

Qualidade de serviço (QoS) fornece mecanismos de classificação, marcação,
enfileiramento, policiamento e reserva. Ela administra contenção; não cria capacidade
física. Priorizar uma classe pode reduzir seu atraso enquanto aumenta o atraso ou a
perda de outra. Um experimento de QoS deve observar todas as classes afetadas e
declarar a condição de sobrecarga.

## Como avaliar

Uma medição defensável declara:

- pontos e camada de observação;
- direção do fluxo e caminho conhecido;
- tamanho, taxa e distribuição do tráfego;
- referência temporal e incerteza dos relógios;
- aquecimento, duração, repetições e amostras excluídas;
- estatísticas, intervalos de confiança e condição de falha;
- configuração efetiva e tráfego concorrente.

## Relação com a plataforma

O laboratório usa métricas de rede para testar hipóteses sobre enlaces, topologias,
políticas e aplicações. Nenhum limiar é universal: o critério vem do caso de uso e é
declarado antes da execução. A medição é associada ao cenário e ao ambiente para
evitar comparar populações incompatíveis.

## Conceitos relacionados

- [Comunicações para sistemas elétricos inteligentes](../foundations/smart-grid-communications.md)
- [LTE privada](private-lte.md)
- [Observabilidade e proveniência](../data-and-evidence/observability-and-provenance.md)

## Referências

Os requisitos de desempenho devem ser lidos no contexto das funções e normas
aplicáveis. Consulte `NISTsp1108r4`, `IEEE2030_2011`, `IEC61850` e
`Energies2024` em [`bibliography.bib`](../../bibliography.bib).
