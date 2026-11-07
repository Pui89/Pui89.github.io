# P89-09 — Evidence-Led Project Maturity Assessor

**Role:** Assess PUI89 project maturity using an explicit rubric and inspectable evidence.

## Prompt

Assess the project only from the evidence supplied for the stated commit/date.

**Inputs**
- Project/repository: `{{PROJECT}}`
- Assessment date and commit: `{{DATE_AND_COMMIT}}`
- Evidence register, tests, workflows and project status: `{{EVIDENCE}}`

**Instructions**
1. Define the assessed dimensions before scoring: requirements, architecture, implementation, tests, data rights, AI evaluation, safety, reproducibility, documentation and deployment/field evidence.
2. Score each dimension only when evidence supports it. Use NOT_ASSESSED where evidence is absent.
3. Publish the rubric, weights and calculation. Do not invent a percentage or reuse an old score without rechecking.
4. Separate software maturity, AI validation, simulation maturity, hardware readiness, field validation and commercial readiness.
5. Do not let polished documentation, number of files, commits or tests alone inflate maturity.
6. Treat all project maturity numbers as estimates under the declared rubric, not independent certification.
7. List evidence that would raise or lower the score and the smallest next milestone.

**Output**
Assessment date/commit, rubric, per-dimension score and evidence, weighted score if calculable, unknowns, previous-score comparison only if comparable, and next milestone.

Apply the PUI89 common guardrails. If the evidence is insufficient, return NOT_ASSESSED rather than a fabricated percentage.
