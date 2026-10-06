# Termo de Abertura da Plataforma de Pesquisa — CISEI SmartGrid Lab

> **Versão:** 3.4
>
> **Status:** em revisão
>
> **Data:** 2026-08-31
>
> **Plataforma:** ambiente de rede estável, configurável e orientado por dados para pesquisa aplicada em redes de comunicação destinadas a sistemas elétricos inteligentes
>
> **Horizonte:** contínuo, realizado por incrementos sucessivos em trilhas de projeto paralelas

---

## Histórico de Versões

| **Versão** | **Data**               | **Alteração**                                                                                                                                                                                                                             |
| ---------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.0        | 2026&#8209;08&#8209;17 | Reestruturação segundo o PIC: objetivos, medidas, premissas e diretrizes estratégicas                                                                                                                                                     |
| 2.2        | 2026-08-19             | Atribuição de estado de execução à decomposição do trabalho                                                                                                                                                                               |
| 3.0        | 2026-08-19             | Reorientação ao eixo de capacidade                                                                                                                                                                                                        |
| 3.1        | 2026-08-21             | Declaração do grau de inovação e posicionamento da plataforma (§1.4)                                                                                                                                                                      |
| 3.2        | 2026-08-22             | Objetivos reordenados por dependência e **renumerados** para que o identificador expresse a sequência (§4.2)                                                                                                                              |
| 3.3        | 2026-08-25             | Redenominação do artefato de *Product Charter* para **Termo de Abertura da Plataforma de Pesquisa**; declaração da natureza do instrumento e da custódia institucional; distinção entre a estrutura tomada do PIC e o objeto do documento |
| 3.4        | 2026-09-03             | Revisão e melhorias de entendimento do texto do documento em geral                                                                                                                                                                        |

---

## Resumo

Este **Termo de Abertura da Plataforma de Pesquisa** (*Research Platform Charter*) estabelece a orientação estratégica de longo prazo do CISEI SmartGrid Lab. Seu objetivo é descrever a capacidade da plataforma de configurar, executar, observar e reproduzir experimentos em diferentes redes físicas, virtuais e híbridas. Além disso, o ambiente deve gerar, armazenar e analisar dados segundo boas práticas de pesquisa científica e normas de engenharia. 

O laboratório não se reduz à instalação física, ao acervo de equipamentos ou a uma arquitetura tecnológica específica. Sua proposta de valor consiste em transformar questões de pesquisa e problemas técnicos relevantes em cenários controlados e experimentos reproduzíveis, dos quais resultem dados com qualidade e proveniência conhecidas, análises verificáveis, modelos avaliados contra evidências e conclusões ou decisões rastreáveis, com incertezas e limitações devidamente mapeadas.

O presente documento define a identidade, a tese e o grau de inovação da plataforma (§1), o foco e suas fronteiras (§2), a experiência experimental que o laboratório deve proporcionar (§3), os objetivos permanentes (§4), as medidas de sucesso (§5), as premissas e incertezas que podem impactar a viabilidade técnica (§6) e as diretrizes de governança e a estratégia de evolução (§7).

**Palavras-chave:** plataforma de pesquisa; redes configuráveis; redes físicas e virtuais; emulação de tráfego; análise de dados; proveniência; gêmeo digital; SDN; NFV; inteligência artificial; autorrecuperação; experimentação reproduzível; grau de inovação.

---

## Nota Metodológica

A gerência deste projeto adota como referência principal o conceito de *Product Innovation Charter* — PIC, entendido como expressão escrita da estratégia de inovação de produto [Crawford1980] [Bart2002] [BartPujari2007] [Anderson2024]. O modelo organiza antecedentes, foco, metas e objetivos, medidas de avaliação e diretrizes estratégicas para cenários de longo prazo. 

Embora tenha sido inicialmente concebida para promover a inovação constante em produtos comerciais, a **estrutura** apresentada aqui orienta uma plataforma com um horizonte contínuo e de longo prazo, capaz de acomodar e permitir a coexistência de diferentes domínios sem que estes interfiram ou comprometam a qualidade dos dados e modelos em suas respectivas pesquisas acadêmicas ou consultas técnicas. 

Por se tratar de uma plataforma de pesquisa e desenvolvimento, este Termo ainda explicita premissas, incertezas e condições de revisão, em consonância com os critérios de novidade, criatividade, incerteza, sistematicidade e transferibilidade ou reprodutibilidade que caracterizam as atividades de P&D [OECDFrascati2015]. Na gestão de dados e evidências, são adotados como referências os princípios FAIR [Wilkinson2016] e o modelo de proveniência PROV-DM [W3CPROVDM]. A ISO/IEC 17025:2017 [ISO17025], por sua vez, orienta aspectos relativos à competência, à imparcialidade e à operação consistente dos processos experimentais. É importante ressaltar que o emprego dessas referências não constitui declaração de conformidade integral nem, no caso da ISO/IEC 17025:2017, alegação de acreditação.

O gerenciamento de riscos associados à inteligência artificial toma como referência o NIST AI RMF 1.0 [NISTAIRMF2023]. As referências orientam o desenho da plataforma; os controles verificáveis e sua implementação pertencem aos documentos derivados.

---

## 1. Identidade, Problema, Oportunidade e Tese de Valor

### 1.1 Identidade

O CISEI SmartGrid Lab é uma plataforma permanente de pesquisa aplicada dedicada à investigação de redes de comunicação que sustentam operações de sistemas elétricos inteligentes. Ela integra infraestrutura de rede física, ambientes virtualizados e simulados, geração e emulação de tráfego, instrumentação, automação, gestão de dados, métodos analíticos e inteligência artificial em uma única experiência experimental.

O laboratório é governado como plataforma permanente porque reúne usuários, proposta de valor, capacidades compartilhadas, critérios de sucesso e evolução contínua em diferentes domínios e linhas de pesquisa que podem compor investigações e reutilizar infraestrutura, dados, métodos e serviços comuns. Deste modo, são preservados, quando necessário, fronteiras de responsabilidade, isolamento de recursos e independência de execução, de modo que uma atividade não interfira em outra, salvo quando essa interação for deliberada e integrar o cenário experimental. Projetos temporários financiam, contribuem ou aperfeiçoam incrementos da plataforma, mas nenhum deles, isoladamente, define seu propósito, condiciona sua continuidade ou esgota suas possibilidades de uso.
### 1.2 Problema

