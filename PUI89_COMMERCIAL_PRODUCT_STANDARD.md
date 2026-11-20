# PUI89 Commercial Product & Company-Readiness Standard

**Portfolio rule:** mandatory for this and every future PUI89 project. Goal: lawful commercial use and an evidence-backed path from research to high-quality products and a future PUI89 company.

## Project-specific gates
PUI89 company/product portfolio website. Commercial gates: accurate status claims, ownership and asset notices, privacy/accessibility review, working support routes and clear separation of concepts from products available for sale.

## Commercial rights and intellectual property
- The root LICENSE governs original materials the owner is entitled to license. MIT and Apache-2.0 permit commercial use, modification and redistribution subject to their conditions.
- Existing licences are preserved; this standard does not retroactively relicense earlier releases.
- Third-party code, models, datasets, images, CAD, fonts and other assets are not automatically covered. Record source, version, owner, exact licence, attribution, restrictions and commercial-use permission before inclusion or sale.
- Exclude assets with unclear, research-only, non-commercial, no-redistribution or incompatible terms.
- PUI89 names, logos and trademarks are not granted by the software licence. Keep brand permissions separate.
- Maintain copyright provenance, contributor permissions, third-party notices and an SBOM for distributable software.

## First-class product quality
Define customers, intended use and exclusions; measurable requirements and acceptance criteria; architecture and interfaces; reproducible builds and tests; traceability; secure defaults and vulnerability handling; privacy/data governance; user, installation, maintenance and troubleshooting documentation; support, incident, rollback and end-of-life plans.

## Safety, security and regulatory gates
Complete hazard and risk assessments, safe-state design, human override and misuse analysis before field/customer use. For AI, document data provenance, label quality, leakage-safe splits, calibration, uncertainty, error rates, limitations and human-review rules. For hardware, define and test mechanical, electrical, thermal, battery, fire, ingress, EMC/radio and environmental requirements as applicable. Identify applicable laws, standards and approvals for each target market with qualified assessors. Simulation/software tests do not establish physical safety or field performance.

## Commercial stage gates
| Gate | Evidence | Status |
|---|---|---|
| G0 Concept | Customer problem, intended use, exclusions, risks | Concept |
| G1 Requirements | Requirements, architecture, hazards, IP/data/licence review | Specified |
| G2 Prototype | Working software/prototype and reproducible tests | Prototype |
| G3 Verification | Tests, benchmarks, security review, failure analysis | Verified within scope |
| G4 Validation | Representative user/environment trials and independent review where needed | Validated within scope |
| G5 Compliance | Required legal, safety, privacy and market approvals | Approved only with evidence |
| G6 Pilot | Qualified supply, support, warranty and service processes | Pilot |
| G7 Commercial release | Sign-off, unit economics, quality controls, documentation and post-market support | Sale-ready only after required gates |

## Startup readiness
Maintain a product catalogue; IP/contributor register; third-party licence inventory; customer discovery and pilot records; bill-of-materials and unit-economics model; supplier qualification; manufacturing, repair, warranty and support plans; and clear separation of open-source code, future proprietary components, services and brand assets. Existing open-source grants cannot simply be withdrawn.

## Strict zero-cost rule
Prefer free/open-source and offline/local tools. No paid APIs, subscriptions, cloud GPUs, paid datasets, metered services, automatic paid upgrades or unexpected billing. Check licence, provenance, security, resource fit and cost before adding dependencies/models/data/services. If certification, lab testing, legal review or manufacturing requires funding, record it as a future funding/partner gate; do not incur charges without explicit approval.

## Required records
Create and maintain as the project matures: docs/PRODUCT_REQUIREMENTS.md, docs/HAZARD_AND_RISK_REGISTER.md, docs/VERIFICATION_AND_VALIDATION_PLAN.md, docs/THIRD_PARTY_NOTICES.md and docs/COMMERCIAL_READINESS.md. Their mention does not mean they exist or have passed review.

## Truthful claims
Use explicit labels: PROPOSED, IMPLEMENTED, TESTED, SIMULATION-ONLY, BENCH-TESTED, FIELD-TESTED, INDEPENDENTLY-VALIDATED, CERTIFIED/APPROVED. Never market a concept as finished or claim a gate passed without traceable evidence.

**PUI89 standard:** high ambition, clear commercial rights, disciplined engineering, safety-first design, evidence before claims, and zero-cost development until funding is explicitly approved.
