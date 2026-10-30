#!/usr/bin/env python3
"""Dependency-free PUI89 verification report builder and contract validator."""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

PROJECT_IDS = {
    "coconut-harvest-ai",
    "extreme-flood-rescue-ai",
    "multimodal-narcotics-screening-ai",
    "pui89-shared-core",
}
RUN_KINDS = {
    "unit_test", "integration_test", "static_check", "simulation",
    "dataset_preflight", "model_evaluation", "hardware_test",
}
STATUSES = {"PASS", "FAIL", "BLOCKED", "NOT_RUN", "PARTIAL"}
SEVERITIES = {"critical", "high", "medium", "low", "info"}
CATEGORIES = {
    "assertion", "import", "dependency", "data", "configuration",
    "timeout", "safety_gate", "environment", "unknown",
}


def validate_report(report: Any) -> list[str]:
    """Validate required contract fields without third-party packages."""
    errors: list[str] = []
    if not isinstance(report, dict):
        return ["report must be a JSON object"]
    required = {"schema_version", "project", "run", "status", "summary",
                "failures", "blockers", "claims"}
    missing = sorted(required - report.keys())
    if missing:
        errors.append("missing required fields: " + ", ".join(missing))
    if report.get("schema_version") != "1.0.0":
        errors.append("schema_version must be '1.0.0'")

    project = report.get("project")
    if not isinstance(project, dict):
        errors.append("project must be an object")
    else:
        if project.get("id") not in PROJECT_IDS:
            errors.append("project.id is not a supported PUI89 project id")
        if not isinstance(project.get("name"), str) or not project["name"].strip():
            errors.append("project.name must be a non-empty string")
        repository = project.get("repository")
        if repository is not None:
            parsed = urlparse(repository) if isinstance(repository, str) else None
            if not parsed or parsed.scheme not in {"https", "http"} or not parsed.netloc:
                errors.append("project.repository must be an absolute HTTP(S) URI")

    run = report.get("run")
    if not isinstance(run, dict):
        errors.append("run must be an object")
    else:
        if run.get("kind") not in RUN_KINDS:
            errors.append("run.kind is invalid")
        if not isinstance(run.get("started_at"), str) or not run["started_at"].strip():
            errors.append("run.started_at must be a non-empty timestamp string")
        else:
            try:
                datetime.fromisoformat(run["started_at"].replace("Z", "+00:00"))
            except ValueError:
                errors.append("run.started_at must be an ISO 8601 date-time")
        commit = run.get("commit")
        if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-fA-F]{7,40}", commit):
            errors.append("run.commit must be a 7-40 character hexadecimal commit")
        for key in ("finished_at", "workflow_url"):
            if key in run and run[key] is not None and not isinstance(run[key], str):
                errors.append(f"run.{key} must be a string or null")
        if run.get("finished_at") is not None:
            try:
                datetime.fromisoformat(run["finished_at"].replace("Z", "+00:00"))
            except (ValueError, AttributeError):
                errors.append("run.finished_at must be an ISO 8601 date-time or null")
        if isinstance(run.get("workflow_url"), str):
            parsed = urlparse(run["workflow_url"])
            if parsed.scheme not in {"https", "http"} or not parsed.netloc:
                errors.append("run.workflow_url must be an absolute HTTP(S) URI")
        elif run.get("workflow_url") is not None:
            errors.append("run.workflow_url must be an absolute HTTP(S) URI or null")

    if report.get("status") not in STATUSES:
        errors.append("status is invalid")

    summary = report.get("summary")
    if not isinstance(summary, dict):
        errors.append("summary must be an object")
    else:
        for key in ("passed", "failed", "skipped", "blocked"):
            if not isinstance(summary.get(key), int) or isinstance(summary.get(key), bool) or summary[key] < 0:
                errors.append(f"summary.{key} must be a non-negative integer")
        total = summary.get("tests_total")
        if total is not None and (not isinstance(total, int) or isinstance(total, bool) or total < 0):
            errors.append("summary.tests_total must be a non-negative integer or null")
        elif total is not None and all(
            isinstance(summary.get(key), int) and not isinstance(summary.get(key), bool)
            and summary[key] >= 0 for key in ("passed", "failed", "skipped")
        ):
            if summary["passed"] + summary["failed"] + summary["skipped"] != total:
                errors.append("summary.tests_total must equal passed + failed + skipped")
        if report.get("status") == "PASS" and isinstance(summary.get("failed"), int) and (
            summary.get("failed", 0) > 0 or summary.get("blocked", 0) > 0
        ):
            errors.append("PASS status cannot contain failed or blocked checks")
        if report.get("status") == "FAIL" and summary.get("failed") == 0:
            errors.append("FAIL status requires at least one failed test")

    if not isinstance(report.get("failures"), list):
        errors.append("failures must be an array")
    else:
        for i, failure in enumerate(report["failures"]):
            prefix = f"failures[{i}]"
            if not isinstance(failure, dict):
                errors.append(f"{prefix} must be an object")
                continue
            for key in ("id", "message"):
                if not isinstance(failure.get(key), str) or not failure[key].strip():
                    errors.append(f"{prefix}.{key} must be a non-empty string")
            if failure.get("severity") not in SEVERITIES:
                errors.append(f"{prefix}.severity is invalid")
            if failure.get("category") not in CATEGORIES:
                errors.append(f"{prefix}.category is invalid")
            if not isinstance(failure.get("reproducible"), bool):
                errors.append(f"{prefix}.reproducible must be boolean")

    if not isinstance(report.get("blockers"), list) or not all(
        isinstance(item, str) for item in report.get("blockers", [])
    ):
        errors.append("blockers must be an array of strings")

    claims = report.get("claims")
    if not isinstance(claims, dict):
        errors.append("claims must be an object")
    else:
        for key in ("software_checks_only", "ai_performance_measured",
                    "simulation_executed", "hardware_validated"):
            if not isinstance(claims.get(key), bool):
                errors.append(f"claims.{key} must be boolean")
        if "limitations" in claims and not (
            isinstance(claims["limitations"], list)
            and all(isinstance(item, str) for item in claims["limitations"])
        ):
            errors.append("claims.limitations must be an array of strings")

    artifacts = report.get("artifacts", [])
    if not isinstance(artifacts, list):
        errors.append("artifacts must be an array")
    else:
        for i, artifact in enumerate(artifacts):
            parsed = urlparse(artifact) if isinstance(artifact, str) else None
            if not parsed or parsed.scheme not in {"https", "http"} or not parsed.netloc:
                errors.append(f"artifacts[{i}] must be an absolute HTTP(S) URI")
    return errors