Pesquisadores, estudantes e organizações parceiras que necessitam avaliar redes destinadas a serviços críticos sem depender de intervenções em ambientes produtivos, de configurações artesanais difíceis de reproduzir ou de dados cuja origem e qualidade sejam desconhecidas. Em laboratórios heterogêneos, a introdução sucessiva de equipamentos, ferramentas e linhas de pesquisa tende a produzir demora de preparação, resultados incomparáveis, dependência de conhecimento tácito, fragmentação de dados e aumento do custo de manutenção.

O problema central não é apenas disponibilizar equipamentos. É permitir que diferentes questões sejam investigadas com rapidez e rigor por meio de cenários configuráveis, perfis de tráfego e falha controlados, observação confiável e análise reprodutível, preservando a distinção entre resultado físico, resultado virtual, simulação, inferência analítica e decisão operacional.

### 1.3 Oportunidade e Tese de Valor

O laboratório pode reduzir o custo e o tempo de preparação de experimentos, ampliar sua repetibilidade e produzir conhecimento comparável entre ambientes físicos, virtuais e híbridos. Sobre uma base comum de configuração e dados, torna-se possível desenvolver e avaliar mecanismos de inteligência artificial que auxiliem a escolha de configurações, detectem condições anômalas e promovam recuperação segura da rede.

> **Tese da plataforma:** se topologias, parâmetros de enlace, perfis de tráfego, falhas, instrumentação, critérios de aceite e políticas de recuperação forem descritos de forma versionada e executável sobre ambientes físicos, virtuais e híbridos, então pesquisadores e engenheiros de campo poderão realizar experimentos com menor esforço de preparação e maior reprodutibilidade. Se os dados resultantes possuírem qualidade, proveniência e contexto experimental explícitos, então métodos analíticos e modelos de inteligência artificial poderão ser avaliados com rigor e empregados, de maneira progressiva e controlada, na direção e na autorrecuperação da rede.

### 1.4 Grau de Inovação e Posicionamento

A declaração do grau de inovação pretendido é elemento do enquadramento PIC [Crawford1980] [Bart2002] [Anderson2024]. Parte da plataforma incorpora práticas e tecnologias consolidadas — como automação, integração contínua, observabilidade, SDN, NFV e gestão de dados orientada pelos princípios FAIR — que constituem sua base habilitadora. A adoção desses elementos é uma decisão legítima de engenharia, mas não representa, por si só, alegação de novidade nem de contribuição científica ou tecnológica..

A intenção se concentra em três frentes, condicionadas à evidência de caracterização empírica e sombra calibrada do enlace sub-GHz proprietário da planta, qualidade experimental — proveniência, portabilidade, reprodução por operador distinto — como critério de avaliação de *testbed* e um protocolo de promoção de autonomia sobre ativo físico, com independência demonstrada entre execução, verificação e interrupção. Nenhuma dessas frentes se propõe como alegação, ou seja, cada uma delas pode ser abandonada se a evidência não a sustentar.

---

## 2. Foco e Fronteiras do Laboratório

### 2.1 Visão

> Constituir uma plataforma experimental de longo prazo, configurável e orientada por evidências, capaz de reproduzir redes físicas, virtuais e híbridas e seus perfis de tráfego, produzir dados confiáveis para análise e desenvolver mecanismos progressivos de inteligência artificial aplicados à configuração, ao diagnóstico e à recuperação segura da rede.

### 2.2 Missão

A missão do CISEI SmartGrid Lab é prover, manter e evoluir um ambiente experimental no qual pesquisadores, estudantes e parceiros possam configurar, executar, observar e reproduzir cenários de redes de comunicação para sistemas elétricos inteligentes em infraestrutura física, virtual ou híbrida. O laboratório combina perfis declarativos de topologia, enlace, tráfego, falha, instrumentação, aceite e recuperação com processos governados de coleta, tratamento, análise e preservação de dados. Sobre essa base, desenvolve e avalia mecanismos de inteligência artificial para diagnóstico, recomendação de configuração e autorrecuperação progressiva, sempre sob limites explícitos de segurança, autorização, reversibilidade, auditabilidade e evidência.

### 2.3 Partes Interessadas e Necessidades Principais

| **Parte interessada**                               | **Necessidade**                                                                                                    |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Pesquisadores                                       | Formular modelos e reproduzir experimentos, comparar alternativas e produzir evidência publicável                  |
| Estudantes                                          | Aprender e aperfeiçoar experimentos em ambiente controlado                                                         |
| Equipes técnicas parceiras / engenheiros de campo   | Avaliar arquiteturas, configurações, tráfego, degradações e estratégias de recuperação antes de aplicação em campo |
| Responsáveis por redes, observabilidade e segurança | Identificar e compreender estados, riscos, limites e efeitos das ações propostas ou executadas                     |
| Gestores de pesquisa e inovação                     | Preservar infraestrutura, conhecimento e valor entre projetos, equipes e parcerias sucessivas                      |

### 2.4 Fundamentos da Plataforma

1. **Experimentação configurável e multiplataforma:** cenários devem ser compostos por perfis reutilizáveis e aplicáveis, conforme sua compatibilidade, a redes físicas (*bare metal*), virtuais, simuladas ou híbridas. A configuração efetiva deve ser lida de volta e comparada ao estado pretendido.

2. **Emulação controlada de tráfego, degradações e falhas:** o laboratório deve representar padrões normais e adversos de comunicação por perfis versionados de carga, prioridade, periodicidade, rajada, concorrência, perda, atraso, variação de atraso, indisponibilidade e falha de componentes, sem confundir emulação controlada com ocorrência de campo.

