# PUI89 Manufacturing Control Templates v1.0

**Status:** Blank controlled-record templates. Not a released product specification, approved BOM, supplier approval, work instruction, or production authorisation.
**Applies to:** All six active PUI89 products and qualified engineering/manufacturing partners.
**Language:** Controlled engineering English. Translate worker-facing instructions locally while preserving IDs, units, limits and revision references.
**Units:** SI by default. State the unit explicitly for every measured value.

## Purpose

These templates make production work transferable between countries and factories. They define the minimum records needed to understand what to build, which exact parts and revisions to use, how to assemble and inspect them, what constitutes acceptance, and how to trace every change and result.

## Non-negotiable use rules

1. Never guess a missing dimension, tolerance, material grade, component model, torque, adhesive, firmware version, test limit or acceptance criterion.
2. Use **TBD** only for an unresolved value; use **NOT APPLICABLE** with a reason when a field genuinely does not apply. Blank cells are not a valid status.
3. A template is not an approval. Only a separately authorised **RELEASED** record can authorise the activity within its stated scope.
4. Do not buy, build, substitute, rework, test for release or ship from a draft, concept image, chat message or supplier suggestion.
5. Every record must identify product, variant, configuration, document ID, revision, owner, approver, issue date and status.
6. Preserve failed results, superseded revisions, deviations and NCRs. Never silently overwrite or delete quality evidence.
7. Every acceptance criterion must be objective and linked to a requirement ID and a verification method.
8. If documents conflict, stop affected work and raise a Technical Query (TQ). Do not select whichever value appears newest.
9. Supplier/factory changes, materials, processes, tools, firmware, models and test methods require approved change control before use.
10. Safety-critical work requires competent personnel, independent review where specified, and applicable local legal approval.

## Included templates

| File | Use |
|---|---|
| requirements-register.csv | One uniquely identified, testable requirement per row |
| hardware-component-register.csv | Functional hardware definition, ratings, environment, interfaces and selected-part traceability |
| engineering-decision-register.csv | Open design decisions, evidence needed, ownership and approval gates |
| product-configuration-baseline.csv | Exact released product/variant/site/software/BOM/drawing configuration baseline |
| bom.csv | Exact item identity, manufacturer part number, rating, approved source and traceability |
| drawing-register.csv | CAD/STEP/PDF/DXF files, datums, tolerances, materials and approvals |
| interface-register.csv | Mechanical, electrical, data, thermal and software interfaces |
| supplier-source-register.csv | Supplier legal/site identity, capability, audit, origin evidence and approval scope |
| process-work-instruction-register.csv | Controlled process and operation instructions for workers |
| control-plan.csv | Critical-to-quality characteristics, checks, limits and reaction plans |
| test-report-register.csv | Procedure, DUT configuration, equipment, actual results and evidence |
| calibration-equipment-register.csv | Measurement equipment identity, calibration status and due dates |
| change-ncr-tq-register.csv | Engineering changes, deviations, nonconformance and technical queries |
| software-configuration-register.csv | Firmware, drivers, AI models, dependencies, hashes, licences and rollback |
| training-matrix.csv | Role competence, training revision, assessment and authorisation |
| factory-transfer.csv | Site qualification, FAI, process validation and release scope |
| release-authorization.csv | Formal approval for exact product/variant/site/process/revision scope |

## Field conventions

- IDs are stable and never reused (example patterns: `P89-HOME-REQ-0001`, `P89-SENTINEL-BOM-0001`, `P89-SUV-ICD-0001`).
- Product codes: `COCONUT`, `SENTINEL`, `HOME`, `NOMAD`, `SUV`, `SCOOTER`. Use the approved product configuration register for variants.
- Lifecycle status: `DRAFT`, `IN REVIEW`, `RELEASED`, `SUPERSEDED`, `WITHDRAWN`.
- Evidence state: `PROPOSED`, `SPECIFIED`, `TESTED`, `VERIFIED`.
- Work/result status: `OPEN`, `PASS`, `FAIL`, `BLOCKED`, `WAIVED` (WAIVED only with approved, scoped waiver).
- Use ISO 8601 dates (`YYYY-MM-DD`) and explicit time zone for timestamps.
- Use decimal point in machine-readable CSV. Do not embed units in numeric cells; use the paired unit field.
- Use controlled vocabulary and exact part/document IDs. Do not use vague terms such as “high quality”, “industrial grade”, “waterproof”, “equivalent” or “as required” as acceptance criteria.

## Release gates

**G0 — Requirements:** intended use, users, environment, hazards and measurable requirements approved.
**G1 — Design:** drawings/CAD, materials, interfaces, calculations and risk controls independently reviewed as required.
**G2 — Supply:** exact BOM, suppliers, alternates, origin and incoming acceptance approved.
**G3 — Process:** work instructions, tooling, gauges, calibration, training and control plan released.
**G4 — Verification:** FAI, functional, safety, environmental and reliability evidence passes the approved criteria.
**G5 — Site release:** factory/site qualification, traceability, open NCR disposition and release authorisation complete.
**G6 — Change/release maintenance:** configuration, field feedback, service, obsolescence and change history controlled.

A gate may be marked PASS only with linked evidence and an authorised approver. Missing evidence is not PASS.

## How to use

1. Copy the applicable template into the product's controlled engineering records.
2. Assign document IDs and record owners; link each row to the exact product and variant.
3. Populate values only from approved engineering sources.
4. Review and approve under the project's delegated authority matrix.
5. Freeze the released revision and distribute it to the specific qualified factory/site.
6. Train workers against the released local-language work instructions.
7. Record inspections and test results against serial/lot numbers.
8. Raise TQ/NCR/ECR for every ambiguity, failure or proposed change.

## Scope boundary

The templates are intentionally blank. They do not contain approved product dimensions, material grades, component models, torque values, electrical ratings, tolerances, safety limits, test results, supplier approvals or production authorisation. Those values must be developed and approved separately for each product and variant.
