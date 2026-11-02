# PUI89 AI Core — Cross-Project Verification Snapshot

**Snapshot date:** 2026-11-02  
**Purpose:** Record observed automated checks across the four PUI89 AI applications and robot concepts. This is a software verification snapshot, not a real-world performance report.

## Evidence benchmark engine — 1 November 2026

The deterministic PUI89 Evidence Benchmark Engine has now been merged into the three robotics/screening project repositories; HOMEGUARD has a separate initial foundation CI. The corresponding hosted simulation/evidence workflows completed successfully on 31 October 2026, and each project reports **6 standard-library benchmark-engine tests passed**.

| Project | Merged PR | Successful hosted run | What this verifies |
|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | [#160](https://github.com/Pui89/Coconut-Harvest-AI/pull/160) | [Run 41222933984](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/41222933984) | Evidence-report structure, metric consistency, source-report and ordered world-state snapshot hashes, and rejection of hardware-actuation claims |
| [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | [#124](https://github.com/Pui89/Extreme-Flood-Rescue-AI/pull/124) | [Run 41222937936](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/41222937936) | Same deterministic evidence-integrity checks; simulation evidence only |
| [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | [#101](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/pull/101) | [Run 41222943024](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/41222943024) | Same deterministic evidence-integrity checks; simulation evidence only |

All three benchmark-engine PRs are merged, and all three cited runs have GitHub Actions conclusion **success**. HOMEGUARD's separate initial CI run also completed successfully; it is not yet running the same benchmark engine. The engine checks integrity and consistency of supplied evidence; it does not authenticate the truth of the underlying observations, measure model accuracy, establish comparable cross-project scores, or validate physical performance. The runs reject any simulation step that claims hardware actuation.

The default-branch workflow runs observed on 31 October 2026 also completed successfully:
- Coconut: [automated verification](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/41241337764), [lightweight core tests](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/41241337730), and [security](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/41241337679).
- Flood Rescue: [automated verification](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/41241212702), [regression checks](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/41241212718), and [security](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/41241212728).
- Screening: [automated verification](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/41241242511), [Python tests](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/41241242543), and [security](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/41241242522).

These are separate workflow runs and test suites. Their results must not be summed into a single project score or presented as proof of field readiness.

## Current automated-check status

The listed workflow runs had completed with GitHub Actions conclusion **success** when inspected on 2026-10-30. The three lightweight CI-fix PRs (#151, #115, #93), three simulation-evaluation workflow PRs (#153, #116, #94), three fault-injection PRs (#154, #117, #95), and three modality/approval-gate PRs (#156, #118, #96) are now merged.

| Project | Merged workflow PRs | Observed passing workflow runs | Evidence boundary |
|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | [#151 — lightweight CI](https://github.com/Pui89/Coconut-Harvest-AI/pull/151); [#153 — simulation evaluation](https://github.com/Pui89/Coconut-Harvest-AI/pull/153); [#154 — adversarial safety cases](https://github.com/Pui89/Coconut-Harvest-AI/pull/154); [#156 — modality/approval gates](https://github.com/Pui89/Coconut-Harvest-AI/pull/156) | Lightweight verification, shared-interface smoke, pitfall detector, security, free local checks, and simulation evaluation | Software and rule-based simulation only; no coconut detector accuracy measured. |
| [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | [#115 — lightweight CI](https://github.com/Pui89/Extreme-Flood-Rescue-AI/pull/115); [#116 — simulation evaluation](https://github.com/Pui89/Extreme-Flood-Rescue-AI/pull/116); [#117 — adversarial safety cases](https://github.com/Pui89/Extreme-Flood-Rescue-AI/pull/117); [#118 — modality/approval gates](https://github.com/Pui89/Extreme-Flood-Rescue-AI/pull/118) | Automated verification, shared-interface smoke, Python tests on 3.10/3.11/3.12, security, pitfall detector, and simulation evaluation | Does not validate flood physics, 15 m depth capability, navigation, buoyancy or real rescue performance. |
| [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | [#93 — lightweight CI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/pull/93); [#94 — simulation evaluation](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/pull/94); [#95 — adversarial safety cases](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/pull/95); [#96 — modality/approval gates](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/pull/96) | Python tests, automated verification, shared-interface smoke, Python tests on 3.10/3.11/3.12, synthetic app regression, security, pitfall detector, and simulation evaluation | Does not validate chemical identification, X-ray capability, field screening accuracy or physical robot safety. Human review remains necessary. |

**Review state:** the three lightweight CI-fix PRs and three simulation-evaluation workflow PRs are merged. The workflow logs and report artifacts were inspected for the simulation PR heads before merge; later changes to the default branches can still alter results.


## Selected observed test counts

The job logs were inspected, not just the green status icons:

- **Coconut shared-interface smoke:** 15 tests run, 0 reported failures; interface/proposal-gate checks only.
- **Extreme Flood Rescue AI:** 419 pytest items passed in the inspected Python 3.11.17 job (3.17 seconds); the Python 3.10, 3.11 and 3.12 jobs all concluded success.
- **Multimodal Narcotics Screening AI:** 385 pytest items passed in the inspected Python 3.11.17 job (1.06 seconds); the Python 3.10, 3.11 and 3.12 jobs all concluded success.
- **Multimodal app regression:** the inspected synthetic pipeline smoke check passed for six synthetic cases; it explicitly says it is not a real-world benchmark. Regression jobs for Python 3.10, 3.11 and 3.12 all concluded success.

These counts are from different test suites and must not be summed into a single “PUI89 test count.” The two pytest counts are for one Python-version job each; their other matrix jobs also passed but are not added here. A passing CI job is not evidence of AI accuracy or physical-world performance.

## Reproducible simulation evaluation — observed results

On 2026-10-29, each simulation-evaluation workflow completed successfully on Python 3.11.17. Two follow-up PRs added six additional fault/modality/approval cases per project in total; the updated simulation workflows completed successfully after each addition. Each run printed a machine-readable report summary and uploaded report artifacts.

| Project | Scenarios passed | Steps passed | Failures | Hardware actuation |
|---|---:|---:|---:|---|
| Coconut Harvest AI | 13/13 | 15/15 | 0 | false |
| Extreme Flood Rescue AI | 13/13 | 15/15 | 0 | false |
| Multimodal Narcotics Screening AI | 13/13 | 15/15 | 0 | false |

The fault-injection cases verify expected fail-closed handling for missing emergency-stop telemetry (`SAFE_HOLD`), a malformed sensor-health Boolean (`SAFE_HOLD`), and Boolean-valued confidence (`UNKNOWN`). Additional gates verify conflicting observations and missing required modalities return `UNKNOWN`, while missing operator approval returns `REQUEST_APPROVAL`. These are specific software-policy checks, not exhaustive safety assurance.

These are results from the projects' existing **rule-based software simulation scenarios**. A 100% scenario pass rate applies only to the defined scenarios and is not a measure of perception accuracy, flood-depth capability, chemical identification, robot reliability, or field safety. The three project scenario sets are not interchangeable and should not be combined into a single cross-project performance score.

## World-state timestamp validation

On 2026-10-30, three dependency-light world-state validation changes were merged: [Coconut #146](https://github.com/Pui89/Coconut-Harvest-AI/pull/146), [Flood Rescue #111](https://github.com/Pui89/Extreme-Flood-Rescue-AI/pull/111), and [Multimodal Screening #88](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/pull/88). The changes reject combined world states when an observation timestamp is missing or malformed, including string, Boolean, and non-finite values, instead of risking ordering errors or silently selecting another observation. The associated Python tests and security/regression checks passed on the pull-request commits before merge. These are software input-validation safeguards only; they do not establish sensor calibration, real-time performance, perception accuracy, or physical safety.

## Observation source-provenance validation

On 2026-10-30, the same input-validation fix was merged across all three project repositories: [Coconut Harvest AI #157](https://github.com/Pui89/Coconut-Harvest-AI/pull/157), [Extreme Flood Rescue AI #119](https://github.com/Pui89/Extreme-Flood-Rescue-AI/pull/119), and [Multimodal Narcotics Screening AI #97](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/pull/97). Missing, empty, whitespace-only and non-string observation source identifiers are now treated as missing provenance and require human review. The focused PR workflows completed successfully before merge, including the shared world-state, free-local-check and security checks reported for each repository.

This is a software-contract improvement only. It does not prove that a sensor's source claim is authentic, that a dataset has reuse rights, or that a physical system is safe. Hardware actuation remains outside this interface.

## Shared evidence safeguards

The standard-library observability generator starts with conservative statuses: software/model/system/workflow/safety checks are `NOT_RUN`, and hardware is `NOT_CONNECTED`, unless supplied evidence is provided. A `PASS` or `FAIL` entry requires an evidence reference and observation timestamp. Schema validation checks format only; it does not authenticate evidence.

Shared software-contract and simulation-evidence checks cover world-state/confidence-field contracts, simulation-only action proposals, machine-readable failure/evidence reports, and rejection of missing or inconsistent report evidence. Passing validators prove only the checked software/report properties, not physical-world robot performance.

## Failure history and resolution status

A prior lightweight-runner attempt failed because it discovered and imported dependency-backed test modules without the project's full dependency/import environment (errors included missing project modules and optional packages). The three CI-fix PRs changed the lightweight job to compile configured Python folders and smoke-test the standard-library observability report, while leaving full unit/integration testing to dedicated project workflows. Those PRs are now merged, and the replacement lightweight jobs passed on the observed PR heads.

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

1. Continue monitoring the merged simulation workflows and preserve failed reports rather than hiding them.
2. Run Coconut dataset provenance, local file hash, annotation and source-group split checks when the original candidate image is available.
3. Obtain genuine detector predictions on a frozen held-out set and publish reproducible metrics—or document why inference remains blocked.
4. Add simulator-specific telemetry only where an actual simulator emits it; keep hardware fields NOT_CONNECTED until hardware is present and measured.


## Continuous improvement programme — approved direction

The shared programme now defines the 21-capability intelligence catalogue, common AI Core architecture, daily/weekly report contract, event-driven quality checks, weekly engineering review, monthly architecture review, human approval gates and staged HOMEGUARD demonstration. These are strategic specifications and staged targets; they are not claims that all capabilities or schedules are already implemented.

- [Read the PUI89 Continuous Improvement & Intelligence Programme](PUI89_CONTINUOUS_IMPROVEMENT_PROGRAMME.md).
- Current project evidence remains limited to the dated workflow runs and test results documented above. Audit existing automation before adding new jobs; reuse working checks and avoid duplicate workflows.
- HOMEGUARD AI is a proposed next project. Its first target is a clearly labelled synthetic three-floor building demonstration, not live building monitoring.
- Safety-critical changes, model/data approvals, releases and hardware-related interfaces require human review. No automatic hardware action, paid service, model download or unverified performance claim is authorized.


## Fourth product added — HOMEGUARD AI (2 November 2026)

[HOMEGUARD AI](https://github.com/Pui89/HomeguardAI) is now included in the PUI89 portfolio and website's product 04 pages. Its standalone repository contains a deterministic Python foundation, evidence-aware observations and baselines, quality/freshness/calibration checks, a synthetic three-floor scenario, machine-readable finding schema, automated tests and GitHub Actions CI.

- Initial CI run: [Run 41453149397](https://github.com/Pui89/HomeguardAI/actions/runs/41453149397) — completed successfully.
- Website product pages: [English](https://pui89.github.io/homeguard.html) · [Thai](https://pui89.github.io/homeguard-th.html).
- Standalone repository: [Pui89/HomeguardAI](https://github.com/Pui89/HomeguardAI).

**Evidence boundary:** HOMEGUARD's first CI validates its software foundation and synthetic report generation only. It is not yet using the same shared benchmark engine as the other three repositories. No calibrated building sensors, trained AI model, live monitoring, certified hazard detection, structural certification or field performance are claimed. The 29-capability catalogue remains a roadmap.

## Four-product PUI89 engineering direction

The four projects now follow the [PUI89 World-Class AI Blueprint](PUI89_WORLD_CLASS_AI_BLUEPRINT.md), which defines the shared AI Core, domain-specific adapters, zero-cost technology adoption rules, safe automation boundaries, evidence gates and staged development roadmap. The shared core is a set of contracts and reusable engineering practices; it does not imply one universal model or one common performance score.

- Coconut: reviewed dataset and first valid held-out vision benchmark.
- Flood Rescue: robust world-state, fault injection and platform-specific simulation.
- Screening: lawful sensor/data provenance, false-positive/false-negative evaluation and human review.
- HOMEGUARD: spatial sensor-quality model and multi-sensor building evidence.

Do not sum tests or scenario passes across projects into a single PUI89 score. Do not infer field readiness from successful CI.
