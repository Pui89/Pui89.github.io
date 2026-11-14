# PUI89 Innovation Selection Framework
## Build what the world has not recognised yet — then prove it

**Status:** Strategy and evaluation framework  
**Scope:** Shared AI Core and the seven PUI89 product lines  
**Planning horizon:** 1–5 years  
**Evidence rule:** A promising idea is a hypothesis, not a demonstrated capability.

## 1. Strategic principle

PUI89 will not adopt a technology merely because it is fashionable, widely discussed, or technically impressive. We will look for important problems that are underserved, form a differentiated solution hypothesis, and validate it through small, measurable experiments before committing significant time or resources.

The lesson from products such as the original Samsung Galaxy Note is not simply “ignore critics.” It is that a new form factor can succeed when it solves a real user problem with a coherent experience. The lesson from product failures is equally important: novelty never excuses rushed engineering, inadequate testing, or unsupported safety claims.

**PUI89 rule:** Be early in insight, disciplined in execution, and conservative in claims.

## 2. The seven decision gates

Every candidate technology or product feature must pass these gates in order.

| Gate | Question | Required evidence | Decision |
|---|---|---|---|
| 1. Problem | Is there a real, recurring, consequential user problem? | User/problem statement, operating context, affected users | Reject if the problem is vague or invented |
| 2. Differentiation | Does the idea improve the outcome in a meaningful way? | Comparison with current alternatives and a clear advantage hypothesis | Do not build a feature with no meaningful advantage |
| 3. Feasibility | Can PUI89 investigate it with available skills, open-source tools, and realistic compute? | Architecture sketch, dependency/licence review, resource estimate | Defer if it requires unaffordable infrastructure or unavailable expertise |
| 4. Safety and trust | Can risks, misuse, privacy, failure modes, and human authority be controlled? | Hazard list, data boundaries, fallback and human-review plan | Block unsafe or ungovernable designs |
| 5. Evidence | Can the core claim be tested objectively? | Baseline, metric, test dataset/scenario, acceptance threshold | No performance claim without measurement |
| 6. Product fit | Does it strengthen a named PUI89 product or the Shared AI Core? | Reuse path, owner, scope, and maintenance cost | Avoid disconnected side projects |
| 7. Release readiness | Can it be documented, reproduced, supported, and maintained? | Tests, provenance, limitations, versioning, recovery plan | Do not call it production-ready prematurely |

A candidate must not skip a gate because it is exciting or because a competitor has launched something similar.

## 3. Lightweight scoring

Score each dimension from 0 to 5. Use **Unknown** when evidence is missing; do not silently score unknown as a pass.

- Problem importance — 25%
- User benefit and differentiation — 20%
- Technical feasibility with available resources — 15%
- Safety, privacy, and trust — 15%
- Evidence and testability — 15%
- Reuse across PUI89 products — 10%

Weighted score = sum of (dimension score ÷ 5 × weight).

Interpretation:
- **80–100:** Candidate for a small, gated validation experiment; not automatic approval to build.
- **60–79:** Keep under observation or run a narrowly scoped discovery test.
- **Below 60:** Do not prioritise now.
- **Any unresolved critical safety, legal, privacy, provenance, or affordability issue:** Block regardless of score.

Record the assessor, date, evidence links, assumptions, unknowns, and next review date. Scores support judgement; they do not replace it.

## 4. Technology adoption states

Use these states in the PUI89 Technology Radar:

- **Explore:** A relevant signal exists; gather evidence and compare alternatives.
- **Validate:** A specific hypothesis and low-cost experiment are defined.
- **Adopt:** Evidence shows a repeatable benefit and the technology passes security, licence, resource, and maintenance review.
- **Hold:** Potential value exists, but a dependency, cost, maturity, or safety issue blocks adoption.
- **Reject:** The technology is unsuitable, untrustworthy, unsupported, or offers no meaningful advantage.

Every radar entry must identify its target project, evidence date, provenance, licence, compute needs, risks, and next decision. “Latest” is not itself a reason to adopt.

## 5. PUI89 application map