3. **Dados e análises governados:** dados brutos, transformações, indicadores, conjuntos de dados, códigos analíticos e modelos devem possuir identidade, proveniência, qualidade, versão, critérios de inclusão, incertezas e limitações suficientes para exame e reutilização. A prática analítica deve separar exploração, calibração, validação e avaliação reservada sempre que a pergunta exigir inferência ou comparação de modelos. Reprodução exige, além disso, que o **ambiente de execução** seja declarado e recuperável e que as **fontes de aleatoriedade** de toda execução ou análise dependente de sorteio sejam registradas. Quando a identidade exata do resultado não for alcançável, declara-se a **tolerância** e o critério — valor, estatística ou decisão de aceite — dentro dos quais a reprodução é considerada bem-sucedida.

4. **Inteligência artificial aplicada à configuração e à resiliência:** a IA deve evoluir de observação e diagnóstico para recomendação, execução supervisionada e autorrecuperação delimitada. Seu desempenho deve ser comparado a critérios de base, e cada ação deve respeitar a política de atuação, os limites operacionais da planta e os mecanismos de verificação e reversão. A integridade e a proveniência da telemetria e do contexto que alimentam o mecanismo são condição de validade de sua decisão: entrada forjada, corrompida ou de origem não verificável invalida a ação proposta ou executada, ainda que ela permaneça dentro da política de atuação. O próprio mecanismo — suas entradas, seu contexto e suas credenciais — constitui superfície de ataque a ser modelada e testada, e não apenas um componente a ser avaliado por desempenho.
5. **Aprendizagem e continuidade institucional:** cenários, dados, resultados, decisões e limitações devem permanecer compreensíveis e reutilizáveis por novos participantes. A expansão do laboratório deve aumentar sua capacidade de investigação sem produzir fragmentação desnecessária.

### 2.5 Escopo da Plataforma

Integram o escopo permanente:

- Redes de comunicação relevantes para sistemas elétricos inteligentes, com ênfase inicial em *backhaul* sem fio.
- Ambientes físicos, virtuais, simulados e híbridos.
- Sombras e gêmeos digitais de rede, calibrados e avaliados contra medição física.
- Configuração declarativa de topologias, enlaces, serviços e funções de rede.
- SDN e NFV como mecanismos de programabilidade, isolamento e composição experimental.
- Geração e emulação de perfis de tráfego, degradação e falha.
- Observabilidade independente e coleta sincronizada de dados.
- Engenharia, governança e análise de dados experimentais.
- Modelos estatísticos, aprendizado de máquina e sistemas de IA aplicados à configuração, à detecção, ao diagnóstico, à previsão e à recuperação.
- Avaliação de segurança, desempenho, confiabilidade, interoperabilidade e eficiência operacional.
- Preservação de cenários, evidências, software, conhecimento e competência humana.

Neste Termo, **sombra digital** designa o modelo alimentado por medições da planta física, sem via de retorno, e **gêmeo digital**, aquele cuja correspondência com a planta é mantida nos dois sentidos. A distinção é normativa e vale para ambos: nenhum modelo pode ser apresentado como representação da planta enquanto sua fidelidade não tiver sido avaliada contra medição reservada e sua faixa de validade declarada. O critério que a separa — correspondência mantida nos dois sentidos — converge com a definição de rede-gêmea digital da ITU-T Y.3090 [ITUY3090], à qual este Termo remete a condição de fidelidade avaliada.

Em relação aos **limites operacionais da planta física**, o que um perfil pode representar em ambiente físico é limitado pela planta instalada. A planta vigente é composta por enlaces sem fio em faixa não licenciada e de baixa taxa de transmissão; está prevista sua extensão por uma planta LTE privada, com a possibilidade de enlace por SDR, sujeita à autorização de uso de radiofrequência. Faixa, taxas, potência, número de nós e demais limites operacionais de cada planta são declarados nos documentos derivados e não são reproduzidos aqui, para que o presente documento não se desatualize a cada mudança de inventário. Deles decorre uma regra permanente: as **condições que excedam os limites operacionais da planta vigente que não podem ser confirmadas por execução física** são objetos de ambiente virtual ou simulado, com a diferença entre ambientes medida e declarada (OBJ-09). A incorporação de nova planta amplia esses limites e não altera esta regra.

### 2.6 Fora de Escopo

Não constituem finalidade da plataforma:

- Operar ou controlar diretamente redes elétricas ou redes de telecomunicações em ambientes de produção.
- Providenciar uma equivalência imediata entre os resultados de laboratório e o desempenho de campo.
- Homologar comercialmente equipamentos ou certificar conformidade regulatória sem mandato e método específicos.
- Permitir autonomia irrestrita ou ações sem identidade, autorização, limites, verificação e possibilidade de interrupção segura.
- Emitir radiofrequência fora das faixas, potências e condições autorizadas, ou sem responsável técnico designado quando exigido, inclusive quando a emissão provier de instrumento de laboratório.

A **condição regulatória de capacidade**, cujo funcionamento dependa de autorização de uso de radiofrequência pode ser planejada, especificada, desenvolvida e validada em ambiente virtual, simulado ou em caminho conduzido, mas não é declarada disponível antes de obtida a autorização da autoridade competente e designado o responsável técnico correspondente. Esta é a única classe de restrição da plataforma que não depende de esforço próprio do laboratório, e por isso é tratada também como premissa estratégica (§6). Os instrumentos regulatórios aplicáveis a cada planta são identificados nos documentos derivados.

---

## 3. Experiência Experimental da Plataforma

Este capítulo descreve como uma pergunta de pesquisa se transforma em evidência. Em um primeiro passo, a pergunta é expressa como um **cenário**, composto por perfis reutilizáveis. Em seguida, seleciona-se um **ambiente** compatível, aplica-se o cenário, observa-se sua execução e preservam-se os dados e as evidências resultantes. Quando o experimento inclui diagnóstico, recomendação ou atuação automatizada sobre a rede, aplicam-se também os níveis e controles de autonomia definidos no §3.3.

### 3.1 Unidade Configurável de Cenário

