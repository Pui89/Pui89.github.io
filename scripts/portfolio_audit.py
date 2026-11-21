#!/usr/bin/env python3
"""PUI89 portfolio consistency auditor. Standard library only.

Scans public HTML pages and root README files for portfolio drift. Existing
baseline findings are reported as warnings; findings in files changed by a
pull request fail the check, preventing new regressions without blocking
unrelated PRs while legacy content is being corrected.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS = (
    "Coconut Harvest AI",
    "PUI89 Sentinel",
    "AI HOME",
    "AI NOMAD",
    "AI Global SUV",
    "AI Step-Through Scooter",
)
BILINGUAL_PAGES = (
    ("coconut.html", "coconut-th.html"),
    ("sentinel.html", "sentinel-th.html"),
    ("home.html", "home-th.html"),
    ("nomad.html", "nomad-th.html"),
    ("ai-global-suv.html", "ai-global-suv-th.html"),
    ("ai-robot-motorcycle.html", "ai-robot-motorcycle-th.html"),
)
# These phrases specifically describe obsolete NOMAD rover/ground-robot designs.
# Generic references to four-wheel AI HOME or quadruped Sentinel are not flagged.
STALE_NOMAD = (
    re.compile(r"four\s+spinner\s+caster\s+wheels?", re.I),
    re.compile(r"four\s+spinner\s+wheels?", re.I),
    re.compile(r"ground[- ]use\s+four[- ]wheel\s+mobile\s+assistant", re.I),
    re.compile(r"four[- ]wheel\s+ground[- ]use\s+mobile\s+assistant", re.I),
    re.compile(r"NOMAD.{0,100}(?:ground[- ]use|four[- ]wheel\s+mobile)", re.I),
    re.compile(r"(?:ground[- ]use|four[- ]wheel\s+mobile).{0,100}NOMAD", re.I),
    re.compile(r"ผู้ช่วยเคลื่อนที่ภาคพื้นดินแบบ\s*4\s*ล้อ"),
    re.compile(r"หุ่นยนต์ผู้ช่วยภายนอก\s*4\s*ล้อ"),
)

def tracked_sources() -> list[Path]:
    files = sorted(ROOT.glob("*.md")) + sorted(ROOT.glob("*.MD")) + sorted(ROOT.rglob("*.html"))
    return [p for p in files if ".git" not in p.parts and "node_modules" not in p.parts]

def changed_paths() -> set[str] | None:
    # Only PRs provide a base ref. Scheduled/manual audits report the full
    # baseline but do not fail solely on previously-existing drift.
    base = os.environ.get("GITHUB_BASE_REF", "").strip()
    if not base:
        return None
    remote_ref = f"origin/{base}"
    try:
        subprocess.run(["git", "fetch", "--no-tags", "origin", base], cwd=ROOT,
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        result = subprocess.run(
            ["git", "diff", "--name-only", f"{remote_ref}...HEAD"],
            cwd=ROOT, check=True, capture_output=True, text=True
        )
        return {line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()}
    except (subprocess.CalledProcessError, OSError):
        print("WARNING: Could not determine PR changed files; treating all scanned files as changed.")
        return {p.relative_to(ROOT).as_posix() for p in tracked_sources()}

def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    sources = tracked_sources()
    changed = changed_paths()
    readme = ROOT / "README.md"
    homepage = ROOT / "index.html"

    if not readme.is_file():
        errors.append("Root README.md is missing.")
    if not homepage.is_file():
        errors.append("index.html is missing.")

    for required in PRODUCTS:
        for path in (readme, homepage):
            if path.is_file() and required.casefold() not in path.read_text(encoding="utf-8").casefold():
                errors.append(f"{path.relative_to(ROOT)}: missing active product name: {required}")

    for en_page, th_page in BILINGUAL_PAGES:
        for filename in (en_page, th_page):
            if not (ROOT / filename).is_file():
                errors.append(f"Missing bilingual product page: {filename}")

    stale_count = 0
    for path in sources:
        rel = path.relative_to(ROOT).as_posix()
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            warnings.append(f"{rel}: unable to read as UTF-8 ({exc})")
            continue
        for pattern in STALE_NOMAD:
            for match in pattern.finditer(content):
                stale_count += 1
                line = content.count("\n", 0, match.start()) + 1
                message = f"{rel}:{line}: obsolete NOMAD design wording: {match.group(0)!r}"
                if changed is not None and rel in changed:
                    errors.append(message)
                else:
                    warnings.append(message)

    status = "FAILED" if errors else ("PASSED WITH BASELINE WARNINGS" if warnings else "PASSED")
    report = [
        "# PUI89 Portfolio Consistency Audit",
        "",
        f"**Status: {status}**",
        "",
        f"- Product names checked: {len(PRODUCTS)}",
        f"- Bilingual product page files required: {len(BILINGUAL_PAGES) * 2}",
        f"- Source files scanned: {len(sources)}",
        f"- Obsolete NOMAD wording matches: {stale_count}",
        f"- PR changed-file enforcement: {'enabled' if changed is not None else 'baseline/report mode'}",
        "",
        "## Errors (block this pull request)",
    ]
    report += [f"- {item}" for item in errors] or ["- None"]
    report += ["", "## Existing baseline warnings (reported, not blocking unrelated PRs)"]
    report += [f"- {item}" for item in warnings] or ["- None"]
    report += [
        "",
        "## Scope and limitations",
        "- Checks canonical six-product naming, required English/Thai product-page files, and retired NOMAD rover/four-wheel wording.",
        "- The companion site checker validates HTML metadata, local links, image alt attributes, sitemap paths, duplicate IDs and QR asset file structure.",
        "- This audit does not verify product performance, translate content quality, render responsive layouts, decode QR destinations, or prove Google indexing.",
        "- Human review remains required for images, technical claims, Thai/English meaning parity and product-design approval.",
    ]
    text = "\n".join(report) + "\n"
    print(text)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as handle:
            handle.write(text)
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
