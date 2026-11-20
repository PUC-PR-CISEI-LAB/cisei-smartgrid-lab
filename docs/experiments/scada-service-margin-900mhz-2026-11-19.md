# SCADA Service Dimensioning and Margin in a 900 MHz FHSS Relay Backhaul

| Field       | Value                                                                                         |
| ----------- | --------------------------------------------------------------------------------------------- |
| Author      | Fernando Dantas — PUC-PR, CISEI Lab                                                           |
| Execution   | 2026-11-19                                                                                    |
| Version     | 0.4.1 — draft                                                                                 |
| Status      | Research questions redefined; characterization campaigns complete; service campaigns planned |
| Environment | Physical (radio bench) with containerized traffic generation                                  |

Version 0.4 replaces the fault-management framing of version 0.3 with the service framing
below. The environment, the characterization campaigns, and their results are unchanged.
Version 0.4.1 renames the unit behind each remote radio from gateway to field aggregator;
nothing else changes.

---

## 1. Research definition

### 1.1 Context

Distribution automation reaches reclosers and remote-controlled switches through private
radio backhauls. The supervisory control and data acquisition (SCADA) master polls these
devices and sends commands over the same channel; when a configured response timeout
expires for the configured number of retries, the master declares a communication failure
for the device [CEPEL2020]. From that instant the operator loses supervision and remote
control of that point of the feeder.

Each remote radio serves a field aggregator with a network of endpoints behind it. When the aggregator
forwards each endpoint session end to end, the master polls every endpoint individually
[Zambenedetti2005]. The engineering question in planning such a backhaul is how much
supervision it can carry — how many endpoints, at which polling rate, at which depth of a
tree of store-and-forward relays — and how much margin remains before sessions start to
fail. The research addresses this question for a frequency-hopping spread-spectrum (FHSS)
backhaul in the 902–928 MHz band.

The term *field aggregator* is used instead of *gateway* because, in utility practice, *gateway*
also designates the access point at the head end of the backhaul and, in the radio
configuration, the parent radio of a remote. The aggregator is named for its effect on the
backhaul in all of its modes: the sessions of many endpoints carried over a single radio link.

### 1.2 Research questions

- **RQ1 — Supervision capacity.** For field aggregators that forward each endpoint session, what is
  the largest service load (endpoints per aggregator and polling rate) at each depth of the
  relay tree for which every endpoint session meets the declared acceptance criteria?
- **RQ2 — Margin erosion.** How does that capacity erode as the radio link margin of a hop
  decreases, and in the presence of competing traffic (event bursts, bulk metering
  transfers, network management collection)?
- **RQ3 — Governing mechanisms and prediction.** Which radio mechanisms determine
  transaction time and capacity — forwarding at the relays synchronized to the hopping
  dwell, phase locking between the polling period and the dwell, packet concatenation, and
  queueing — and can a calibrated simulation model predict supervision capacity beyond the
  bench configuration within a declared error?
- **RQ4 — Visibility of erosion.** Does the in-band network management — SNMP polling
  through the radio network, the view an operator has — show margin erosion before
  endpoint sessions fail, measured against the out-of-band laboratory instrumentation?

### 1.3 Scope

The scope is the radio backhaul as carrier of SCADA supervision. Aggregators and endpoint
networks are represented by the sessions and traffic they place on the backhaul; their
internal behaviour is outside the scope. The research does not attribute degradations to
causes: degradations are imposed as declared factors, and their effect is measured on the
service. Acceptance criteria are declared before data collection.

## 2. Service model and factors

### 2.1 Service and margin

- **Endpoint session**: the master's association with one endpoint, carrying periodic
  polls, event reports, and commands as transactions of request and response.
- **Communication failure**: the declaration by the master, under the rule of section 4.3,
  that a session has stopped responding.
- **Supervision capacity**: the largest service load for which every session meets the
  acceptance criteria of section 4.2.
