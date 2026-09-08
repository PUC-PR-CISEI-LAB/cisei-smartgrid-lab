# Como contribuir para a base de conhecimento

Esta coleção recebe explicações autorais sobre os fundamentos científicos e de
engenharia relacionados ao CISEI SmartGrid Lab. Uma boa página deve continuar útil
mesmo quando equipamentos, versões de software e configurações da plataforma
mudarem.

## Antes de escrever

Escolha o destino correto para a contribuição:

| Se o conteúdo... | Destino |
| --- | --- |
| Explica um conceito, modelo ou relação | Base de conhecimento |
| Define uma sigla ou termo em poucas linhas | [Glossário](../glossary.md) |
| Altera propósito, escopo ou direção da plataforma | [Termo de Abertura](../charter.md) |
| Descreve configuração, inventário ou procedimento | Espaço operacional privativo |
| Relata um resultado científico | Publicação ou conjunto de dados apropriado |

Não transforme um documento interno em artigo por recorte. Reescreva o assunto para
o público, elimine detalhes operacionais e cite fontes publicáveis.

## Estrutura recomendada

Use somente as seções necessárias, nesta ordem:

```markdown
# Nome do conceito

> Definição curta em linguagem direta.

## Por que importa
## Modelo conceitual
## Relação com a plataforma
## Como avaliar
## Limites de interpretação
## Conceitos relacionados
## Referências
```

Uma página deve responder qual problema o conceito resolve, quais variáveis ou
relações o definem, como pode ser observado e o que não se pode concluir a partir
dele. Fórmulas devem definir todas as grandezas e unidades.

## Linguagem e nomes

- A prosa canônica é escrita em português do Brasil.
- Nomes de arquivo usam inglês, minúsculas e hífens.
- Na primeira ocorrência, apresente o termo em português e, quando útil, o termo
  técnico consolidado em inglês.
- Prefira linguagem precisa a slogans. Não chame uma tecnologia de segura,
  inteligente, resiliente ou de missão crítica sem declarar o critério.
- Diferencie capacidade existente, trabalho em avaliação e possibilidade futura.

## Referências

Toda afirmação normativa, definição externa ou resultado quantitativo relevante
precisa de uma fonte primária ou normativa. Reuse uma entrada de
[`bibliography.bib`](../bibliography.bib) ou acrescente os metadados necessários.
Não distribua cópias de normas, artigos ou figuras sem autorização.

Ao mencionar uma norma, informe a parte ou edição quando isso alterar o sentido.
Não declare conformidade, certificação ou acreditação apenas porque uma prática foi
inspirada por determinada norma.

## Fronteira de divulgação

Antes do envio, confirme que a mudança não contém:

- credenciais, chaves, tokens ou nomes de usuários;
- endereços, identificadores de segmentos, nomes de *hosts* ou de equipamentos;
- topologia física ou de campo não aprovada para publicação;
- dados brutos, capturas de tráfego ou resultados ainda não publicados;
- informações contratuais ou identificação não autorizada de parceiros;
- caminhos ou links que dependam de repositórios privativos.

Exemplos devem usar papéis abstratos, como “nó de campo”, “enlace sem fio” e “centro
de operação”. Valores numéricos devem ser didáticos ou provenientes de fonte
citada, nunca copiados de configuração operacional.

## Revisão

Uma revisão editorial verifica correção conceitual, clareza, referências, ligações
com outros artigos e fronteira de divulgação. A revisão técnica verifica se a
aplicação descrita é coerente com o método científico e não confunde simulação,
emulação e medição física.
