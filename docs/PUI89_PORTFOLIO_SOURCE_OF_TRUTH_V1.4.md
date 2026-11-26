# PUI89 Portfolio Source of Truth v1.5

**Effective review date:** 26 November 2026  
**Owner:** PUI89  
**Status:** Portfolio governance and documentation reference  
**Scope:** Official active product identity, repository mapping, shared infrastructure boundaries and evidence-language rules.

This document is the canonical reference for the current PUI89 product portfolio. It describes project scope and documented maturity; it does not claim company registration, commercial availability, a completed physical prototype, certification or validated field performance.

## 1. Official active portfolio

PUI89 has **six active products**. The Shared AI Core is common engineering infrastructure and is **not** a product.

| No. | Official product name | Repository | English page | Thai page | Documented evidence status (21 Nov 2026) |
|---:|---|---|---|---|---|
| 1 | Coconut Harvest AI | [Pui89/Coconut-Harvest-AI](https://github.com/Pui89/Coconut-Harvest-AI) | [coconut.html](https://pui89.github.io/coconut.html) | [coconut-th.html](https://pui89.github.io/coconut-th.html) | Implemented software/evaluation-preparation work; real-image detector accuracy and physical harvesting are not validated. |
| 2 | PUI89 Sentinel — Quadruped Environmental Inspection Robot | [Pui89/PUI89-All-Terrain-Inspection-Robot](https://github.com/Pui89/PUI89-All-Terrain-Inspection-Robot) | [sentinel.html](https://pui89.github.io/sentinel.html) | [sentinel-th.html](https://pui89.github.io/sentinel-th.html) | Specified — four-legged quadruped requirements; no physical prototype, integrated sensor suite or field validation. Narcotics/X-ray screening is excluded. |
| 3 | PUI89 AI HOME | [Pui89/AI-Home-Safety-Robot](https://github.com/Pui89/AI-Home-Safety-Robot) | [home.html](https://pui89.github.io/home.html) | [home-th.html](https://pui89.github.io/home-th.html) | Implemented early software foundations; no physical robot or validated home-safety performance. |
| 4 | PUI89 AI NOMAD | [Pui89/AI-Mobile-Assistant-Robot](https://github.com/Pui89/AI-Mobile-Assistant-Robot) | [nomad.html](https://pui89.github.io/nomad.html) | [nomad-th.html](https://pui89.github.io/nomad-th.html) | Implemented early software foundations; compact suitcase-style four-wheel mobile assistant with an integrated handle; physical mobility and handling performance are unvalidated. |
| 5 | PUI89 AI Global SUV | [Pui89/PUI89-AI-Global-SUV](https://github.com/Pui89/PUI89-AI-Global-SUV) | [ai-global-suv.html](https://pui89.github.io/ai-global-suv.html) | [ai-global-suv-th.html](https://pui89.github.io/ai-global-suv-th.html) | Implemented early software-only safety/contract foundation; no vehicle integration, road testing or certification. |
| 6 | PUI89 AI Step-Through Scooter | [Pui89/AI-Step-Through-Scooter](https://github.com/Pui89/AI-Step-Through-Scooter) | [ai-robot-motorcycle.html](https://pui89.github.io/ai-robot-motorcycle.html) | [ai-robot-motorcycle-th.html](https://pui89.github.io/ai-robot-motorcycle-th.html) | Specified rider-first two-wheel step-through requirements; no functioning scooter, rider trials or road certification. |

Repository and page names above are identifiers and links, not evidence that a physical product exists.

## 2. Product identity boundaries

### Coconut Harvest AI
Agricultural computer-vision and harvesting-assistance project focused on coconut maturity/perception workflows. Software evaluation and real-world agricultural performance must be reported separately. Do not claim validated detection accuracy, autonomous harvesting or field deployment without corresponding evidence.

### PUI89 Sentinel — Quadruped Environmental Inspection Robot
A human-supervised four-legged quadruped for authorised industrial, infrastructure, logistics and selected outdoor exploration/inspection. Candidate functions include terrain and obstacle perception, localisation/mapping, supervised inspection evidence capture, anomaly cues, and traceable multimodal observations. Mobility, gait, terrain traversal, sensor integration and field performance remain unvalidated until supported by separate evidence.

**Explicitly excluded legacy scope:** narcotics detection or screening; X-ray screening, payloads or datasets; associated narcotics datasets and forensic spectra; chemical identification and enforcement. These items must not be restored as Sentinel product capabilities.

### PUI89 AI HOME
Indoor four-wheel assistant concept. Its design and software scope must remain distinct from NOMAD. Physical mobility, payload, home-safety and sensor performance require separate validation.

### PUI89 AI NOMAD — Compact Four-Wheel Mobile Assistant
Compact suitcase-style AI mobile assistant with four wheels, an integrated pull handle and a functional internal storage compartment for approved belongings. It is distinct from AI HOME. NOMAD is a robot, not ordinary passenger luggage, and must not be carried in an aircraft passenger cabin or overhead bin because impact and baggage handling may damage its electronic and mechanical systems. Any air-cargo transport requires carrier approval and compliance with applicable battery and dangerous-goods rules. No physical prototype, storage capacity, mobility performance, environmental tolerance, payload or battery endurance is established; dimensions and physical specifications remain subject to engineering validation.

### PUI89 AI Global SUV
AI-enabled vehicle intelligence and safety-assistance project. Advisory perception and warning concepts must not be represented as autonomous driving, vehicle-control authority, road-tested performance or certified safety capability.

### PUI89 AI Step-Through Scooter
Rider-first two-wheel step-through scooter/motorcycle concept. AI assistance is advisory. No autonomous throttle, steering or braking capability is claimed. Water-depth tolerance, payload, roadworthiness and safety remain engineering targets until physically tested and independently evidenced.

## 3. Shared AI Core boundary

[PUI89 Shared AI Core](https://github.com/Pui89/PUI89-Shared-AI-Core) is reusable engineering infrastructure for the six products. It is not a standalone customer product in the six-product count.

Shared interfaces and engineering principles may include observation, world-state representation, bounded action proposals, failure reporting, provenance, timestamps, uncertainty, abstention, human review, safe-state handling, heterogeneous compute efficiency, edge inference and recovery. A shared capability is a design direction until implementation and product-specific evidence demonstrate it. Do not assume that every product implements every shared capability.

## 4. Retired and excluded scope

- **Extreme Flood Rescue AI** is retired and is not an active PUI89 product. Do not include it in active portfolio lists, product counts, current architecture diagrams, product roadmaps or active project navigation.
- General flood, road-water, weather and environmental awareness may remain as advisory requirements within relevant active products, particularly mobility products, when clearly scoped and supported by evidence. This does not create a separate rescue product or establish flood-driving capability.
- **PUI89 Sentinel is active** as the All-Terrain Inspection Robot Dog: a human-supervised four-legged quadruped for authorised industrial, infrastructure, logistics and selected outdoor inspection. Its former narcotics-screening scope is excluded: do not restore narcotics detection/screening, X-ray screening or datasets, associated forensic spectra, chemical identification or enforcement. Preserve historical screening artifacts only as legacy records; do not represent them as current Sentinel capabilities.
- Do not rewrite historical Git commits or imply that historical repository records have been erased.

## 5. Evidence and maturity language

Use the narrowest accurate status, with date, configuration, evidence source, limitations and next gate where applicable:

- **Proposed:** a suggested direction, not yet specified.
- **Specified:** requirements or design are documented; implementation is not implied.
- **Implemented:** the stated software or documentation artifact exists; physical implementation is not implied.
- **Simulated:** results come from a simulation and must remain labelled as simulated.
- **Software-tested:** identified software tests passed in the stated environment; physical performance is not implied.
- **Bench-tested:** a defined physical component or assembly passed a documented bench test.
- **Field-tested:** a defined configuration was tested in a documented real-world setting.
- **Validated:** stated requirements were verified against an appropriate, documented validation protocol.
- **Certified:** a named, applicable certification was issued by an authorised body.
- **Unknown / Not assessed:** evidence is absent or has not been reviewed.

Rules:
1. Do not infer physical readiness from software implementation, simulation or documentation.
2. Keep synthetic, simulation, software, bench, physical and field evidence separate.
3. Do not claim accuracy, safety, reliability, autonomy, certification, manufacturing readiness, procurement readiness or commercial availability without appropriate evidence.
4. Do not publish commercial-readiness percentages unless a dated, approved evidence register explicitly authorises the methodology and values.
5. A passing software test cannot establish water resistance, structural strength, battery safety, sensor accuracy or roadworthiness.

## 6. Cross-portfolio engineering direction

These are shared strategic and engineering directions, not blanket claims of completed implementation:

- Industrial AI Platform: software-first intelligence integration and efficiency across real product constraints; PUI89 does not claim semiconductor manufacturing.
- Perception and task intelligence: observe, assess, decide and respond with provenance, uncertainty, abstention and human review.
- Multimodal intelligence: authorised vision, audio, text, spatial/map and sensor/time-series observations with timestamp alignment, quality checks and disagreement handling.
- Heterogeneous compute: CPU/GPU/NPU/MCU task placement, memory and power awareness, model sizing, quantisation, scheduling, edge inference and fallback.
- Simulation and digital twins: staged simulation before controlled physical prototypes; simulated outcomes remain explicitly labelled.
- Safety and human authority: AI outputs are bounded observations or proposals; independent safety controls and authorised human decisions remain authoritative.
- Security, privacy and recovery: least privilege, safe input handling, evidence integrity, failure reporting, recovery/version history and privacy-by-design. Do not publish sensitive security configurations.
- Supply-chain integrity: document origin, manufacturer, model, supplier, ownership/control, provenance and compatibility before adopting or purchasing components, software, models, datasets or services.
- Open-source-first governance: review provenance, licensing, security, privacy, compute requirements and maintainability before adopting external tools, models or datasets.

Product-specific configurations remain distinct. Do not copy a capability from one product to another solely because both use Shared AI Core.

## 7. Required alignment

Use this source together with the [Portfolio Alignment Register](PUI89_PORTFOLIO_ALIGNMENT_REGISTER_2026-11-18.md). Keep the following consistent in English and Thai:

- Main portfolio pages and navigation.
- All six product READMEs and product pages.
- Group pages and Shared AI Core pages.
- Evidence and development-maturity pages/data.
- Architecture diagrams, registries, project indexes and roadmaps.

If a conflict appears, do not silently guess. Treat this source as the portfolio identity baseline, inspect the product-specific repository and evidence, and submit a reviewable correction through a feature branch and pull request.

## 8. Change control

- Update this document when the founder approves a portfolio identity or scope change.
- Record review date and concise change history.
- Use feature branches and pull requests; do not write directly to the default branch or merge without explicit approval.
- Preserve historical records and clearly label retired or superseded material.
- A portfolio listing is not evidence of implementation, validation, certification or commercial release.

## Change history

- **v1.2 — 21 November 2026:** Re-established a directly retrievable canonical source; confirmed the six-product portfolio and Shared AI Core boundary.
- **v1.3 — 24 November 2026:** Incorrectly marked Sentinel as retired. Superseded by v1.4 after correction of the product identity.
- **v1.4 — 25 November 2026:** Restored PUI89 Sentinel as the sixth active product: All-Terrain Inspection Robot Dog. Explicitly retained narcotics screening, X-ray screening/datasets and related forensic/chemical-identification scope as excluded. Extreme Flood Rescue AI remains retired.
- **v1.5 — 26 November 2026:** Corrected Sentinel's canonical name to Quadruped Environmental Inspection Robot and corrected AI NOMAD's identity to a suitcase-style four-wheel mobile assistant with an integrated handle. Clarified that NOMAD has a functional internal storage compartment and is not for passenger aircraft cabin or overhead-bin carriage; air-cargo shipment requires carrier approval and applicable battery/shipping compliance.
