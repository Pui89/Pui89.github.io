# PUI89 — Authoritative Portfolio Source of Truth v1.2

**Version:** 1.2  
**Review baseline:** 21 November 2026  
**Founder-confirmed Sentinel identity:** 21 November 2026 — quadruped All-Terrain Exploration & Inspection Robot.  
**Active portfolio:** exactly six products. **PUI89 Shared AI Core is shared infrastructure, not a product.**

## The six active products

| # | Official product name | Repository | Website (EN / TH) |
|---:|---|---|---|
| 1 | Coconut Harvest AI | [Pui89/Coconut-Harvest-AI](https://github.com/Pui89/Coconut-Harvest-AI) | [EN](https://pui89.github.io/coconut.html) · [TH](https://pui89.github.io/coconut-th.html) |
| 2 | PUI89 Sentinel — All-Terrain Exploration & Inspection Robot | [Pui89/PUI89-All-Terrain-Inspection-Robot](https://github.com/Pui89/PUI89-All-Terrain-Inspection-Robot) | [EN](https://pui89.github.io/sentinel.html) · [TH](https://pui89.github.io/sentinel-th.html) |
| 3 | PUI89 AI HOME | [Pui89/AI-Home-Safety-Robot](https://github.com/Pui89/AI-Home-Safety-Robot) | [EN](https://pui89.github.io/home.html) · [TH](https://pui89.github.io/home-th.html) |
| 4 | PUI89 AI NOMAD | [Pui89/AI-Mobile-Assistant-Robot](https://github.com/Pui89/AI-Mobile-Assistant-Robot) | [EN](https://pui89.github.io/nomad.html) · [TH](https://pui89.github.io/nomad-th.html) |
| 5 | PUI89 AI Global SUV | [Pui89/PUI89-AI-Global-SUV](https://github.com/Pui89/PUI89-AI-Global-SUV) | [EN](https://pui89.github.io/ai-global-suv.html) · [TH](https://pui89.github.io/ai-global-suv-th.html) |
| 6 | PUI89 AI Step-Through Scooter | [Pui89/AI-Step-Through-Scooter](https://github.com/Pui89/AI-Step-Through-Scooter) | [EN](https://pui89.github.io/ai-robot-motorcycle.html) · [TH](https://pui89.github.io/ai-robot-motorcycle-th.html) |

## Independent vehicle-project boundary

**PUI89 AI Global SUV and PUI89 AI Step-Through Scooter are two separate products and two independent development projects.** They have different vehicle classes, users, engineering requirements, product repositories, validation plans and maturity records. The SUV is a medium-size, five-door passenger vehicle concept; the Scooter is a rider-first, two-wheel step-through scooter concept. They are not variants, trims or subprojects of one another. Shared AI Core and selected platform-level intelligence interfaces do not merge their product identities or engineering work.

## Product boundaries and founder-approved requirements

- **Coconut Harvest AI:** software-first, four maturity classes (young green, mature green, yellow, brown). Establish image rights and provenance, human-reviewed labels, leakage-safe train/validation/test splits, then CPU evaluation. Report per-class precision, recall and F1, sample counts, confusion matrix and failure cases only after a valid held-out evaluation.
- **Sentinel:** four-legged (quadruped) All-Terrain Exploration & Inspection Robot. This identity was explicitly confirmed by the founder on 21 November 2026. Define and approve the first supervised inspection mission, environment, operating envelope and hazards before selecting hardware. Narcotics screening, X-ray screening payloads and chemical-identification functions are excluded from the official Sentinel product scope; any historical screening-related artifacts are legacy material only and must not be presented as Sentinel capabilities.
- **AI HOME:** complete robot mass target **8 kg**, maximum **10 kg**, including battery and all installed hardware. These are design requirements, not measured prototype mass.
- **AI NOMAD:** compact, dog-inspired four-wheel outdoor/mobile assistant with a retractable handle for manual handling and repositioning. It is not a quadruped; it has four wheels, not articulated legs. Its mission is practical assistance and supervised mobility in suitable environments—not security patrol or luggage transport. Physical mobility and outdoor performance remain unvalidated.
- **AI Global SUV:** human-driver vehicle concept with advisory AI; no autonomous steering, throttle or braking claim.
- **AI Step-Through Scooter:** rider-first two-wheel step-through scooter concept. Include advisory road-water and flood-risk warnings; unknown water condition means do not enter. No autonomous steering, throttle or braking.

## Cross-product flood and road-water awareness

Flood and road-water awareness may be developed as advisory capabilities within the AI Global SUV and AI Step-Through Scooter. These are product-specific safety requirements, not a separate product or a claim of validated flood-driving capability. Unknown or insufficient water and road evidence must be reported as unknown; the rider or driver retains control.

## Evidence-based maturity vocabulary

Do not use unsupported commercial-readiness percentages. Use these labels and cite the evidence for each claim: Proposed, Specified, Implemented, Simulated, Software-tested, Bench-tested, Field-tested, Validated, Certified, Unknown.

A later label does not automatically follow from an earlier one. Simulation is not field testing; software tests do not prove physical safety; certification requires the applicable certificate and scope. Keep unknowns explicit.

## Coconut evidence release gates

1. Dataset manifest with source, provenance, collection date and intended use.
2. Licence record and evidence for reuse; commercial-use rights must be explicit before commercial claims or use.
3. Human annotation guide, reviewed labels and adjudication record.
4. Leakage-safe, independently held-out test split.
5. CPU benchmark with hardware/runtime, command, model/version, thresholds and repeatable method.
6. Precision, recall, F1 by class, confusion matrix, sample counts and representative false-positive/false-negative cases.
7. Limitations and out-of-distribution cases. No physical harvesting or robot capability claim follows from image-model metrics.

No dataset is assumed licensed, no new images are downloaded, and no model is trained or evaluated by this document.

## Governance

- Shared AI Core is infrastructure, not a seventh product.
- Keep product website pages and product READMEs bilingual in meaning, even where technical identifiers remain English.
- Repository links must point to the canonical repositories listed above.
- Use feature branches and separate reviewable pull requests. No default-branch writes, auto-merge or deployment is authorised by this source document.
- This document does not claim company registration, manufacturing, certification, customer deployment or physical validation.
