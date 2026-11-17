#!/usr/bin/env python3
"""Offline guard for third-party JavaScript loaded by PUI89 HTML pages.

The checker never fetches remote code. External scripts are denied unless an
exact URL is documented in security/third_party_script_allowlist.json with an
owner, purpose, review date, expiry date, SRI hash, and crossorigin=anonymous.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE_HOST = "pui89.github.io"
ALLOWLIST_PATH = ROOT / "security" / "third_party_script_allowlist.json"
SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__"}
NON_EXECUTABLE_TYPES = {"application/ld+json", "application/json"}


class ScriptParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.scripts: list[dict[str, str]] = []
        self._current: dict[str, str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "script":
            return
        attributes = {key.lower(): (value or "").strip() for key, value in attrs}
        self._current = attributes
        self.scripts.append(attributes)

    def handle_data(self, data: str) -> None:
        if self._current is not None and data.strip():
            self._current["_inline"] = self._current.get("_inline", "") + data

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "script":
            self._current = None


def load_allowlist() -> dict[str, dict[str, str]]:
    try:
        raw = json.loads(ALLOWLIST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot read {ALLOWLIST_PATH.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(raw, list):
        raise ValueError("Allowlist must be a JSON array.")
    entries: dict[str, dict[str, str]] = {}
    required = {"url", "owner", "purpose", "reviewed_on", "expires_on", "integrity"}
    for index, item in enumerate(raw):
        if not isinstance(item, dict) or not required.issubset(item):
            raise ValueError(f"Allowlist entry {index} must contain: {', '.join(sorted(required))}.")
        for field in ("owner", "purpose"):
            if not str(item[field]).strip():
                raise ValueError(f"Allowlist entry {index} must provide a non-empty {field}.")
        url = str(item["url"]).strip()
        parsed = urlsplit(url)
        if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
            raise ValueError(f"Allowlist entry {index} must use a credential-free HTTPS URL.")
        if url in entries:
            raise ValueError(f"Duplicate allowlist URL: {url}")
        for field in ("reviewed_on", "expires_on"):
            try:
                date.fromisoformat(str(item[field]))
            except ValueError as exc:
                raise ValueError(f"Allowlist entry {index} has invalid {field} date.") from exc
        if not re.fullmatch(r"sha(?:256|384|512)-[A-Za-z0-9+/=]+", str(item["integrity"])):
            raise ValueError(f"Allowlist entry {index} must pin one valid SRI hash.")
        reviewed = date.fromisoformat(str(item["reviewed_on"]))
        expires = date.fromisoformat(str(item["expires_on"]))
        if reviewed > date.today() or expires <= reviewed:
            raise ValueError(f"Allowlist entry {index} has an invalid review/expiry window.")
        entries[url] = {str(k): str(v) for k, v in item.items()}
    return entries


def html_files() -> list[Path]:
    return sorted(
        path for path in ROOT.rglob("*.html")
        if not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)
    )


def inspect_dynamic_script_patterns(source: str, location: str, warnings: list[str]) -> int:
    """Flag runtime code patterns that can load or execute code dynamically."""
    patterns = [
        ("dynamic script element creation", re.compile(r"""document\s*\.\s*createElement\s*\(\s*['"]script['"]\s*\)""", re.I)),
        ("document.write usage", re.compile(r"""document\s*\.\s*write(?:ln)?\s*\(""", re.I)),
        ("eval usage", re.compile(r"""\beval\s*\(""", re.I)),
        ("Function constructor usage", re.compile(r"""\bnew\s+Function\s*\(""", re.I)),
        ("dynamic import() usage", re.compile(r"""\bimport\s*\(""", re.I)),
    ]
    count = 0
    for label, pattern in patterns:
        if pattern.search(source):
            warnings.append(f"{location}: manual security review required: {label}")
            count += 1
    return count


def javascript_files() -> list[Path]:
    return sorted(
        path for path in ROOT.rglob("*.js")
        if not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)
    )


