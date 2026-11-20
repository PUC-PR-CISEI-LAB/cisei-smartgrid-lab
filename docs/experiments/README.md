# Experiments — CISEI SmartGrid Lab

> Experimental protocols, testbed configurations, aggregate measurements, and validity
> conditions for communication-network studies conducted on the CISEI SmartGrid Lab platform.

## Scope and experimental unit

This catalogue documents controlled experiments conducted on the laboratory testbed.
Each campaign comprises experimental runs performed under a single bench condition,
defined by the physical arrangement, equipment configuration, and network topology.
Interventions that alter these conditions establish a distinct experimental condition
and must be identified in the campaign record. Results from different conditions are
reported separately unless their joint analysis is explicitly justified.

Each experimental report specifies:

1. **Research objective:** the experimental question, diagnostic target, and scope of
   inference.
2. **Experimental configuration:** topology, radio parameters, per-hop link margins,
   traffic-generation mechanisms, and measurement instrumentation.
3. **Protocol:** load regimes, rate conventions, step durations, measurement windows,
   termination criteria, and adaptations of reference methodologies.
4. **Execution record:** campaigns, run counts, repetitions, execution status, and
   exclusion criteria with their technical justification.
5. **Results:** aggregate measurements, sample counts, variability across repetitions,
   and uncertainty estimates with their statistical assumptions.
6. **Analysis and evaluation:** detection rules and thresholds declared before data
   collection, temporal observation units, and partitioning of independent experimental runs.
7. **Validity conditions:** measurement constraints, confounding factors, and limits to
   generalization beyond the evaluated configuration.

## Anonymization and configuration disclosure

In the 900 MHz SCADA service experiment, radios are designated N1–N6 and characterized by
network role (AP, SAF, or RM) and depth in the relay tree. Network addresses, equipment
identifiers, firmware versions, and third-party operational data are excluded from the
public record. Reported configuration parameters and bench measurements, including RSSI
and per-hop link margin, provide the technical context required to interpret the results.

## Data provenance and availability

Execution records and network-telemetry time series are retained by the laboratory.
Each run is associated with a unique identifier and a record of the imposed conditions:
offered load per source and step, start time, step duration, and termination criterion.
These records support temporal alignment of observations with experimental interventions
and documentation of entity–activity–agent relationships using PROV-DM [W3CPROVDM].

Dataset publication is planned as versioned releases with persistent identifiers (DOIs),
following finalization of the annotation scheme. Data curation is guided by the FAIR
principles [Wilkinson2016]. Before public release, access may be requested through the
repository's access-request issue template.

## Experiment catalogue

| Date | Report | Status |
|---|---|---|
| 2026-11-19 | [SCADA service dimensioning and margin in a 900 MHz FHSS relay backhaul](scada-service-margin-900mhz-2026-11-19.md) | Draft v0.4 — characterization complete; service campaigns planned |

## Citation

DANTAS, Fernando. **CISEI SmartGrid Lab: experiment catalogue**. Curitiba: PUC-PR, CISEI
Lab, 2026. Available at: https://github.com/PUC-PR-CISEI-LAB/cisei-smartgrid-lab.

Repository citation metadata are provided in [`CITATION.cff`](../../CITATION.cff).
Published dataset versions will be cited using their respective DOIs.

## References

MOREAU, Luc; MISSIER, Paolo. **PROV-DM: the PROV data model**. W3C Recommendation.
[S. l.]: World Wide Web Consortium, 2013. Available at: https://www.w3.org/TR/prov-dm/.
`[W3CPROVDM]`

WILKINSON, Mark D. *et al*. The FAIR guiding principles for scientific data management
and stewardship. **Scientific Data**, v. 3, p. 160018, 2016. DOI: 10.1038/sdata.2016.18.
`[Wilkinson2016]`