def build_report(args: argparse.Namespace) -> dict[str, Any]:
    now = datetime.now(timezone.utc).isoformat()
    failures = []
    if args.status == "FAIL":
        failures.append({
            "id": args.failure_id or "UNCLASSIFIED-1",
            "severity": args.severity,
            "category": args.category,
            "message": args.failure_message or "Run failed; inspect linked workflow logs.",
            "reproducible": args.reproducible,
        })
    return {
        "schema_version": "1.0.0",
        "project": {
            "id": args.project_id,
            "name": args.project_name,
            "repository": args.repository,
        },
        "run": {
            "kind": args.kind,
            "started_at": args.started_at or now,
            "finished_at": now,
            "workflow_url": args.workflow_url,
            "commit": args.commit,
            "environment": {
                "os": args.os_name,
                "python": args.python_version,
                "dependencies": args.dependency,
                "hardware": None,
            },
            "seed": None,
            "config_hash": None,
        },
        "status": args.status,
        "summary": {
            "tests_total": args.tests_total,
            "passed": args.passed,
            "failed": args.failed,
            "skipped": args.skipped,
            "blocked": args.blocked,
            "duration_seconds": None,
        },
        "failures": failures,
        "blockers": args.blocker,
        "claims": {
            "software_checks_only": args.software_checks_only,
            "ai_performance_measured": args.ai_performance_measured,
            "simulation_executed": args.simulation_executed,
            "hardware_validated": args.hardware_validated,
            "limitations": args.limitation,
        },
        "artifacts": args.artifact,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-id", required=True, choices=sorted(PROJECT_IDS))
    parser.add_argument("--project-name", required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--kind", required=True, choices=sorted(RUN_KINDS))
    parser.add_argument("--status", required=True, choices=sorted(STATUSES))
    parser.add_argument("--commit", required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--started-at")
    parser.add_argument("--workflow-url")
    parser.add_argument("--os-name")
    parser.add_argument("--python-version")
    parser.add_argument("--dependency", action="append", default=[])
    parser.add_argument("--tests-total", type=int)
    parser.add_argument("--passed", type=int, default=0)
    parser.add_argument("--failed", type=int, default=0)
    parser.add_argument("--skipped", type=int, default=0)
    parser.add_argument("--blocked", type=int, default=0)
    parser.add_argument("--failure-id")
    parser.add_argument("--failure-message")
    parser.add_argument("--severity", choices=sorted(SEVERITIES), default="medium")
    parser.add_argument("--category", choices=sorted(CATEGORIES), default="unknown")
    parser.add_argument("--reproducible", action="store_true")
    parser.add_argument("--blocker", action="append", default=[])
    parser.add_argument("--limitation", action="append", default=[])
    parser.add_argument("--artifact", action="append", default=[])
    parser.add_argument("--software-checks-only", action="store_true")
    parser.add_argument("--ai-performance-measured", action="store_true")
    parser.add_argument("--simulation-executed", action="store_true")
    parser.add_argument("--hardware-validated", action="store_true")
    args = parser.parse_args()

    counts = (args.passed, args.failed, args.skipped, args.blocked)
    if any(value < 0 for value in counts) or (args.tests_total is not None and args.tests_total < 0):
        parser.error("test counts must be non-negative")
    if args.status == "PASS" and (args.failed or args.blocked):
        parser.error("PASS cannot be used when failed or blocked counts are non-zero")
    if args.status == "FAIL" and args.failed == 0:
        parser.error("FAIL requires --failed greater than zero")
    if args.hardware_validated and not args.simulation_executed and args.kind != "hardware_test":
        parser.error("hardware validation requires a hardware_test run kind")

    report = build_report(args)
    errors = validate_report(report)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 2
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"{report['status']}: wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
