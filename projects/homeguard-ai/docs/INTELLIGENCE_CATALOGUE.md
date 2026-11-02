# HOMEGUARD AI — Intelligence Catalogue

**Status: PROPOSED PRODUCT ARCHITECTURE.** The catalogue defines intended capability areas. It does not claim that every capability is implemented, trained, integrated or validated.

## The 29 intelligence capabilities

### I. Core intelligence

1. **Evidence Integrity** — identify missing, conflicting, stale or unreliable evidence.
2. **Loss Intelligence** — identify expected assets, signals or functions that have disappeared.
3. **Change Intelligence** — compare current observations with previous valid states.
4. **Deterioration Intelligence** — identify persistent worsening trends.
5. **Predictive Intelligence** — estimate possible future conditions with calibrated uncertainty.
6. **Decision Intelligence** — prioritize verification and human review.
7. **World Model Intelligence** — represent buildings, floors, rooms, components, sensors and relationships.
8. **Root Cause Intelligence** — compare plausible explanations and counter-evidence; never equate correlation with causation.
9. **Spatial Intelligence** — locate observations and affected components.
10. **Adaptive Intelligence** — adjust monitoring priorities within reviewed limits.
11. **What-If Intelligence** — evaluate hypothetical conditions in validated simulations.
12. **Prevention & Recovery Intelligence** — track mitigation, repairs, verification and recurrence.
13. **Trust & Sensor Intelligence** — track calibration, drift, health, provenance and measurement quality.
14. **Impact Intelligence** — estimate potential consequences and urgency for human review.
15. **Relationship Intelligence** — represent dependencies and possible cascading effects.
16. **Hidden Pattern Intelligence** — identify unusual combinations and temporal sequences.
17. **Active Investigation Intelligence** — recommend the next useful observation or measurement.
18. **Confidence Calibration Intelligence** — test whether confidence estimates match observed performance.
19. **Resilience Intelligence** — evaluate missing sensors, corrupted data, outages and simultaneous faults.
20. **Knowledge Evolution Intelligence** — preserve reviewed lessons, decisions and regression cases.
21. **Continuous Improvement Intelligence** — propose, rank, test and document controlled upgrades.

### II. Environmental and sensory intelligence

22. **Acoustic Intelligence** — identify unusual sound features such as dripping, buzzing, impact or crack-like events without assuming a sound proves its cause.
23. **Odour & Gas Intelligence** — combine suitable gas/VOC sensor readings; never claim universal smell recognition.
24. **Light Intelligence** — monitor illumination, darkness, flicker and emergency-light status where instrumented.
25. **Thermal Intelligence** — identify abnormal heat distributions and hotspots using suitable temperature sensors or thermal imaging.
26. **Cold & Temperature Drop Intelligence** — identify unexpected cooling and temperature gradients.
27. **Humidity & Moisture Intelligence** — assess humidity, condensation risk and moisture trends using appropriate measurements.
28. **Multi-Sensory Fusion Intelligence** — combine independent modalities while preserving evidence provenance, dependencies and uncertainty.

### III. Electrical intelligence

29. **Electrical Intelligence** — assess voltage, current, power quality, load patterns, protective-device status and suitable arc-fault indicators.

## Nine AI and computational technology categories

These are complementary methods, not nine separate products or necessarily nine neural networks.

1. **Multimodal AI** — combine structured measurements, acoustic features, images and other approved modalities.
2. **Predictive AI** — forecast trends and possible failures when validated data supports it.
3. **World Model / Digital Twin Intelligence** — maintain a time-aware representation of building components and state.
4. **Anomaly Detection AI** — detect deviations from valid baselines.
5. **Explainable AI (XAI)** — show evidence, logic, uncertainty and limitations.
6. **Causal and Diagnostic AI** — compare hypotheses and causal mechanisms with appropriate domain models.
7. **Simulation and What-If Intelligence** — test scenarios against explicit assumptions and validated models.
8. **Agentic AI** — coordinate bounded investigation and reporting workflows; consequential actions remain human-approved.
9. **Continual Learning AI** — propose updates from reviewed evidence with regression tests, versioning and rollback.

## Six product domains

1. **Structural Health** — vibration, modal behaviour, strain, displacement and crack observations.
2. **Electrical Safety** — power, circuits, electrical equipment and protective-device status.
3. **Fire & Life Safety** — certified alarm integration and life-safety status visibility.
4. **Environmental & Air Quality** — temperature, humidity, ventilation and suitable gas measurements.
5. **Water & Moisture** — leak, flow, pressure, dampness and condensation indicators.
6. **Multi-Sensory Building Intelligence** — acoustic, light, thermal and cross-domain interpretation.

## Implementation rule

Do not build 29 disconnected features or market them as 29 AI models. Build a small shared evidence platform, then add domain adapters and validated algorithms incrementally. Each capability must have an owner, input contract, output contract, failure modes, test cases, metrics, licence/provenance review and evidence status.

## Current implementation boundary

The initial software foundation implements typed observations, baseline records, quality/calibration/unit gates, transparent baseline-deviation detection, a deterministic synthetic three-floor scenario, JSON reporting and automated tests. It does **not** yet implement production sensor fusion, a digital twin, trained multimodal models, predictive maintenance, causal diagnosis, agentic control or real-world hazard detection.