A unidade configurável da experiência é o **cenário**: a descrição completa do que se pretende investigar, em quais condições e segundo quais critérios. Cada cenário é composto por **perfis**, que descrevem dimensões reutilizáveis do experimento, e é realizado em um **ambiente** físico, virtual, simulado ou híbrido. A representação tecnológica dos perfis poderá evoluir, mas deverá expressar, quando aplicável:

| **Perfil**             | **Conteúdo mínimo**                                                                                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Ambiente**           | Alvo físico, virtual, simulado ou híbrido; recursos e versões                                                                                                      |
| **Topologia**          | Nós, enlaces, funções, relações e endereçamento lógico                                                                                                             |
| **Enlace ou rádio**    | Parâmetros que o ambiente permite controlar e condições que só podem ser caracterizadas por medição — capacidade, propagação, qualidade e interferência entre elas |
| **Tráfego**            | Fontes, destinos, protocolos, classes, periodicidade, rajadas, volumes e prioridades                                                                               |
| **Falha e degradação** | Condição injetada, instante, duração, intensidade e estado esperado                                                                                                |
| **Observabilidade**    | Relógios, sinais, frequências, unidades, pontos de coleta e controles de qualidade                                                                                 |
| **Aceite**             | Hipóteses, indicadores, limiares, comparações e critérios de encerramento                                                                                          |
| **Recuperação**        | Condições de disparo, ações permitidas, restrições, verificação e reversão                                                                                         |

Por exemplo, para investigar se uma estratégia de recuperação preserva um serviço após a degradação de um enlace, o cenário pode combinar uma topologia com caminhos alternativos, um perfil de tráfego, a degradação pretendida, os sinais que serão observados, os critérios de aceite e as ações de recuperação permitidas. Em simulação, a degradação pode ser configurada diretamente; na planta física, deve ser produzida por meio físico controlado ou registrada como condição observada. Se o estudo apenas comparar resultados, encerra-se com a evidência e a conclusão. Se recomendar ou executar uma recuperação, submete-se também ao §3.3.

#### 3.1.1 Controlado e Observado

Nem todo item de perfil é controlável em todo ambiente. Em ambiente simulado, propagação, interferência e qualidade de enlace são variáveis controladas; na planta física, são condições do meio, caracterizadas por medição e alteráveis apenas por meio físico — atenuação, blindagem, reposicionamento ou injeção controlada de sinal. O perfil deve distinguir, por ambiente, o que é **controlado** do que é **observado**: parâmetro que o ambiente não permite controlar é registrado como condição observada, e não como configuração. Nenhum procedimento de automação, isoladamente, cria ou comprova uma condição física.

O **limite de medição física** é definido pelo trecho cuja única via de sincronização seja o próprio meio sob medição não admite afirmação de atraso unidirecional.

#### 3.1.2 Compatibilidade e Portabilidade

Um perfil é portável para um ambiente quando todas as suas funcionalidades são controláveis nesse ambiente, todos os requisitos de seus critérios de aceite são observáveis lá e suas demandas se encaixam nos limites operacionais correspondentes. A compatibilidade é, portanto, propriedade do par perfil–ambiente, mas não é simétrica. Executar um perfil mediante reparametrização, substituição de condição controlada por observada ou troca de indicador de aceite constitui **alteração semântica**, ou seja, o cenário resultante é outro e deve ser declarado como tal.

#### 3.1.3 Facilidade de configuração

Neste Termo, **facilidade de configuração** significa reduzir esforço manual sem ocultar o estado efetivo. Deve ser avaliada por tempo de preparação, quantidade de intervenções manuais, proporção de parâmetros declarados, portabilidade do perfil entre ambientes, detecção de deriva, leitura do estado aplicado e capacidade de desfazer o cenário.

### 3.2 Ciclo Experimental Canônico

Todo experimento percorre um fluxo comum até a análise. Diagnóstico, recomendação e atuação são extensões opcionais desse fluxo e somente integram o cenário quando a pergunta de pesquisa as exige.

```text
pergunta e hipótese
  → composição e validação do cenário
  → seleção do ambiente físico, virtual, simulado ou híbrido
  → aplicação da configuração e leitura do estado efetivo
  → execução dos perfis de tráfego, degradação e falha
  → observação e coleta governada
  → análise, avaliação de modelos e declaração de incerteza
  → diagnóstico ou proposta de configuração/recuperação
  → autorização e execução controlada, quando aplicável
  → verificação do resultado e reversão, quando necessária
  → evidência, conclusão e aprendizagem reutilizável
```

Quando houver atuação, insere-se entre a análise e a conclusão o ramo correspondente:

```text

diagnóstico ou proposta de configuração/recuperação
  → autorização segundo a política de atuação
  → execução controlada
  → verificação do resultado
  → reversão ou parada segura, quando necessária
  → evidência da decisão, da ação e de seus efeitos
```

  Cada transição deve preservar a identidade do cenário, do ambiente, da execução, dos dados, dos agentes humanos ou automatizados e das transformações realizadas.

### 3.3 Autonomia

Esta seção aplica-se aos experimentos em que um mecanismo automatizado ou de inteligência artificial diagnostica, recomenda ou executa uma alteração. Os níveis de observação e recomendação integram a escala porque constituem a base de evidência necessária antes que o mecanismo receba autoridade para atuar.

Para este Termo, **autorrecuperação** ou *self-healing* é o ciclo controlado pelo qual o laboratório detecta uma condição anômala, produz diagnóstico rastreável, seleciona uma ação permitida, avalia seus riscos, executa-a dentro de limites definidos, verifica a recuperação e realiza reversão ou parada segura quando o resultado não satisfaz os critérios estabelecidos.

Entende-se por **política de atuação** o conjunto de ações permitidas ao mecanismo e das condições sob as quais são permitidas, declarado por classe de ação e por ambiente.

Uma **classe de ação** reúne alterações com finalidade, risco e controles equivalentes, como reiniciar um serviço, selecionar uma rota ou modificar um parâmetro de configuração. O nível é atribuído separadamente a cada classe de ação e ambiente; não existe um único nível global de autonomia do laboratório.

