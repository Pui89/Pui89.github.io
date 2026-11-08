#!/usr/bin/env python3
"""Refresh public PUI89 project metrics using GitHub's public REST API.

Only structured feedback issues created from the PUI89 feedback form are counted.
No external packages or paid services are required.
"""
from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

PROJECTS = [
    ("Coconut Harvest AI", "Pui89/Coconut-Harvest-AI"),
    ("Extreme Flood Rescue AI", "Pui89/Extreme-Flood-Rescue-AI"),
    ("PUI89 Sentinel", "Pui89/Multimodal-Narcotics-Screening-AI"),
    ("PUI89 AI HOME", "Pui89/AI-Home-Safety-Robot"),
    ("PUI89 AI NOMAD", "Pui89/AI-Mobile-Assistant-Robot"),
    ("PUI89 AI Robot Car", "Pui89/AI-Autonomous-Robot-Car"),
    ("PUI89 AI Robot Motorcycle", "Pui89/AI-Motorcycle-Robotics"),
]
API_ROOT = "https://api.github.com"
FEEDBACK_MARKER = "<!-- PUI89_PROJECT_FEEDBACK_V1 -->"
RATING_PATTERN = re.compile(
    r"###\s*Overall feedback score \(1-5\)\s*\n+\s*([1-5])(?:\s|$)",
    re.IGNORECASE,
)


def github_json(url: str) -> dict | list:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "PUI89-project-metrics",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(url, headers=headers)
    try:
        with urlopen(request, timeout=25) as response:
            return json.load(response)
    except (HTTPError, URLError, TimeoutError) as exc:
        raise RuntimeError(f"GitHub API request failed for {url}: {exc}") from exc


def list_feedback_issues(repo: str) -> tuple[int, list[int], int]:
    page = 1
    feedback_count = 0
    ratings: list[int] = []
    open_issue_count = 0
    while True:
        url = f"{API_ROOT}/repos/{repo}/issues?state=all&per_page=100&page={page}"
        items = github_json(url)
        if not isinstance(items, list):
            raise RuntimeError(f"Unexpected issues response for {repo}")
        for issue in items:
            if "pull_request" in issue:
                continue
            if issue.get("state") == "open":
                open_issue_count += 1
            body = issue.get("body") or ""
            if FEEDBACK_MARKER not in body:
                continue
            feedback_count += 1
            match = RATING_PATTERN.search(body)
            if match:
                ratings.append(int(match.group(1)))
        if len(items) < 100:
            break
        page += 1
    return feedback_count, ratings, open_issue_count


def collect_project(name: str, repo: str) -> dict:
    metadata = github_json(f"{API_ROOT}/repos/{repo}")
    feedback_count, ratings, open_issue_count = list_feedback_issues(repo)
    average = round(sum(ratings) / len(ratings), 2) if ratings else None
    return {
        "name": name,
        "repository": repo,
        "repository_url": f"https://github.com/{repo}",
        "feedback_url": f"https://github.com/{repo}/issues/new?template=project-feedback.yml",
        "stars": metadata.get("stargazers_count"),
        "forks": metadata.get("forks_count"),
        "open_issues": open_issue_count,
        "feedback_submissions": feedback_count,
        "rating_count": len(ratings),
        "average_feedback_score": average,
        "last_repository_update": metadata.get("updated_at"),
    }


def main() -> int:
    try:
        projects = [collect_project(name, repo) for name, repo in PROJECTS]
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    payload = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "GitHub REST API",
        "feedback_definition": (
            "Public issues submitted using the PUI89 Project Feedback form; "
            "scores are community feedback, not verified customer reviews."
        ),
        "projects": projects,
    }
    output = Path("data/project-metrics.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary.replace(output)
    print(f"Updated metrics for {len(projects)} PUI89 projects at {payload['generated_at']}")
    for project in projects:
        print(
            f"{project['repository']}: stars={project['stars']}, "
            f"feedback={project['feedback_submissions']}, "
            f"ratings={project['rating_count']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
