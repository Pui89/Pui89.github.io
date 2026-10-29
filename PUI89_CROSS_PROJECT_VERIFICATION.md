# PUI89 AI Core — Cross-Project Verification Snapshot

**Snapshot date:** 2026-10-29  
**Purpose:** Record observed automated checks across the three PUI89 AI applications and robot concepts. This is a software verification snapshot, not a real-world performance report.

## Current automated-check status

The listed pull-request-head workflow runs had completed with GitHub Actions conclusion **success** when inspected on 2026-10-29.

| Project | Draft PR | Observed passing workflow runs | Evidence boundary |
|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | [#151 — lightweight CI dependency boundary](https://github.com/Pui89/Coconut-Harvest-AI/pull/151) | Lightweight Python verification; shared-interface smoke; pitfall detector; security; free local checks; duplicate automated-verification run | Software and report-generator checks only; no coconut detector accuracy measured. |
| [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | [#115 — lightweight CI dependency boundary](https://github.com/Pui89/Extreme-Flood-Rescue-AI/pull/115) | Fast preflight; free local checks; automated verification; shared-interface smoke; Python tests on 3.10/3.11/3.12; security; pitfall detector; Ruff | Does not validate flood physics, 15 m depth capability, navigation, buoyancy or real rescue performance. |
| [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | [#93 — lightweight CI dependency boundary](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/pull/93) | Lightweight verification; shared-interface smoke; fast preflight; free local checks; Python tests on 3.10/3.11/3.12; app regression checks on 3.10/3.11/3.12; security; pitfall detector; Ruff | Does not validate chemical identification, X-ray capability, field screening accuracy or physical robot safety. Human review remains necessary. |

**Review state (updated 2026-10-29):** all three CI-fix PRs have since been merged into their respective default branches: [Coconut #151](https://github.com/Pui89/Coconut-Harvest-AI/pull/151), [Flood #115](https://github.com/Pui89/Extreme-Flood-Rescue-AI/pull/115), and [Screening #93](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/pull/93). The test counts below refer to the specific inspected PR-head workflow logs and are evidence of those software checks only. New commits can change workflow results.


## Selected observed test counts

The job logs were inspected, not just the green status icons:

- **Coconut shared-interface smoke:** 15 tests run, 0 reported failures; interface/proposal-gate checks only.
- **Extreme Flood Rescue AI:** 419 pytest items passed in the inspected Python 3.11.17 job (3.17 seconds); the Python 3.10, 3.11 and 3.12 jobs all concluded success.
- **Multimodal Narcotics Screening AI:** 385 pytest items passed in the inspected Python 3.11.17 job (1.06 seconds); the Python 3.10, 3.11 and 3.12 jobs all concluded success.
- **Multimodal app regression:** the inspected synthetic pipeline smoke check passed for six synthetic cases; it explicitly says it is not a real-world benchmark. Regression jobs for Python 3.10, 3.11 and 3.12 all concluded success.

These counts are from different test suites and must not be summed into a single “PUI89 test count.” The two pytest counts are for one Python-version job each; their other matrix jobs also passed but are not added here. A passing CI job is not evidence of AI accuracy or physical-world performance.

## Shared evidence safeguards

The standard-library observability generator starts with conservative statuses: software/model/system/workflow/safety checks are `NOT_RUN`, and hardware is `NOT_CONNECTED`, unless supplied evidence is provided. A `PASS` or `FAIL` entry requires an evidence reference and observation timestamp. Schema validation checks format only; it does not authenticate evidence.

Shared software-contract and simulation-evidence checks cover world-state/confidence-field contracts, simulation-only action proposals, machine-readable failure/evidence reports, and rejection of missing or inconsistent report evidence. Passing validators prove only the checked software/report properties, not physical-world robot performance.

## Failure history and resolution status

A prior lightweight-runner attempt failed because it discovered and imported dependency-backed test modules without the project's full dependency/import environment (errors included missing project modules and optional packages). The three open CI-fix PRs change that lightweight job to compile configured Python folders and smoke-test the standard-library observability report, while leaving full unit/integration testing to the dedicated project test workflows. The replacement lightweight jobs now pass on the observed PR heads.

**Important:** this resolves the lightweight preflight's test-discovery boundary; it does not mean every possible test failure has been eliminated. No failing test was present in the workflow runs inspected for the current PR heads. If a later run fails, keep its failure in the report with the job/test name and log evidence rather than suppressing it.

## Coconut Harvest AI — first measurable AI evaluation

Coconut Harvest AI is selected first for a genuine perception benchmark. The repository has a standard-library evaluator for manually reviewed ground-truth boxes and actual detector prediction CSVs. It calculates precision, recall and F1 at declared IoU and score thresholds; it does **not** calculate mAP and does not run a detector.

- Evaluator/tool checks were previously recorded as passing in the Coconut Harvest AI README.
- Real held-out detector evaluation: **NOT RUN / NOT MEASURED** in the evidence reviewed for this snapshot.
- Source/licence review, annotation QA and leakage-safe source/tree/session splits remain prerequisites.
- No detector accuracy, maturity-class accuracy, 0–30 m reach, harvest success or physical robot performance is claimed.

A valid benchmark needs a reviewed held-out set, actual model predictions, documented model/checkpoint and dataset provenance, fixed thresholds, per-class counts, and error review. If a compatible model/checkpoint is unavailable locally, record inference as not run rather than inventing predictions.

## Common fields for future reproducible runs

Record repository and commit SHA; command and environment; scenario/configuration ID and hash; dataset version/manifest/source licence/split; cases attempted, completed, failed and safely rejected; per-class counts and metrics; uncertainty summaries; failure categories and evidence artifacts; runtime measurement method; human-review, safe-hold and simulation-only gate outcomes.

Do not compare scores across projects unless scenario definitions and measurement procedures are comparable.

## Free-first execution policy

- Prefer deterministic Python standard-library checks and small local scenarios.
- Do not download models automatically or require paid APIs, subscriptions or cloud GPUs.
- Before optional VLM/VLA evaluation, check licence, download size, disk/RAM/VRAM needs and offline operation.
- Keep actions simulated until software evidence, simulation evidence, hardware readiness and independent safety review justify the next stage.
- GitHub Actions usage may be subject to account quotas; do not promise unlimited or universally cost-free CI.

## Next milestone

1. Keep the merged lightweight-runner fixes under CI monitoring; if any new run fails, record the failing job and log evidence.
2. Complete the Coconut source-byte hash, licence/provenance, annotation QA and source/tree/session split checks. The published readiness snapshot records 34 candidate rows and 0 approved for training; the dataset remains blocked.
3. Only after the dataset promotion gate passes, obtain genuine detector predictions on a frozen held-out set and publish reproducible metrics. Until then, keep detector evaluation marked NOT RUN / NOT MEASURED.
4. Add observed test counts and failure details from actual run artifacts, never estimates.