A maturidade será expressa pelos seguintes níveis, cuja formulação converge deliberadamente com os níveis de rede autônoma da literatura normativa [TMFAN] [TS28100] — inclusive na regra de avaliar por cenário, e não globalmente — e com a governança retroativa que declara política, supervisão e ciclo de vida da ação [ZSM009]. Suplementarmente, este Termo acrescenta o critério de promoção que define a mudança de nível:

| **Nível** | **Definição**                           | **Capacidade**                                                                                                                                                                                              |
| --------- | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A0**    | Observação                              | A IA detecta, classifica ou prevê, sem propor alteração                                                                                                                                                     |
| **A1**    | Recomendação                            | A IA propõe ação e apresenta evidência, confiança, riscos e alternativas                                                                                                                                    |
| **A2**    | Execução Supervisionada                 | A pessoa autorizada aprova cada ação antes da aplicação                                                                                                                                                     |
| **A3**    | Autonomia Delimitada — Ambiente Virtual | Ações previamente autorizadas podem ocorrer em ambiente virtual ou simulado, com limites e reversão automática                                                                                              |
| **A4**    | Autonomia Delimitada — Ambiente Físico  | Ações previamente autorizadas podem ocorrer sobre ativos físicos do laboratório, após demonstração de segurança, desempenho e recuperação em níveis anteriores                                              |
| **A5**    | Autonomia Composta sob Política         | O mecanismo compõe e aplica respostas a condições não antecipadas individualmente, sem aprovação por ação; a pessoa autorizada define a política de atuação e os critérios de parada, mas não cada execução |

O estado registrado representa o nível alcançado por **classe de ação** e por ambiente, com cada nível indicando a maturidade atingida. Isso implica que a autonomia superior é validada por meio de uma questão de pesquisa ou demanda operacional que ultrapasse o nível de autonomia inferior.

O avanço de nível não é automático nem definitivo. Deve ocorrer por caso de uso, ambiente e classe de ação, com possibilidade de regressão quando a evidência se tornar insuficiente.

**Independência do comando e da verificação.** A capacidade de interromper uma ação e de verificar seu resultado não pode depender do mecanismo que a executa nem do meio que ela altera: exige caminho de observação e comando independente de ambos. Sem essa independência demonstrada, não há promoção ao nível que atue sobre ativos físicos.

A5 corresponde a um horizonte de pesquisa de longo prazo e sua investigação exige, no mínimo, política de atuação declarada e verificada de forma contínua, auditoria por ação, parada independente do próprio mecanismo e recuperação demonstrada nos níveis anteriores para a mesma classe de ação. Ausência de aprovação por ação não significa ausência de limite, de identidade, de verificação ou de possibilidade de interrupção segura: autonomia irrestrita permanece fora do escopo permanente (§2.6).

Esta escala A0–A5 é a referência única de maturidade de autonomia da plataforma. Documentos derivados que empreguem os mesmos identificadores devem adotar estas definições.

---

## 4. Metas e Objetivos

### 4.1 Meta Geral

Manter e evoluir uma plataforma experimental configurável capaz de produzir evidências reproduzíveis e conhecimento transferível sobre redes de comunicação aplicadas a sistemas elétricos inteligentes, integrando ambientes físicos e virtuais, perfis controlados de tráfego e falha, análise de dados e inteligência artificial para configuração e recuperação segura.

### 4.2 Objetivos

A numeração dos objetivos expressa a ordem em que eles se sustentam, de modo que a fundação experimental anteceda as disciplinas que lhe conferem validade e que ambas antecedam as capacidades que delas derivam. A exposição está organizada em três camadas, cuja função é tornar explícita a relação de dependência entre os objetivos permanentes e evitar que a ordem de leitura seja tomada como cronograma de execução, matéria que pertence aos documentos derivados.

#### Camada 1 — Fundação Experimental

Esta camada antecede as demais porque delimita a condição mínima de existência de um experimento, ou seja, enquanto não for possível configurar, executar, observar e desfazer um cenário de maneira controlada, não há objeto sobre o qual incidam avaliação, comparação ou inferência.

| **ID**           | **Objetivo**                                    | **Resultado Pretendido**                                                                                                 |
| ---------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **OBJ&#8209;01** | Prover configuração multiplataforma de cenários | O mesmo modelo conceitual de cenário pode ser realizado em ambientes físicos, virtuais, simulados e híbridos compatíveis |
| **OBJ&#8209;02** | Tornar a preparação e a reversão eficientes     | Cenários são aplicados, verificados e desfeitos com esforço manual mensurável e progressivamente menor                   |
| **OBJ&#8209;03** | Reproduzir tráfego, degradações e falhas        | Perfis versionados permitem repetir e combinar condições normais e adversas de modo controlado                           |

Cabe registrar que **OBJ-02** constitui objetivo de tendência e sua conclusão não se verifica em um instante determinado, mas na comparação sucessiva com uma linha de base medida ao longo do tempo, razão pela qual sua avaliação depende de instrumentação estabelecida desde os primeiros
experimentos.

#### Camada 2 — Disciplinas Contínuas

As disciplinas reunidas nesta camada não constituem entrega de etapa alguma, mas condição de validade que incide sobre todo experimento desde o primeiro. Sua instituição tardia é onerosa e retroage sobre o que já foi produzido, uma vez que proveniência, reprodutibilidade e rastreabilidade não podem ser atribuídas a posteriori a resultados obtidos sem elas. Sendo assim, o avanço de um *milestone* pode instituí-las ou reforçá-las, mas nenhum dos *milestones* as encerra.

| **ID**           | **Objetivo**                                            | **Resultado Pretendido**                                                                                                               |
| ---------------- | ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **OBJ&#8209;04** | Assegurar integridade e reprodutibilidade experimental  | hipótese, configuração efetiva, execução, dados, análise, resultado e limitações permanecem vinculados e auditáveis                    |
| **OBJ&#8209;05** | Instituir boas práticas e padrões para dados e análises | dados e resultados possuem proveniência, qualidade, semântica, transformação, incerteza e condições de reutilização declaradas         |
| **OBJ&#8209;06** | Preservar continuidade e aprendizagem institucional     | novos participantes compreendem, reproduzem e aperfeiçoam experimentos com base em conhecimento explícito e rastreável                 |
| **OBJ&#8209;07** | Sustentar evolução coerente                             | novas capacidades demonstram valor científico, tecnológico, formativo ou institucional superior ao custo e à complexidade introduzidos |