def main() -> int:
    try:
        allowlist = load_allowlist()
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1

    errors: list[str] = []
    warnings: list[str] = []
    seen_allowlisted: set[str] = set()
    external_count = 0
    inline_count = 0
    checked_pages = 0
    dynamic_pattern_findings = 0

    for page in html_files():
        checked_pages += 1
        parser = ScriptParser()
        try:
            parser.feed(page.read_text(encoding="utf-8"))
            parser.close()
            for script_index, script_item in enumerate(parser.scripts, start=1):
                inline_source = script_item.get("_inline", "")
                inline_type = script_item.get("type", "").lower().split(";", 1)[0].strip()
                if inline_source.strip() and not script_item.get("src") and inline_type not in NON_EXECUTABLE_TYPES:
                    dynamic_pattern_findings += inspect_dynamic_script_patterns(
                        inline_source, f"{page.relative_to(ROOT)}:inline-script-{script_index}", warnings
                    )
        except (OSError, UnicodeError) as exc:
            errors.append(f"{page.relative_to(ROOT)}: cannot parse HTML: {exc}")
            continue

        for item in parser.scripts:
            rel = page.relative_to(ROOT).as_posix()
            script_type = item.get("type", "").lower().split(";", 1)[0].strip()
            src = item.get("src", "").strip()
            if not src:
                if item.get("_inline", "").strip() and script_type not in NON_EXECUTABLE_TYPES:
                    inline_count += 1
                    warnings.append(f"{rel}: inline script requires manual review (no CSP nonce/hash assessment performed)")
                continue

            parsed = urlsplit(src)
            if parsed.scheme in ("",) and not parsed.netloc:
                continue
            if parsed.scheme == "https" and parsed.netloc.lower() == SITE_HOST:
                continue

            external_count += 1
            if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
                errors.append(f"{rel}: external script must use credential-free HTTPS: {src}")
                continue

            entry = allowlist.get(src)
            if entry is None:
                errors.append(f"{rel}: unapproved third-party script: {src}")
                continue

            seen_allowlisted.add(src)
            if date.fromisoformat(entry["expires_on"]) < date.today():
                errors.append(f"{rel}: expired third-party script approval: {src}")
            integrity = item.get("integrity", "")
            if not re.search(r"(?:^|\s)sha(?:256|384|512)-[A-Za-z0-9+/=]+(?:\s|$)", integrity):
                errors.append(f"{rel}: allowlisted third-party script is missing a valid SRI integrity attribute: {src}")
            if integrity and integrity != entry["integrity"]:
                errors.append(f"{rel}: SRI value does not match the reviewed allowlist hash: {src}")
            if item.get("crossorigin", "").lower() != "anonymous":
                errors.append(f"{rel}: allowlisted third-party script must set crossorigin=\"anonymous\": {src}")

    checked_js_files = 0
    for js_file in javascript_files():
        checked_js_files += 1
        try:
            source = js_file.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{js_file.relative_to(ROOT)}: cannot read JavaScript: {exc}")
            continue
        dynamic_pattern_findings += inspect_dynamic_script_patterns(
            source, js_file.relative_to(ROOT).as_posix(), warnings
        )

    for url in sorted(set(allowlist) - seen_allowlisted):
        warnings.append(f"Allowlisted script is not currently referenced by HTML: {url}")

    report = {
        "status": "failed" if errors else "passed_with_warnings" if warnings else "passed",
        "html_pages_checked": checked_pages,
        "javascript_files_checked": checked_js_files,
        "dynamic_script_pattern_findings": dynamic_pattern_findings,
        "script_sources_external": external_count,
        "allowlisted_external_scripts_used": len(seen_allowlisted),
        "inline_executable_scripts_review_required": inline_count,
        "errors": errors,
        "warnings": warnings,
        "limitations": [
            "Static HTML inspection does not detect scripts injected dynamically by already-running JavaScript.",
            "This check does not fetch, sandbox, or inspect remote script contents.",
            "A passing check does not prove that first-party hosting, DNS, the repository, or the browser is uncompromised.",
            "Inline-script warnings require a separate CSP and source review."
        ]
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
