# PUI89 Manufacturing Control Templates v1.0

These CSV files are controlled starting templates for all six PUI89 products. They are not completed engineering data and do not authorise procurement, assembly or release.

## Use rules
- Keep one controlled copy per product, variant and released revision in the appropriate engineering record location.
- Do not rename or remove mandatory columns without an approved document change.
- Use SI units and ISO 8601 dates (YYYY-MM-DD); use decimal point; do not mix units in one column.
- Use stable IDs and link every record to the governing requirement, drawing, part, serial/lot, procedure and evidence.
- Use explicit values such as `TBD`, `N/A` (with rationale), `OPEN`, `NOT RELEASED`; never leave a blank that could be mistaken for approval.
- Never enter invented ratings, tolerances, test results, supplier approvals or certification claims.
- Protect commercially sensitive supplier, security and detailed test records in access-controlled project records.

## Templates
- `requirements-register.csv` — measurable requirements and verification traceability.
- `bom.csv` — exact part identity, source, rating, material and approved alternate.
- `drawing-register.csv` — controlled CAD/drawing deliverables and revision.
- `interface-register.csv` — mechanical/electrical/data/software interfaces.
- `control-plan.csv` — critical characteristics, inspection method and reaction plan.
- `test-report-register.csv` — test configuration, equipment, conditions, results and evidence.
- `change-and-nonconformance.csv` — TQ/NCR/ECR/deviation lifecycle and approvals.
- `training-matrix.csv` — task competence and authorisation.
- `factory-transfer.csv` — site qualification, FAI, process validation and release scope.

A row is production-authoritative only when the record is complete, reviewed, approved and included in the released configuration baseline.
