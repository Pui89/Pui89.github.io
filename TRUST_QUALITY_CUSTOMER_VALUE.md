# PUI89 AI Robotics — Trust, Quality and Customer Value Standard

**Public promise:** Practical AI and robotics prototypes developed with measurable evidence, transparent limitations, and a zero-spend-first approach.

This standard describes how PUI89 intends to work. It is not a certification, independent audit, or claim that every project is already commercially validated.

## What trust looks like in practice

### 1. Evidence is visible
For each public product claim, identify the repository version, test conditions, dataset provenance and permissions, metric definitions, baseline, sample count, failures, and reproducibility instructions. Mark features as **implemented**, **tested**, **prototype**, **planned**, or **not validated**. Do not turn concept artwork into evidence of a working robot.

### 2. Comparisons are fair
Compare against relevant alternatives doing the same job, on the same held-out data or scenario where feasible. Record versions and licences, use predeclared scoring rules, and state what was not tested. Never say “best”, “most accurate”, or “industry-leading” without evidence that supports that exact claim.

### 3. Safety and people come first
Flag uncertain results; allow human correction and override; document failure modes. Software tests do not certify physical safety. Flood-rescue operation, physical harvesting, and consequential screening decisions require separate domain-specific engineering, appropriate permissions, and qualified review before any operational deployment.

### 4. Privacy and rights are respected
Use data only with permission and a clear purpose. Do not publish customer images, personal information, confidential records, credentials, or sensitive operational details. Check licences for code, datasets, and model weights separately. State data handling and retention clearly for each pilot.

### 5. Value is measured, not promised
Start with the customer's existing workflow and baseline. Agree on success criteria before a pilot. Measure relevant outcomes such as task time, correction effort, false alarms, missed cases, task success, runtime, support burden, and total cost. Do not promise savings or return on investment before measuring them.

### 6. Cost is transparent
Target **฿0 additional development spending**. Prefer existing hardware, free and open-source tools, and local execution where practical. Do not use services that may create charges, buy equipment, or make financial commitments without explicit owner approval. Free-tier limits and licences must be checked; free does not always mean unlimited or commercially unrestricted.

## Product maturity labels

- **Concept:** design or proposed workflow only.
- **Prototype:** initial implementation exists; reliability and task performance may be unproven.
- **Tested:** specified tests have been run; publish scope, results and limitations.
- **Pilot-evaluated:** tested with a consenting partner under a written scope and agreed criteria.
- **Deployment-ready:** only after applicable reliability, safety, privacy, security, licensing, support and operational requirements have been reviewed. This label must not be used casually.

A product can be at different maturity levels for different capabilities. Report each capability separately.

## Product-specific customer value

### Coconut Harvest AI
Target job: help orchard users review coconut observations and organize inspection/harvest planning. Prove value by comparing against the current human workflow and a defined computer-vision baseline. Measure misses, false detections, correction time, report time, and performance across varied orchard conditions. Do not claim autonomous harvesting, maturity accuracy, yield prediction, or savings until each is implemented and validated.

### Flood Rescue AI
Target job: research and simulation for reconnaissance, hazard mapping, and navigation support. Measure repeatable simulated mission success, collisions, mapping error, recovery, and human interventions. Simulation is not evidence of real flood capability; no real rescue use should be implied.

### Multimodal Narcotics Screening AI
Target job must be narrowly defined and lawful. Appearance alone cannot establish chemical identity. Any screening evaluation requires authorized data and suitable expert-reviewed ground truth. Measure false positives and false negatives and retain human review. Do not claim validated substance identification or enable autonomous enforcement from model outputs.

## Customer pilot discipline

Before starting any pilot, write down:
- The customer problem, current process, and person responsible for the decision.
- The data and permissions available, including confidentiality and retention.
- Exact scope, exclusions, timeline, responsibilities, and any costs.
- Baseline, evaluation metrics, sample size, and success/failure criteria.
- What results may be shared publicly and what must remain confidential.
- What happens if the system fails or produces uncertain output.

No partner, pilot, testimonial, or commercial result should be implied until it actually exists.

## Release checklist

- [ ] Intended user and job are clearly stated.
- [ ] Implemented capabilities are separated from roadmap items.
- [ ] Tests and current CI results are linked and checked.
- [ ] A relevant baseline and fair evaluation protocol exist.
- [ ] Failure cases and limitations are documented.
- [ ] Data permissions and software/model licences are checked.
- [ ] Privacy, security and applicable safety risks are reviewed.
- [ ] Cost assumptions and free-tier limits are documented.
- [ ] Every marketing claim is supported by evidence.
- [ ] No unapproved expense or financial commitment is created.

## Our standard

**Trust is not a design style or a slogan. It is a habit of showing evidence, admitting uncertainty, respecting customers, protecting their data, and improving against a measurable baseline.**
