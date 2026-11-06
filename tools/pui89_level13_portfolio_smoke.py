#!/usr/bin/env python3
"""Dependency-free PUI89 Level 13 cross-project smoke verifier.

Runs only selected existing unittest suites. It does not install packages,
download models, call external APIs, access hardware, or claim model accuracy.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = [
    {
        "id": "coconut-harvest-ai",
        "name": "Coconut Harvest AI",
        "repo": "Pui89/Coconut-Harvest-AI",
        "path": "projects/coconut",
        "patterns": ["test_pui89_core.py", "test_pui89_ai_core_conformance.py"],
    },
    {
        "id": "extreme-flood-rescue-ai",
        "name": "Extreme Flood Rescue AI",
        "repo": "Pui89/Extreme-Flood-Rescue-AI",
        "path": "projects/flood",
        "patterns": ["test_pui89_core.py", "test_pui89_ai_core_conformance.py"],
    },
    {
        "id": "multimodal-narcotics-screening-ai",
        "name": "Multimodal Narcotics Screening AI",
        "repo": "Pui89/Multimodal-Narcotics-Screening-AI",
        "path": "projects/screening",
        "patterns": ["test_pui89_core.py", "test_pui89_ai_core_conformance.py"],
    },
    {
        "id": "pui89-ai-home",
        "name": "PUI89 AI HOME",
        "repo": "Pui89/AI-HOME",
        "path": "projects/home",
        "patterns": ["test*.py"],
    },
    {
        "id": "pui89-ai-nomad",
        "name": "PUI89 AI NOMAD",
        "repo": "Pui89/AI-NOMAD",
        "path": "projects/nomad",
        "patterns": [
            "test_pui89_shared_workflow_contract.py",
            "test_pui89_shield_policy.py",
        ],
    },
    {
        "id": "pui89-ai-robot-car",
        "name": "PUI89 AI Robot Car",
        "repo": "Pui89/ai-robot-car",
        "path": "projects/car",
        "patterns": ["test_contracts.py", "test_safety.py"],
    },
    {
        "id": "pui89-ai-robot-motorcycle",
        "name": "PUI89 AI Robot Motorcycle",
        "repo": "Pui89/ai-robot-motorcycle",
        "path": "projects/motorcycle",
        "patterns": ["test_motorcycle_risk_scenarios.py"],
        "pythonpath": "src",
        "excluded_suites": ["test_core.py requires pytest; skipped by the no-package-install policy."],
    },
]


def git_sha(path: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=path,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        return result.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def run_suite(project_root: Path, pattern: str, pythonpath: str | None, log_parts: list[str]) -> dict:
    env = os.environ.copy()
    if pythonpath:
        prior = env.get("PYTHONPATH")
        env["PYTHONPATH"] = pythonpath + (os.pathsep + prior if prior else "")
    command = [
        sys.executable,
        "-m",
        "unittest",
        "discover",
        "-s",
        "tests",
        "-p",
        pattern,
        "-v",
    ]
    try:
        proc = subprocess.run(
            command,
            cwd=project_root,
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=180,
        )
        output = proc.stdout or ""
        match = re.search(r"Ran (\d+) tests?", output)
        count = int(match.group(1)) if match else 0
        failed_match = re.search(r"FAILED \((.*?)\)", output)
        suite_status = "PASS" if proc.returncode == 0 and count > 0 else "FAIL"
        log_parts.append(
            f"## {pattern}\n$ {' '.join(command)}\nexit_code={proc.returncode}; tests_run={count}\n{output}"
        )
        return {
            "pattern": pattern,
            "status": suite_status,
            "tests_run": count,
            "exit_code": proc.returncode,
            "failure_summary": failed_match.group(1) if failed_match else None,
        }
    except subprocess.TimeoutExpired as exc:
        output = exc.stdout or ""
        if isinstance(output, bytes):
            output = output.decode("utf-8", errors="replace")
        log_parts.append(f"## {pattern}\nTIMEOUT after 180 seconds\n{output}")
        return {
            "pattern": pattern,
            "status": "FAIL",
            "tests_run": 0,
            "exit_code": None,
            "failure_summary": "timeout after 180 seconds",
        }


def main() -> int:
    report_dir = ROOT / "reports" / "level13"
    log_dir = report_dir / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    results = []

    for project in PROJECTS:
        project_root = ROOT / project["path"]
        item = {
            "project_id": project["id"],
            "project": project["name"],
            "repository": f"https://github.com/{project['repo']}",
            "commit": git_sha(project_root) if project_root.is_dir() else None,
            "suites": [],
            "excluded_suites": project.get("excluded_suites", []),
        }
        if not project_root.is_dir():
            item["status"] = "BLOCKED"
            item["note"] = "Repository checkout is unavailable to this workflow; no tests were run."
        elif not (project_root / "tests").is_dir():
            item["status"] = "BLOCKED"
            item["note"] = "No tests directory was found; no test pass is claimed."
        else:
            log_parts = []
            item["suites"] = [
                run_suite(project_root, pattern, project.get("pythonpath"), log_parts)
                for pattern in project["patterns"]
            ]
            item["status"] = (
                "PASS"
                if item["suites"] and all(suite["status"] == "PASS" for suite in item["suites"])
                else "FAIL"
            )
            item["note"] = (
                "Selected dependency-free unittest suites only; not the full project test suite."
            )
            (log_dir / f"{project['id']}.txt").write_text(
                "\n\n".join(log_parts) + "\n", encoding="utf-8"
            )
        results.append(item)
        print(f"{item['status']}: {item['project']} ({item['commit'] or 'no commit checked out'})")

    statuses = {item["status"] for item in results}
    overall = "FAIL" if "FAIL" in statuses else ("REVIEW_REQUIRED" if "BLOCKED" in statuses else "PASS")
    report = {
        "schema_version": "1.0",
        "milestone": "PUI89 Level 13 cross-project automation",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "portfolio_commit": os.environ.get("GITHUB_SHA", "local"),
        "trigger": os.environ.get("GITHUB_EVENT_NAME", "local"),
        "overall_status": overall,
        "projects": results,
        "limitations": [
            "Only the explicitly listed existing unittest suites are run; this is not a full test-suite result.",
            "A passing suite verifies selected software behaviour only, not AI accuracy, calibration, sensor truth, simulator fidelity, physical safety or field readiness.",
            "BLOCKED means the repository or test directory was unavailable; it is not a pass.",
            "No model weights, datasets or packages are downloaded or installed. No paid service, GPU, hardware or actuator is used.",
            "Each project's test results and commit are reported separately; no cross-project score is calculated.",
        ],
    }
    json_path = report_dir / "pui89-level13-portfolio-report.json"
    md_path = report_dir / "pui89-level13-portfolio-report.md"
    json_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# PUI89 Level 13 — Cross-Project Verification",
        "",
        f"- Generated: {report['generated_at']}",
        f"- Overall: **{overall}**",
        f"- Portfolio commit: `{report['portfolio_commit']}`",
        "",
        "| Project | Status | Commit | Selected suites |",
        "|---|---|---|---|",
    ]
    for item in results:
        suites = ", ".join(suite["pattern"] for suite in item["suites"]) or "not run"
        commit = item["commit"][:12] if item["commit"] else "not available"
        lines.append(f"| {item['project']} | **{item['status']}** | `{commit}` | {suites} |")
        if item.get("note"):
            lines.append("")
            lines.append(f"**{item['project']}:** {item['note']}")
    lines.extend(["", "## Limitations", ""])
    lines.extend(f"- {note}" for note in report["limitations"])
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as summary:
            summary.write(md_path.read_text(encoding="utf-8"))

    print(f"Report: {json_path.relative_to(ROOT)}")
    print(f"Summary: {md_path.relative_to(ROOT)}")
    return 1 if overall == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
