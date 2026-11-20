# PUI89 Product Readiness and Release Gates

This policy applies to every current and future PUI89 project.

## Gate 0 — Concept
Required: problem statement, intended users, use context, assumptions, known unknowns, initial hazard and privacy review.

Allowed public claim: concept or proposed design.

## Gate 1 — Feasibility prototype
Required: bounded scope, lawful sample data, reproducible setup, documented dependencies/licences, basic tests, limitations and failure cases.

Allowed public claim: prototype or proof of concept, with exact scope.

## Gate 2 — Verified software
Required:
- Automated tests and recorded results.
- Reproducible evaluation against a baseline.
- Data provenance and permission records.
- Robustness tests for missing, noisy, stale and conflicting inputs.
- Security review, dependency review and secret scanning.
- Human oversight and safe failure behavior where decisions affect people or property.
- Versioned release notes and rollback procedure.

Allowed public claim: tested in the stated conditions only.

## Gate 3 — Controlled pilot
Required: written pilot scope, named responsible operator, user consent and data terms, risk assessment, incident process, support plan, success criteria and exit criteria. Independent review where risk warrants it.

Allowed public claim: pilot conducted, with scope, dates and limitations.

## Gate 4 — External validation
Required: independent test protocol, representative operating conditions, statistically appropriate evaluation, unresolved-risk disclosure, legal and regulatory review, and evidence retained for audit.

Allowed public claim: externally validated only for the tested claims and conditions.

## Gate 5 — Commercial release
Required: product ownership and licence clearance, customer contract and support model, security/privacy controls, documented deployment and maintenance, warranty/liability review, monitoring and incident response, and applicable regulatory approvals.

Allowed public claim: commercially released only for the approved product scope.

## Physical robotics and mobility hard gate

No physical robot, vehicle, rescue craft, or actuator may be controlled by an experimental AI agent. Simulation and proposal-only interfaces remain the default.

Before any physical test, require:
- Independent safety controller and emergency stop.
- Hazard analysis and safe-state definition.
- Mechanical/electrical design review by qualified personnel.
- Verified braking, stability, power isolation and environmental limits as relevant.
- Geofenced, supervised test area and trained operator.
- Test plan, stop criteria, incident logging and insurance/legal review.
- Separate validation for water ingress, fire behavior, load capacity, weather resistance, battery safety and durability claims.

A render, CAD model, simulation, or software test is not evidence of physical safety.

## High-impact decision systems

For screening, rescue, health-adjacent, home safety and mobility applications:
- AI output is advisory unless a lawful, validated system explicitly establishes otherwise.
- Human review must be meaningful and documented.
- Uncertainty and abstention must be visible.
- No enforcement, diagnosis, emergency dispatch or safety-critical action based solely on an unvalidated model.
- Test false positives, false negatives, subgroup performance where lawful and appropriate, distribution shift, sensor failure and adversarial conditions.

## Release evidence record

Every release must record:
- Product and version.
- Intended use and prohibited use.
- Commit and build identifiers.
- Test environment and dataset provenance.
- Metrics, baseline, sample size and known limitations.
- Open defects and risk acceptance owner.
- Licence and security review status.
- Approver and release date.