| PUI89 area | High-value problem to investigate | Evidence before claiming success |
|---|---|---|
| Shared AI Core | Reliable, resource-aware AI operation across heterogeneous CPU/GPU/NPU/MCU and sensor systems | Reproducible workload benchmarks, latency/memory/power measurements, fault and fallback tests |
| Coconut Harvest AI | Reliable coconut maturity assessment and safe harvesting workflow | Licensed real images, reviewed labels, held-out evaluation, class-wise precision/recall/F1; physical harvesting claims require separate trials |
| Extreme Flood Rescue AI | Better situational awareness for human-supervised flood response | Clearly bounded simulation tests, sensor assumptions, depth/route error measurements, field validation before operational claims |
| PUI89 Sentinel | Multimodal inspection support with uncertainty and human review | Authorised representative data, modality-specific evaluation, false-positive/false-negative analysis, privacy and human-review controls |
| AI HOME | Useful indoor awareness and assistance without unsafe autonomous actions | Defined home scenarios, obstacle/safety tests, privacy boundaries, supervised prototype validation |
| AI NOMAD | Reliable outdoor mobile assistance in a compact form | Terrain, weather, stability, obstacle and stop/fallback tests in a declared operating envelope |
| AI Global SUV | Driver-support intelligence across powertrain options without taking control away from the driver | Scenario-based perception and warning tests, degraded-sensor behaviour, cybersecurity and automotive safety review |
| EasyRide AI Motorcycle | Rider-centred road awareness and hazard warnings | Motorcycle-specific visibility, vibration, weather, latency and false-alert tests; no autonomous throttle, steering, or braking |

These are research directions and validation requirements, not claims that the listed capabilities are already implemented or validated.

## 6. One-to-five-year execution discipline

### Year 1 — Establish proof
- Keep the portfolio focused; do not create extra product lines for every trend.
- Strengthen Shared AI Core contracts, provenance, uncertainty, abstention, safe hold, and failure reporting.
- Prioritise real, licensed evidence for Coconut Harvest AI and one carefully bounded end-to-end workflow.
- Establish CPU-first baselines and reproducible tests before considering accelerator-specific optimisation.
- Publish a concise Technology Radar with evidence dates and explicit Explore/Validate/Adopt/Hold/Reject states.

### Years 2–3 — Demonstrate repeatability
- Reuse proven Shared AI Core components in more than one project.
- Compare against clear baselines using repeatable datasets and scenarios.
- Validate selected simulations against controlled physical tests where safe and feasible.
- Retire features that fail user-value, reliability, cost, or safety gates.

### Years 4–5 — Earn product readiness
- Concentrate investment on the few products with the strongest verified user need and evidence.
- Build integration, maintainability, documentation, support, and procurement evidence.
- Seek external partners or funding only around specific validated capabilities and transparent remaining gaps.
- Make commercial, safety, and performance claims only within independently supportable limits.

This is a decision horizon, not a promise that every project will reach a particular maturity stage by a particular year.

## 7. Low-cost experiment card

Before starting an experiment, write down:

1. **Hypothesis:** What measurable user outcome should improve?
2. **Baseline:** What happens without the proposed technology?
3. **Smallest test:** What is the cheapest experiment that could disprove the idea?
4. **Data and provenance:** Are the data authorised, licensed, representative, and documented?
5. **Metric and threshold:** What result would count as a pass or fail?
6. **Failure behaviour:** What happens with missing, stale, uncertain, or conflicting inputs?
7. **Resource ceiling:** Can the experiment run with approved open-source tools and available local compute, without paid APIs, subscriptions, or metered cloud/GPU services?
8. **Decision:** Adopt for the next stage, revise, hold, or reject — with evidence and date.

Do not download models, datasets, or tools, install dependencies, incur charges, or change production systems without the required approval.

## 8. Non-negotiable rules

- No hype-driven roadmap changes.
- No fabricated metrics, customer demand, partnerships, prototypes, or deployment claims.
- No unverified claims of autonomy, safety, all-weather operation, flood tolerance, fire resistance, or commercial readiness.
- No technology adoption without provenance, licence, security, privacy, resource, and maintenance review.
- No destructive or irreversible changes without explicit approval and a recovery path.
- Human authority remains explicit for consequential decisions and physical actions.
- Preserve negative results and failed experiments; they are useful engineering evidence.

## 9. Review record

For each review, record: date, reviewer, candidate, target project, gate results, score with unknowns, evidence links, risks, decision, owner, and next review date.

An empty review log means no completed review has been evidenced. Do not report a review as completed merely because this framework exists.

---

**North star:** PUI89 should not try to predict every winning technology. It should become exceptionally good at finding important problems, testing unconventional solutions cheaply, and turning only proven advantages into dependable products.
