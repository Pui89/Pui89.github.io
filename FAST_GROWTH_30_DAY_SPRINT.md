# PUI89 AI Robotics — 30-Day Fast-Growth Sprint

**Goal:** Increase credible product value, visible proof, and customer-learning speed in 30 days without introducing unapproved spending. This is a plan with measurable exit criteria, not a claim of completed work or guaranteed growth.

## Growth strategy in one sentence

Win trust with one narrow, demonstrable agriculture workflow; show evidence publicly; speak to potential users; reuse the strongest components only after the flagship works.

## Rules for speed

- Keep the default additional budget at **฿0**. Use existing equipment and local/free tools; do not activate paid APIs, cloud compute, datasets, subscriptions or hardware without explicit approval.
- Never invent detector accuracy, field validation, customer interest, revenue or autonomous capability.
- Work in short increments that end with a test, screenshot, benchmark report, user conversation, or documented blocker.
- Do not build all five products at once. Coconut Orchard Intelligence is the flagship; the other repos remain smaller, honest research prototypes.
- Prefer a small working end-to-end workflow over adding many disconnected features.

## Week 1 — Make the flagship easy to evaluate

### Deliverables
1. Run the dataset promotion gate and publish the current blocked/eligible counts.
2. Resolve candidate image rights and label review only when evidence supports the decision.
3. Make the local annotator and demo instructions work from a clean Windows checkout.
4. Audit the launch scripts and document exact prerequisites.
5. Publish one concise product-status section: implemented, measured, blocked, next.

### Exit criteria
- Reproducible setup steps.
- No archived or unapproved labels entering training.
- Current data blockers are explicit and actionable.
- CI results are linked to the exact commit.

## Week 2 — Demonstrate one real AI capability

### Deliverables
1. Select a small, licence-compatible detector that can run locally on the available computer.
2. Check model licence, dependency footprint, hardware needs and weight-download size before choosing.
3. Run inference on permitted sample images; preserve outputs and configuration.
4. Compare detections against independently reviewed labels if enough valid labels exist.
5. Publish error examples and report precision/recall/F1 only if the evaluation set and ground truth support them.

### Exit criteria
- A reviewer can reproduce inference.
- Measured results include dataset size, hardware/software environment, threshold and limitations.
- If the dataset is too small or unapproved, publish the blocker rather than a misleading score.

## Week 3 — Turn the demo into customer learning

### Target users
- Coconut growers and orchard managers.
- Agricultural extension or research staff.
- Agricultural machinery and robotics groups.

### Actions
- Prepare a one-page problem brief and a short, honest demonstration.
- Ask at least five relevant people for feedback if access is available; record who was approached only with appropriate consent.
- Ask what task costs them time, how they currently measure it, what error is unacceptable, and what evidence would justify a pilot.
- Do not promise autonomous harvesting or claim market demand based on informal compliments.

### Exit criteria
- A short anonymized feedback summary, or an explicit note that user access remains a blocker.
- One prioritised problem hypothesis with a measurable success criterion.
- No claims of customer validation unless real feedback was obtained.

## Week 4 — Prove the next technical step

### Deliverables
1. Define a stable detection result schema with image ID, class, confidence, bounding box, model version and timestamp.
2. Add tests for invalid inputs, empty results and confidence thresholds.
3. Create one reproducible simulation scenario for coconut target selection or mobile orchard inspection.
4. Document what is simulated versus measured on real images.
5. Update the product evidence dashboard and record the next experiment.

### Exit criteria
- A tested interface that could be reused by later robot modules.
- One repeatable simulation run with scenario and outcome logs.
- No direct physical actuation from model output.

## Weekly scorecard

Record values only after evidence exists.

| Metric | Target / rule |
|---|---|
| Additional spend | ฿0 unless explicitly approved |
| Reproducible demo | 1 end-to-end local workflow |
| Dataset governance | 100% of training candidates pass the documented gate before promotion |
| AI benchmark | One reproducible result, only if approved labels and adequate test data exist |
| Customer discovery | Aim for 5 conversations; report actual count, never assume |
| Simulation | 1 repeatable scenario with logs |
| Public evidence | Update dashboard with links to commits, tests, data limitations and results |
| Unsupported claims | 0 |

## What not to do this month

- Do not buy a robot, GPU, domain, dataset or subscription.
- Do not train on images with unresolved rights or unreviewed annotations.
- Do not claim a simulated robot works in a real orchard.
- Do not spread effort evenly across all repositories.
- Do not optimize metrics on the final held-out test set.
- Do not use follower counts, stars or attractive images as substitutes for product evidence.

## Definition of progress

The sprint succeeds if PUI89 ends the month with a more reproducible flagship demo, a clearer evidence-backed product claim, a verified understanding of the next technical blocker, and real user feedback where access is possible. Revenue or company growth cannot be guaranteed by a 30-day engineering plan.
