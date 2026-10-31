#!/usr/bin/env python3
"""Build a free, read-only status dashboard for PUI89's three public project repositories.

Uses only Python's standard library and GitHub's public REST API. No token, hosted AI,
model downloads, third-party package, or repository write is performed by this script.
The workflow may publish the generated reports using its repository-scoped GITHUB_TOKEN.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = [
    ("Coconut Harvest AI", "Pui89/Coconut-Harvest-AI", "Priority 1: dataset provenance, reviewed labels, leakage-safe evaluation."),
    ("Extreme Flood Rescue AI", "Pui89/Extreme-Flood-Rescue-AI", "Simulation-first: scenario coverage, navigation and fail-safe evidence."),
    ("Multimodal Screening AI", "Pui89/Multimodal-Narcotics-Screening-AI", "Data provenance, uncertainty, modality failures and human review."),
]
API = "https://api.github.com"


def get_json(path: str) -> dict:
    request = urllib.request.Request(
        API + path,
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "PUI89-Free-Command-Centre",
        },
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))


def collect(project: tuple[str, str, str]) -> dict:
    name, repo, focus = project
    result = {
        "name": name,
        "repository": repo,
        "url": f"https://github.com/{repo}",
        "focus": focus,
        "status": "UNKNOWN",
        "default_branch": None,
        "latest_commit": None,
        "latest_commit_url": None,
        "latest_workflows": [],
        "non_default_branch_run_count": 0,
        "key_workflows": [],
        "warnings": [],
    }
    try:
        meta = get_json(f"/repos/{repo}")
        branch = meta.get("default_branch", "main")
        result["default_branch"] = branch
        try:
            commit = get_json(f"/repos/{repo}/commits/{branch}")
            result["latest_commit"] = commit.get("sha", "")[:12]
            result["latest_commit_url"] = commit.get("html_url")
        except (urllib.error.URLError, TimeoutError, ValueError, KeyError) as exc:
            result["warnings"].append(f"Latest commit unavailable: {type(exc).__name__}")
        try:
            runs = get_json(f"/repos/{repo}/actions/runs?per_page=50")
            all_runs = runs.get("workflow_runs", [])
            # Query the default branch directly: Dependabot/feature runs can otherwise
            # occupy the 50-run window and hide the latest main-branch evidence.
            encoded_branch = urllib.parse.quote(branch, safe="")
            branch_runs = get_json(
                f"/repos/{repo}/actions/runs?branch={encoded_branch}&per_page=50"
            )
            default_branch_runs = branch_runs.get("workflow_runs", [])
            result["non_default_branch_run_count"] = sum(
                1 for run in all_runs if run.get("head_branch") != branch
            )
            latest_by_name = {}
            for run in default_branch_runs:
                workflow_name = run.get("name") or run.get("path") or "Unnamed workflow"
                if workflow_name not in latest_by_name:
                    latest_by_name[workflow_name] = {
                        "name": workflow_name,
                        "status": run.get("status"),
                        "conclusion": run.get("conclusion"),
                        "updated_at": run.get("updated_at"),
                        "url": run.get("html_url"),
                        "branch": run.get("head_branch"),
                    }
            result["latest_workflows"] = list(latest_by_name.values())
            if not default_branch_runs:
                result["warnings"].append("No default-branch workflow runs found in the latest 50; branch health is unknown.")
            # Keep important safeguards visible even when routine CI runs are newer.
            key_terms = {
                "Free cloud verification": ("free cloud verification", "free-cloud-verification"),
                "Dataset recovery audit": ("dataset recovery", "dataset-recovery"),
                "Free-resource link audit": ("free-resource link", "free-resource-link-cleanup"),
                "Rule-based simulation evaluation": ("coconut harvest ai simulation evaluation", "flood rescue ai simulation evaluation", "multimodal narcotics screening ai simulation evaluation"),
                "Coconut dataset evidence audit": ("coconut dataset evidence audit", "dataset provenance, hashes and split integrity"),
                "Simulation benchmark + report validator": ("simulation benchmark", "pui89-simulation-benchmark"),
                "Autonomy / safety regression tests": ("autonomy", "safety regression"),
            }
            for label, terms in key_terms.items():
                match = next(
                    (item for item in default_branch_runs
                     if any(term in (str(item.get("name", "")) + " " + str(item.get("path", ""))).lower()
                            for term in terms)),
                    None,
                )
                result["key_workflows"].append({
                    "name": label,
                    "status": (match or {}).get("status", "not_seen_in_recent_runs"),
                    "conclusion": (match or {}).get("conclusion"),
                    "updated_at": (match or {}).get("updated_at"),
                    "url": (match or {}).get("html_url"),
                    "branch": (match or {}).get("head_branch"),
                })
            if not result["latest_workflows"]:
                result["warnings"].append("No workflow runs returned; this is not proof that checks failed.")
        except (urllib.error.URLError, TimeoutError, ValueError, KeyError) as exc:
            result["warnings"].append(f"Workflow status unavailable: {type(exc).__name__}")
        result["status"] = "CHECKS_AVAILABLE" if not result["warnings"] else "PARTIAL"
    except (urllib.error.URLError, TimeoutError, ValueError, KeyError) as exc:
        result["status"] = "UNAVAILABLE"
        result["warnings"].append(f"Repository status unavailable: {type(exc).__name__}")
    return result


def main() -> int:
    timestamp = datetime.now(timezone.utc).isoformat()
    projects = [collect(project) for project in PROJECTS]
    report = {
        "generated_at_utc": timestamp,
        "mode": "read-only public GitHub status summary",
        "projects": projects,
        "limitations": [
            "This report reads public repository metadata and recent workflow runs; it does not execute project tests.",
            "A missing workflow run is unknown, not a passing result or proof of failure.",
            "Only the most recent 50 repository workflow runs are scanned; a safeguard absent from that window is unknown.",
            "Headline workflow and safeguard status is filtered to the repository default branch; other-branch runs are counted separately and do not prove default-branch health.",
            "A successful workflow does not validate real-world robot performance or dataset correctness.",
            "The Coconut dataset evidence audit runs only where its workflow is configured; not_seen_in_recent_runs for other projects means not observed, not a failure.",
            "GitHub API rate limits or temporary network errors can make status partial.",
        ],
    }
    reports = ROOT / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    (reports / "pui89-command-centre.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    lines = [
        "# PUI89 AI Robotics — Cross-Project Command Centre",
        "",
        f"> Generated (UTC): {timestamp}",
        "",
        "Read-only overview of public repository commits and recent GitHub Actions runs. "
        "This report is not a substitute for running tests or reviewing evidence.",
        "",
        "| Project | Status | Latest commit | Latest workflow summary | Next focus |",
        "|---|---|---|---|---|",
    ]
    for project in projects:
        latest = project["latest_workflows"]
        if latest:
            workflow_text = "; ".join(
                f'{w["name"]}: {w["conclusion"] or w["status"] or "unknown"} [{w.get("branch") or "branch unknown"}]'
                for w in latest[:3]
            ).replace("|", "\\|")
        else:
            workflow_text = "No recent run data"
        commit = project["latest_commit"] or "unavailable"
        if project["latest_commit_url"] and project["latest_commit"]:
            commit = f'[{commit}]({project["latest_commit_url"]})'
        focus = project["focus"].replace("|", "\\|")
        lines.append(
            f'| [{project["name"]}]({project["url"]}) | {project["status"]} | '
            f'{commit} | {workflow_text} | {focus} |'
        )
    lines += [
        "",
        "## Key engineering safeguards",
        "",
        "Selected safeguards are scanned across the latest 50 repository workflow runs, rather than only the newest 10, and are filtered to the repository default branch. A status of not_seen_in_recent_runs means unknown, not failed or passed. Feature/Dependabot runs are counted separately and never substituted for default-branch evidence. The simulation check includes the report validator step only when that workflow run completes successfully. The Coconut dataset evidence audit is currently project-specific; other projects may show not_seen_in_recent_runs because that workflow is not configured there.",
        "",
    ]
    for project in projects:
        lines.append("### " + project["name"])
        lines += ["", f'Non-default-branch runs in the scanned window: {project.get("non_default_branch_run_count", 0)}', "", "| Safeguard | Status | Branch | Last updated (UTC) | Run |", "|---|---|---|---|---|"]
        for check in project.get("key_workflows", []):
            status = check.get("conclusion") or check.get("status") or "unknown"
            updated_at = check.get("updated_at") or "unknown"
            run_link = "[open](" + check["url"] + ")" if check.get("url") else "—"
            branch = check.get("branch") or "not seen on default branch"
            lines.append("| " + check["name"] + " | " + status + " | " + branch + " | " + updated_at + " | " + run_link + " |")
        lines.append("")
    lines += ["## Warnings and limitations", ""]
    for project in projects:
        for warning in project["warnings"]:
            lines.append(f'- **{project["name"]}:** {warning}')
    for limitation in report["limitations"]:
        lines.append(f"- {limitation}")
    lines += [
        "",
        "## Free-first policy",
        "",
        "- No paid AI API, cloud GPU, third-party Python package, or model download is used by this report generator.",
        "- The script only reads public GitHub metadata; it does not change project repositories.",
        "- The scheduled GitHub Actions workflow publishes this report in this website repository.",
        "- Do not interpret unknown, partial, or missing data as a passing test.",
        "",
    ]
    (reports / "pui89-command-centre.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated reports/pui89-command-centre.md and reports/pui89-command-centre.json")
    print("Project statuses: " + ", ".join(f'{p["name"]}={p["status"]}' for p in projects))
    return 0 if all(p["status"] != "UNAVAILABLE" for p in projects) else 1


if __name__ == "__main__":
    raise SystemExit(main())
