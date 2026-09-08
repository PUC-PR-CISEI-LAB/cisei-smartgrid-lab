# Segurança em experimentos de tecnologia operacional

> Segurança experimental protege pessoas, processo físico, infraestrutura, dados e
> continuidade da pesquisa por meio de limites técnicos e organizacionais.

## Por que OT exige contexto próprio

Em tecnologia da informação (TI), confidencialidade, integridade e disponibilidade
são objetivos clássicos. Em tecnologia operacional (OT), eles permanecem válidos,
mas segurança física, continuidade do processo, comportamento determinístico e
recuperação controlada frequentemente impõem prioridades adicionais. Uma ação
aceitável em ambiente puramente computacional pode interromper um processo ou criar
estado inseguro quando atua sobre equipamento físico.

O laboratório reduz exposição em relação a uma rede produtiva, mas não elimina
risco. Equipamentos podem ser danificados, configurações podem bloquear acesso,
tráfego pode escapar do cenário e dados podem conter informação não publicável.

## Defesa em profundidade

Defesa em profundidade combina controles independentes para que uma falha isolada
não determine o resultado. Entre as camadas conceituais estão:

- delimitação de zonas e caminhos de comunicação autorizados;
- separação entre tráfego experimental, gestão e observação;
- identidade individual e privilégio mínimo;
- autenticação, integridade e confidencialidade adequadas ao risco;
- configuração versionada e mudança revisada;
- registro de ações e detecção de comportamento inesperado;
- cópias, reversão e recuperação ensaiadas;
- barreiras físicas e supervisão humana quando aplicáveis.

Segmentação reduz caminhos possíveis, mas não é sinônimo de isolamento. Toda conexão
entre zonas constitui um conduto que precisa de finalidade, protocolo, direção e
responsável conhecidos. Um canal de gestão separado pode preservar capacidade de
diagnóstico e recuperação quando o plano experimental falha.

## Acesso e autoridade

Autenticação responde quem ou o que solicita acesso. Autorização responde o que essa
identidade pode fazer. Auditoria registra a ação e seu contexto. Controle de acesso
baseado em papéis ajuda a associar permissões a funções, mas privilégios ainda
precisam ser revisados, ter duração adequada e ser revogados quando o vínculo muda.

Em automação, a identidade do serviço não basta. A decisão também deve respeitar a
classe de mudança, o ambiente, a janela, o limite de impacto e a autoridade humana
ou institucional definida para aquele caso.

## Mudança segura

Uma mudança experimental de maior impacto deve possuir:

1. intenção e escopo declarados;
2. estado inicial conhecido;
3. validação estática e ensaio sem aplicação quando possível;
4. aprovação compatível com o risco;
5. observação durante a aplicação;
6. critérios de interrupção;
7. procedimento de reversão e verificação posterior.

Reversão não pode ser presumida. Alterações de estado, versão ou formato podem ser
irreversíveis ou exigir recuperação a partir de cópia. O procedimento precisa ser
compatível com o mecanismo real de falha.

## Pesquisa em cibersegurança

Testes ofensivos, injeção de falhas e exploração de vulnerabilidades precisam de
escopo e contenção explícitos. O fato de uma técnica ter finalidade científica não
autoriza atingir sistemas, redes ou dados fora do ambiente aprovado. Resultados
públicos devem ser sanitizados e seguir divulgação responsável quando envolverem
vulnerabilidades.

## Relação com a plataforma

Segurança funciona simultaneamente como requisito da plataforma e objeto de
experimento. Controles protegem a infraestrutura compartilhada; cenários controlados
permitem avaliar detecção, resposta e recuperação. Os resultados permanecem
condicionados à ameaça modelada e aos mecanismos presentes no ambiente.

## Conceitos relacionados

- [Infraestrutura programável](../networking/programmable-infrastructure.md)
- [Automação progressiva](../intelligence/progressive-autonomy.md)
- [Observabilidade e proveniência](../data-and-evidence/observability-and-provenance.md)

## Referências

Consulte `IEC62443`, `IEC62351`, `NISTIR7628r1`, `NISTAIRMF2023` e
`Manadhata2011` em [`bibliography.bib`](../../bibliography.bib).
