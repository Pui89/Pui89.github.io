#!/usr/bin/env python3
"""Local-first cross-project test runner for the PUI89 AI portfolio.

Uses only the Python standard library. It does not install dependencies, download
models, call hosted APIs, or trigger cloud compute.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

PROJECTS = {
    "coconut-harvest-ai": "Coconut-Harvest-AI",
    "extreme-flood-rescue-ai": "Extreme-Flood-Rescue-AI",
    "multimodal-narcotics-screening-ai": "Multimodal-Narcotics-Screening-AI",
}


def run_command(command: list[str], cwd: Path, timeout: int) -> dict:
    started = time.monotonic()
    try:
        result = subprocess.run(
            command, cwd=cwd, text=True, capture_output=True,
            timeout=timeout, check=False,
        )
        status = "PASS" if result.returncode == 0 else "FAIL"
        return {
            "status": status,
            "return_code": result.returncode,
            "duration_seconds": round(time.monotonic() - started, 3),
            "stdout": result.stdout[-12000:],
            "stderr": result.stderr[-6000:],
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "status": "TIMEOUT", "return_code": None,
            "duration_seconds": round(time.monotonic() - started, 3),
            "stdout": (exc.stdout or "")[-12000:] if isinstance(exc.stdout, str) else "",
            "stderr": "Command exceeded configured timeout.",
        }
    except OSError as exc:
        return {
            "status": "ERROR", "return_code": None,
            "duration_seconds": round(time.monotonic() - started, 3),
            "stdout": "", "stderr": str(exc),
        }


def git_revision(project_dir: Path, timeout: int) -> str | None:
    result = run_command(["git", "rev-parse", "--short", "HEAD"], project_dir, timeout)
    return result["stdout"].strip() if result["status"] == "PASS" else None


def evaluate_project(slug: str, folder: str, root: Path, timeout: int, skip_tests: bool) -> dict:
    project_dir = root / folder
    record = {
        "project": slug,
        "path": str(project_dir),
        "revision": None,
        "status": "NOT_RUN",
        "checks": {},
    }
    if not project_dir.is_dir():
        record["status"] = "MISSING"
        record["checks"]["repository"] = {"status": "MISSING", "stderr": "Project folder not found."}
        return record

    record["revision"] = git_revision(project_dir, timeout)
    tests_dir = project_dir / "tests"
    if skip_tests:
        record["checks"]["pytest"] = {"status": "SKIPPED", "stderr": "Skipped by request."}
    elif not tests_dir.is_dir():
        record["checks"]["pytest"] = {"status": "SKIPPED", "stderr": "No tests/ directory found."}
    else:
        record["checks"]["pytest"] = run_command(
            [sys.executable, "-m", "pytest", "-q"], project_dir, timeout
        )

    ruff_available = subprocess.run(
        [sys.executable, "-m", "ruff", "--version"],
        cwd=project_dir, text=True, capture_output=True, check=False,
    ).returncode == 0
    if ruff_available:
        record["checks"]["ruff"] = run_command(
            [sys.executable, "-m", "ruff", "check", "."], project_dir, timeout
        )
    else:
        record["checks"]["ruff"] = {
            "status": "SKIPPED",
            "stderr": "Ruff is not installed in this Python environment; no installation was attempted.",
        }

    statuses = [item["status"] for item in record["checks"].values()]
    if "FAIL" in statuses or "ERROR" in statuses or "TIMEOUT" in statuses:
        record["status"] = "FAIL"
    elif "MISSING" in statuses:
        record["status"] = "MISSING"
    elif all(status == "SKIPPED" for status in statuses):
        record["status"] = "SKIPPED"
    else:
        record["status"] = "PASS"
    return record


def write_reports(report: dict, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "pui89-report.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    with (output_dir / "pui89-report.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=["project", "status", "revision", "path", "checks"]
        )
        writer.writeheader()
        for project in report["projects"]:
            writer.writerow({
                **{key: project.get(key) for key in ("project", "status", "revision", "path")},
                "checks": "; ".join(
                    f"{name}={value['status']}" for name, value in project["checks"].items()
                ),
            })


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--projects-root", type=Path, default=Path.cwd(),
                        help="Folder containing the three project repositories.")
    parser.add_argument("--output-dir", type=Path, default=Path("pui89-reports"))
    parser.add_argument("--timeout", type=int, default=900,
                        help="Per-command timeout in seconds (default: 900).")
    parser.add_argument("--skip-tests", action="store_true",
                        help="Inventory repositories without running pytest.")
    args = parser.parse_args()
    if args.timeout < 1:
        parser.error("--timeout must be at least 1 second")

    root = args.projects_root.expanduser().resolve()
    output = args.output_dir.expanduser().resolve()
    projects = [
        evaluate_project(slug, folder, root, args.timeout, args.skip_tests)
        for slug, folder in PROJECTS.items()
    ]
    report = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "runner": "PUI89 local cross-project runner",
        "execution_mode": "local_only",
        "network_access_requested": False,
        "model_downloads_requested": False,
        "projects_root": str(root),
        "summary": {
            "projects": len(projects),
            "passed": sum(p["status"] == "PASS" for p in projects),
            "failed": sum(p["status"] == "FAIL" for p in projects),
            "missing": sum(p["status"] == "MISSING" for p in projects),
            "skipped": sum(p["status"] == "SKIPPED" for p in projects),
        },
        "projects": projects,
    }
    write_reports(report, output)
    print(json.dumps(report["summary"], indent=2))
    print(f"JSON report: {output / 'pui89-report.json'}")
    print(f"CSV report:  {output / 'pui89-report.csv'}")
    return 1 if report["summary"]["failed"] or report["summary"]["missing"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
