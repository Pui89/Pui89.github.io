# PUI89 AI Core — Cross-Project Verification Snapshot

**Snapshot date:** 2026-10-28  
**Purpose:** Document shared simulation-evidence safeguards across the three PUI89 AI application and robot-concept projects. This is a software verification snapshot, not a real-world performance report.

## Project matrix

| Project | Scope | Shared safeguards covered by automated tests |
|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | Agricultural perception and harvesting task-planning concept | World-state contract; confidence validation; simulation-only action proposals; failure-report evidence validation |
| [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | Flood-response perception and rescue-planning concept | World-state contract; confidence validation; simulation-only action proposals; failure-report evidence validation |
| [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | Multimodal screening and human-review concept | World-state contract; confidence validation; simulation-only action proposals; failure-report evidence validation |

## Evidence-validation checks

The latest merged test additions exercise failure cases that a benchmark report must reject:

- CSV evidence row count does not match the report.
- A report claims success while its failure count contradicts that status.
- Required CSV evidence is missing.

The simulation workflow is designed to generate machine-readable JSON and CSV reports, validate the report against its scenario configuration, check for prohibited hardware actuation, and retain the reports as workflow artifacts. A passing validator means the report is structurally consistent with these checks; it does **not** mean a robot works in the physical world.

## Verification status

- The adversarial evidence-validation PR checks passed before merge in all three repositories on 2026-10-28.
- Post-merge workflow runs were still in progress when this snapshot was prepared. Check each repository's [Actions](https://github.com/Pui89/Coconut-Harvest-AI/actions), [Actions](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions), and [Actions](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions) pages for the latest main-branch result.
- No numeric accuracy, latency, success-rate, or physical-robot capability is claimed in this snapshot. Publish those metrics only after a named scenario, data split, measurement method, and reproducible run produce evidence.

## Common metric contract for future comparisons

When comparable scenario outputs are available, report the same fields for each project:

1. Scenario/configuration identifier and configuration hash.
2. Number of cases attempted, completed, failed, and safely rejected.
3. Perception confidence summary and count of low-confidence cases.
4. Task-planning success/failure counts and failure categories.
5. Runtime/latency statistics, including measurement environment.
6. Evidence completeness: JSON/CSV present, row counts consistent, and validation result.
7. Safety: proposed actions versus rejected actions; simulation-only gate outcome.

Do not compare raw scores across projects unless the scenario definitions and measurement procedures are comparable. For screening scenarios, keep human review explicit; for rescue and harvesting, treat robot actions as simulated proposals until separately validated.

## Free-first execution policy

- Prefer Python standard-library checks and small deterministic scenarios.
- Do not download models automatically or require paid APIs, subscriptions, or cloud GPUs.
- Evaluate any optional VLM/VLA only after checking license, download size, RAM/VRAM needs, and whether it can be run locally.
- Keep action execution simulated. No hardware actuation is enabled by this report.

## Next milestone

Collect validated outputs from the three simulation workflows, then generate a comparison table from actual artifacts. Do not fill metric values with estimates or placeholders presented as results.
