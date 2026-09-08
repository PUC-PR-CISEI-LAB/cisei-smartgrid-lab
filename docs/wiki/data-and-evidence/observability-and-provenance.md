# Observabilidade, qualidade de dados e proveniência

> Observar é produzir sinais sobre o sistema; confiar em uma conclusão exige também
> conhecer a qualidade, o contexto e a história desses sinais.

## Monitoramento e observabilidade

**Monitoramento** acompanha condições conhecidas por meio de consultas, métricas e
alertas predefinidos. **Observabilidade**, em sentido mais amplo, é a capacidade de
inferir estados internos a partir das saídas disponíveis. Em sistemas reais, os
termos se sobrepõem; a distinção útil é entre verificar perguntas previstas e
investigar comportamentos não antecipados.

Fontes comuns incluem:

- métricas numéricas em séries temporais;
- eventos e registros (*logs*);
- rastros que relacionam etapas de uma operação;
- capturas ou contadores de protocolo;
- estado de configuração e inventário;
- condições ambientais e anotações do experimento.

Coletar mais sinais não produz automaticamente mais conhecimento. Instrumentação
tem custo, pode alterar o sistema observado e pode gerar contradições entre relógios,
camadas e pontos de captura.

## Da medida ao indicador

Uma medida precisa declarar grandeza, unidade, ponto de observação, método,
resolução, frequência e incerteza relevante. O indicador agrega ou transforma
medidas para responder a uma pergunta. Essa transformação deve ser reproduzível.

Dados ausentes não equivalem a valor zero. Amostragem irregular, reinício de
contadores, mudanças de unidade, perda de telemetria e atraso de ingestão podem
produzir padrões artificiais. Regras de validação devem distinguir, quando possível,
ausência, invalidade, valor fora de faixa e indisponibilidade do produtor.

## Tempo como eixo de integração

Correlacionar rádio, rede, aplicação e processo físico requer uma referência
temporal conhecida. Sincronização não significa igualdade perfeita entre relógios.
Cada fonte possui erro, resolução, deriva e caminho de coleta. A precisão necessária
depende do fenômeno: análise de tendência e análise de sequência de eventos exigem
escalas diferentes.

Registrar a fonte de tempo e sua condição permite estimar se duas observações podem
ser ordenadas com confiança. Quando a incerteza temporal é comparável ao fenômeno,
uma relação de causalidade não deve ser inferida apenas pela ordem aparente dos
registros.

## Proveniência

Proveniência descreve a história de um dado: de onde veio, por qual atividade foi
produzido ou transformado e quem ou o que foi responsável. O modelo PROV-DM organiza
essa ideia em três classes centrais:

- **entidade:** dado, configuração, modelo ou resultado;
- **atividade:** coleta, execução, transformação ou análise;
- **agente:** pessoa, organização ou sistema responsável.

Relações entre elas permitem responder, por exemplo, qual execução gerou um arquivo,
qual código produziu uma tabela e qual conjunto de parâmetros alimentou um modelo.

## FAIR não significa irrestritamente aberto

Os princípios FAIR propõem dados localizáveis, acessíveis, interoperáveis e
reutilizáveis. “Acessível” inclui acesso sob condições declaradas; dados sensíveis
podem exigir autenticação, autorização ou publicação de uma versão sanitizada.
Metadados persistentes, vocabulário claro e licença explícita aumentam a reutilização
sem remover obrigações de segurança e confidencialidade.

## Evidência

Um pacote de evidência é uma associação verificável entre afirmação, critério,
execução e artefatos. Hashes apoiam integridade; metadados apoiam interpretação;
revisão apoia a decisão. Nenhum dos três substitui os demais. Evidência não é apenas
o resultado favorável: condições, falhas e resultados negativos também são
necessários para avaliar a afirmação.

## Relação com a plataforma

A plataforma trata telemetria, configuração e contexto experimental como partes da
mesma cadeia. Isso permite comparar execuções, refazer transformações e declarar o
limite de cada conclusão. A instrumentação é escolhida a partir da pergunta; não se
presume que um painel operacional constitua, por si só, um conjunto de dados
científico.

## Conceitos relacionados

- [Da pergunta à evidência](../experimentation/research-question-to-evidence.md)
- [Qualidade de rede](../networking/network-quality.md)
- [Ambientes experimentais](../experimentation/experimental-environments.md)

## Referências

Consulte `Wilkinson2016`, `W3CPROVDM`, `GoFAIR`, `DataCite44` e
`ISO17025` em [`bibliography.bib`](../../bibliography.bib).
