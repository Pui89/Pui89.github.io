# HOMEGUARD AI Architecture

## Product identity

**Multi-Modal Predictive Building Intelligence System.**

The differentiator is not a large number of model names. It is traceable evidence across multiple sensing modalities, explicit uncertainty, spatial context, safe escalation and reproducible verification.

## Six product domains

1. Structural health — vibration, strain, displacement and crack observations.
2. Electrical safety — voltage, current, power quality, protective-device status and qualified-installed arc-fault indicators.
3. Fire and life safety — certified alarm integration and emergency-status visibility.
4. Environmental and air quality — temperature, humidity, VOC and suitable gas measurements.
5. Water and moisture — leak, flow, pressure, wall moisture and condensation indicators.
6. Multi-sensory building intelligence — acoustic, light, thermal and cross-domain evidence fusion.

## Logical layers

1. **Acquisition adapters:** vendor-neutral sensor interfaces; no hardware assumed in the first milestone.
2. **Evidence contract:** sensor identity, domain, metric, units, event time, location, quality, calibration and uncertainty.
3. **Quality gate:** missing/stale data, invalid values, unit mismatch, clock problems and calibration status.
4. **Baseline and change engine:** transparent statistical methods with documented baseline periods.
5. **Fusion and world model:** relate rooms, floors, components, sensors and events. Fusion must preserve source-level evidence and avoid treating correlated measurements as independent proof.
6. **Risk and explanation:** state what was observed, what is inferred, what is unknown and why a human should review it.
7. **Reporting and interfaces:** JSON first; dashboard and APIs later.
8. **Verification loop:** synthetic tests, fault injection, regression corpus, measured pilot outcomes and reviewed releases.

## Data contract

Every observation should eventually include:
- stable observation and sensor IDs;
- building/floor/room/component location;
- metric, value and SI or explicitly documented unit;
- UTC-aware event timestamp and ingestion timestamp;
- sensor quality, calibration reference and firmware/software provenance;
- uncertainty or known measurement limits;
- source data reference and integrity checksum where appropriate.

## Initial algorithm strategy

Start with deterministic rules, signal-quality checks, baseline statistics, change-point methods and transparent feature extraction. Consider SciPy-based signal analysis and OpenSeesPy numerical simulation only after dependency and licence review. Deep learning is not required for the first demonstrator.

## Model strategy

The first demonstrator uses **no trained model**. Future models require:
- named model, publisher, ownership and provenance;
- model card, licence and permitted use;
- weights and dependency checksums;
- data residency and telemetry review;
- security and vulnerability review;
- benchmark against a non-ML baseline;
- calibration, subgroup/environment robustness and failure tests;
- explicit rollback and human approval.

No Chinese-origin models, providers or model-hosting services are approved for this project. A future exception requires explicit owner review; no silent substitution or remote model download.

## Deployment stages

Synthetic simulation → offline software evaluation → bench-tested calibrated sensors → supervised building pilot → independent validation. Each stage has a documented go/no-go review.