- **Load margin**: supervision capacity divided by the offered service load.
- **Link margin to service failure**: the attenuation, in dB, that a hop tolerates at a
  given service load before an acceptance criterion fails. It differs from the radio link
  margin over receiver sensitivity, which says nothing about the service.

### 2.2 Factors

| Factor            | Levels                                                                                     | Imposed by                                  | Status  |
| ----------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------- | ------- |
| Service load      | Endpoints per aggregator; polling period                                                   | Traffic agents                              | Planned |
| Depth             | 1, 2, and 3 hops                                                                           | Relay tree (section 3.1)                    | Fixed   |
| Link margin       | Attenuation steps on the hops reaching N4, N2, and N3                                      | Step attenuators                            | Planned |
| Competing traffic | Event bursts, bulk transfer, network management collection interval                        | Traffic agents; collection configuration    | Planned |
| Polling phase     | Polling period commensurate or not with the 100 ms dwell; phase randomized per session     | Agent schedule                              | Planned |
| Aggregator mode   | End-to-end forwarding first; SCADA data concentrator and metering collector later          | Traffic model                               | Planned |

The relay tree places one remote at each depth, so that the service can be measured at
1, 2, and 3 hops on the same radio network. A natural link-margin erosion occurred during
campaign A: the margin of hop N5 → N3 decreased from approximately 16 dB to 0 dB across
six runs and was corrected by re-tightening a connector (section 5). It was not imposed,
and its start time is not known with precision; it is retained as an observed record.

## 3. Environment

### 3.1 Radio network

The physical testbed comprises six industrial FHSS radios operating in the 902–928 MHz ISM
band. The modem rate is fixed at 1.25 Mbit/s, with rate adaptation disabled. All radios
share a single collision domain. The topology comprises one access point (AP), two
store-and-forward relays (SAF), and three remote radios (RM).

| Node | Role | Depth | Antenna chain                                   |
| ---- | ---- | ----- | ----------------------------------------------- |
| N4   | AP   | 0     | 30 dB fixed attenuator, step attenuator at 0 dB |
| N2   | RM   | 1     | 30 dB fixed attenuator, step attenuator at 0 dB |
| N5   | SAF  | 1     | 30 dB fixed attenuator                          |
| N1   | RM   | 2     | Magnetic-base antenna, no attenuator            |
| N3   | SAF  | 2     | 30 dB fixed attenuator, step attenuator at 0 dB |
| N6   | RM   | 3     | Magnetic-base antenna, no attenuator            |

```mermaid
flowchart TD
    N4["N4 — AP"] --> N2["N2 — RM (1 hop)"]
    N4 --> N5["N5 — SAF (1 hop)"]
    N5 --> N1["N1 — RM (2 hops)"]
    N5 --> N3["N3 — SAF (2 hops)"]
    N3 --> N6["N6 — RM (3 hops)"]
```

Per-hop margin over the sensitivity of the 1.25 Mbit/s mode (−95 dBm) at the start of the
bench condition. The value is the average RSSI that each child reports for its parent; the
averaging period is not documented by the manufacturer.

| Hop (parent → child, received at child) | Average RSSI (dBm) | Margin (dB) |
| --------------------------------------- | ------------------ | ----------- |
| N4 → N2                                 | −77                | 18          |
| N4 → N5                                 | −78                | 17          |
| N5 → N1                                 | −68                | 27          |
| N5 → N3                                 | −75                | 20          |
| N3 → N6                                 | −41                | 54          |

The step attenuators on N4, N2, and N3 impose the link-margin factor on the hops that
reach those nodes.

### 3.2 Traffic generation and application metrics

Each radio is connected through its Ethernet interface to an edge computer executing the
laboratory traffic agent in a Kubernetes-orchestrated container. Traffic sources are
attached to remote radios N1, N2, and N6; the UDP reflector is attached to the AP, N4.
All sources within a run start at the same wall-clock instant.

