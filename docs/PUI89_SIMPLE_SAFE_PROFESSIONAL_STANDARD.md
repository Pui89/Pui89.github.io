# PUI89 Simple, Safe & Professional Engineering Standard

**Version:** 1.0  
**Review date:** 8 November 2026  
**Applies to:** All seven PUI89 projects and shared engineering infrastructure  
**Status:** Proposed portfolio standard — review required

## Purpose

Make every PUI89 system easy to understand, safe by default, professionally maintained and supported by verifiable evidence. Prefer the smallest design that meets the requirement. Complexity must earn its place.

## 1. Easy to understand and operate

- Give every page, tool and workflow one clear purpose and a plain-language explanation.
- Use consistent names, navigation, status labels and units across English and Thai.
- Show the next safe action; avoid unnecessary settings, duplicate controls and unexplained scores.
- Provide useful empty, loading, success, warning and failure states.
- Make errors explain what happened, what was affected and how to recover safely.
- Keep essential functions usable on mobile, with keyboard navigation, visible focus and readable contrast.

## 2. Safe by default

- Default to read-only, advisory or simulation-only behavior.
- Never turn a model prediction into a physical command or consequential decision automatically.
- Require explicit human approval for any future action with physical, financial, legal, privacy or safety consequences.
- Validate inputs, units, timestamps, ranges, identity and evidence references at system boundaries.
- On missing, stale, contradictory, malformed or out-of-scope evidence, abstain or enter a safe hold; never silently guess.
- Use least privilege, protected secrets, minimal permissions and documented recovery procedures.
- Provide a clear stop, disable or rollback path wherever an action could have an effect.
- Keep people, animals and bystanders in the safety analysis for robotics and mobility concepts.

## 3. Evidence and honest status

Use these status terms consistently:

| Status | Meaning |
|---|---|
| Proposed | Design or plan only |
| Implemented | Code or documentation exists |
| Tested | A named test passed in a stated environment |
| Measured | A value was measured with method, units and date |
| Simulation-only | Tested in a defined simulated environment |
| Validated | Appropriate independent or domain-specific evidence supports the stated claim |
| Not assessed | No adequate evidence is available |

- Every score, percentage, graph and readiness claim must link to a dated method and evidence.
- Distinguish test coverage from product readiness and from real-world validation.
- Record known limitations, uncertainty, data provenance and unresolved failures.
- Never imply certification, field performance, autonomy, waterproofing, fire resistance or commercial readiness without appropriate evidence.

## 4. Professional software and repository practice

- Keep dependencies minimal, pinned where practical, licence-checked and justified.
- Prefer standard-library and existing repository capabilities when adequate.
- Do not add paid APIs, subscriptions, cloud compute or external services without explicit approval.
- Require automated tests and security checks for relevant changes; investigate failures rather than suppressing them.
- Use small, reviewable pull requests with purpose, scope, risk, tests and rollback notes.
- Protect default branches. Do not merge, deploy or change repository security settings without explicit authorization.
- Never commit credentials, personal data or unlicensed datasets.

## 5. Robotics, devices and physical product concepts

- Keep physical actuation disabled in software tests and examples unless a separately approved, controlled test plan exists.
- Define operating envelope, hazards, emergency stop, safe state, maintenance and failure behavior before any physical trial.
- Treat water resistance, fire resistance, battery safety, structural strength and environmental tolerance as unverified until tested to a suitable method.
- Do not represent a concept drawing, simulation or software mock-up as a built or certified product.

## 6. Privacy and responsible data

- Collect only data necessary for a stated purpose; avoid unnecessary retention and exposure.
- Document data source, licence, consent or lawful basis where applicable, access and retention.
- Treat sensitive or uncertain detections as review prompts, not proof.
- Provide human review and an appeal or correction path for consequential outputs.

## 7. Release checklist

A change is ready for review only when applicable items are satisfied:

- [ ] Purpose and user impact are clear.
- [ ] Safe default and failure behavior are documented.
- [ ] Inputs and evidence are validated.
- [ ] Tests and security checks have been run; results are linked.
- [ ] Limitations and unverified claims are explicit.
- [ ] Privacy, licence and dependency impacts are checked.
- [ ] English and Thai user-facing content is consistent where applicable.
- [ ] Rollback or recovery steps are available.
- [ ] A human reviewer can understand the change without hidden context.

A failed or unrun check must be labelled clearly; it is not a pass.

## 8. Continuous improvement

Review this standard monthly and after any security incident, safety-relevant failure, major architecture change or new physical capability. Record the review date, evidence examined, decisions, owner and open actions. Do not inflate maturity scores merely because documentation has been added.

---

**PUI89 engineering principle:** Simple to use. Strict about safety. Honest about evidence. Consistent in quality.
