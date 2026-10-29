# PUI89 AI — Engineering Quality Dashboard

**Purpose:** one place to track software-verification progress across the three PUI89 AI projects. This dashboard distinguishes implemented checks from results that still need to be observed or measured.

## Execution status

**Current truthful status before the next GitHub Actions run:** automated test infrastructure is configured; the newest run outcome is **not yet verified here**. Do not infer a pass from the presence of workflow files.

The combined workflow runs the standard-library unit tests in all three repositories, writes a JSON/Markdown report, and preserves each project's full test log even when a project fails. The artifact is retained for 14 days. A failed project causes the combined job to fail, while the per-project logs remain available for diagnosis.

## Current project comparison

| Project | Engineering focus | Current evidence foundation | Highest-priority gap |
|---|---|---|---|
| [Coconut Harvest AI](https://github.com/Pui89/Coconut-Harvest-AI) | Agricultural perception, maturity classes, harvesting task planning | Shared PUI89 core tests; detector-CSV evaluator and its unit tests; dataset and evaluation gates documented | Verified/licensed dataset, reviewed annotations, leakage-safe held-out split, real detector predictions, then measured metrics |
| [Extreme Flood Rescue AI](https://github.com/Pui89/Extreme-Flood-Rescue-AI) | Flood-response perception and rescue planning | Shared core tests and documented simulation/fault-injection roadmap | Reproducible scenarios, missing/stale/conflicting sensor tests, and validated water/navigation simulation |
| [Multimodal Narcotics Screening AI](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI) | Multimodal screening support with human review | Shared core tests and documented uncertainty, abstention and human-review safeguards | Lawful, licensed evaluation data and independently validated sensor-specific screening performance |

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