In campaigns A–C the traffic is a **synthetic reference workload**: remote-originated,
symmetric UDP echo at selected rates. It is not derived from any SCADA traffic model and
represents no service condition; it serves only as a reproducible load for network
characterization. Campaign D uses the service workload of section 4.2 instead. The
definitions below apply to both workloads.

- **Datagram**: UDP, 200 bytes of payload, carrying run identifier, flow, sequence
  number, step number, and the sender's monotonic transmission time.
- **Reflector**: returns every received datagram to its source, marked as a reply, with
  the same size.
- **Response matching**: by run, flow, and sequence number. Duplicate replies are counted
  separately and do not count as responses; reordered replies are counted.
- **Step attribution**: a response is attributed to the step in which its request was
  sent. The first 10 s of each step are excluded from the step's measurement.
- **Response timeout**: a request is counted as lost if no response has arrived by the end
  of the run plus 5 s.
- **Application loss**: requests without a response. Echo loss combines outbound-path
  loss, reflector behaviour, and return-path loss, which cannot be separated in the
  present data.
- **RTT**: measured on the sender's monotonic clock. All RTT statistics are conditional
  on received responses.
- **Longest silence**: the longest interval without any response within a step. In
  campaigns A–C it is the only application-side indicator of an interruption; campaign D
  replaces it with the communication-failure instant of each emulated master session
  (section 4.3).
- **Per-packet timing** is not preserved; the agent keeps per-step aggregates.

### 3.3 Network observation

Two planes observe the radios, and they are kept distinct.

- **In-band network management.** The network under test has its own management, as an
  operator would run it: SNMP and ICMP polling of each radio through the radio network
  itself. This traffic traverses the radio channel, is part of the load the channel
  carries, and stops arriving when the path to a radio degrades. Its view of the network
  is the subject of RQ4.
- **Out-of-band laboratory instrumentation.** The laboratory polls the same radios with the
  Simple Network Management Protocol (SNMP) over a separate wired network that does not use
  the radio channel, at 30 s during campaigns A–C and window R and at 15 s from 2026-11-20.
  It keeps arriving when the radio network degrades and is the source of the radio
  telemetry reported here and in the dataset.

The monitored variables comprise:

- per radio: average RSSI and LQI of the link to the parent; MAC counters of frames
  transmitted, retransmissions, and failures after the retransmission limit; sync
  changes; temperature; alarms;
- per remote, in the AP's table: downlink RSSI, LQI, and SNR, which carry each remote's
  reception of its own parent and therefore describe every hop of the tree; and uplink
  RSSI, LQI, and SNR, which describe the AP's reception of the last hop only;
- per hopping channel: average RSSI and LQI.

These variables define the observation constraints relevant to RQ4:

- the relays do not report their children, so the child-to-parent direction is observed
  only on hops that reach the AP;
- LQI is a proprietary quality index, not a quantity in dB;
- the MAC counters account for every frame transmitted over the air, including frames
  forwarded by a relay; the interface counters of the radio account only for traffic
  crossing the radio's local bridge and exclude forwarded payload; the AP's per-remote
  packet counters account for management traffic and do not measure application payload;
- the radios concatenate up to four packets per over-the-air frame, so MAC frame counts
  and application packet counts are not interchangeable under load.

On the day of the campaigns, the collected values were checked field by field against the
radios' command-line interface on all six radios and on the five entries of the AP's
table, without divergence; the counter semantics above were verified against the imposed
loads of the capacity ramps. Samples are timestamped at polling initiation; observed
polling duration had a median of approximately 4 s and a maximum of 20 s.

## 4. Experimental protocol

**Rate convention.** Every rate in this document is the UDP payload bit rate offered by a
source, excluding IP, UDP, and Ethernet headers, radio framing, acknowledgments, and
retransmissions.

### 4.1 Characterization regimes

The characterization regimes describe the radio network under the synthetic reference
workload (section 3.2). They characterize capacity and delay; they do not define a service
condition.

