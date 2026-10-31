# PUI89 AI Robotics — Cross-Project Command Centre

> Generated (UTC): 2026-10-31T18:04:03.532561+00:00

Read-only overview of public repository commits and recent GitHub Actions runs. This report is not a substitute for running tests or reviewing evidence.

| Project | Status | Latest commit | Latest workflow summary | Next focus |
|---|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | CHECKS_AVAILABLE | [1b23950b4edb](https://github.com/Pui89/Coconut-Harvest-AI/commit/1b23950b4edb1e08a7c9b9353d5a76bac18ef6fd) | PUI89 Health Gate Regression: success; PUI89 Pitfall Detector Checks: success; PUI89 Automated Verification: success | Priority 1: dataset provenance, reviewed labels, leakage-safe evaluation. |
| [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | CHECKS_AVAILABLE | [d4a6ba989941](https://github.com/Pui89/Extreme-Flood-Rescue-AI/commit/d4a6ba989941283af45a7af20a5b36107b304bab) | Fault monitor tests: queued; Flood Rescue AI Simulation Evaluation: queued; Dataset recovery and replacement queue: queued | Simulation-first: scenario coverage, navigation and fail-safe evidence. |
| [Multimodal Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | CHECKS_AVAILABLE | [3236929ac09a](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/commit/3236929ac09a5881575f8cb94bb4af4d7968ba26) | github_actions in / for actions/setup-python - Update #1668299703: queued; github_actions in / for actions/checkout - Update #1668299560: in_progress; github_actions in / for actions/upload-artifact - Update #1668299555: in_progress | Data provenance, uncertainty, modality failures and human review. |

## Key engineering safeguards

Selected safeguards are scanned across the latest 50 repository workflow runs, rather than only the newest 10. The Evidence benchmark + report integrity row points to the latest project simulation workflow, which runs the benchmark validator before uploading its simulation report artifact. A completed-success conclusion confirms the configured workflow steps passed; it is not an independent reading of benchmark JSON. A status of not_seen_in_recent_runs means unknown, not failed or passed. The Coconut dataset evidence audit is currently project-specific; other projects may show not_seen_in_recent_runs because that workflow is not configured there.

### Coconut Harvest AI

| Safeguard | Status | Last updated (UTC) | Run |
|---|---|---|---|
| Free cloud verification | not_seen_in_recent_runs | unknown | — |
| Dataset recovery audit | not_seen_in_recent_runs | unknown | — |
| Free-resource link audit | not_seen_in_recent_runs | unknown | — |
| Rule-based simulation evaluation | not_seen_in_recent_runs | unknown | — |
| Coconut dataset evidence audit | success | 2026-10-31T18:03:13Z | [open](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/41227466513) |
| Simulation benchmark + report validator | success | 2026-10-31T18:03:22Z | [open](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/41227461507) |
| Evidence benchmark + report integrity | success | 2026-10-31T18:03:16Z | [open](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/41227466500) |
| Autonomy / safety regression tests | not_seen_in_recent_runs | unknown | — |

### Extreme Flood Rescue AI

| Safeguard | Status | Last updated (UTC) | Run |
|---|---|---|---|
| Free cloud verification | queued | 2026-10-31T18:03:23Z | [open](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/41227499687) |
| Dataset recovery audit | queued | 2026-10-31T18:03:24Z | [open](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/41227503317) |
| Free-resource link audit | not_seen_in_recent_runs | unknown | — |
| Rule-based simulation evaluation | queued | 2026-10-31T18:03:24Z | [open](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/41227503323) |
| Coconut dataset evidence audit | not_seen_in_recent_runs | unknown | — |
| Simulation benchmark + report validator | queued | 2026-10-31T18:03:23Z | [open](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/41227499649) |
| Evidence benchmark + report integrity | queued | 2026-10-31T18:03:24Z | [open](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/41227503323) |
| Autonomy / safety regression tests | not_seen_in_recent_runs | unknown | — |

### Multimodal Screening AI

| Safeguard | Status | Last updated (UTC) | Run |
|---|---|---|---|
| Free cloud verification | success | 2026-10-31T18:01:46Z | [open](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/41227358868) |
| Dataset recovery audit | not_seen_in_recent_runs | unknown | — |
| Free-resource link audit | not_seen_in_recent_runs | unknown | — |
| Rule-based simulation evaluation | success | 2026-10-31T18:01:48Z | [open](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/41227358866) |
| Coconut dataset evidence audit | not_seen_in_recent_runs | unknown | — |
| Simulation benchmark + report validator | not_seen_in_recent_runs | unknown | — |
| Evidence benchmark + report integrity | success | 2026-10-31T18:01:48Z | [open](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/41227358866) |
| Autonomy / safety regression tests | not_seen_in_recent_runs | unknown | — |

## Warnings and limitations

- This report reads public repository metadata and recent workflow runs; it does not execute project tests.
- A missing workflow run is unknown, not a passing result or proof of failure.
- Only the most recent 50 repository workflow runs are scanned; a safeguard absent from that window is unknown.
- A successful simulation workflow confirms its configured scenario and evidence-benchmark steps completed; it does not validate real-world robot performance or dataset correctness.
- Evidence benchmark status is inferred from the latest matching simulation workflow conclusion; the generated JSON benchmark is retained in the workflow workspace and is not independently parsed by this dashboard.
- The Coconut dataset evidence audit runs only where its workflow is configured; not_seen_in_recent_runs for other projects means not observed, not a failure.
- GitHub API rate limits or temporary network errors can make status partial.

## Free-first policy

- No paid AI API, cloud GPU, third-party Python package, or model download is used by this report generator.
- The script only reads public GitHub metadata; it does not change project repositories.
- The scheduled GitHub Actions workflow publishes this report in this website repository.
- Do not interpret unknown, partial, or missing data as a passing test.