#### Camada 3 — Capacidades Avançadas

As capacidades desta camada dependem das duas anteriores e guardam entre si uma ordem de precedência própria pela programabilidade e pela comparação entre ambientes que antecedem a inferência. A inferência, desta forma, antecede a atuação e a inversão dessa ordem produziria uma decisão automatizada sobre base cuja fidelidade não foi avaliada, sendo que essa hipótese é expressamente rejeitada por §3.3.

| **ID**           | **Objetivo**                                                                  | **Resultado Pretendido**                                                                                                                                               |
| ---------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **OBJ&#8209;08** | Desenvolver redes programáveis e funções virtualizadas                        | SDN/NFV ampliam a composição, o isolamento e a investigação de cenários sem acoplamento obrigatório a uma implementação única                                          |
| **OBJ&#8209;09** | Calibrar modelos digitais e integrar resultados físicos, virtuais e simulados | Sombras e gêmeos digitais são calibrados contra medição física reservada; diferenças entre ambientes são medidas, explicadas e consideradas na validade das conclusões |
| **OBJ&#8209;10** | Aplicar IA à configuração e ao diagnóstico                                    | Modelos produzem recomendações avaliadas contra linhas de base, com confiança e limites explícitos                                                                     |
| **OBJ&#8209;11** | Desenvolver autorrecuperação de rede segura e progressiva                     | Mecanismos detectam, diagnosticam, atuam, verificam e revertem dentro das políticas de atuação previamente avaliadas                                                   |

**OBJ-08** habilita e fortalece a fundação experimental, ampliando a composição e o isolamento de cenários, e não constitui uma trilha tecnológica autônoma (§2.5). **OBJ-11**, por sua vez, exige, além do que estabelece **OBJ-10**, uma política de atuação declarada, sua reversão verificada e os caminhos de comando e observação independente do mecanismo que atua, conforme a condição
de promoção fixada no §3.3.

---

## 5. Medidas de Sucesso

### 5.1 Regras de Mensuração

Cada objetivo deve possuir ao menos uma medida observável, pela razão de que objetivo cujo atingimento não pode ser observado não se distingue da afirmação de que foi atingido. Uma medida somente sustenta decisão quando declara definição, unidade, população ou denominador, fonte, período, regra de cálculo, responsável, qualidade dos dados, incerteza e limitações — contrato mínimo que segue o modelo de informação de medição da literatura normativa [ISO15939] e a disciplina de declaração de incerteza exigida de laboratório de ensaio e calibração [ISO17025]. Metas numéricas serão estabelecidas após a obtenção e a aprovação de linhas de base; este Termo não inventa valores sem evidência. Medida cujo valor esperado é zero expressa **limite de política**, e não meta derivada de linha de base.

As medidas avaliam a capacidade permanente da plataforma. Critérios de aceite de uma entrega, desempenho de uma execução e níveis de serviço pertencem, respectivamente, ao projeto, ao cenário executado e ao instrumento operacional aplicável.

### 5.2 Matriz de Medidas

| **ID**          | **Medida**                         | **Definição Mínima**                                                                                                                                      | **Objetivos**                            |
| --------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **MS&#8209;01** | Tempo para cenário pronto          | Tempo entre solicitação válida e ambiente configurado, verificado e apto à execução                                                                       | OBJ&#8209;01, OBJ&#8209;02               |
| **MS&#8209;02** | Cobertura declarativa              | Parâmetros aplicáveis descritos em perfis versionados ÷ parâmetros necessários à execução                                                                 | OBJ&#8209;01, OBJ&#8209;02               |
| **MS&#8209;03** | Portabilidade de cenário           | Perfis executados em ambiente alvo sem alteração semântica ÷ tentativas de portabilidade, com registro das dimensões que exigiram alteração quando houve  | OBJ&#8209;01, OBJ&#8209;09               |
| **MS&#8209;04** | Reprodutibilidade independente     | Reproduções que satisfazem os critérios por operador distinto ÷ tentativas elegíveis                                                                      | OBJ&#8209;03, OBJ&#8209;04, OBJ&#8209;06 |
| **MS&#8209;05** | Fidelidade dos perfis              | Diferença entre comportamento solicitado e comportamento observado de tráfego, degradação ou falha                                                        | OBJ&#8209;03                             |
| **MS&#8209;06** | Integridade experimental           | Execuções utilizáveis com manifesto, configuração efetiva, dados e evidência válidos ÷ execuções declaradas utilizáveis                                   | OBJ&#8209;04                             |
| **MS&#8209;07** | Qualidade e proveniência dos dados | Conjuntos promovidos que satisfazem contratos, controles de qualidade e proveniência ÷ conjuntos promovidos                                               | OBJ&#8209;05                             |
| **MS&#8209;08** | Reprodutibilidade analítica        | Resultados reproduzidos a partir dos mesmos dados, código, ambiente, parâmetros e sementes, dentro da tolerância declarada ÷ tentativas elegíveis         | OBJ&#8209;05                             |
| **MS&#8209;09** | Validade entre ambientes           | Erro, viés e incerteza por indicador nas comparações entre ambientes, com faixa de validade declarada                                                     | OBJ&#8209;09                             |
| **MS&#8209;10** | Valor incremental da IA            | Desempenho contra linha de base, com incerteza, custo dos erros, robustez e condições de validade                                                         | OBJ&#8209;10, OBJ&#8209;11               |
| **MS&#8209;11** | Efetividade da recuperação         | Eventos elegíveis recuperados dentro dos critérios ÷ eventos de recuperação iniciados                                                                     | OBJ&#8209;11                             |
| **MS&#8209;12** | Segurança da recuperação           | Ações fora da política de atuação, sem autorização, sem verificação ou sem possibilidade de interrupção; limite de política: zero                         | OBJ&#8209;11                             |
| **MS&#8209;13** | Reversão bem-sucedida              | Reversões que restauram estado seguro e verificável ÷ reversões necessárias                                                                               | OBJ&#8209;02, OBJ&#8209;11               |
| **MS&#8209;14** | Transferência de conhecimento      | Entregas promovidas com responsável, documentação e reprodução independente ÷ entregas promovidas                                                         | OBJ&#8209;06                             |
| **MS&#8209;15** | Sustentabilidade da expansão       | Capacidades promovidas com valor e custo de ciclo de vida avaliados ÷ capacidades promovidas                                                              | OBJ&#8209;07                             |
| **MS&#8209;16** | Composição programável             | Cenários elegíveis realizados por mecanismos SDN/NFV reutilizáveis ÷ cenários elegíveis, acompanhados do consumo de recursos e da interferência observada | OBJ&#8209;08                             |
| **MS&#8209;17** | Maturidade de autonomia            | Distribuição das classes de ação, por ambiente, segundo o nível demonstrado, aceito e vigente, acompanhada do número de regressões no período             | OBJ&#8209;10, OBJ&#8209;11               |

