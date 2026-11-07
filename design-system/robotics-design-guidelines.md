# Robotics Design Guidelines

## Shared principles
Use modular interfaces, documented wiring/connectors, sensor provenance, calibration records, power telemetry, communication-health reporting, diagnostics, safe-state behaviour and replaceable assemblies. Keep safety-critical controls independent of high-level AI where feasible.

## Physical safety
- Define emergency stop, manual override, safe hold/stop and recovery behaviour before autonomy.
- Assess stability, centre of gravity, tip-over, braking, traction, pinch/crush/entanglement hazards and human/animal interaction.
- Protect batteries and power systems with appropriate electrical design, fusing, isolation, charging and thermal management.
- Guard moving parts and provide strain relief and service access.
- Define environmental requirements; water/fire resistance is a test programme, not a visual styling claim.
- Treat all payload, reach, speed, range, ingress protection and endurance values as targets until measured.

## AI safety
High-level AI may propose actions; a deterministic safety layer validates preconditions, limits and safe-state transitions. Preserve uncertainty, provenance, timestamps and reasons for abstention. Log failures in a machine-readable form. Do not permit autonomous enforcement or unreviewed high-risk actions.

## Validation ladder
Requirements review → calculations/CAD → dependency-free tests → simulation → low-energy bench tests → controlled supervised tests → field trials only with suitable facilities and explicit approval. Do not actuate hardware through software automation.

## Project-specific cautions
- Coconut: tool force, reach, fruit retention/drop zones, worker/animal exclusion and ground stability.
- Flood: buoyancy reserve, compartmentalisation, current/wave stability, propulsion, entanglement and recovery.
- Sentinel: modality-specific evidence, calibration, privacy and authorised human review.
- HOME/NOMAD: safe indoor/outdoor navigation, tip resistance, obstacle detection, battery isolation and environmental limits.
- Car/Motorcycle: remain design/simulation-first until professional vehicle safety engineering and suitable test facilities exist.
