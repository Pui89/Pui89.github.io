#!/usr/bin/env python3
"""Generate a non-enforcing CSP compatibility inventory for static HTML.

This tool does not change headers or rewrite pages. It records fingerprints,
not inline source, so reviewers can plan nonce/hash migration without copying
application code into the report.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__"}
NON_EXECUTABLE = {"application/json", "application/ld+json"}


class InventoryParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.inline_scripts: list[dict[str, object]] = []
        self.external_scripts: list[str] = []
        self.event_handlers: Counter[str] = Counter()
        self.style_attributes = 0
        self.javascript_urls: list[str] = []
        self.csp_meta = 0
        self.nonce_attributes = 0
        self.sri_attributes = 0
        self._script: dict[str, object] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {k.lower(): (v or "").strip() for k, v in attrs}
        for key, value in values.items():
            if key.startswith("on"):
                self.event_handlers[key] += 1
            elif key == "style":
                self.style_attributes += 1
            if key in {"href", "src", "action", "formaction", "xlink:href"} and value.lower().startswith("javascript:"):
                self.javascript_urls.append(f"{tag}[{key}]")
            if key == "nonce":
                self.nonce_attributes += 1
        if tag.lower() == "meta" and values.get("http-equiv", "").lower() == "content-security-policy":
            self.csp_meta += 1
        if tag.lower() != "script":
            return
        src = values.get("src", "")
        if src:
            self.external_scripts.append(src)
            if values.get("integrity"):
                self.sri_attributes += 1
            return
        script_type = values.get("type", "").lower().split(";", 1)[0].strip()
        if script_type not in NON_EXECUTABLE:
            self._script = {"type": script_type or "classic", "text": ""}

    def handle_data(self, data: str) -> None:
        if self._script is not None:
            self._script["text"] = str(self._script["text"]) + data

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "script" and self._script is not None:
            source = str(self._script["text"])
            if source.strip():
                digest = base64.b64encode(hashlib.sha256(source.encode("utf-8")).digest()).decode("ascii")
                self.inline_scripts.append({
                    "type": self._script["type"],
                    "bytes": len(source.encode("utf-8")),
                    "sha256_csp": f"sha256-{digest}",
                })
            self._script = None


def page_paths() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.html")
                  if not any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts))


def origin(value: str) -> str:
    parsed = urlsplit(value)
    if parsed.scheme and parsed.netloc:
        return f"{parsed.scheme.lower()}://{parsed.netloc.lower()}"
    if value.startswith("//"):
        parsed = urlsplit("https:" + value)
        return f"//{parsed.netloc.lower()}"
    return "relative-or-invalid"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, help="Optional JSON report path")
    args = parser.parse_args()

    pages = []
    totals = Counter()
    origin_counts: Counter[str] = Counter()
    for path in page_paths():
        inventory = InventoryParser()
        source = path.read_text(encoding="utf-8")
        inventory.feed(source)
        inventory.close()
        external_origins = sorted({origin(src) for src in inventory.external_scripts})
        for key, value in {
            "inline_executable_scripts": len(inventory.inline_scripts),
            "external_script_tags": len(inventory.external_scripts),
            "inline_event_handlers": sum(inventory.event_handlers.values()),
            "style_attributes": inventory.style_attributes,
            "javascript_urls": len(inventory.javascript_urls),
            "csp_meta_tags": inventory.csp_meta,
            "nonce_attributes": inventory.nonce_attributes,
            "external_scripts_with_sri": inventory.sri_attributes,
        }.items():
            totals[key] += value
        origin_counts.update(external_origins)
        pages.append({
            "page": path.relative_to(ROOT).as_posix(),
            "inline_scripts": inventory.inline_scripts,
            "external_scripts": inventory.external_scripts,
            "external_script_origins": external_origins,
            "inline_event_handlers": dict(sorted(inventory.event_handlers.items())),
            "style_attributes": inventory.style_attributes,
            "javascript_urls": inventory.javascript_urls,
            "csp_meta_tags": inventory.csp_meta,
            "nonce_attributes": inventory.nonce_attributes,
            "external_scripts_with_sri": inventory.sri_attributes,
        })

    report = {
        "report_type": "non_enforcing_csp_compatibility_inventory",
        "scope": "HTML files in the checked-out repository",
        "generated_from": "current working tree",
        "enforcement_enabled": False,
        "summary": {
            "html_pages_scanned": len(pages),
            **dict(sorted(totals.items())),
            "third_party_script_origins": dict(sorted(origin_counts.items())),
        },
        "pages": pages,
        "limitations": [
            "Static source inventory only; runtime-generated DOM and scripts are not observed.",
            "Does not inspect CSS files, response headers, browser execution, or hosting configuration.",
            "CSP hash entries are fingerprints for review, not a ready-to-deploy policy.",
            "Event-handler and style attributes need migration or a carefully reviewed CSP strategy.",
            "No CSP is enabled or changed by this tool."
        ],
    }
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        destination = args.output if args.output.is_absolute() else ROOT / args.output
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
