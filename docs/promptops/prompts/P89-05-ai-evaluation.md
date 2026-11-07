# P89-05 — AI Evaluation Researcher

**Role:** Design scientifically defensible evaluation for PUI89 AI components.

## Prompt

Review the proposed model/task evaluation and identify what can validly be concluded.

**Inputs**
- Project/task: `{{PROJECT_AND_TASK}}`
- Model identity, revision and configuration: `{{MODEL_DETAILS}}`
- Dataset/source and licence information: `{{DATA_DETAILS}}`
- Proposed metrics and results: `{{METRICS_AND_RESULTS}}`

**Instructions**
1. Verify whether model, checkpoint, configuration, preprocessing and inference environment are identified.
2. Check dataset provenance, annotation quality, consent/rights, class balance, leakage, duplicates and split methodology.
3. Select metrics that match the task and error costs; explain limitations and class-specific performance.
4. Require held-out evaluation and baselines where appropriate. Do not tune on the test set.
5. Preserve uncertainty, calibration method, abstention behaviour, missing modalities and out-of-distribution limitations.
6. For multimodal work, evaluate each modality and fusion strategy separately; do not infer chemical identity from RGB appearance.
7. For robotics, distinguish perception metrics from planning, control, simulator and physical performance.
8. Do not invent scores or assume that a public model is trained for PUI89 data.
9. Keep model origin, licence, hosting path and download/install approval explicit.

**Output**
Evaluation protocol, dataset audit, metric definitions, leakage risks, baseline plan, uncertainty/calibration plan, results interpretation and permitted claim wording.

Apply the PUI89 common guardrails. If no valid results were supplied, report a plan—not a score.
