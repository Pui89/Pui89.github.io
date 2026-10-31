# PUI89 Sensor Evidence Assessment

## Purpose
A dependency-free baseline for assessing supplied observations across Coconut
Harvest AI, Extreme Flood Rescue AI, and Multimodal Narcotics Screening AI.

## Current implementation
- Validates required fields, timezone-aware timestamps, unique IDs, and supplied
  quality states: GOOD, DEGRADED, INVALID.
- Rejects stale, future-dated, malformed, duplicate, or non-good observations.
- Checks required modality coverage.
- Preserves disagreements; it does not vote, average, or silently select a sensor.
- Returns CONTINUE, REQUEST_EVIDENCE, REQUEST_HUMAN_REVIEW, or SAFE_HOLD.

## Interpretation
This is deterministic evidence assessment, not statistical sensor fusion.
A supplied quality label is not calibrated confidence. Exact value comparison is
a conflict flag, not a physical-world truth determination. CONTINUE means only
that the supplied records passed these checks.

## Cost and safety boundary
Python standard library only. No model downloads, APIs, cloud GPU, paid services,
or additional packages. Simulation only; physical actuation is prohibited.
Synthetic unit tests do not establish sensor accuracy or field readiness.

## Next validation
Add project-specific adapters and synthetic fault scenarios, then evaluate
permission-cleared recorded datasets with provenance and documented limitations.