| Regime                                    | Senders                     | Load                                                                                                                                         |
| ----------------------------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Idle (`idle`)                             | N1, N2, and N6 together     | 1.6 kbit/s probe each (1 datagram/s), 5 steps                                                                                                |
| Capacity (`capacity`)                     | One sender at a time, alone | 16, 32, 64, 128, 192, 256, 384, 512, 640, 768, 896, 1024 kbit/s; stops after two consecutive steps with loss above 20 % or RTT p95 above 3 s |
| Synthetic reference (`nominal` in records) | N1, N2, and N6 together     | 16 kbit/s each, 8 steps                                                                                                                      |

Steps last 60 s, with the first 10 s excluded from measurement, and runs are separated by
a 60 s pause. The capacity ramp is adapted from the throughput search of RFC 2544
[RFC2544]; metrics follow the IP performance metrics framework [RFC2330].

**Synthetic reference workload.** The 16 kbit/s per source is a selected load, below the
loss onset of every path in the capacity ramps (section 6.2). It is not a nominal service
condition: low aggregate loss under this load does not establish that a service would be
met, and the within-run delay drift reported in section 6.3 shows that the reference is
not stationary. Concurrent operation of three sources adds demand through repeated
forwarding over the shared channel; the hop-weighted outgoing payload rate is
16 + 2 × 16 + 3 × 16 = 96 kbit/s, or approximately 192 kbit/s including successful
replies, excluding protocol overhead. This quantity is a payload transmission proxy, not
measured airtime.

### 4.2 Service workload for campaign D (to be declared)

Campaign D uses a service workload derived from SCADA traffic over the backhaul, not the
synthetic reference. Each remote radio serves a field aggregator in transparent-router mode, which
forwards the session of every endpoint behind it end to end; the SCADA master polls each
endpoint individually, as documented for distribution automation over serial-to-IP
converters [Zambenedetti2005]. The workload is fully declared in the campaign
descriptor before any campaign D run, with the following content:

| Element              | Declaration                                                                                                                                                                                                     |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Traffic matrix       | Master attached to the AP (N4); field aggregators at N1, N2, and N6; number of endpoints per aggregator; direction of each flow (master-originated polls and commands, endpoint-originated event reports and confirmations) |
| Timing               | Event-poll period per endpoint, start offsets between endpoints, integrity-scan period, connection keep-alive period, clock-synchronization period, and the instants of declared event bursts and commands  |
| Message sizes        | Request and response sizes per message type, from the DNP3 framing, with the transport overhead stated                                                                                                         |
| Transaction behavior | At most one outstanding transaction per endpoint session; response timeout; retry count; the rule by which an endpoint session is declared in communication failure                                          |
| Acceptance criteria  | Per endpoint session and per run: transaction success ratio, upper percentile of transaction time, number of communication failures (zero required), longest silence below the failure horizon, and absence of a monotonic trend in transaction time across the run |
| Operating margin     | Ratio of the offered service load to the measured loss onset of each path (section 6.2), and verification that the acceptance criteria still hold at a declared multiple of the service load            |

A validation run at the declared service workload, with no imposed degradation, must meet every acceptance
criterion before campaign D starts. Only then is the workload designated the reference
service condition of the bench, to which capacity and margins are referred.

### 4.3 Dimensioning and margin-erosion protocol (planned)

Campaign D comprises two kinds of run, each recorded with its declared factors.

1. **Capacity search** (RQ1): at a declared aggregator mode and polling phase, the service
   load increases in declared steps — endpoints per aggregator, then polling rate — until an
   acceptance criterion fails in two consecutive steps. The supervision capacity is the
   last step at which every criterion holds. The procedure adapts the throughput search of
   RFC 2544 [RFC2544] from packets to service sessions.
2. **Margin erosion** (RQ2): at a declared fraction of the measured capacity, the
   attenuation on one hop increases in declared steps until an acceptance criterion fails,
   giving the link margin to service failure of that hop at that load. The same run is
   repeated with competing traffic.

