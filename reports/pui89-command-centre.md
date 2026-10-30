# PUI89 AI Robotics — Cross-Project Command Centre

> Generated (UTC): 2026-10-30T13:21:00.030996+00:00

Read-only overview of public repository commits and recent GitHub Actions runs. This report is not a substitute for running tests or reviewing evidence.

| Project | Status | Latest commit | Latest workflow summary | Next focus |
|---|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | CHECKS_AVAILABLE | [312940246095](https://github.com/Pui89/Coconut-Harvest-AI/commit/3129402460950a0bc2508f173f88e24a62cbc22a) | PUI89 Pitfall Detector Checks: success; Coconut Simulation Evaluation: success; PUI89 Free Local Checks: success | Priority 1: dataset provenance, reviewed labels, leakage-safe evaluation. |
| [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | CHECKS_AVAILABLE | [83977802ef6b](https://github.com/Pui89/Extreme-Flood-Rescue-AI/commit/83977802ef6be9adbb12dd4dce55c81185b6a795) | PUI89 Automated Verification: success; PUI89 Pitfall Detector Checks: success; PUI89 Shared Interface Smoke: success | Simulation-first: scenario coverage, navigation and fail-safe evidence. |
| [Multimodal Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | CHECKS_AVAILABLE | [4b26daf1c2aa](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/commit/4b26daf1c2aa7e97f3d24dc9d9896b580c4bbb13) | PUI89 Automated Verification: success; Multimodal Screening AI regression checks: success; Fault monitor tests: success | Data provenance, uncertainty, modality failures and human review. |

## Key engineering safeguards

Selected safeguards are scanned across the latest 50 repository workflow runs, rather than only the newest 10. A status of not_seen_in_recent_runs means unknown, not failed or passed. The simulation check includes the report validator step only when that workflow run completes successfully. The Coconut dataset evidence audit is currently project-specific; other projects may show not_seen_in_recent_runs because that workflow is not configured there.

### Coconut Harvest AI

| Safeguard | Status | Last updated (UTC) | Run |
|---|---|---|---|
| Free cloud verification | not_seen_in_recent_runs | unknown | — |
| Dataset recovery audit | not_seen_in_recent_runs | unknown | — |
| Free-resource link audit | not_seen_in_recent_runs | unknown | — |
| Rule-based simulation evaluation | not_seen_in_recent_runs | unknown | — |
| Coconut dataset evidence audit | success | 2026-10-30T08:27:48Z | [open](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/41026451738) |
| Simulation benchmark + report validator | success | 2026-10-30T08:26:41Z | [open](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/41026443056) |
| Autonomy / safety regression tests | not_seen_in_recent_runs | unknown | — |

### Extreme Flood Rescue AI

| Safeguard | Status | Last updated (UTC) | Run |
|---|---|---|---|
| Free cloud verification | success | 2026-10-30T08:27:45Z | [open](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/41026465322) |
| Dataset recovery audit | success | 2026-10-30T08:29:08Z | [open](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/41026473120) |
| Free-resource link audit | not_seen_in_recent_runs | unknown | — |
| Rule-based simulation evaluation | success | 2026-10-30T08:28:12Z | [open](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/41026473029) |
| Coconut dataset evidence audit | not_seen_in_recent_runs | unknown | — |
| Simulation benchmark + report validator | success | 2026-10-30T08:27:24Z | [open](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/41026465346) |
| Autonomy / safety regression tests | not_seen_in_recent_runs | unknown | — |

### Multimodal Screening AI

| Safeguard | Status | Last updated (UTC) | Run |
|---|---|---|---|
| Free cloud verification | success | 2026-10-30T08:28:13Z | [open](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/41026484878) |
| Dataset recovery audit | success | 2026-10-30T08:29:36Z | [open](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/41026491540) |
| Free-resource link audit | not_seen_in_recent_runs | unknown | — |
| Rule-based simulation evaluation | success | 2026-10-30T08:28:43Z | [open](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/41026491630) |
| Coconut dataset evidence audit | not_seen_in_recent_runs | unknown | — |
| Simulation benchmark + report validator | success | 2026-10-30T08:28:21Z | [open](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/41026484956) |
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
