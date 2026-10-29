# PUI89 AI — Engineering Quality Dashboard

**Purpose:** one place to track software-verification progress across the three PUI89 AI projects. This dashboard distinguishes implemented checks from results that still need to be observed or measured.

## Current project comparison

| Project | Engineering focus | Current evidence foundation | Highest-priority gap |
|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | Agricultural perception, maturity classes, harvesting task planning | Shared PUI89 core tests for world state, confidence validation, simulation-only action proposals and structured failure reports; project-specific dataset and evaluation gates documented | Verified/licensed dataset, reviewed annotations, leakage-safe splits, then measured baseline metrics |
| [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | Flood-response perception and rescue planning | Shared core tests and documented simulation/fault-injection roadmap | Reproducible scenarios, missing/stale/conflicting sensor tests, and validated water/navigation simulation |
| [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | Multimodal screening support with human review | Shared core tests and documented uncertainty, abstention and human-review safeguards | Lawful, licensed evaluation data and independently validated sensor-specific screening performance |

**Readiness ranking:** Coconut Harvest AI is the recommended first project to advance based on the documented engineering and evaluation path. This is not a ranking of measured AI accuracy. All three currently share the same core test suite, so the evidence does not establish that one has superior runtime or detection performance.

## Automated verification

- [Run combined quality report](https://github.com/Pui89/Pui89.github.io/actions/workflows/pui89-combined-quality-report.yml)
- [Coconut Harvest AI Actions](https://github.com/Pui89/Coconut-Harvest-AI/actions)
- [Extreme Flood Rescue AI Actions](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions)
- [Multimodal Narcotics Screening AI Actions](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions)
- [Portfolio verification Actions](https://github.com/Pui89/Pui89.github.io/actions)

The combined workflow checks out all three public repositories, runs Python standard-library unit tests, and publishes JSON/Markdown plus per-project logs as a workflow artifact. Open the latest workflow run and inspect its conclusion and artifact before reporting pass/fail.

## Status definitions

- **Implemented:** code or documented test exists in the repository.
- **Passed:** the relevant automated run has completed successfully and its result is visible.
- **Measured:** a reproducible experiment reports the method, configuration, data/scenario count, environment and result.
- **Validated in the real world:** independent evidence supports the claim under the stated operating conditions.

These labels are not interchangeable. A passing unit test is not proof of model accuracy, safety certification, or a working physical robot.

## Free-first and safety limits

- No paid model API, cloud GPU, or automatic large-model download is required by the combined unit-test workflow.
- GitHub-hosted runner usage depends on repository visibility and account allowances; monitor usage and avoid adding paid services.
- No robot hardware is actuated by these checks.
- Do not publish accuracy, precision/recall, latency, flood depth capability, chemical-identification capability, or harvesting success without appropriate measured evidence.
- Keep proposed robot actions simulation-only and retain human review for uncertain or consequential screening decisions.

## Next engineering sequence

1. **Observe the first combined workflow run** and fix any genuine failures.
2. Add project-specific tests beyond the shared core contract, prioritizing safety-critical edge cases.
3. For Coconut Harvest AI, finish dataset provenance and annotation QA before running a baseline.
4. For Flood Rescue AI, test sensor dropout, stale readings, contradictory measurements and conservative safe-stop behavior in deterministic scenarios.
5. For Narcotics Screening AI, test missing/conflicting modalities, uncertainty/abstention and human-review routing; do not equate RGB appearance with chemical identification.
6. Publish comparable metrics only when the scenario definitions and measurement conditions are recorded and comparable.
