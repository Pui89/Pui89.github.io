#!/usr/bin/env python3
"""Read-only, dependency-free inventory of GitHub Actions workflow files.

This tool does not call GitHub, invoke AI APIs, install packages, or modify
workflow files. It reads .github/workflows/*.yml and prints a Markdown audit.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"


def parse_workflow(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    name_match = re.search(r"^name:\s*(.+?)\s*$", text, re.M)
    name = name_match.group(1).strip('"\'') if name_match else path.stem
    events: list[str] = []
    schedules: list[str] = []
    runners: list[str] = []
    timeouts: list[str] = []
    action_refs: list[str] = []
    has_paths = False
    in_on = False
    in_jobs = False
    for line in lines:
        if re.match(r"^on:\s*(?:#.*)?$", line):
            in_on, in_jobs = True, False
            continue
        if re.match(r"^jobs:\s*$", line):
            in_on, in_jobs = False, True
            continue
        if line and not line[0].isspace() and not line.startswith("#"):
            if not line.startswith("on:") and not line.startswith("jobs:"):
                in_on = False
                in_jobs = False
        if in_on:
            event_match = re.match(r"^  ([A-Za-z_-]+):\s*(?:#.*)?$", line)
            if event_match:
                events.append(event_match.group(1))
            cron = re.search(r"cron:\s*[\"']([^\"']+)", line)
            if cron:
                schedules.append(cron.group(1))
            if re.match(r"^\s{4,}(paths|paths-ignore):", line):
                has_paths = True
        if in_jobs:
            runner = re.search(r"^\s{4}runs-on:\s*(.+?)\s*$", line)
            if runner:
                runners.append(runner.group(1).strip())
            timeout = re.search(r"^\s{4}timeout-minutes:\s*(\d+)", line)
            if timeout:
                timeouts.append(timeout.group(1))
        action = re.search(r"\buses:\s*([^\s#]+)", line)
        if action:
            action_refs.append(action.group(1))
    return {
        "file": path.name,
        "name": name,
        "events": sorted(set(events)),
        "schedules_utc": schedules,
        "runners": sorted(set(runners)),
        "timeouts_minutes": sorted(set(timeouts)),
        "path_filters_detected": has_paths,
        "external_actions": sorted(set(action_refs)),
        "lines": len(lines),
    }


def findings(items: list[dict]) -> list[str]:
    out: list[str] = []
    for item in items:
        events = set(item["events"])
        if {"push", "pull_request"}.issubset(events) and not item["path_filters_detected"]:
            out.append(
                f"- **Broad trigger review:** `{item['file']}` runs on both push and "
                "pull_request without a detected path filter. Confirm both events are required."
            )
        if "schedule" in events:
            out.append(
                f"- **Scheduled compute:** `{item['file']}` has schedule(s) "
                f"`{', '.join(item['schedules_utc']) or 'present (cron not parsed)'}` UTC."
            )
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json-out", type=Path, help="Optional path for a JSON report")
    args = parser.parse_args()
    if not WORKFLOWS.is_dir():
        raise SystemExit(f"Workflow directory not found: {WORKFLOWS}")
    files = sorted([*WORKFLOWS.glob("*.yml"), *WORKFLOWS.glob("*.yaml")])
    items = [parse_workflow(path) for path in files]
    report = {
        "repository": "Pui89/Pui89.github.io",
        "mode": "read-only-static-analysis",
        "workflow_count": len(items),
        "workflows": items,
        "heuristic_findings": findings(items),
        "limitations": [
            "This is static text analysis, not a full YAML parser.",
            "Runner minutes must be measured from GitHub billing/Actions usage; they cannot be inferred from YAML.",
            "Similar names or triggers do not prove duplicated work.",
            "No workflow changes or GitHub API calls are performed.",
        ],
    }
    print("# PUI89 GitHub Actions — Read-only workflow audit")
    print()
    print(f"- Workflow files: **{len(items)}**")
    print("- Mode: read-only; standard library only; no AI/API calls; no Actions job created")
    print()
    print("| Workflow | Events | Runner(s) | Schedule (UTC) | Path filters |")
    print("|---|---|---|---|---|")
    for item in items:
        print(
            f"| `{item['file']}` | {', '.join(item['events']) or 'not parsed'} | "
            f"{', '.join(item['runners']) or 'not parsed'} | "
            f"{', '.join(item['schedules_utc']) or '—'} | "
            f"{'detected' if item['path_filters_detected'] else 'not detected'} |"
        )
    print()
    print("## Heuristic findings")
    print()
    found = findings(items)
    print("\n".join(found) if found else "No heuristic findings.")
    print()
    print("## Limitations")
    for limitation in report["limitations"]:
        print(f"- {limitation}")
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print()
        print(f"JSON report written to: {args.json_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
