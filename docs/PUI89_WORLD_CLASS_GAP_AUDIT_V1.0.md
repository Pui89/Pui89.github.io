# PUI89 World-Class Engineering Gap Audit v1.0

**Review date:** 15 November 2026  
**Scope:** Seven product READMEs and seven English product pages; the World-Class Engineering Standard v1.0 reference integration  
**Review type:** Documentation and repository-evidence review only  
**Status:** Initial baseline — corrective actions proposed, not yet approved or implemented

## 1. Executive summary

The World-Class Engineering Standard v1.0 has been merged into the portfolio website repository, and all seven product README reference changes have been merged. The seven English product pages reviewed also contain a link to the standard. This confirms documentation linkage, not implementation or compliance with every engineering gate.

The most important findings are two conflicting physical-mass specifications between product READMEs and website pages:
- AI HOME: README states 8 kg target / 10 kg maximum complete robot mass; website states 5 kg preferred, 4–6 kg design range and 6 kg hard ceiling.
- AI NOMAD: README states 8–10 kg target / 10 kg maximum; website states a 6 kg product target and 6 kg maximum.

These conflicts must be resolved before BOM freeze, supplier selection, mechanical sizing or public promotion. This audit uses the latest portfolio decisions as the intended baseline: HOME 8 kg target / 10 kg maximum; NOMAD 8–10 kg target / 10 kg maximum. Both remain design targets, not measured results.


## 2. Scope and method

Reviewed:
- Seven default-branch product READMEs.
- Six English product pages: coconut.html, sentinel.html, home.html, nomad.html, ai-global-suv.html and ai-robot-motorcycle.html.
- Presence of the World-Class Engineering Standard v1.0 reference in those files.
- Product identity, development-stage wording, selected design targets, safety boundaries, evidence statements and cost/BOM language visible in repository documentation.

Not performed:
- No independent source-code test execution, hardware inspection, supplier quotation, model benchmark, dataset-rights audit, field test, certification assessment or independent safety assessment.
- No Thai-page line-by-line semantic audit in this first pass.
- No claim that any product has passed a World-Class Engineering Gate.

## 3. Priority findings

### P0 — Resolve conflicting product specifications

| Product | README specification | Website specification | Required correction |
|---|---|---|---|
| AI HOME | 8 kg target; 10 kg maximum complete robot mass | 5 kg preferred; 4–6 kg design range; 6 kg hard ceiling | Align EN and TH pages to 8 kg target / 10 kg maximum, or formally approve a new product-wide specification before changing either source |
| AI NOMAD | 8–10 kg target; 10 kg maximum complete robot mass | 6 kg product target; 6 kg maximum | Align EN and TH pages to 8–10 kg target / 10 kg maximum, or formally approve a new product-wide specification |

**Why this is P0:** total mass drives chassis, motors, wheel loading, battery sizing, centre of gravity, payload, stability, braking, packaging and prototype cost. Conflicting targets make the BOM and design calculations unreliable.

**Control:** treat both values as design targets only. Do not claim achieved mass, payload or mobility until a weighed physical prototype and documented tests exist.

### P1 — Clarify legacy maturity labels for Coconut and Flood

The Coconut README's specific “Development stage” section says “Software & evaluation-preparation prototype” and states that no approved training dataset or validated field detector exists. Its later maturity snapshot says “Level 4 — Tested Prototype”, while also stating that detector accuracy and physical harvesting remain unvalidated.

The Flood README's specific “Development stage” section says “Software & synthetic-scenario evaluation”. Its later maturity snapshot says “Level 4 — Tested Prototype”, while explicitly stating that flood physics and physical rescue capability remain unvalidated.

**Required correction:** retain historical maturity values only if their definition is clearly documented as a software/project maturity scale. Add an explicit mapping to the World-Class gates:
- Software tests and synthetic scenarios may support G2 software/simulation evidence.
- They do not establish G3 bench-integrated hardware or G4 controlled physical prototype testing.
- Physical product maturity must be reported separately from software maturity.

Do not mechanically downgrade valid software progress; disambiguate the scale and evidence category.

### P1 — Standardise product evidence and release-gate reporting

All seven products link to the shared standard, but the product documents do not yet present one consistent, easy-to-compare evidence summary with:
- Requirement ID and acceptance criterion.
- Verification method and test ID.
- Environment, software/model/hardware version and date.
- Result, evidence link and reviewer.
- Open defect, risk, corrective action and retest.
- Current World-Class gate for software, simulation and physical product separately.

**Required correction:** add a compact product-specific gate/evidence table to every README and matching EN/TH website pages. Do not mark a gate passed solely because a document or code module exists.

### P1 — Keep physical product status distinct from software/AI status

