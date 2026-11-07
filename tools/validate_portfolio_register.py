#!/usr/bin/env python3
"""Validate the dated PUI89 portfolio evidence register using Python's standard library."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

REGISTER = Path(__file__).resolve().parents[1] / "docs" / "pui89-portfolio-evidence-register.json"
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
    print("PASS: PUI89 portfolio evidence register is structurally consistent.")
    print(f"Projects: 7 | Active rulesets: {active}/{total} | Workflow files: {workflows}")
    print("Note: this validates register structure, not the truth or freshness of external evidence.")

if __name__ == "__main__":
    main()
