#!/usr/bin/env python3
"""Read-only quality checks for PUI89 blank manufacturing control templates."""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / "docs" / "manufacturing-templates"

EXPECTED = {
    "requirements-register.csv": {"requirement_id", "product_code", "shall_statement", "acceptance_min", "acceptance_max", "unit", "verification_method", "verification_evidence_id", "lifecycle_status"},
    "bom.csv": {"bom_item_id", "pui89_part_number", "manufacturer_part_number", "material_specification", "exact_grade_temper_condition", "approved_supplier_id", "inspection_method", "acceptance_criteria", "approval_record_id"},
    "drawing-register.csv": {"drawing_id", "drawing_revision", "units", "datum_scheme", "critical_dimensions_and_tolerances", "cad_native_file", "step_file", "pdf_file", "dxf_file", "approval_record_id"},
    "interface-register.csv": {"interface_id", "interface_type", "endpoint_a_part_number", "endpoint_b_part_number", "pinout_document_id", "protocol", "fault_response_safe_state", "verification_evidence_id"},
    "supplier-source-register.csv": {"supplier_id", "legal_entity_name", "manufacturing_site_id", "country_of_manufacture", "approved_part_numbers", "approval_status", "approval_scope"},
    "process-work-instruction-register.csv": {"operation_id", "required_part_numbers_and_revisions", "tools_fixtures_and_gauges", "work_instruction_id", "work_instruction_revision", "acceptance_criteria", "abnormal_stop_trigger"},
    "control-plan.csv": {"control_id", "requirement_id", "critical_characteristic", "measurement_method", "equipment_gauge_id", "acceptance_lower_limit", "acceptance_upper_limit", "reaction_plan"},
    "test-report-register.csv": {"test_id", "configuration_id", "unit_serial_or_lot", "requirement_ids", "procedure_id", "measurement_equipment_ids", "raw_data_location", "measured_results", "pass_fail_blocked"},
    "calibration-equipment-register.csv": {"equipment_id", "exact_model", "serial_number", "measurement_range", "accuracy_uncertainty", "calibration_certificate_id", "calibration_due_date", "status"},
    "change-ncr-tq-register.csv": {"record_id", "record_type", "affected_part_numbers", "affected_document_ids_and_revisions", "containment_action", "impact_assessment_safety_quality_reliability_thermal_emc_software_environment_regulatory_service_supply", "proposed_disposition", "approval_record_id", "lifecycle_status"},
    "software-configuration-register.csv": {"configuration_id", "hardware_configuration_id", "firmware_version", "firmware_hash", "model_name", "model_version", "model_hash", "model_license", "rollback_package_id", "verification_evidence_id"},
    "training-matrix.csv": {"personnel_id_or_role", "site_id", "job_role", "operation_id", "work_instruction_id", "training_language", "assessment_method", "authorisation_scope", "authorised_by"},
    "factory-transfer.csv": {"transfer_id", "product_code", "configuration_id", "manufacturing_site_id", "first_article_inspection_report_id", "process_validation_report_id", "qualification_status", "approval_record_id"},
    "release-authorization.csv": {"release_id", "product_code", "configuration_id", "manufacturing_site_id", "document_revision_set", "verification_evidence_package_id", "release_status", "product_release_authority", "approval_record_id"},
}

def main() -> int:
    errors: list[str] = []
    if not TEMPLATE_DIR.is_dir():
        print(f"ERROR: missing template directory: {TEMPLATE_DIR}")
        return 1

    for filename, required in EXPECTED.items():
        path = TEMPLATE_DIR / filename
        if not path.is_file():
            errors.append(f"{filename}: required template file is missing")
            continue
        try:
            with path.open("r", encoding="utf-8-sig", newline="") as handle:
                reader = csv.reader(handle)
                header = next(reader, None)
                rows = list(reader)
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"{filename}: cannot parse CSV: {exc}")
            continue

        if not header or any(not cell.strip() for cell in header):
            errors.append(f"{filename}: header is empty or contains a blank column name")
            continue
        if len(header) != len(set(header)):
            errors.append(f"{filename}: duplicate column names")
        missing = sorted(required.difference(header))
        if missing:
            errors.append(f"{filename}: missing required columns: {', '.join(missing)}")
        if rows:
            errors.append(f"{filename}: template must remain blank; found {len(rows)} data row(s)")

    guide = TEMPLATE_DIR / "README.md"
    if not guide.is_file():
        errors.append("README.md: template guide is missing")
    else:
        guide_text = guide.read_text(encoding="utf-8")
        for filename in EXPECTED:
            if filename not in guide_text:
                errors.append(f"README.md: does not document {filename}")

    if errors:
        print("PUI89 manufacturing template QA: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PUI89 manufacturing template QA: PASS ({len(EXPECTED)} blank CSV templates)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