The emulated master follows the declared communication-failure rule: after each scheduled
request, or a keep-alive request on an idle session, it waits the response timeout and
repeats up to the declared number of attempts; when all attempts fail, the session is
declared failed. Timeout and attempts are configurable in the master [CEPEL2020] and are
declared parameters of the campaign. Because the master notices a degradation only at its
next request, the delay from onset to declaration lies between attempts × timeout and the
request interval plus attempts × timeout, and the sessions behind one aggregator fail at
instants spread over approximately one request interval.

For each run the analysis reports, per session, the transaction-time distribution, the
transaction success ratio, and the communication-failure instants; per aggregator, the
capacity and the margins of section 2.1; and, for RQ4, the instant at which each monitored
telemetry signal departs from its reference distribution, compared with the first and the
last session failure behind each aggregator. Polling periods both commensurate and
incommensurate with the dwell are run, with the phase randomized per session and per run,
because phase locking changes transaction time (section 6.5). Runs at the reference service
load are interleaved with the dimensioning and erosion runs as controls.

## 5. Campaigns and experimental runs

| Campaign | Regime         | Runs | Senders                                  | Status                                                                                                                                                                                  |
| -------- | -------------- | ---- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A        | Idle, capacity | 6    | —                                        | Retained as the record of a natural link-margin erosion (hop N5 → N3 margin decreasing from approximately 16 dB to 0 dB, corrected by connector re-tightening); excluded from the reference |
| B        | Idle           | 3    | N1, N2, and N6                           | Complete                                                                                                                                                                                |
| B        | Capacity       | 6    | N2 (1), N1 (2), N6 (3), two repetitions  | Complete                                                                                                                                                                                |
| C        | Synthetic ref. | 5    | N1, N2, and N6                           | Complete                                                                                                                                                                                |
| D        | Capacity, erosion | — | Master at N4; aggregators at N1, N2, N6  | Planned (sections 4.2, 4.3)                                                                                                                                                               |

Each run has a unique identifier and an execution record specifying the offered load per
source and step, start time, step duration, termination criterion, and, for campaign D,
the declared service load, attenuation steps, competing traffic, and polling phase.

## 6. Results of the characterization campaigns

The results characterize the three source-to-AP paths in the specified topology. Because
each depth is represented by a single source, depth is confounded with device identity,
path, link conditions, and branch position. Repeated runs quantify repeatability within
this configuration but do not isolate the effect of hop count.

### 6.1 Idle

RTT p95 per step, median over the three runs, with the 1.6 kbit/s probe:

| Sender (depth) | RTT p95 (ms) |
| -------------- | ------------ |
| N2 (1)         | 12.6         |
| N1 (2)         | 162          |
| N6 (3)         | 213          |

Differences in idle RTT p95 between adjacent depths range from approximately 50 to 150 ms.
Frequency-hopping dwell timing is a possible contributing mechanism; it was not measured,
and the present design does not isolate it from other path-dependent effects.

### 6.2 Capacity

Loss per step in the two repetitions of campaign B, with the number of measured requests
per step in parentheses (50 s × rate ÷ 1600 bit):

| Sender (depth) | 64 kbit/s (2000) | 128 kbit/s (4000) | 192 kbit/s (6000) | Last step           | RTT p95 at last step (ms) |
| -------------- | ---------------- | ----------------- | ----------------- | ------------------- | ------------------------- |
| N2 (1)         | 0 % / 0 %        | 0 % / 0 %         | 22.6 % / 23.0 %   | 384 kbit/s: 61 %    | 387 / 388                 |
| N1 (2)         | 0 % / 0 %        | 1.9 % / 1.8 %     | 24.6 % / 23.4 %   | 384 kbit/s: 61–62 % | 432 / 442                 |
| N6 (3)         | 0 % / 0 %        | 7.2 % / 11.1 %    | 49.2 % / 47.7 %   | 256 kbit/s: 61–63 % | 646 / 662                 |

