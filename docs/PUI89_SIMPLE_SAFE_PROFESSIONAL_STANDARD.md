# PUI89 Simple, Safe & Professional Engineering Standard

**Version:** 1.1  
**Review date:** 15 November 2026  
**Applies to:** All seven PUI89 projects, the Shared AI Core and shared engineering infrastructure  
**Status:** Proposed portfolio standard — review required

## Purpose

Make every PUI89 system easy to understand, safe by default, professionally maintained and supported by verifiable evidence. Prefer the smallest design that meets the requirement. Complexity must earn its place. Prefer open-source, inspectable and maintainable approaches where they meet the requirement.

## 1. Easy to understand and operate

- Give every page, tool and workflow one clear purpose and a plain-language explanation.
- Use consistent product names, navigation, status labels and units across English and Thai.
- Show the next safe action; avoid unnecessary settings, duplicate controls, feature bloat and unexplained scores.
- Provide useful empty, loading, success, warning and failure states.
- Make errors explain what happened, what was affected and how to recover safely.
- Keep essential functions usable on mobile, with keyboard navigation, visible focus and readable contrast.
- Distinguish essential capabilities from optional, advanced and research-stage capabilities.

## 2. Safe by default

- Default to read-only, advisory or simulation-only behavior.
- Never turn a model prediction into a physical command or consequential decision automatically.
- Require explicit human approval for any action with physical, financial, legal, privacy or safety consequences.
- Keep safety and control independent from model-generated recommendations; enforce permissions and operating limits outside the model.
- Validate inputs, units, timestamps, ranges, identity and evidence references at system boundaries.
- On missing, stale, contradictory, malformed or out-of-scope evidence, abstain or enter a safe hold; never silently guess.
- Use least privilege, protected secrets, minimal permissions and documented recovery procedures.
- Provide a clear stop, disable or rollback path wherever an action could have an effect.
- Keep people, animals and bystanders in the safety analysis for robotics and mobility concepts.
- Do not allow autonomous accusation, detention, enforcement or other consequential decisions based solely on AI output.

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

- Every score, percentage, graph, cost estimate and readiness claim must link to a dated method, assumptions and evidence where available.
- Distinguish documentation progress, test coverage, simulation results, prototype status, product readiness and real-world validation.
- Record known limitations, uncertainty, data provenance and unresolved failures.
- Label estimates as preliminary when they are not supported by supplier quotations or a verified bill of materials. State scope, exclusions, currency and estimate date.
- Never imply certification, field performance, autonomy, waterproofing, fire resistance, detection accuracy or commercial readiness without appropriate evidence.
- A concept image, SVG, simulation or software mock-up is not evidence that a physical product exists or works.

## 4. Professional software and repository practice

- Keep dependencies minimal, pinned where practical, licence-checked and justified.
- Prefer standard-library and existing repository capabilities when adequate.
- Prefer open-source tools, models and datasets with clear licences and verifiable provenance. Avoid resources of unclear origin; record manufacturer/developer and country of origin when relevant to sourcing decisions.
- Do not add paid APIs, subscriptions, cloud compute, external services or metered resources without explicit approval.
- Do not download, install, purchase or connect new external resources without the required approval.
- Require automated tests and security checks for relevant changes; investigate failures rather than suppressing them.
- Use small, reviewable pull requests with purpose, scope, risk, tests and rollback notes.
- Protect default branches. Do not write directly to protected default branches, merge, deploy or change repository security settings without explicit authorization.
- Never commit credentials, personal data or unlicensed datasets.
- Do not automatically delete, overwrite or bulk-modify important project assets or records; preserve version history and a recovery path.

## 5. Visual assets, diagrams and SVG

- Use SVG as the preferred format for logos, icons, diagrams, architecture drawings, interface illustrations and product concept artwork when vector graphics are suitable.
- Keep SVG source editable, readable, responsive and version-controlled in the relevant repository. Use descriptive filenames and meaningful `title` and `desc` elements where appropriate.
- Do not embed scripts, event handlers, hidden tracking, unnecessary external resources or unsafe active content in SVG files.
- Provide meaningful alternative text for informative images; mark purely decorative graphics appropriately in the page markup.
- Maintain consistent PUI89 visual identity and clear English/Thai descriptions. Avoid clutter, misleading labels and decorative effects that reduce readability.
- Keep product identities distinct. In particular, Sentinel is a four-legged quadruped concept; NOMAD is a separate four-wheel mobile assistant. Do not reuse one product's illustration to represent the other.
- Use raster imagery only when it materially serves the purpose (for example, a clearly labelled photorealistic concept render or genuine evidence photograph). Do not replace editable technical diagrams with raster images.
- Label concept art, renders and illustrative visuals as concepts. Never present them as photographs of a built, tested or validated product.

## 6. Robotics, devices and physical product concepts

- Keep physical actuation disabled in software tests and examples unless a separately approved, controlled test plan exists.
- Define operating envelope, hazards, emergency stop, safe state, maintenance and failure behavior before any physical trial.
- Define safe behavior for loss of power, communications, localisation, sensor validity and operator connection.
- Treat water resistance, fire resistance, battery safety, structural strength, terrain capability and environmental tolerance as unverified until tested to a suitable method.
- Do not represent a concept drawing, simulation or software mock-up as a built or certified product.
- Separate simulation, bench testing, controlled prototype testing and real-world deployment; report the environment and limitations for each.
- Human operators retain control of consequential physical actions. For road vehicles, driver steering, throttle and braking remain human-controlled unless a separately approved safety case authorizes otherwise.

## 7. Privacy and responsible data

- Collect only data necessary for a stated purpose; avoid unnecessary retention and exposure.
- Document data source, licence, consent or lawful basis where applicable, access and retention.
- Treat sensitive or uncertain detections as review prompts, not proof.
- Do not infer identity, emotion, mental state or sensitive traits from voice or other signals without a clearly lawful, necessary and separately reviewed basis.
- Provide human review and an appeal or correction path for consequential outputs.
- Use synthetic or properly licensed data for development where practical; do not imply synthetic data is equivalent to real-world validation.

## 8. Release checklist

A change is ready for review only when applicable items are satisfied:

- [ ] Purpose, user impact and scope are clear.
- [ ] Safe default, permissions and failure behavior are documented.
- [ ] Inputs, evidence and data provenance are checked.
- [ ] Tests and security checks have been run; results are linked.
- [ ] Limitations, assumptions, costs and unverified claims are explicit.
- [ ] Privacy, licence, origin and dependency impacts are checked.
- [ ] SVG and other visual assets are safe, accessible, correctly labelled and version-controlled where applicable.
- [ ] English and Thai user-facing content is consistent where applicable.
- [ ] Rollback, version history or recovery steps are available.
- [ ] A human reviewer can understand the change without hidden context.

A failed or unrun check must be labelled clearly; it is not a pass.

## 9. Continuous improvement

Review this standard monthly and after any security incident, safety-relevant failure, major architecture change or new physical capability. Record the review date, evidence examined, decisions, owner and open actions. Do not inflate maturity scores merely because documentation, diagrams or SVG assets have been added.

---

**PUI89 engineering principle:** Simple to use. Strict about safety. Honest about evidence. Consistent in quality.
