# HOMEGUARD AI Roadmap

## Stage 0 — Foundation (current)

- [x] Product scope and safety boundary documented
- [x] Evidence-first observation contract
- [x] Deterministic baseline deviation engine
- [x] Synthetic three-floor scenario
- [x] JSON report schema
- [x] Automated tests and CI definition
- [ ] Execute CI on GitHub and review results

## Stage 1 — Reliable evidence pipeline

- Add schema validation in CI.
- Add UTC clock-skew, stale-data and duplicate-event handling.
- Add source checksums, baseline versioning and report provenance.
- Add missing-sensor and sensor-drift fault injection.
- Acceptance: malformed, stale, uncalibrated and missing data are never silently classified as normal.

## Stage 2 — Multi-sensor scenario engine

- Add synthetic electrical, water, thermal, humidity, acoustic and structural channels.
- Add spatial model for building/floor/room/component.
- Add event correlation while preserving each original evidence record.
- Add alternative hypotheses and explicit uncertainty.
- Acceptance: reproducible scenario reports explain evidence, exclusions, limitations and recommended human verification.

## Stage 3 — Engineering analysis

- Add signal-processing benchmarks for vibration and acoustic features.
- Evaluate FFT/PSD and modal-analysis methods against known synthetic signals.
- Add environment and occupancy confounder tests.
- Acceptance: numerical error and false-positive/false-negative metrics are reported against defined test data.

## Stage 4 — Dashboard and partner demonstration

- Building/floor map, event timeline, evidence detail, sensor health and report export.
- Accessibility, localization and privacy review.
- Acceptance: a reviewer can trace each finding to raw/synthetic evidence and understand what is unknown.

## Stage 5 — Bench and building pilot

- Qualified sensor selection and calibration.
- Professional installation, safety and privacy assessment.
- Independent engineering review and documented pilot agreement.
- Acceptance: no real-world performance claim without measured, repeatable pilot evidence.

## Initial success metrics

- Input rejection rate for malformed records.
- Detection sensitivity and false-positive rate on labelled synthetic test cases.
- Time-to-detect in controlled scenarios.
- Report reproducibility for a fixed seed and version.
- Percentage of findings with complete evidence provenance.
- Calibration and data-gap visibility.
- Runtime and memory use on documented hardware.

## Work policy

Prioritize one stage at a time. No paid services, subscriptions, cloud GPUs, physical purchases or unreviewed autonomous actions. Use public/open-source resources only after licence, provenance and security checks.