- **Loss onset** (first step with observed loss): between 128 and 192 kbit/s for N2;
  between 64 and 128 kbit/s for N1 and N6. Zero losses in 2000 requests at 64 kbit/s bound
  the loss at that step below 0.18 % (exact 95 % binomial interval), not at zero.
- **Severe degradation** (crossing of 20 % loss): between 128 and 192 kbit/s on all three
  paths.
- **Stopping criterion** reached at 384 kbit/s for N2 and N1, and at 256 kbit/s for N6.

Differences between the two repetitions are approximately 4 percentage points or less. At
the terminal steps, RTT p95 characterizes only the 37–40 % of requests receiving a
response. Transition locations are reported as intervals bounded by successive tested
rates. These ramps bound the payload capacity of each path; supervision capacity (RQ1) is
measured in campaign D with the service workload.

### 6.3 Synthetic reference workload

Five runs with the three sources at 16 kbit/s each; 4000 measured requests per sender per
run:

| Sender (depth) | Measured requests | Lost | Loss    | Exact 95 % interval |
| -------------- | ----------------- | ---- | ------- | ------------------- |
| N1 (2)         | 20 000            | 7    | 0.035 % | 0.014 – 0.072 %     |
| N2 (1)         | 20 000            | 11   | 0.055 % | 0.028 – 0.098 %     |
| N6 (3)         | 20 000            | 1    | 0.005 % | 0.0001 – 0.028 %    |

For the counts aggregated over five runs, the upper limits of the three intervals are
below the 10⁻³ packet loss objective of classes 0–4 in ITU-T Y.1541 [ITUY1541, Table 1].
The comparison is restricted to the loss objective; one-way delay was not measured, and
RTT p95 does not substitute for it. Binomial intervals assume independent trials and do
not account for temporal dependence or between-run variation.

These results describe the synthetic reference workload only. They do not establish a
nominal service condition, which campaign D defines separately (section 4.2).

Within each run of the synthetic reference workload, RTT p95 decreased monotonically;
for example, N1 decreased from approximately 143 to 108 ms across eight steps. The mechanism was not identified. A
reference that drifts within a run affects the measurement of margin erosion (RQ2); the
probable mechanism is described in section 6.5.

### 6.4 Application silences

The longest interval without responses was at most 0.44 s during the capacity ramps and
7.2 s during idle probing, the latter corresponding to approximately seven consecutive
missing probes at 1 datagram/s. Silence lengths depend on the probing rate and are not
comparable across regimes. No characterization run produced a silence long enough to
cause communication failure at a SCADA master with a response timeout and retry count of
the order of tens of seconds; the reference therefore contains no application-level
failures.

### 6.5 Relay delay and polling phase (preliminary)

Within each run of the idle and reference regimes, the round-trip time at depths 2 and 3
is nearly constant: the spread within a 60 s step is between 1 and 10 ms. Across the steps
of a run it changes linearly, and it then jumps by approximately one dwell; in one
reference run, the depth-3 median fell from 184 to 164 ms over six steps and then rose to
258 ms. The polling periods used (1 s and 100 ms) are integer multiples of the 100 ms dwell,
so every request reaches the relays at the same phase of the hopping cycle; a slow drift
between the clocks of the edge computers and of the radios moves that phase. The working
hypothesis is that the relays forward at transmit opportunities synchronized to the dwell,
and that the measured relay delay is the wait for that opportunity at the phase of the
run. A simulation with a single opportunity per relay per dwell does not reproduce the
bench: it cannot produce the approximately 53 ms that the second relay adds, which is about
half a dwell. The hypothesis is tested in campaign D with polling periods incommensurate
with the dwell. Until then, round-trip times at depths 2 and 3 are conditional on an
unknown phase, and section 6.1 reports one phase per run.

## 7. Measurement constraints

