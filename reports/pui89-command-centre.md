# PUI89 AI Robotics — Cross-Project Command Centre

> Generated (UTC): 2026-10-31T21:45:07.676262+00:00

Read-only overview of public repository commits and recent GitHub Actions runs. This report is not a substitute for running tests or reviewing evidence.

| Project | Status | Latest commit | Latest workflow summary | Next focus |
|---|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | CHECKS_AVAILABLE | [66cb218b679e](https://github.com/Pui89/Coconut-Harvest-AI/commit/66cb218b679e10618d4ec43f117c4a791210f69a) | PUI89 Shared Interface Smoke: success [main]; PUI89 Free Local Checks: success [main]; PUI89 Automated Verification: success [main] | Priority 1: dataset provenance, reviewed labels, leakage-safe evaluation. |
| [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | CHECKS_AVAILABLE | [07657be4a4fa](https://github.com/Pui89/Extreme-Flood-Rescue-AI/commit/07657be4a4fab211d8bb6819eb505b03922e4fec) | PUI89 Automated Verification: success [main]; Flood Rescue AI regression checks: success [main]; PUI89 Free Local Checks: success [main] | Simulation-first: scenario coverage, navigation and fail-safe evidence. |
| [Multimodal Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | CHECKS_AVAILABLE | [7caa06a3b83f](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/commit/7caa06a3b83fd83d43d213e00c6c4bb36ba227f8) | Security Checks: success [main]; Free cloud-side verification: success [main]; PUI89 Free Local Checks: success [main] | Data provenance, uncertainty, modality failures and human review. |

## Key engineering safeguards

Selected safeguards are scanned across the latest 50 repository workflow runs, rather than only the newest 10, and are filtered to the repository default branch. A status of not_seen_in_recent_runs means unknown, not failed or passed. Feature/Dependabot runs are counted separately and never substituted for default-branch evidence. The simulation check includes the report validator step only when that workflow run completes successfully. The Coconut dataset evidence audit is currently project-specific; other projects may show not_seen_in_recent_runs because that workflow is not configured there.

### Coconut Harvest AI

Non-default-branch runs in the scanned window: 32

| Safeguard | Status | Branch | Last updated (UTC) | Run |
|---|---|---|---|---|
| Free cloud verification | not_seen_in_recent_runs | not seen on default branch | unknown | — |
| Dataset recovery audit | not_seen_in_recent_runs | not seen on default branch | unknown | — |
| Free-resource link audit | not_seen_in_recent_runs | not seen on default branch | unknown | — |
| Rule-based simulation evaluation | not_seen_in_recent_runs | not seen on default branch | unknown | — |
| Coconut dataset evidence audit | not_seen_in_recent_runs | not seen on default branch | unknown | — |
| Simulation benchmark + report validator | not_seen_in_recent_runs | not seen on default branch | unknown | — |
| Autonomy / safety regression tests | not_seen_in_recent_runs | not seen on default branch | unknown | — |

### Extreme Flood Rescue AI

Non-default-branch runs in the scanned window: 39

| Safeguard | Status | Branch | Last updated (UTC) | Run |
|---|---|---|---|---|
| Free cloud verification | success | main | 2026-10-31T20:56:26Z | [open](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/41241212604) |
| Dataset recovery audit | not_seen_in_recent_runs | not seen on default branch | unknown | — |
| Free-resource link audit | not_seen_in_recent_runs | not seen on default branch | unknown | — |
| Rule-based simulation evaluation | success | main | 2026-10-31T18:01:22Z | [open](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/41227320457) |
| Coconut dataset evidence audit | not_seen_in_recent_runs | not seen on default branch | unknown | — |
| Simulation benchmark + report validator | not_seen_in_recent_runs | not seen on default branch | unknown | — |
| Autonomy / safety regression tests | not_seen_in_recent_runs | not seen on default branch | unknown | — |

### Multimodal Screening AI

Non-default-branch runs in the scanned window: 38

| Safeguard | Status | Branch | Last updated (UTC) | Run |
|---|---|---|---|---|
| Free cloud verification | success | main | 2026-10-31T20:56:54Z | [open](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/41241242522) |
| Dataset recovery audit | not_seen_in_recent_runs | not seen on default branch | unknown | — |
| Free-resource link audit | not_seen_in_recent_runs | not seen on default branch | unknown | — |
| Rule-based simulation evaluation | success | main | 2026-10-31T18:01:48Z | [open](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/41227358866) |
| Coconut dataset evidence audit | not_seen_in_recent_runs | not seen on default branch | unknown | — |
| Simulation benchmark + report validator | not_seen_in_recent_runs | not seen on default branch | unknown | — |
| Autonomy / safety regression tests | not_seen_in_recent_runs | not seen on default branch | unknown | — |

## Warnings and limitations

- This report reads public repository metadata and recent workflow runs; it does not execute project tests.
- A missing workflow run is unknown, not a passing result or proof of failure.
- Only the most recent 50 repository workflow runs are scanned; a safeguard absent from that window is unknown.
- Headline workflow and safeguard status is filtered to the repository default branch; other-branch runs are counted separately and do not prove default-branch health.
- A successful workflow does not validate real-world robot performance or dataset correctness.
- The Coconut dataset evidence audit runs only where its workflow is configured; not_seen_in_recent_runs for other projects means not observed, not a failure.
- GitHub API rate limits or temporary network errors can make status partial.

## Free-first policy

- No paid AI API, cloud GPU, third-party Python package, or model download is used by this report generator.
- The script only reads public GitHub metadata; it does not change project repositories.
- The scheduled GitHub Actions workflow publishes this report in this website repository.
- Do not interpret unknown, partial, or missing data as a passing test.
