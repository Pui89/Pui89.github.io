# PUI89 AI Robotics — Cross-Project Command Centre

> Generated (UTC): 2026-10-29T19:56:32.407037+00:00

Read-only overview of public repository commits and recent GitHub Actions runs. This report is not a substitute for running tests or reviewing evidence.

| Project | Status | Latest commit | Latest workflow summary | Next focus |
|---|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | CHECKS_AVAILABLE | [896588fa1d8d](https://github.com/Pui89/Coconut-Harvest-AI/commit/896588fa1d8d21fb4222b7fd44382e124bb82cd1) | PUI89 Pitfall Detector Checks: success; Coconut Simulation Evaluation: success; PUI89 reproducible simulation benchmark: success | Priority 1: dataset provenance, reviewed labels, leakage-safe evaluation. |
| [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | CHECKS_AVAILABLE | [cf0636497c8b](https://github.com/Pui89/Extreme-Flood-Rescue-AI/commit/cf0636497c8b314e990847e7e843dc0abcb953fe) | Flood Rescue AI Simulation Evaluation: success; PUI89 Automated Verification: success; PUI89 reproducible simulation benchmark: success | Simulation-first: scenario coverage, navigation and fail-safe evidence. |
| [Multimodal Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | CHECKS_AVAILABLE | [f28685493c07](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/commit/f28685493c07f545adc4bdcfa2da95ae4f464a44) | PUI89 Pitfall Detector Checks: success; Multimodal Narcotics Screening AI Simulation Evaluation: success; PUI89 reproducible simulation benchmark: success | Data provenance, uncertainty, modality failures and human review. |

## Key engineering safeguards

Selected safeguards are scanned across the latest 50 repository workflow runs, rather than only the newest 10. A status of not_seen_in_recent_runs means unknown, not failed or passed. The simulation check includes the report validator step only when that workflow run completes successfully. The Coconut dataset evidence audit is currently project-specific; other projects may show not_seen_in_recent_runs because that workflow is not configured there.

### Coconut Harvest AI

| Safeguard | Status | Last updated (UTC) | Run |
|---|---|---|---|
| Free cloud verification | not_seen_in_recent_runs | unknown | — |
| Dataset recovery audit | not_seen_in_recent_runs | unknown | — |
| Free-resource link audit | not_seen_in_recent_runs | unknown | — |
| Rule-based simulation evaluation | not_seen_in_recent_runs | unknown | — |
| Coconut dataset evidence audit | success | 2026-10-29T19:56:02Z | [open](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40944477700) |
| Simulation benchmark + report validator | success | 2026-10-29T19:56:23Z | [open](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40944526517) |
| Autonomy / safety regression tests | not_seen_in_recent_runs | unknown | — |

### Extreme Flood Rescue AI

| Safeguard | Status | Last updated (UTC) | Run |
|---|---|---|---|
| Free cloud verification | success | 2026-10-29T19:05:02Z | [open](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40936790867) |
| Dataset recovery audit | not_seen_in_recent_runs | unknown | — |
| Free-resource link audit | not_seen_in_recent_runs | unknown | — |
| Rule-based simulation evaluation | success | 2026-10-29T19:56:28Z | [open](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40944537535) |
| Coconut dataset evidence audit | not_seen_in_recent_runs | unknown | — |
| Simulation benchmark + report validator | success | 2026-10-29T19:56:29Z | [open](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40944537311) |
| Autonomy / safety regression tests | not_seen_in_recent_runs | unknown | — |

### Multimodal Screening AI

| Safeguard | Status | Last updated (UTC) | Run |
|---|---|---|---|
| Free cloud verification | success | 2026-10-29T19:05:08Z | [open](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40936800529) |
| Dataset recovery audit | not_seen_in_recent_runs | unknown | — |
| Free-resource link audit | not_seen_in_recent_runs | unknown | — |
| Rule-based simulation evaluation | success | 2026-10-29T19:56:32Z | [open](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40944546429) |
| Coconut dataset evidence audit | not_seen_in_recent_runs | unknown | — |
| Simulation benchmark + report validator | success | 2026-10-29T19:56:30Z | [open](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40944546379) |
| Autonomy / safety regression tests | not_seen_in_recent_runs | unknown | — |

## Warnings and limitations

- This report reads public repository metadata and recent workflow runs; it does not execute project tests.
- A missing workflow run is unknown, not a passing result or proof of failure.
- Only the most recent 50 repository workflow runs are scanned; a safeguard absent from that window is unknown.
- A successful workflow does not validate real-world robot performance or dataset correctness.
- The Coconut dataset evidence audit runs only where its workflow is configured; not_seen_in_recent_runs for other projects means not observed, not a failure.
- GitHub API rate limits or temporary network errors can make status partial.

## Free-first policy

- No paid AI API, cloud GPU, third-party Python package, or model download is used by this report generator.
- The script only reads public GitHub metadata; it does not change project repositories.
- The scheduled GitHub Actions workflow publishes this report in this website repository.
- Do not interpret unknown, partial, or missing data as a passing test.