**Temporal alignment.** The nominal 30 s polling interval provides approximately two
samples per 60 s step. Analysis retains only counter intervals wholly contained within a
measurement window and flags intervals crossing boundaries. Actual polling timestamps and
durations are recorded. Edge-computer clock offsets were not verified during the
characterization campaigns; campaign D records clock offsets per run, since session
events and telemetry are aligned across hosts (RQ4).

**Reference drift.** The synthetic reference runs were executed as a block. Campaign D
interleaves control runs at the reference service load with the dimensioning and erosion
runs, so that capacity and margins are referred to a reference that spans the same period.

**Counter coverage.** A degradation on a hop whose child-to-parent direction is not reported
(section 3.3) is observable only through the parent-to-child direction, the MAC counters
of the nodes involved, and the effect on downstream nodes. This constraint bounds the
erosion that the operations centre can observe (RQ4) and is reported per hop.

**Traffic-generation verification.** The achieved source rate matched the configured rate
(10.01 datagrams/s at 16 kbit/s), and per-step request counts matched the planned counts.
Socket-drop counters and reflector health metrics were not recorded.

## 8. Limitations

- Short-range bench: path losses and interference do not represent a field link.
- Modem rate fixed at 1.25 Mbit/s: other rates are another experimental condition.
- A single collision domain for the six radios: a degradation on one branch can affect the
  whole tree.
- One source per depth: depth effects are confounded with path and device (section 6).
- Management traffic is carried over a wired network in this bench; a field deployment in
  which management traffic shares the radio channel is a distinct condition.
- The SCADA communication-failure horizon is a declared parameter, not a value measured
  on an operational system.

## 9. Availability

Complete run records and time series remain in the laboratory's custody. Public data are
released by version in `data/cisei-ssm-t4-characterization/`, each version with a dataset card,
a codebook, and a manifest of SHA-256 hashes, and with a persistent identifier assigned at
release. Version 0.1.0 contains the characterization windows A–C and the idle reference window
R; campaign D data enter later versions. Intervals with generated traffic outside the scope of
this study are withheld and listed in the dataset card.

## References

BRADNER, S.; McQUAID, J. **Benchmarking methodology for network interconnect devices**.
RFC 2544. [S. l.]: Internet Engineering Task Force, 1999. Available at:
https://www.rfc-editor.org/rfc/rfc2544. `[RFC2544]`

CENTRO DE PESQUISAS DE ENERGIA ELÉTRICA. **Documento de interoperabilidade do protocolo
DNP V3.0 no SAGE**. Rio de Janeiro: CEPEL, Oct. 2020. 7 p. Available at:
https://sage.cepel.br/images/protocolos/profile_sage_dnp.pdf. Accessed on: 19 Nov. 2026.
`[CEPEL2020]`


INTERNATIONAL TELECOMMUNICATION UNION. **Recommendation ITU-T Y.1541: network performance
objectives for IP-based services**. Geneva: ITU, 2011. Available at:
https://www.itu.int/rec/T-REC-Y.1541-201112-I. `[ITUY1541]`

PAXSON, V. *et al*. **Framework for IP performance metrics**. RFC 2330. [S. l.]: Internet
Engineering Task Force, 1998. Available at: https://www.rfc-editor.org/rfc/rfc2330.
`[RFC2330]`

ZAMBENEDETTI, V. C.; COUTINHO, F. R.; BARBIERO, A.; SIQUEIRA, R. P.; PEREIRA, J. G.;
HEXSEL, R. A. **Uso de comunicação celular digital GPRS para sistemas de automação da
distribuição de energia elétrica**. Curitiba: LACTEC; COPEL Distribuição; UFPR, [2005].
6 p. Available at:
https://www.cgti.org.br/publicacoes/wp-content/uploads/2016/01/Uso-de-Comunica%C3%A7%C3%A3o-Celular-Digital-GPRS-para-Sistemas-de-Automa%C3%A7%C3%A3o-da-Distribui%C3%A7%C3%A3o-de-Energia-El%C3%A9trica.pdf.
Accessed on: 19 Nov. 2026. `[Zambenedetti2005]`
