#!/usr/bin/env python3
"""Small dependency-free checks for the PUI89 static portfolio site."""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = [ROOT / "index.html", ROOT / "th.html", ROOT / "404.html"]
MARKDOWN_FILES = [
    ROOT / "README.md",
    ROOT / "GROWTH_ROADMAP.md",
    ROOT / "RESEARCH_PORTFOLIO.md",
    ROOT / "MARKET_AND_PRODUCT_STRATEGY.md",
    ROOT / "INNOVATION_STRATEGY.md",
    ROOT / "DIFFERENTIATION_STRATEGY.md",
    ROOT / "PRODUCT_QUALITY_AND_BENCHMARK_STANDARD.md",
    ROOT / "TRUST_QUALITY_CUSTOMER_VALUE.md",
    ROOT / "COCONUT_ORCHARD_PILOT_BRIEF.md",
    ROOT / "PRODUCT_STATUS.md",
]


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_map = dict(attrs)
        for key in ("href", "src"):
            value = attrs_map.get(key)
            if value:
                self.links.append(value)
        element_id = attrs_map.get("id")
        if element_id:
            self.ids.add(element_id)
        name = attrs_map.get("name")
        if tag == "a" and name:
            self.ids.add(name)


def local_target(link: str) -> tuple[Path | None, str | None]:
    parsed = urlparse(link.strip())
    if parsed.scheme or parsed.netloc or link.startswith(("mailto:", "tel:", "data:")):
        return None, None
    path = unquote(parsed.path)
    fragment = unquote(parsed.fragment)
    target = (ROOT / path.lstrip("/")) if path else None
    return target, fragment or None


def main() -> int:
    errors: list[str] = []
    for path in HTML_FILES + MARKDOWN_FILES:
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"Required file missing or empty: {path.relative_to(ROOT)}")

    html_ids: dict[Path, set[str]] = {}
    for path in HTML_FILES:
        if not path.is_file():
            continue
        parser = LinkCollector()
        parser.feed(path.read_text(encoding="utf-8"))
        html_ids[path] = parser.ids
        for link in parser.links:
            target, fragment = local_target(link)
            if target is None:
                continue
            if not target.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken local link/asset {link!r}")
            elif fragment and target.suffix.lower() in {".html", ".htm"}:
                target_ids = html_ids.get(target)
                if target_ids is None:
                    target_parser = LinkCollector()
                    target_parser.feed(target.read_text(encoding="utf-8"))
                    target_ids = target_parser.ids
                    html_ids[target] = target_ids
                if fragment not in target_ids:
                    errors.append(f"{path.relative_to(ROOT)}: missing fragment {link!r}")

    markdown_link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for path in MARKDOWN_FILES:
        if not path.is_file():
            continue
        source = path.read_text(encoding="utf-8")
        for match in markdown_link_pattern.finditer(source):
            link = match.group(1).strip().split()[0].strip("<>")
            target, _ = local_target(link)
            if target is not None and not target.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken local link {link!r}")

    if (ROOT / "index.html").is_file():
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        for required in (
            'name="description"',
            'name="viewport"',
            'id="main-content"',
            "Coconut Harvest AI",
            "Flood Rescue AI",
            "Multimodal Screening AI",
            "SAFETY_AND_RESILIENCE.md",
            "PRODUCT_STATUS.md",
            'id="coconut"',
            'id="collaborate"',
            'id="contact"',
        ):
            if required not in html:
                errors.append(f"index.html is missing expected content: {required}")

    # Validate the English and Thai homepages as one bilingual release unit.
    localized_pages = {
        "index.html": {
            "language": '<html lang="en">',
            "theme": '<meta name="theme-color" content="#14251c">',
            "qr_asset": 'src="images/pui89-english-qr.svg"',
            "qr_target": 'href="https://pui89.github.io/"',
        },
        "th.html": {
            "language": '<html lang="th">',
            "theme": '<meta name="theme-color" content="#14251c">',
            "qr_asset": 'src="images/pui89-thai-qr.svg"',
            "qr_target": 'href="https://pui89.github.io/th.html"',
        },
    }
    for filename, required_values in localized_pages.items():
        path = ROOT / filename
        if not path.is_file():
            continue
        source = path.read_text(encoding="utf-8")
        for label, value in required_values.items():
            if value not in source:
                errors.append(f"{filename} is missing or has incorrect {label}: {value}")
        if r"\n" in source:
            errors.append(f"{filename} contains a literal escaped newline sequence")
        if 'id="share"' not in source:
            errors.append(f"{filename} is missing its QR sharing section")

    thai_path = ROOT / "th.html"
    if thai_path.is_file():
        thai_source = thai_path.read_text(encoding="utf-8")
        if 'href="growth.html"' in thai_source:
            errors.append("th.html navigation must link to the Thai growth page, not growth.html")
        if thai_source.count('href="growth-th.html"') != 1:
            errors.append("th.html must contain exactly one Thai growth-roadmap navigation link")

    english_path = ROOT / "index.html"
    if english_path.is_file():
        english_source = english_path.read_text(encoding="utf-8")
        if english_source.count('href="growth.html"') != 1:
            errors.append("index.html must contain exactly one English growth-roadmap navigation link")
    if errors:
        print("Portfolio site checks FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Portfolio site checks passed.")
    print("Checked required files, local HTML assets/links, HTML fragments, Markdown links, and key homepage content.")
    print("External links and the live GitHub Pages deployment are not tested by this script.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
