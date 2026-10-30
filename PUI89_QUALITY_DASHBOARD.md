# PUI89 AI — Engineering Quality Dashboard

**Purpose:** one place to track software-verification progress across the three PUI89 AI projects. This dashboard distinguishes implemented checks from results that still need to be observed or measured.

## Execution status

**Latest checked evidence (29 October 2026):** the combined report [run 40877473235](https://github.com/Pui89/Pui89.github.io/actions/runs/40877473235) passed 52 selected tests (39 shared-core, 5 Coconut evaluator, 4 Coconut dataset-preflight). Newer per-project runs show [Flood full tests](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40882267388) passing 419 tests on `main`, and [Narcotics full tests](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40919469797) passing 385 tests on the feature branch across Python 3.10, 3.11 and 3.12. The [Flood simulation](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40919457152) and [Narcotics simulation](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40919469891) each passed 7/7 configured rule-based scenarios and 9/9 steps with hardware actuation disabled. These do not establish model accuracy or physical validation. The combined artifact is available [here](https://github.com/Pui89/Pui89.github.io/actions/runs/40877473235/artifacts/12899230702).

The combined workflow runs the standard-library unit tests in all three repositories, writes a JSON/Markdown report, and preserves each project's full test log even when a project fails. The artifact is retained for 14 days. A failed project causes the combined job to fail, while the per-project logs remain available for diagnosis.

## Current project comparison

| Project | Engineering focus | Current evidence foundation | Highest-priority gap |
|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | Agricultural perception, maturity classes, harvesting task planning | Selected shared-core/evaluator/preflight tests pass; lightweight main-branch verification pass | Full dependency-backed test evidence, reviewed dataset, leakage-safe held-out split and real detector predictions |
| [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | Flood-response perception and rescue planning | 419 tests passed on `main`; feature-branch rule-based simulation passed 7/7 scenarios and 9/9 steps | Merge/verify latest feature-branch simulation changes on `main`; validate actual perception/navigation only with appropriate data and simulator |
| [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | Multimodal screening support with human review | 385 tests passed on feature branch across Python 3.10–3.12; rule-based simulation passed 7/7 scenarios and 9/9 steps | Confirm changes on `main`; lawful sensor-specific evaluation data and independently validated performance |

**Readiness ranking:** Coconut Harvest AI is the recommended first project to advance based on the documented engineering and evaluation path. This is not a ranking of measured AI accuracy. No real detector benchmark score is claimed by this dashboard.

## Automated verification

- [Run combined quality report](https://github.com/Pui89/Pui89.github.io/actions/workflows/pui89-combined-quality-report.yml)
- [Coconut Harvest AI Actions](https://github.com/Pui89/Coconut-Harvest-AI/actions)
- [Extreme Flood Rescue AI Actions](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions)
- [Multimodal Narcotics Screening AI Actions](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions)
- [Portfolio verification Actions](https://github.com/Pui89/Pui89.github.io/actions)

Open the newest combined workflow run. Check its conclusion and download the `pui89-combined-quality-report` artifact. The Markdown/JSON report gives each project's status; each `pui89-*-tests.txt` file contains the full unittest output, including tracebacks and failed test names. A report that says `review_required` or a project that says `failed` must remain visible and be fixed, not rewritten as a pass.

## Coconut Harvest AI — first measurable baseline

The evaluator already in the repository is `tools/evaluate_coconut_detections.py`. It compares manually reviewed ground-truth bounding boxes with predictions exported by an actual detector. It reports counts, precision, recall and F1 at declared IoU/score thresholds; it is a single-threshold box evaluator, **not mAP**, and does not run a model.

After rights review, annotation QA, and a source/tree/session-separated held-out split are complete, run:

```bash
python tools/evaluate_coconut_detections.py --ground-truth path/to/heldout_ground_truth.csv --predictions path/to/real_detector_predictions.csv --iou 0.50 --score 0.25 --output evaluation.json
```

Required ground-truth columns: `image_id,xmin,ymin,xmax,ymax,class`.
Required prediction columns: `image_id,xmin,ymin,xmax,ymax,class,score`.

Use actual model predictions and the same pixel coordinate system as the ground-truth boxes. Record the dataset/manifest SHA-256, code commit, detector/checkpoint and its hash, split policy, number of held-out images/scenes, environment and thresholds. Do not use the same images to tune and report final performance.

**Baseline status: NOT RUN / NOT MEASURED in this dashboard.** No reviewed held-out ground-truth CSV and corresponding real detector prediction CSV have been established as available evidence for this run. Empty, invented or synthetic predictions must not be reported as model accuracy. The existing evaluator's unit tests validate the metric code only; they are not a performance benchmark.

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

1. Observe the triggered combined workflow and publish its actual per-project results, including failures.
2. Fix any genuine shared-test failures before adding new model dependencies.
3. For Coconut Harvest AI, complete dataset provenance, annotation QA and leakage-safe split; then run the detector evaluator against actual held-out predictions.
4. For Flood Rescue AI, test sensor dropout, stale readings, contradictory measurements and conservative safe-stop behavior in deterministic scenarios.
5. For Narcotics Screening AI, test missing/conflicting modalities, uncertainty/abstention and human-review routing; do not equate RGB appearance with chemical identification.
6. Add VLMs, mock VLA interfaces and robotics simulation only after the software tests are stable; preflight licence, resource use and cost before optional installs.


## New engineering gates added

- [Shared engineering charter](https://github.com/Pui89/Pui89.github.io/blob/main/PUI89_ENGINEERING_CHARTER.md): evidence labels, experiment metadata, safety principles and merge checklist.
- [Coconut dataset preflight validator](https://github.com/Pui89/Coconut-Harvest-AI/blob/main/tools/validate_coconut_dataset.py): dependency-free checks for manifest fields, duplicate image IDs, annotation box validity, optional image file/hash checks, and source/tree/session split leakage.
- [Coconut safety and validation gates](https://github.com/Pui89/Coconut-Harvest-AI/blob/main/docs/PUI89_SAFETY_AND_VALIDATION_GATES.md).
- [Flood rescue safety and validation gates](https://github.com/Pui89/Extreme-Flood-Rescue-AI/blob/main/docs/PUI89_SAFETY_AND_VALIDATION_GATES.md).
- [Multimodal screening safety and human-review gates](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/blob/main/docs/PUI89_SAFETY_AND_VALIDATION_GATES.md).

The Coconut validator and its new unit tests have been added to the combined workflow. Their result remains **not verified until the next Actions run completes**. The validator's PASS_PREFLIGHT status is not a detector benchmark; it deliberately emits no accuracy metrics.

- [Experiment record JSON Schema](https://github.com/Pui89/Pui89.github.io/blob/main/schemas/pui89-experiment-record.schema.json): a common structure for reproducible run metadata and explicit status labels.
- [Flood rescue repeatable scenario matrix](https://github.com/Pui89/Extreme-Flood-Rescue-AI/blob/main/docs/REPEATABLE_SCENARIO_MATRIX.md): scenario and fault-injection plan; not yet executed simulation evidence.
- [Multimodal screening repeatable scenario matrix](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/blob/main/docs/REPEATABLE_SCENARIO_MATRIX.md): sensor disagreement, calibration, ambiguity and human-review tests; not validated sensor performance.


## Per-project status — 29 October 2026 (latest checked runs)

| Project | Verified software checks in combined run | AI/model performance | Simulation / physical status | Next gate |
|---|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | 13 shared-core + 5 evaluator + 4 dataset-preflight tests passed in selected run; lightweight main checks pass | Real detector accuracy **NOT MEASURED** | Preflight tests used synthetic fixtures; physical harvesting **not validated** | Run full dependency-backed suite; validate real dataset and held-out predictions |
| [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | 419 tests passed on `main` | Detection/navigation performance **not established by these tests** | Feature-branch rule-based simulation: 7/7 scenarios, 9/9 steps; physical rescue **not validated** | Confirm/merge feature branch; then validate simulator/perception separately |
| [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | 385 tests passed on feature branch (Python 3.10, 3.11, 3.12) | Substance-identification performance **NOT MEASURED** | Feature-branch rule-based simulation: 7/7 scenarios, 9/9 steps; physical screening **not validated** | Confirm/merge feature branch; validate sensor-specific lawful test data and human review |
| [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | 13 shared-core tests passed | Substance-specific performance **not measured** | Scenario matrix documented; sensor and physical robot validation **not established** | Define sensor modality/calibration and run human-reviewed, lawful evaluation |

**Interpretation:** 52 passing tests in the combined run means the selected software test scopes passed. It does not mean 52 AI capability tests, a trained model benchmark, or physical robot validation. Earlier broad project test runs exposed optional-dependency/import errors and remain a separate unresolved test-infrastructure task.


## Master roadmap: unfinished work, current checks, fixes and future levels

See the [PUI89 Master Roadmap](PUI89_MASTER_ROADMAP.md) for each project's:
- verified work and test results;
- work currently identified for checking (not implied background execution);
- unresolved defects and blockers;
- ordered next process;
- next upgrade level and longer-term future;
- definition-of-done checklist.

The immediate priority is to verify the newest CI run, repair broad-suite test-environment/import failures transparently, then run the Coconut dataset preflight against reviewed real data. Model benchmarks, flood simulations and sensor tests remain unmeasured until actually run.


## Latest Coconut simulation-only run (29 October 2026)

The [Coconut Simulation Evaluation run 40881372992](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40881372992) completed successfully: **7/7 configured simulation scenarios passed, 9/9 steps passed, 0 reported scenario failures**. The run recorded hardware_actuation=false and explicitly labels the result simulation-only, not real-world detector or robot validation. [Download the simulation report artifact](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40881372992/artifacts/12901050654).

This is a separate simulation result and must not be added to the 52 software unit-test count or interpreted as model accuracy.


## Latest per-project lightweight verification — 29 October 2026

The newest checked default-branch lightweight verification runs completed successfully:

| Project | Run | Result in the emitted report | Explicit limit |
|---|---|---|---|
| Coconut Harvest AI | [40881602888](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40881602888) | Python 3.11.17 compile checks: 0 errors; observability smoke: PASS; reported failure count: 0 | Full dependency-backed unit tests were not run in this lightweight preflight |
| Extreme Flood Rescue AI | [40878523954](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40878523954) | Python 3.11.17 compile checks: 0 errors; observability smoke: PASS; reported failure count: 0 | Full dependency-backed unit tests were not run in this lightweight preflight |
| Multimodal Narcotics Screening AI | [40878549402](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40878549402) | Python syntax compilation and dependency-free observability smoke: PASS | This workflow is a lightweight verification scope, not a full model/sensor benchmark |

Artifacts:
- [Coconut lightweight report](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40881602888/artifacts/12901395117)
- [Flood lightweight report](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/runs/40878523954/artifacts/12898129816)
- [Narcotics lightweight report](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/40878549402/artifacts/12899860349)

The recent lightweight checks pass, but they do **not** close the previously recorded broad-suite import/optional-dependency repair task because they deliberately do not discover or execute the full dependency-backed test suites. Continue to report that work as unfinished until a dedicated broad-suite run proves otherwise.


## New shared reporting standard — 30 October 2026

- [PUI89 Verification and Failure Report Standard](PUI89_FAILURE_REPORT_STANDARD.md) defines common PASS / FAIL / BLOCKED / NOT_RUN / PARTIAL statuses and requires explicit scope and evidence limitations.
- [Machine-readable JSON Schema](schemas/pui89-failure-report.schema.json) defines a consistent structure for run metadata, test counts, failure records, blockers, measured metrics, and claims about software checks, AI evaluation, simulation, and hardware validation.
- [Coconut lightweight core tests](https://github.com/Pui89/Coconut-Harvest-AI/actions/runs/40937571854) completed successfully: **36 selected tests passed** under Python 3.12 using pytest only. This is a focused core/world-state test scope, not Coconut's full test suite and not AI-performance validation.

**Next engineering step:** add a tiny report emitter and schema-validation tests to the shared core, then adopt the report format project by project. Do not publish guessed metrics or mark a planned simulator as executed.


## Report generator implementation — 30 October 2026

- Added [dependency-free report builder and contract validator](tools/pui89_report.py). It writes the shared JSON report structure, records explicit software/AI/simulation/hardware claims, and rejects invalid status/count/commit/failure fields without requiring a JSON Schema package.
- Added [six contract tests](tests/test_pui89_report.py), including valid report acceptance, missing fields, invalid status/commit, negative counts, incomplete failure details, and a CLI round-trip.
- Updated the combined quality workflow to run the report-contract tests and trigger on changes to the standard, schema, generator, and tests.
- **Verification status:** [combined workflow run 40944240576 passed](https://github.com/Pui89/Pui89.github.io/actions/runs/40944240576). All six report-contract tests passed; the three shared-core project checks also passed in that run, along with five Coconut evaluator tests and four dataset-preflight tests. The validator is a dependency-free contract check, not a complete implementation of every JSON Schema keyword.


## Automated per-project verification reports — 30 October 2026

The [combined quality workflow run 41062484106](https://github.com/Pui89/Pui89.github.io/actions/runs/41062484106) completed successfully. It generated and validated one standardized JSON report for each project from the actual selected shared-core and safety/conformance test outcomes:

- `reports/coconut-harvest-verification.json`
- `reports/extreme-flood-rescue-verification.json`
- `reports/narcotics-screening-verification.json`

The reports were uploaded with the combined Markdown/JSON report and test logs in the [workflow artifact](https://github.com/Pui89/Pui89.github.io/actions/runs/41062484106/artifacts/12979947742). Artifact retention is 14 days (through 13 November 2026).

**Scope limitation:** these reports cover only the two selected dependency-free shared suites per project. They are not full-suite, AI-performance, simulator-fidelity or physical-hardware validation results. The report generator uses the actual discovered test totals and separates passed, failed, skipped and blocked counts.

**Next:** improve failure-summary parsing for all unittest summary formats, add explicit report-schema validation, and extend the same evidence contract to separately executed project-specific suites without installing heavy AI dependencies by default.


## Shared health-gate upgrade — 31 October 2026

A matching dependency-free `pui89_core/health_gate.py` module, regression tests, and a dedicated lightweight GitHub Actions workflow have been added to all three application repositories:

- [Coconut Harvest AI health-gate workflow](https://github.com/Pui89/Coconut-Harvest-AI/actions/workflows/pui89-health-gate.yml)
- [Extreme Flood Rescue AI health-gate workflow](https://github.com/Pui89/Extreme-Flood-Rescue-AI/actions/workflows/pui89-health-gate.yml)
- [Multimodal Narcotics Screening AI health-gate workflow](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/workflows/pui89-health-gate.yml)

The gate checks required telemetry types, emergency-stop state, sensor freshness, perception/localization/communications health, safety-monitor health, operator approval, and finite confidence. Outcomes are limited to `SIMULATION_READY`, `SAFE_HOLD`, `STOPPED`, or `REQUEST_HUMAN_REVIEW`. Every outcome explicitly sets `physical_actuation_permitted=false`.

Ten regression tests per repository cover healthy simulation-only proposals, missing/malformed telemetry, emergency stop, unhealthy safety monitor, sensor faults, missing operator approval, low/invalid confidence, invalid thresholds, and absent input.

**Verification status:** workflows were created and queued at the time of this update; passing results have not yet been confirmed. The change adds a software-level gate, not a certified safety controller or hardware interlock.


## Long-horizon robustness evaluation — 31 October 2026

The shared platform now contains a dependency-free [PUI89 Long-Horizon Evaluation Framework](https://github.com/Pui89/Pui89.github.io/blob/main/PUI89_LONG_HORIZON_EVALUATION.md), including a deterministic runner, synthetic scenarios, regression tests and a lightweight [GitHub Actions workflow](https://github.com/Pui89/Pui89.github.io/actions/workflows/pui89-long-horizon-evaluation.yml).

The first scenario pack exercises multi-step baseline behavior, missing/stale evidence, sensor recovery, conflicting/noisy/OOD evidence, uncertainty carry-forward and latched stop behavior. Reports contain per-step state traces and injected faults.

**Verification:** the first CI attempt found one failing invalid-confidence precedence test. The code was corrected in commit 67126702170101d941e41b7fb48c2f49e79e7524; the corrected workflow is pending verification. Do not describe this as a passing benchmark until the rerun is complete.

**Scope:** synthetic policy tests only. No AI accuracy, statistical calibration, real sensor performance, simulation fidelity or physical robot safety is established. Project-specific adapters for the three applications are still pending.
