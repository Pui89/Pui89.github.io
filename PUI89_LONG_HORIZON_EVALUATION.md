# PUI89 Long-Horizon Evaluation Framework

**Status:** dependency-free evaluator and synthetic scenario pack implemented; project-specific adapters and real-data evaluation remain future work.

## Purpose
Test whether decision policies behave consistently across sequences rather than isolated inputs. The same evaluator is intended to support Coconut Harvest AI, Extreme Flood Rescue AI and Multimodal Narcotics Screening AI through project-specific scenario adapters.

## Current benchmark dimensions
- Uncertainty carry-forward across a sequence (policy-level only).
- Missing, stale, clock-skewed, noisy, conflicting and out-of-distribution evidence.
- Fail-safe transitions: continue, safe hold, human review and latched stop.
- Explicit recovery requiring fresh, consistent evidence and operator approval.
- Long-horizon step counts, expected outcomes and failure reports.

## Run locally
`python tools/pui89_long_horizon.py --input benchmarks/pui89_long_horizon_scenarios.json --output long-horizon-report.json --commit <git-sha>`

Run tests:
`python -m unittest tests.test_pui89_long_horizon -v`

## Report interpretation
The report records scenario IDs, step traces, uncertainty values, faults, final states, expected outcomes and limitations. It is deterministic for the same input and code revision.

**Important boundaries:** This is synthetic policy testing. The uncertainty field is not a calibrated probability. It does not measure AI accuracy, Brier score, expected calibration error (ECE), sensor truth, simulator fidelity, physical robot safety or field capability. Calibration metrics must only be added when independent labelled predictions are available. Project adapters must preserve raw evidence and distinguish observed, inferred, missing and conflicting values.
