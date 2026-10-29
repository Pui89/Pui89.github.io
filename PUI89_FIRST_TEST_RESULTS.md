# PUI89 First Automated Test Results

**Report date:** 29 October 2026 (UTC)  
**Status:** Shared-core CI passed; Coconut evaluator implementation tests passed; real detector performance remains **NOT RUN**.

## Latest verified combined run

- Workflow run: [PUI89 Combined Quality Report — successful run](https://github.com/Pui89/Pui89.github.io/actions/runs/40874307468)
- Workflow commit: `59340197a4829daf39505712165e8f1ed67a0378`
- Artifact: [Download combined report and per-test logs](https://github.com/Pui89/Pui89.github.io/actions/runs/40874307468/artifacts/12897491813)
- Environment: GitHub-hosted Ubuntu runner, Python 3.11; no model weights, GPU, paid API or robot hardware used.

| Test scope | Actual result | Meaning |
|---|---:|---|
| Coconut Harvest AI shared PUI89 core | **13 passed, 0 failed** | World-state, confidence validation, simulation-only action proposal and failure-report contracts |
| Extreme Flood Rescue AI shared PUI89 core | **13 passed, 0 failed** | Same shared contract suite |
| Multimodal Narcotics Screening AI shared PUI89 core | **13 passed, 0 failed** | Same shared contract suite |
| Coconut detection evaluator unit tests | **5 passed, 0 failed** | Checks evaluator logic such as IoU, thresholds and score filtering—not detector accuracy |

**Shared-core total: 39 passed, 0 failed.**  
**Coconut evaluator unit-test total: 5 passed, 0 failed.**

## Failure transparency

The first attempt to run every test discovered under all three `tests/` directories failed. Actual output:

| Repository | Broad-suite outcome | Primary issues observed |
|---|---|---|
| Coconut Harvest AI | 246 tests discovered; **17 errors** | Missing optional `pytest`, `numpy`, `torch` and project import-path/package setup in the lightweight runner; one additional test error also appeared |
| Extreme Flood Rescue AI | 208 tests discovered; **10 errors** | Missing optional `pytest`, `numpy`, `torch` and project import-path setup |
| Multimodal Narcotics Screening AI | 165 tests discovered; **15 errors** | Missing optional `pytest` and project package import paths |

These broad-suite results are **failures**, not passes. They do not by themselves prove the underlying project code is defective: the runner intentionally installed no project dependencies, and several tests could not import their dependencies or modules. However, they show that the entire project-specific suites are **not currently verified in this minimal environment**. The combined workflow was therefore scoped to the explicitly shared, standard-library core contract suite, with Coconut's dependency-free evaluator tests added separately. The complete suite still needs a deliberate dependency and import-path plan before it can be fairly assessed.

## Coconut Harvest AI — first measurable AI evaluation

Existing evaluator: [`tools/evaluate_coconut_detections.py`](https://github.com/Pui89/Coconut-Harvest-AI/blob/main/tools/evaluate_coconut_detections.py).

It compares reviewed ground-truth bounding boxes with predictions exported by a real detector and reports true/false positives, false negatives, precision, recall and F1 at specified IoU and score thresholds. It is a single-threshold box evaluator, **not mAP**, and does not run a detector.

**Real detector baseline: NOT RUN / NOT MEASURED.** The repository evidence available for this run does not establish both a rights-reviewed, leakage-safe held-out ground-truth CSV and predictions from an actually run detector for those same images. We will not fabricate predictions or convert evaluator unit tests into AI accuracy claims.

Once those inputs are ready, run in the Coconut Harvest AI repository:

```bash
python tools/evaluate_coconut_detections.py \
  --ground-truth path/to/heldout_ground_truth.csv \
  --predictions path/to/real_detector_predictions.csv \
  --iou 0.50 --score 0.25 --output evaluation.json
```

Ground-truth columns: `image_id,xmin,ymin,xmax,ymax,class`. Prediction columns: `image_id,xmin,ymin,xmax,ymax,class,score`. Record the dataset/manifest SHA-256, code commit, detector/checkpoint and hash, held-out source/tree/session split, sample counts, environment, thresholds and failures. Do not tune on the final held-out set.

## Next gates

1. Fix the dependency/import setup for full project-specific suites without automatically downloading large ML stacks.
2. Complete Coconut dataset rights review, annotation QA and source/tree/session-separated held-out split.
3. Run the evaluator on actual detector predictions and publish its JSON output and failure analysis.
4. Only after the foundation is stable, test VLMs, mock VLA interfaces and robotics simulation—after checking licences, resource requirements and cost.
5. Keep all proposed actions simulation-only; these tests do not validate real robot operation or physical safety.
