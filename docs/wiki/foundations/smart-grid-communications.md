# Comunicações para sistemas elétricos inteligentes

> Uma rede elétrica inteligente combina processos físicos, medição, computação,
> comunicação e decisão; a rede de comunicação é parte do sistema de controle, não
> apenas um meio de transporte de dados.

## Por que importa

Sistemas elétricos distribuídos precisam observar estados, coordenar dispositivos e
transportar comandos entre locais distintos. Quando uma função elétrica depende da
chegada correta e oportuna de uma mensagem, o comportamento da comunicação passa a
influenciar o comportamento do processo físico. Forma-se, assim, um sistema
ciberfísico: falhas, atrasos ou informações incorretas no domínio digital podem ter
consequências no domínio elétrico.

“Tráfego de rede elétrica” não é uma classe única. Leituras periódicas, alarmes,
proteção, supervisão, comandos, atualização de configuração e transferência de
arquivos possuem escalas de tempo, padrões de fluxo e consequências de falha
diferentes. A arquitetura deve partir da função atendida, e não da tecnologia de
comunicação disponível.

## Um modelo em camadas

Uma forma útil de raciocinar separa quatro camadas:

| Camada | Pergunta principal |
| --- | --- |
| Processo físico | Qual grandeza, ativo ou fenômeno elétrico está envolvido? |
| Função de automação | Qual decisão, proteção, supervisão ou controle é necessário? |
| Informação | Quais mensagens, modelos de dados e relações semânticas sustentam a função? |
| Comunicação | Como os dados são transportados com desempenho, segurança e disponibilidade adequados? |

As camadas são dependentes. Um valor baixo de atraso, isoladamente, não demonstra
que a função foi atendida: a mensagem também precisa representar o fenômeno correto,
chegar ao destino esperado, preservar sua integridade e ser interpretada no contexto
temporal adequado.

## Requisitos dependem do caso de uso

Os atributos mais frequentes incluem atraso, variação do atraso, perda, vazão,
disponibilidade, alcance, densidade de nós, mobilidade, consumo de energia,
interoperabilidade e segurança. Eles formam um problema de compromisso. Aumentar
redundância pode melhorar disponibilidade e, ao mesmo tempo, consumir espectro e
capacidade. Cifrar e autenticar mensagens reduz riscos, mas introduz processamento,
estado e gestão de chaves. Uma rede sem fio amplia alcance e flexibilidade, mas
torna o meio compartilhado e sujeito a propagação variável.

Por isso, “tempo real”, “alta confiabilidade” ou “baixa latência” só são requisitos
verificáveis quando associados a uma função, a uma condição de operação, a uma
métrica, a um limite e a uma janela de observação.

## Relação com a plataforma

No laboratório, a comunicação é estudada como variável experimental e como
infraestrutura de suporte. Um cenário pode variar topologia, características do
enlace, carga, falhas ou políticas de controle e observar o efeito sobre indicadores
técnicos e sobre a função que utiliza a rede.

Essa abordagem permite comparar alternativas sem pressupor que uma tecnologia seja
universalmente superior. O resultado válido é condicionado pelo cenário, pelo
ambiente de execução, pelos instrumentos e pela população de situações observadas.

## Limites de interpretação

- Desempenho de bancada não representa automaticamente desempenho de campo.
- Uma média favorável pode ocultar caudas de distribuição incompatíveis com a
  função.
- Conectividade não implica interoperabilidade semântica.
- Segurança não é propriedade de um protocolo isolado; depende da arquitetura, da
  configuração e da operação.
- Uma demonstração funcional não estabelece disponibilidade de longo prazo.

## Conceitos relacionados

- [Qualidade de rede](../networking/network-quality.md)
- [Ambientes experimentais](../experimentation/experimental-environments.md)
- [Segurança em tecnologia operacional](../security/defense-in-depth.md)
- [Observabilidade e proveniência](../data-and-evidence/observability-and-provenance.md)

## Referências

O enquadramento adotado é consistente com os mapas de interoperabilidade do NIST,
com a família IEC 61850 para automação de sistemas elétricos e com a literatura de
bancadas ciberfísicas. Consulte as entradas `NISTsp1108r4`, `IEC61850`,
`Cintuglu2017` e `Smadi2021` em
[`bibliography.bib`](../../bibliography.bib).
