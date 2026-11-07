#!/usr/bin/env python3
"""Validate PUI89 portfolio evidence and draft shared contracts using the standard library."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "docs" / "pui89-portfolio-evidence-register.json"
SCHEMAS = {
    "observation": ("schemas/pui89/observation.schema.json", "PUI89 Observation"),
    "world-state": ("schemas/pui89/world-state.schema.json", "PUI89 WorldState"),
    "action-proposal": ("schemas/pui89/action-proposal.schema.json", "PUI89 ActionProposal"),
    "failure-report": ("schemas/pui89/failure-report.schema.json", "PUI89 FailureReport"),
}
SHA_RE = re.compile(r"^[0-9a-f]{40}$")


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    try:
        data = json.loads(REGISTER.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read valid evidence register: {exc}")

    if data.get("schema_version") != "1.0.0":
        fail("unsupported register schema_version")
    if data.get("snapshot_date") != "2026-11-08":
        fail("snapshot_date must match this dated register")

    portfolio = data.get("portfolio", {})
    projects = portfolio.get("repositories", [])
    if portfolio.get("project_count") != 7 or len(projects) != 7:
        fail("portfolio must contain exactly seven project repositories")

    seen = set()
    active = total = workflows = 0
    required_keys = {
        "id", "name", "repository", "main_commit", "active_rulesets",
        "total_rulesets", "workflow_count", "security_workflows", "sampled_ruleset",
    }
    for project in projects:
        missing = required_keys - project.keys()
        if missing:
            fail(f"{project.get('id', 'unknown')}: missing {sorted(missing)}")
        if project["id"] in seen:
            fail(f"duplicate project id: {project['id']}")
        seen.add(project["id"])
        if not SHA_RE.fullmatch(project["main_commit"]):
            fail(f"{project['id']}: main_commit must be a full 40-character SHA")
        if project["active_rulesets"] < 1 or project["total_rulesets"] < project["active_rulesets"]:
            fail(f"{project['id']}: invalid ruleset counts")
        if project["workflow_count"] < 1 or not project["security_workflows"]:
            fail(f"{project['id']}: workflow/security inventory incomplete")
        if project["sampled_ruleset"].get("required_approving_review_count") is None:
            fail(f"{project['id']}: sampled review requirement must be explicit")
        active += project["active_rulesets"]
        total += project["total_rulesets"]
        workflows += project["workflow_count"]

    expected_totals = {
        "active_rulesets": active,
        "total_rulesets": total,
        "disabled_rulesets": total - active,
        "workflow_files": workflows,
    }
    for key, expected in expected_totals.items():
        if portfolio.get("totals", {}).get(key) != expected:
            fail(f"portfolio.totals.{key}: expected {expected}")

    if len(data.get("cross_project_findings", [])) < 5:
        fail("cross-project findings are incomplete")
    if len(data.get("next_actions", [])) != 7:
        fail("exactly seven prioritised next actions are required")

    loaded = {}
    for key, (relative_path, expected_title) in SCHEMAS.items():
        try:
            schema = json.loads((ROOT / relative_path).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            fail(f"{key}: cannot read valid schema JSON: {exc}")
        if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            fail(f"{key}: unexpected JSON Schema draft")
        if schema.get("title") != expected_title or schema.get("type") != "object":
            fail(f"{key}: schema identity or root type is invalid")
        if schema.get("x-pui89-contract-version") != "0.1.0-draft":
            fail(f"{key}: contract version must remain explicitly draft")
        if not schema.get("required"):
            fail(f"{key}: required fields are missing")
        loaded[key] = schema

    action = loaded["action-proposal"].get("properties", {})
    if action.get("human_approval_required", {}).get("const") is not True:
        fail("ActionProposal must require human approval")
    if action.get("authority", {}).get("const") != "advisory_only":
        fail("ActionProposal authority must remain advisory_only")
    if action.get("actuation_allowed", {}).get("const") is not False:
        fail("ActionProposal must not enable physical actuation")

    print("PASS: PUI89 evidence register and four draft contract schemas are structurally consistent.")
    print(f"Projects: 7 | Active rulesets: {active}/{total} | Workflow files: {workflows}")
    print("Note: this is a structural check, not full JSON Schema meta-validation or external evidence verification.")


if __name__ == "__main__":
    main()