Current documentation already includes useful limitations, but a portfolio-wide standardised status line is still needed. In particular:
- Coconut: software/evaluation preparation; real-image rights, labels, held-out detector metrics and harvesting hardware remain open.
- Flood: software and synthetic-scenario evaluation; credible flood physics, buoyancy, current resistance and physical rescue capability remain unvalidated; 15 m remains simulation/design scope only.
- Sentinel: physical robot remains concept/requirements definition; no physical prototype or all-terrain performance is claimed.
- HOME: early software foundation and requirements; no built robot or validated home-safety performance is established.
- NOMAD: early software foundation/design targets; no built robot or validated mobility/endurance/weather performance is established.
- SUV: early software/research foundation; no functioning vehicle, vehicle integration, road test or certification is established.
- Step-Through Scooter: concept and engineering foundation; no functioning motorcycle, rider trials, road certification or validated rider-safety performance is established.

**Required correction:** use separate status fields for software, simulation, hardware integration, physical prototype and field validation. Never compress them into one ambiguous “prototype” badge.

### P2 — Complete bilingual consistency review

The initial pass confirmed standard links on the English pages. The website PR also changed the seven Thai pages, but their technical wording has not been line-by-line compared in this audit.

**Required correction:** verify Thai/English parity for product identity, mass and payload targets, safety boundaries, maturity labels, costs, units, dates and validation statements. A translation must not silently change the engineering specification.

### P2 — Strengthen BOM evidence and cost traceability

The READMEs contain preliminary prototype cost estimates and hardware/materials sourcing sections. These remain planning estimates, not purchase quotations or proof that a complete BOM is supplier-verified.

**Required correction:** for each high-impact component, record exact manufacturer and part number, manufacturer model specification, manufacturing country/origin evidence, supplier and source, dated price/currency, stock/lead time, compatibility and verification status. Mark missing fields UNVERIFIED. Separate prototype estimate, shared-tool allocation, production estimate and Thai landed-cost assumptions. Do not make purchases or supplier commitments under this audit.

## 4. Product-by-product initial assessment

| Product | Documentation strengths observed | Highest-priority gap |
|---|---|---|
| Coconut Harvest AI | Four maturity classes, PTI, dataset/evaluation plan, safety limits, software stage and physical limits are described | Clarify legacy Level 4 maturity label; close dataset rights/annotation and real-image benchmark evidence |
| PUI89 Sentinel | Clear quadruped inspection identity, target operating contexts, mobility requirements, safety/human oversight and validation links | Add standardised requirement-to-test evidence table and staged hardware/simulation gate status |
| AI HOME | Indoor assistant identity, 8 kg / 10 kg mass targets, safety/privacy and software foundation are described in README | Website mass specification conflicts with README; align EN/TH pages before BOM work |
| AI NOMAD | Distinct four-wheel dog-inspired mobile assistant, handle and 8–10 kg / 10 kg mass target are described in README | Website mass specification conflicts with README; reconcile indoor/outdoor positioning and align EN/TH pages |
| AI Global SUV | Driver-first advisory direction, HEV-first study, flood/fire safety boundaries and software foundation are described | Add a compact traceable requirement/test matrix and explicit gate status |
| AI Step-Through Scooter | Rider-first design, inclusive requirements, human control and validation boundaries are described | Add a compact traceable requirement/test matrix and explicit gate status |

## 5. Recommended corrective sequence

1. **Specification control:** reconcile HOME and NOMAD mass targets across README, EN page, TH page, product specification and any BOM tables.
2. **Maturity semantics:** document the legacy maturity scale and map each product's software, simulation and physical state separately to G0–G5.
3. **Evidence matrix:** add a common requirements-to-test evidence table to all seven READMEs.
4. **Bilingual parity:** verify all 14 product pages against the approved product specification.
5. **BOM traceability:** identify the highest-risk/high-cost components and mark each supplier/origin/price field verified or UNVERIFIED.
6. **Release review:** only after evidence exists, assess each gate; keep unresolved risks visible.

## 6. Proposed acceptance criteria for closing this audit

- [ ] AI HOME mass target is identical in README and both website languages.
- [ ] AI NOMAD mass target is identical in README and both website languages.
- [ ] Legacy maturity labels for Coconut and Flood have an explicit scale definition and G0–G5 mapping.
- [ ] All seven READMEs contain a consistent software/simulation/hardware/field status summary.
- [ ] All seven READMEs contain requirement-to-test traceability fields, with missing evidence marked NOT RUN or UNVERIFIED.
- [ ] All 14 website pages match the approved product specification in both languages.
- [ ] Cost and BOM figures clearly distinguish estimates, listings, quotes and verified purchase records.
- [ ] No unsupported physical, safety, certification or commercial claims are introduced.

## 7. Governance note

This report is a documentation gap audit based on repository contents. It is not a product certification, engineering sign-off, safety case approval, supplier verification or physical validation report.

Corrective changes should be made in small, reviewable feature branches and pull requests. Do not merge or deploy without the user's approval. Do not purchase, install, download, contact suppliers or use paid services as part of this audit.
