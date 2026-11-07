#!/usr/bin/env python3
"""Validate the dated PUI89 portfolio evidence register using Python's standard library."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]\nREGISTER = ROOT / "docs" / "pui89-portfolio-evidence-register.json"\nSCHEMAS = {\n    "observation": ("schemas/pui89/observation.schema.json", "PUI89 Observation"),\n    "world-state": ("schemas/pui89/world-state.schema.json", "PUI89 WorldState"),\n    "action-proposal": ("schemas/pui89/action-proposal.schema.json", "PUI89 ActionProposal"),\n    "failure-report": ("schemas/pui89/failure-report.schema.json", "PUI89 FailureReport"),\n}
SHA_RE = re.compile(r"^[0-9a-f]{40}$")

def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)

def main() -> None:
    try:
        data = json.loads(REGISTER.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read valid JSON register: {exc}")
    if data.get("schema_version") != "1.0.0":
        fail("unsupported schema_version")
    if data.get("snapshot_date") != "2026-11-08":
        fail("snapshot_date must match this dated register")
    portfolio = data.get("portfolio", {})
    projects = portfolio.get("repositories", [])
    if portfolio.get("project_count") != 7 or len(projects) != 7:
        fail("portfolio must contain exactly seven project repositories")
    seen, active, total, workflows = set(), 0, 0, 0
    required = {"id","name","repository","main_commit","active_rulesets","total_rulesets","workflow_count","security_workflows","sampled_ruleset"}
    for project in projects:
        missing = required - project.keys()
        if missing:
            fail(f"{project.get('id','unknown')}: missing {sorted(missing)}")
        if project["id"] in seen:
            fail(f"duplicate project id: {project['id']}")
        seen.add(project["id"])
        if not SHA_RE.fullmatch(project["main_commit"]):
            fail(f"{project['id']}: main_commit must be a full SHA")
        if project["active_rulesets"] < 1 or project["total_rulesets"] < project["active_rulesets"]:
            fail(f"{project['id']}: invalid ruleset counts")
        if project["workflow_count"] < 1 or not project["security_workflows"]:
            fail(f"{project['id']}: workflow inventory incomplete")
        if project["sampled_ruleset"].get("required_approving_review_count") is None:
            fail(f"{project['id']}: sampled review requirement must be explicit")
        active += project["active_rulesets"]
        total += project["total_rulesets"]
        workflows += project["workflow_count"]
    expected = {"active_rulesets":active,"total_rulesets":total,"disabled_rulesets":total-active,"workflow_files":workflows}
    for key, value in expected.items():
        if portfolio.get("totals", {}).get(key) != value:
            fail(f"portfolio.totals.{key}: expected {value}")
    if len(data.get("cross_project_findings", [])) < 5:
        fail("cross-project findings are incomplete")
    if len(data.get("next_actions", [])) != 7:
        fail("exactly seven prioritised next actions are required")
    for key, (relative_path, expected_title) in SCHEMAS.items():\n        try:\n            schema = json.loads((ROOT / relative_path).read_text(encoding="utf-8"))\n        except (OSError, json.JSONDecodeError) as exc:\n            fail(f"{key}: cannot read valid schema JSON: {exc}")\n        if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":\n            fail(f"{key}: unexpected JSON Schema draft")\n        if schema.get("title") != expected_title or schema.get("type") != "object":\n            fail(f"{key}: schema identity or root type is invalid")\n        if schema.get("x-pui89-contract-version") != "0.1.0-draft":\n            fail(f"{key}: contract version must remain explicitly draft")\n        if not schema.get("required"):\n            fail(f"{key}: required fields are missing")\n    action_schema = json.loads((ROOT / SCHEMAS["action-proposal"][0]).read_text(encoding="utf-8"))\n    action_properties = action_schema.get("properties", {})\n    if action_properties.get("human_approval_required", {}).get("const") is not True:\n        fail("ActionProposal must require human approval")\n    if action_properties.get("authority", {}).get("const") != "advisory_only":\n        fail("ActionProposal authority must remain advisory_only")\n    if action_properties.get("actuation_allowed", {}).get("const") is not False:\n        fail("ActionProposal must not enable physical actuation")\n\n    print("PASS: PUI89 portfolio register and four draft contract schemas are structurally consistent.")
    print(f"Projects: 7 | Active rulesets: {active}/{total} | Workflow files: {workflows}")
    print("Note: this validates JSON structure and safety constants, not full JSON Schema conformance or external evidence truth/freshness.")

if __name__ == "__main__":
    main()
