# PUI89 AI Robotics — Cross-Project Command Centre

> Generated (UTC): 2026-10-27T11:38:24.746512+00:00

Read-only overview of public repository commits and recent GitHub Actions runs. This report is not a substitute for running tests or reviewing evidence.

| Project | Status | Latest commit | Latest workflow summary | Next focus |
|---|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | CHECKS_AVAILABLE | [a6a836d21374](https://github.com/Pui89/Coconut-Harvest-AI/commit/a6a836d21374857a133b148877a1145a8ae02e8a) | PUI89 Free Local Checks: success; PUI89 Shared Interface Smoke: success; security: success | Priority 1: dataset provenance, reviewed labels, leakage-safe evaluation. |
| [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | CHECKS_AVAILABLE | [205cc1c1a607](https://github.com/Pui89/Extreme-Flood-Rescue-AI/commit/205cc1c1a6074f82daf8bf9bf3f556182c3c0fdd) | Security checks: success; PUI89 Fast Preflight: success; Free helper review (Ruff): success | Simulation-first: scenario coverage, navigation and fail-safe evidence. |
| [Multimodal Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | CHECKS_AVAILABLE | [5a92787ab4e3](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/commit/5a92787ab4e3adf2a3c02ea1fdac26de702b0478) | Free local-first app regression checks: success; PUI89 Shared Interface Smoke: success; Security Checks: success | Data provenance, uncertainty, modality failures and human review. |

## Key engineering safeguards

Selected safeguards are scanned across the latest 50 repository workflow runs, rather than only the newest 10. A status of not_seen_in_recent_runs means unknown, not failed or passed. The simulation check includes the report validator step only when that workflow run completes successfully.

### Coconut Harvest AI

| Safeguard | Status | Last updated (UTC) | Run |
|---|---|---|---|
| Free cloud verification | not_seen_in_recent_runs | unknown | — |
| Dataset recovery audit | not_seen_in_recent_runs | unknown | — |
| Free-resource link audit | not_seen_in_recent_runs | unknown | — |
| Simulation benchmark + report validator | failure | 2026-10-27T11:34:13Z | [open](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40497133870) |
| Autonomy / safety regression tests | not_seen_in_recent_runs | unknown | — |

### Extreme Flood Rescue AI

| Safeguard | Status | Last updated (UTC) | Run |
|---|---|---|---|
| Free cloud verification | success | 2026-10-27T11:35:57Z | [open](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40497163989) |
| Dataset recovery audit | not_seen_in_recent_runs | unknown | — |
| Free-resource link audit | not_seen_in_recent_runs | unknown | — |
| Simulation benchmark + report validator | failure | 2026-10-27T11:34:27Z | [open](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40497162414) |
| Autonomy / safety regression tests | not_seen_in_recent_runs | unknown | — |

### Multimodal Screening AI

| Safeguard | Status | Last updated (UTC) | Run |
|---|---|---|---|
| Free cloud verification | success | 2026-10-27T11:36:43Z | [open](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40497376647) |
| Dataset recovery audit | not_seen_in_recent_runs | unknown | — |
| Free-resource link audit | not_seen_in_recent_runs | unknown | — |
| Simulation benchmark + report validator | failure | 2026-10-27T11:36:09Z | [open](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40497374915) |
| Autonomy / safety regression tests | not_seen_in_recent_runs | unknown | — |

## Warnings and limitations

- This report reads public repository metadata and recent workflow runs; it does not execute project tests.
- A missing workflow run is unknown, not a passing result or proof of failure.
- Only the most recent 50 repository workflow runs are scanned; a safeguard absent from that window is unknown.
- A successful workflow does not validate real-world robot performance or dataset correctness.
- GitHub API rate limits or temporary network errors can make status partial.

## Free-first policy

- No paid AI API, cloud GPU, third-party Python package, or model download is used by this report generator.
- The script only reads public GitHub metadata; it does not change project repositories.
- The scheduled GitHub Actions workflow publishes this report in this website repository.
- Do not interpret unknown, partial, or missing data as a passing test.
