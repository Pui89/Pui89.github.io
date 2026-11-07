# PUI89 Shared AI Core contract schemas — draft 0.1.0

These four JSON Schema documents are a **proposed canonical interface baseline**, introduced for review. They are not yet a released software package and are not yet verified as integrated by all seven project adapters.

## Files

- `observation.schema.json` — source-attributed input, timestamp, modality, quality, provenance and integrity.
- `world-state.schema.json` — bounded state estimate, frame context, observation references, freshness, uncertainty, known/unknown fields and limitations.
- `action-proposal.schema.json` — evidence-backed advisory proposal with mandatory human approval and physical actuation explicitly disabled.
- `failure-report.schema.json` — fault, severity, evidence, containment, recovery recommendation, unresolved uncertainty and safe-state outcome.

## Contract rules

1. Contract version is `0.1.0-draft`; breaking changes require a version change and migration note.
2. A missing or conflicting observation must remain unknown or degraded; never invent a value.
3. Preserve timestamps, source identifiers, provenance, calibration and evidence references across adapters.
4. Confidence is optional and bounded from 0 to 1; it must not be treated as calibrated probability unless separately evaluated.
5. Every ActionProposal is advisory-only: `human_approval_required=true`, `authority=advisory_only`, and `actuation_allowed=false`.
6. These schemas define data shape, not sensor accuracy, model validity, safety certification or permission to control hardware.
7. Each project must review the draft against its own data protection, safety and domain requirements before adoption.

## Adoption sequence

- Review the four schemas with project-specific owners/reviewers.
- Add schema-validation tests using an already available validator or a dependency-free compatible check.
- Build a shared versioned package only after the interface review.
- Migrate adapters one project at a time and record the exact compatible schema version.
- Keep local adapters thin; do not copy and silently alter canonical contract definitions.

**Current status:** PROPOSED / DRAFT. No portfolio-wide adapter integration is claimed.
