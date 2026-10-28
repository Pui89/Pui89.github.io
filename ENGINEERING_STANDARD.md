# PUI89 AI Robotics — Engineering Standard

**Purpose:** Build useful AI and robotics products through measured performance, safe design, reproducible evidence, and cost discipline.

This is an internal/public engineering policy for independent projects. It is inspired by systems-engineering and software-assurance practices; it is **not** a claim of NASA certification, regulatory approval, or compliance with any external standard.

## 1. Non-negotiable principles

1. **Evidence before claims.** Describe only capabilities supported by code, tests, retained experiment outputs, or documented demonstrations.
2. **Separate status clearly.** Label features as implemented, tested in simulation, evaluated offline, validated in the field, or planned.
3. **Fail safely.** Missing, stale, contradictory, low-quality, or out-of-distribution evidence must not be converted into a confident actionable result.
4. **Human oversight for high-consequence decisions.** AI recommendations do not replace qualified operators, legal requirements, or independent hardware safety controls.
5. **Reproducibility.** Record the source commit, configuration, dependencies, data provenance, sample counts, metrics, and failure cases for every published benchmark.
6. **Cost discipline.** Prefer local-first, free and open-source tools. Do not introduce paid APIs, cloud compute, subscriptions, or billing-triggering workflows without explicit approval.
7. **Respect rights and privacy.** Check data, image, model, dependency, and asset licences before use or redistribution. Minimise sensitive data collection.
8. **Security by default.** Avoid secrets in source control, pin important dependencies where practical, review permissions, and test error handling.
9. **No misleading demonstrations.** Label synthetic data, conceptual drawings, simulated results, and manually entered examples so they cannot be mistaken for real-world validation.
10. **Learn from failures.** Preserve meaningful failures and regression tests rather than hiding poor results.

## 2. Evidence maturity levels

Use the highest level actually supported by evidence; do not skip levels in public claims.

| Level | Meaning | Minimum evidence |
|---|---|---|
| E0 — Concept | Idea, architecture, or illustration | Explicitly labelled concept and known assumptions |
| E1 — Implemented | Code exists and can be inspected | Reproducible setup and documented scope |
| E2 — Software-tested | Automated checks exercise the behaviour | Passing tests, including negative and failure cases |
| E3 — Offline-evaluated | Tested against a defined, fixed dataset | Dataset provenance, split policy, metrics, counts, and retained outputs |
| E4 — Simulation-tested | Tested in a specified simulator/scenario set | Versioned configuration, repeatable scenarios, failures, and safety-stop results |
| E5 — Field-validated | Evaluated in representative real-world conditions | Approved protocol, sufficient trials, measured outcomes, limitations, and independent review where appropriate |
| E6 — Product-ready | Suitable for a defined customer deployment | User needs, reliability evidence, security/privacy review, support/maintenance plan, legal and regulatory review, and acceptance criteria |

A higher level may apply to one feature but not to the entire project. State the scope of each claim.

## 3. Required project release gate

Before calling a release stable or production-ready, review:

- [ ] Scope and limitations are accurate in the README.
- [ ] Installation and reproduction instructions have been followed from a clean environment.
- [ ] Automated tests pass; important failure modes have regression tests.
- [ ] Security and dependency checks have been reviewed.
- [ ] Data/model/asset licences and attribution are documented.
- [ ] Benchmarks use stated metrics, sample counts, and retained outputs.
- [ ] Safety hazards and mitigations are documented for any consequential action.
- [ ] No secrets, personal data, paid services, or unapproved costs are introduced.
- [ ] Known issues and rollback/recovery steps are recorded.
- [ ] A reviewer can distinguish implemented, simulated, measured, and planned capabilities.

## 4. Project-specific safeguards

### Coconut Harvest AI
- Treat detection, maturity classification, 3D localization, reachability, cutting, fruit retention/lowering, and harvest success as separate capabilities.
- Keep the software prototype disconnected from physical actuator commands unless a separately reviewed safety architecture is implemented.
- Use held-out, rights-cleared images and group-aware splits; publish failures as well as aggregate scores.
- Do not claim 0–30 m reach or successful autonomous harvesting without representative, supervised field evidence.

### Flood Rescue AI
- Keep early development simulation-first.
- Test sensor loss, communication loss, water/current uncertainty, blocked routes, localization drift, human uncertainty, low battery, and emergency-stop behaviour.
- Treat maps and route suggestions as decision support; do not claim operational rescue readiness from simulation alone.

### Multimodal Narcotics Screening AI
- Treat output as screening decision support, not proof of substance identity or criminal activity.
- Missing, invalid, conflicting, or uncertain evidence should trigger abstention or human review.
- Record sensor provenance, limitations, uncertainty, and operator review; evaluate false positives and false negatives before any operational use.

## 5. Continuous improvement loop

1. Choose one specific user or engineering problem.
2. Define an acceptance test before implementing the change.
3. Make the smallest reviewable change.
4. Run automated tests and relevant static/security checks.
5. Retain reproducible results and inspect failures.
6. Update documentation to match the verified state.
7. Review cost, licensing, privacy, and safety impact.
8. Merge only when evidence supports the change; revisit unresolved risks.

## 6. Company-building milestones

- **Foundation:** reliable repositories, reproducible local setup, clean licensing, trustworthy documentation, and passing tests.
- **Evidence:** fixed evaluation datasets or scenarios, measured baselines, error analysis, and clear limitations.
- **User validation:** interviews or structured feedback from intended users; documented problem, workflow, and acceptance criteria.
- **Prototype validation:** controlled demonstrations with safety boundaries and recorded outcomes.
- **Product readiness:** maintainability, security/privacy, deployment support, service plan, cost model, and applicable legal/regulatory review.
- **Commercial readiness:** only after technical and user evidence, define a narrow first customer segment, value proposition, pricing assumptions, and support obligations.

Funding, company registration, or impressive visuals are not substitutes for these gates.

## 7. Reporting rule

Every progress update should separate:

- **Completed:** changes merged or experiments actually run.
- **Verified:** tests, checks, or results with links/logs.
- **Blocked:** the exact missing dependency, data, permission, or decision.
- **Next:** one or more measurable actions.
- **Cost/risk:** expected cost (including “none known” only when checked), data/licence issues, and safety implications.

Do not describe a planned, queued, or unverified task as completed.
