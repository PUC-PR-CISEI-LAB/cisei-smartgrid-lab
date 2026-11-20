# SCADA service dimensioning in a 900 MHz FHSS relay backhaul — characterization data

*Dimensionamento do serviço SCADA em backhaul FHSS de 900 MHz com repetidores — dados de caracterização*

Version 0.1.0 · License CC BY 4.0 (repository `LICENSE`) · Report: `docs/experiments/scada-service-margin-900mhz-2026-11-19.md`

## English

Characterization data of a physical bench of six 902–928 MHz frequency-hopping radios
organized as a tree of store-and-forward relays (one access point, two relays, three
remotes at 1, 2 and 3 hops). It contains radio telemetry collected by the network operations
centre and application-level results of UDP echo traffic, for the observation windows
below. Radios are designated N1–N6; addresses, equipment identifiers and firmware are not
included. The methods, definitions and limitations are in the report.

| Window | Start (UTC) | End (UTC) | Note |
| --- | --- | --- | --- |
| A | 2026-11-19T12:48:00Z | 2026-11-19T14:02:00Z | Registro de erosão natural da margem do salto N5 → N3 (de cerca de 16 dB a 0 dB), corrigida depois por reaperto de conector; fora da referência. |
| B | 2026-11-19T14:31:00Z | 2026-11-19T15:43:00Z |  |
| C | 2026-11-19T16:51:00Z | 2026-11-19T17:40:00Z |  |
| R | 2026-11-19T23:13:00Z | 2026-11-20T11:13:00Z | Bancada ociosa, sem tráfego gerado; janela de referência da telemetria. |

Withheld intervals (traffic generated but not included):

- 2026-11-19T17:41:00Z — 2026-11-19T20:09:00Z: Carga de um emissor elevada acima da referência; regime fora do escopo deste estudo.

Files: `telemetry.csv` (183503 rows), `application_steps.csv`
(269 rows), `runs.csv` (20 rows),
`windows.csv`, `codebook.yaml`, `manifest.json` (SHA-256 of every file). Missing samples are
absent rows, never interpolated.

## Português

Dados de caracterização de uma bancada física de seis rádios de salto de frequência em
902–928 MHz, organizados em árvore com repetidores *store-and-forward* (um ponto de acesso,
dois repetidores e três remotos a 1, 2 e 3 saltos). Contém a telemetria dos rádios coletada
pelo centro de operação da rede e os resultados de aplicação do tráfego de eco UDP, nas
janelas acima. Os rádios são designados N1–N6; endereços, identificadores de equipamento e
*firmware* não estão incluídos. Métodos, definições e limitações estão no relato.

Amostra ausente é linha ausente, nunca interpolada. Os arquivos e o número de linhas são os
listados na seção em inglês; o `manifest.json` traz o SHA-256 de cada arquivo.

## Citation

Dantas, Fernando (Pontifícia Universidade Católica do Paraná (PUC-PR) — CISEI Lab). *SCADA service dimensioning in a 900 MHz FHSS relay backhaul — characterization data*, version
0.1.0. Persistent identifier: assigned at release.