Definições operacionais, fonte de evidência, metas e horizontes devem residir em catálogo ou *codebook* versionado. As revisões da plataforma devem registrar os valores observados, a qualidade dos dados, a decisão resultante e a necessidade de alterar objetivo, capacidade ou premissa.

---

## 6. Premissas, Incertezas e Viabilidade

As premissas seguintes não são fatos consumados. Constituem proposições necessárias à estratégia e devem ser submetidas a testes. Quando uma premissa for rejeitada, a resposta será rever a plataforma, sua arquitetura ou seu investimento, e não ocultar a divergência por meio de exceções documentais.

| **ID**           | **Premissa Estratégica**                                                                                                               | **Evidência Requerida**                                                                                                      |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **PRE&#8209;01** | Projetos temporários sucessivos podem construir e sustentar uma plataforma permanente                                                  | Incrementos reutilizados por projetos ou equipes posteriores, com responsabilidade e manutenção demonstradas                 |
| **PRE&#8209;02** | Perfis declarativos reduzem tempo e variabilidade sem impedir investigação exploratória                                                | Comparação com preparação manual, análise de exceções e avaliação dos usuários                                               |
| **PRE&#8209;03** | Uma semântica comum permite comparar ambientes físicos, virtuais e simulados                                                           | Indicadores compatíveis, experimentos pareados e diferenças quantificadas                                                    |
| **PRE&#8209;04** | A infraestrutura disponível permite iniciar redes virtuais, SDN/NFV leve, emulação de tráfego e análise de dados                       | Provas de capacidade, consumo de recursos, interferência e estabilidade em cenários representativos                          |
| **PRE&#8209;05** | Escalonamento, isolamento e evolução de hardware podem atender cargas que excedam a capacidade inicial                                 | Orçamento de recursos, filas de execução, critérios de expansão e análise de custo-benefício                                 |
| **PRE&#8209;06** | Dados experimentais terão qualidade, diversidade e volume suficientes para os casos de IA selecionados                                 | Avaliação de dados, desempenho contra linhas de base e análise de generalização                                              |
| **PRE&#8209;07** | A autonomia pode progredir com risco controlado por limites, autorização, verificação e reversão                                       | Testes adversos, violações de política iguais a zero e recuperação demonstrada em níveis anteriores                          |
| **PRE&#8209;08** | O valor científico, tecnológico, formativo e institucional compensará o custo do ciclo de vida                                         | Uso efetivo, resultados transferíveis, formação realizada e custo total acompanhado                                          |
| **PRE&#8209;09** | As autorizações de uso de radiofrequência necessárias às plantas licenciadas poderão ser obtidas e mantidas no horizonte da plataforma | Manifestação, licença ou parecer da autoridade competente, responsável técnico designado e condições de operação registradas |

### 6.1 Juízo Preliminar de Viabilidade

A documentação e o inventário existentes indicam viabilidade técnica preliminar para iniciar a proposta em escala laboratorial: há recursos para redes físicas, virtualização, simulação, instrumentação, automação, análise de dados e experimentos leves de SDN/NFV. Essa conclusão não limita a plataforma à configuração atual nem presume que todas as capacidades possam operar simultaneamente ou na escala final desejada.

Cargas concorrentes intensivas em processamento, memória, armazenamento ou interfaces de rede exigirão medição, escalonamento, isolamento e, quando justificado, expansão de capacidade. A autorrecuperação sobre ativos físicos é tecnicamente concebível como objetivo de longo prazo, mas sua viabilidade deve ser demonstrada progressivamente por classe de ação, após validação em ambientes virtuais ou simulados. Portanto, a condição atual sustenta um início incremental; não comprova antecipadamente a capacidade integral da plataforma.

---

## 7. Governança, Autoridade e Evolução

### 7.1 Relação entre Artefatos

| **Nível**                 | **Questão Orientadora**                                    | **Artefato**                                     |
| ------------------------- | ---------------------------------------------------------- | ------------------------------------------------ |
| Orientação Permanente     | Por que a plataforma existe, até onde vai e como se avalia | o presente Termo                                 |
| Planejamento              | O que será feito, em que ordem e sob que dependências      | Plano e decomposição do trabalho                 |
| Especificação verificável | O que deve existir e como se verifica                      | Requisitos e critérios de aceite                 |
| Decisão técnica           | Por que foi construído assim e o que se descartou          | Descrição de arquitetura e registros de decisão  |
| Realização                | Com o que se configura, executa e opera                    | Código, perfis de cenário, dados e procedimentos |
| Prova                     | O que de fato foi executado e observado                    | Execuções e evidências autenticadas              |
| Revisão                   | O que se aprendeu e o que muda                             | Notas de revisão e publicações                   |

Este Termo é autoritativo para a orientação estratégica, o propósito, o foco, as fronteiras e os critérios permanentes da plataforma; fatos de implementação, capacidade vigente, metas operacionais e decisões técnicas permanecem autoritativos nos respectivos documentos derivados.

