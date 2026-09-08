# LTE privada como rede de missão crítica

> Uma rede LTE privada oferece controle local sobre acesso, cobertura e políticas;
> sua adequação a uma função crítica precisa ser demonstrada de ponta a ponta.

## O que torna uma rede privada

Uma rede celular privada é destinada a uma organização, instalação ou conjunto de
usuários delimitado. Dependendo do arranjo técnico e regulatório, a organização pode
controlar parte ou a totalidade da rede de acesso por rádio, do núcleo, das
identidades, das políticas e da integração com suas aplicações.

“Privada” descreve governança e acesso; não garante isolamento absoluto, segurança,
disponibilidade ou desempenho. Esses atributos dependem do desenho, da operação e
das dependências compartilhadas.

## Componentes essenciais

- **UE (*User Equipment*):** terminal que acessa a rede celular.
- **RAN (*Radio Access Network*):** enlace de rádio e estações que conectam os UEs.
- **núcleo de rede:** autenticação, mobilidade, sessões e encaminhamento de dados.
- **transporte:** conecta rádio, núcleo e redes de aplicação.
- **gestão e observabilidade:** configura, registra e mede o serviço.

O desempenho percebido por uma aplicação atravessa todos esses componentes. Uma boa
condição de rádio não elimina filas no transporte, processamento no núcleo ou atraso
no servidor.

## Cobertura, capacidade e qualidade do enlace

Cobertura pergunta onde o serviço pode ser recebido. Capacidade pergunta quanto
tráfego pode ser atendido sob uma combinação de largura de banda, qualidade de
canal, escalonamento e carga. Aumentar cobertura não implica aumentar capacidade.

Um orçamento de enlace relaciona potência transmitida, ganhos e perdas, propagação,
ruído e margem. Indicadores como potência recebida, qualidade de referência,
relação sinal-ruído e taxa de erro descrevem aspectos diferentes. Nenhum indicador
isolado determina a experiência da aplicação.

## Compartilhamento e QoS

O rádio é um recurso compartilhado. O escalonador distribui recursos no tempo e na
frequência conforme condições de canal e políticas. Classes de serviço podem
priorizar tráfego, mas a avaliação precisa considerar admissão, congestionamento,
sentidos de subida e descida e impacto sobre as demais classes.

Para uma função de missão crítica, o requisito deve ser fim a fim: prazo de entrega,
probabilidade de sucesso, disponibilidade, recuperação e segurança sob condições
nominais e degradadas. O nome da tecnologia não substitui esse ensaio.

## Mobilidade e continuidade

Mobilidade introduz seleção de célula, medições, troca de contexto e transferência
entre pontos de acesso. Uma mudança pode causar interrupção, reordenação ou variação
de atraso. Mesmo em instalações com terminais fixos, mudanças de propagação e
indisponibilidade de uma célula podem tornar mecanismos de seleção e recuperação
relevantes.

## Relação com a plataforma

O laboratório estuda redes celulares privadas como uma alternativa de *backhaul*
para funções de sistemas elétricos inteligentes. Os experimentos podem relacionar
condições de rádio, carga e políticas a métricas de transporte e ao comportamento da
aplicação. Faixa, potência, identidade de rede e topologia operacional pertencem ao
desenho autorizado de cada ambiente, não a esta explicação pública.

## Limites de interpretação

- Resultado com poucos terminais não demonstra escalabilidade.
- Ensaio estacionário não caracteriza mobilidade.
- Métrica de rádio não equivale a disponibilidade da aplicação.
- Rede privada não é sinônimo de rede desconectada ou imune a ataques.
- Desempenho em uma faixa ou ambiente de propagação não se transfere sem nova
  avaliação.

## Conceitos relacionados

- [Qualidade de rede](network-quality.md)
- [Ambientes experimentais](../experimentation/experimental-environments.md)
- [Segurança em tecnologia operacional](../security/defense-in-depth.md)

## Referências

Consulte `NISTsp1108r4`, `AmarisoftDigitalTwin2024`, `Testbed5GUnisinos2023`, `SmartGridSimNS3` e
`Energies2024` em [`bibliography.bib`](../../bibliography.bib).
