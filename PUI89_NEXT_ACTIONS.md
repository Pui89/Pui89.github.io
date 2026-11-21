# PUI89 Engineering Roadmap — Current Actions

**Updated:** 17 November 2026  
**Active portfolio:** exactly six products. Shared AI Core is infrastructure, not a seventh product.

The canonical product names, repositories, bilingual website links and founder-approved boundaries are in [PUI89 Portfolio Source of Truth v1.0](PUI89_PORTFOLIO_SOURCE_OF_TRUTH_V1.0.md).

## Shared engineering foundation
- [ ] Review Draft PRs for quality engineering controls 1–9 and portfolio consistency recommendations 10–11; do not merge until human review and approval.
- [ ] Keep shared contracts, evidence provenance, uncertainty, abstention, safe hold and failure reporting consistent across the six products.
- [ ] Use the evidence maturity labels: Proposed, Specified, Implemented, Simulated, Software-tested, Bench-tested, Field-tested, Validated, Certified, Unknown.
- [ ] Do not publish unsupported commercial-readiness percentages.

## Product work — priority order

### 1. Coconut Harvest AI
- [ ] Verify image source, provenance and reuse rights; record exact licence evidence.
- [ ] Finalise four-class human annotation guide and have labels independently reviewed.
- [ ] Create leakage-safe train/validation/test splits.
- [ ] Run reproducible CPU evaluation only after dataset rights and labels pass review.
- [ ] Report per-class Precision, Recall, F1, confusion matrix, sample counts and false-positive/false-negative cases.
- [ ] Keep harvesting mechanics and physical actuation out of scope until software evidence and separate safety gates justify them.

### 2. PUI89 Sentinel — All-Terrain Exploration & Inspection Robot
- [ ] Define the first supervised inspection mission, site, asset, environment and operating envelope.
- [ ] Complete hazard analysis, human roles, no-go conditions, emergency/retreat plan and measurable acceptance criteria.
- [ ] Select hardware only after the mission definition is approved.

### 3. PUI89 AI HOME
- [ ] Maintain complete robot mass target of 8 kg and maximum 10 kg, including battery and all installed hardware.
- [ ] Reconcile the design BOM and later measure the complete assembled prototype.

### 4. PUI89 AI NOMAD
- [ ] Keep identity as a ground-use four-wheel mobile assistant robot, not luggage or airline baggage.
- [ ] Keep storage secondary to supervised mobility and assistance; define mobility/safety tasks before hardware commitment.

### 5. PUI89 AI Global SUV
- [ ] Keep AI outputs advisory to the human driver.
- [ ] Define road-water and flood-risk alert scenarios; unknown water condition means “unknown — do not enter”.
- [ ] No autonomous steering, throttle or braking.

### 6. PUI89 AI Step-Through Scooter
- [ ] Keep rider-first, human-controlled operation.
- [ ] Define advisory road-water/flood-risk alerts; unknown water condition means “unknown — do not enter”.
- [ ] No autonomous steering, throttle or braking; no unverified waterproofing or water-wading claims.

## Later, gated upgrades
- [ ] Evaluate open-source tools only after checking licence, provenance, disk/RAM/VRAM needs and compatibility.
- [ ] Add simulation or hardware only when a defined product mission and evidence gate justify it.
- [ ] Keep procurement, downloads, installations and paid services behind explicit approval.

## Guardrails
- No invented metrics, test results, data provenance or physical capability claims.
- No paid APIs, subscriptions or cloud GPU dependencies in the default workflow.
- A skipped check is not a passing check.
- All material changes go through reviewable pull requests; no default-branch writes or auto-merge.
