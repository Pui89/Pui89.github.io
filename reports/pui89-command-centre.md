# PUI89 AI Robotics — Cross-Project Command Centre

> Generated (UTC): 2026-10-29T19:28:03.198505+00:00

Read-only overview of public repository commits and recent GitHub Actions runs. This report is not a substitute for running tests or reviewing evidence.

| Project | Status | Latest commit | Latest workflow summary | Next focus |
|---|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | CHECKS_AVAILABLE | [92fe31a5f050](https://github.com/Pui89/Coconut-Harvest-AI/commit/92fe31a5f0506f9dc59563f8637b978b18f359f0) | Coconut Lightweight Core Tests: success; PUI89 Pitfall Detector Checks: success; PUI89 Automated Verification: success | Priority 1: dataset provenance, reviewed labels, leakage-safe evaluation. |
| [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | CHECKS_AVAILABLE | [1ad9552047ab](https://github.com/Pui89/Extreme-Flood-Rescue-AI/commit/1ad9552047ab830527e228545803dbe6e0d24321) | Security checks: success; Free cloud-side verification: success; PUI89 Pitfall Detector Checks: success | Simulation-first: scenario coverage, navigation and fail-safe evidence. |
| [Multimodal Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | CHECKS_AVAILABLE | [2fc83ad751ee](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/commit/2fc83ad751ee3fbdf8addcdd5d3e9a5df5d931e4) | PUI89 Pitfall Detector Checks: success; PUI89 Automated Verification: success; Free cloud-side verification: success | Data provenance, uncertainty, modality failures and human review. |

## Key engineering safeguards

Selected safeguards are scanned across the latest 50 repository workflow runs, rather than only the newest 10. A status of not_seen_in_recent_runs means unknown, not failed or passed. The simulation check includes the report validator step only when that workflow run completes successfully.

### Coconut Harvest AI

| Safeguard | Status | Last updated (UTC) | Run |
|---|---|---|---|
| Free cloud verification | not_seen_in_recent_runs | unknown | — |
| Dataset recovery audit | not_seen_in_recent_runs | unknown | — |
| Free-resource link audit | not_seen_in_recent_runs | unknown | — |
| Rule-based simulation evaluation | not_seen_in_recent_runs | unknown | — |
| Simulation benchmark + report validator | not_seen_in_recent_runs | unknown | — |
| Autonomy / safety regression tests | not_seen_in_recent_runs | unknown | — |

### Extreme Flood Rescue AI

| Safeguard | Status | Last updated (UTC) | Run |
|---|---|---|---|
| Free cloud verification | success | 2026-10-29T19:05:02Z | [open](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40936790867) |
| Dataset recovery audit | not_seen_in_recent_runs | unknown | — |
| Free-resource link audit | not_seen_in_recent_runs | unknown | — |
| Rule-based simulation evaluation | success | 2026-10-29T19:05:03Z | [open](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40936790690) |
| Simulation benchmark + report validator | not_seen_in_recent_runs | unknown | — |
| Autonomy / safety regression tests | not_seen_in_recent_runs | unknown | — |

### Multimodal Screening AI

| Safeguard | Status | Last updated (UTC) | Run |
|---|---|---|---|
| Free cloud verification | success | 2026-10-29T19:05:08Z | [open](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40936800529) |
| Dataset recovery audit | not_seen_in_recent_runs | unknown | — |
| Free-resource link audit | not_seen_in_recent_runs | unknown | — |
| Rule-based simulation evaluation | success | 2026-10-29T19:05:10Z | [open](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40936800524) |
| Simulation benchmark + report validator | not_seen_in_recent_runs | unknown | — |
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