### 7.2 Princípios de Decisão

- **evidência antes de alegação:** capacidade somente é declarada disponível após demonstração identificável;
- **configuração explícita:** estados pretendido e efetivo devem ser comparáveis;
- **reprodutibilidade proporcional:** o rigor deve ser compatível com a finalidade exploratória, comparativa ou confirmatória do estudo;
- **proveniência de ponta a ponta:** dados, código, ambiente, agentes e transformações devem permanecer vinculados;
- **separação epistêmica:** medição, simulação, inferência, recomendação e decisão não devem ser apresentadas como equivalentes;
- **segurança por progressão:** maior autonomia exige evidência acumulada, limites mais claros e recuperação demonstrada;
- **neutralidade tecnológica responsável:** componentes são substituíveis, mas sua adoção deve considerar interoperabilidade, sustentabilidade e competência disponível;
- **aprendizagem preservada:** resultados negativos e inconclusivos também integram o patrimônio experimental quando seu método é válido.
- **abertura por padrão, reserva justificada:** método, perfis de cenário, dados curados, resultados e limitações destinam-se à publicação; reserva-se o que, divulgado, exponha a operação a risco (endereçamento, configuração, credenciais, identificação de equipamento) ou descumpra confidencialidade com terceiro.

A reserva é declarada como tal e não se confunde com artefato ainda não publicado por imaturidade; a classificação é feita por tipo de artefato, não caso a caso.

### 7.3 Evolução e Contenção de Entropia

Uma expansão é coerente quando contribui de forma demonstrável para ao menos um objetivo permanente, reutiliza mecanismos comuns, define responsabilidade por todo o ciclo de vida e produz valor científico, tecnológico, formativo ou institucional superior ao custo adicional de operação e manutenção. Considera-se que a expansão aumenta a entropia técnica, operacional ou documental quando introduz duplicação de funções, ambiguidade de autoridade, dependências insustentáveis, interfaces desnecessárias, fontes de verdade concorrentes ou fragmentação de dados e conhecimento.

Nesses casos, a decisão padrão é consolidar ou simplificar a solução, mantê-la isolada como experimento ou rejeitar sua incorporação à plataforma até que evidências demonstrem benefício suficiente para justificar a complexidade acrescentada. A inovação exploratória é permitida em ambiente delimitado; sua promoção a capacidade permanente exige responsável, integração, evidência de valor e plano de ciclo de vida.

### 7.4 Revisão Documental

O *charter* deve ser revisto quando ocorrer ao menos uma das seguintes condições: rejeição de premissa estratégica, alteração relevante do mandato institucional ou dos usuários prioritários, incapacidade persistente de atingir objetivos, mudança substancial de risco, surgimento de oportunidade que altere a tese de valor ou expansão cujo custo não possa ser absorvido pelo modelo vigente.

---

## 8. Referências Bibliográficas

3RD GENERATION PARTNERSHIP PROJECT. **TS 28.100: management and orchestration; levels of autonomous network**, v. 18.0.0. Sophia Antipolis: 3GPP/ETSI, maio 2024. `[TS28100]`

ANDERSON, Allan; MCALLISTER, Chad; HARRIS, Ernie. **Product development and management body of knowledge: a guidebook for product innovation training and certification**. 3. ed. Hoboken: John Wiley & Sons, 2024. ISBN 978-1-119-82994-2. `[Anderson2024]`

BART, Christopher K. Product innovation charters: mission statements for new products. **R&D Management**, v. 32, n. 1, p. 23–34, 2002. DOI: 10.1111/1467-9310.00236. `[Bart2002]`

BART, Christopher K.; PUJARI, Ashish. The performance impact of content and process in product innovation charters. **Journal of Product Innovation Management**, v. 24, n. 1, p. 3–19, 2007. DOI: 10.1111/j.1540-5885.2006.00229.x. `[BartPujari2007]`

CRAWFORD, C. Merle. Defining the charter for product innovation. **Sloan Management Review**, v. 22, n. 1, p. 3–12, 1980. `[Crawford1980]`

EUROPEAN TELECOMMUNICATIONS STANDARDS INSTITUTE. **ETSI GS ZSM 009-1: zero-touch network and service management; closed-loop automation; enablers**, v. 1.1.1. Sophia Antipolis: ETSI, jun. 2021. `[ZSM009]`

INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 17025:2017: general requirements for the competence of testing and calibration laboratories**. 3. ed. Geneva: ISO, 2017. `[ISO17025]`

INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION; INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **ISO/IEC/IEEE 15939:2017: systems and software engineering — measurement process**. Geneva: ISO, 2017. `[ISO15939]`

INTERNATIONAL TELECOMMUNICATION UNION. **Recommendation ITU-T Y.3090: digital twin network — requirements and architecture**. Geneva: ITU-T, fev. 2022. `[ITUY3090]`

NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. **Artificial Intelligence Risk Management Framework (AI RMF 1.0)**. Gaithersburg: NIST, 2023. NIST AI 100-1. DOI: 10.6028/NIST.AI.100-1. `[NISTAIRMF2023]`

ORGANISATION FOR ECONOMIC CO-OPERATION AND DEVELOPMENT. **Frascati manual 2015: guidelines for collecting and reporting data on research and experimental development**. Paris: OECD Publishing, 2015. DOI: 10.1787/9789264239012-en. `[OECDFrascati2015]`

TM FORUM. **Autonomous networks levels evaluation methodology (IG1252)**, v. 1.2.0. Morristown: TM Forum, jul. 2024. `[TMFAN]`

WILKINSON, Mark D. et al. The FAIR Guiding Principles for scientific data management and stewardship. **Scientific Data**, v. 3, art. 160018, 2016. DOI: 10.1038/sdata.2016.18. `[Wilkinson2016]`

WORLD WIDE WEB CONSORTIUM. **PROV-DM: the PROV data model**. W3C Recommendation, 30 abr. 2013. Editores: Luc Moreau; Paolo Missier. Disponível em: <https://www.w3.org/TR/prov-dm/>. `[W3CPROVDM]`
