#!/usr/bin/env python3
"""Dependency-free static and external-link QA for the PUI89 GitHub Pages site.

Run: python3 scripts/check_site.py
Run with public-link checks: python3 scripts/check_site.py --external
The script does not render pages, decode QR payloads, or replace manual device testing.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_HOST = "pui89.github.io"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__"}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.ids: list[str] = []
        self.images_without_alt: list[str] = []
        self.images = 0
        self.title_seen = False
        self.viewport_seen = False
        self.lang = ""
        self.h1_count = 0
        self._in_title = False
        self.title_text = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        tag = tag.lower()
        if tag == "html":
            self.lang = (a.get("lang") or "").strip()
        if tag == "title":
            self.title_seen = True
            self._in_title = True
        if tag == "meta" and (a.get("name") or "").lower() == "viewport":
            self.viewport_seen = True
        if tag == "h1":
            self.h1_count += 1
        if "id" in a and a["id"]:
            self.ids.append(a["id"])
        for attr in ("href", "src", "action", "poster"):
            value = a.get(attr)
            if value:
                self.links.append(value.strip())
        if a.get("srcset"):
            for candidate in a["srcset"].split(","):
                value = candidate.strip().split()
                if value:
                    self.links.append(value[0])
        if tag == "img":
            self.images += 1
            if "alt" not in a:
                self.images_without_alt.append(a.get("src") or "(image without src)")

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_text += data.strip()


def all_html_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.html")
        if not any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts)
    )


def resolve_local(source: Path, raw_url: str) -> tuple[Path | None, str | None]:
    value = raw_url.strip()
    if not value or value.startswith(("data:", "blob:", "javascript:", "mailto:", "tel:")):
        return None, None
    parsed = urllib.parse.urlsplit(value)
    if parsed.scheme or parsed.netloc:
        return None, None
    path = urllib.parse.unquote(parsed.path)
    target = (ROOT / path.lstrip("/")) if path.startswith("/") else (source.parent / path)
    if not path:
        target = source
    target = target.resolve()
    try:
        target.relative_to(ROOT.resolve())
    except ValueError:
        return None, None
    if target.is_dir():
        target = target / "index.html"
    return target, urllib.parse.unquote(parsed.fragment) or None


def parse_page(path: Path) -> tuple[PageParser | None, str | None]:
    parser = PageParser()
    try:
        parser.feed(path.read_text(encoding="utf-8"))
        parser.close()
        return parser, None
    except Exception as exc:
        return None, str(exc)


def check_external(url: str) -> dict[str, str]:
    request_url = urllib.parse.urldefrag(url)[0]
    headers = {"User-Agent": "PUI89-Website-QA/1.0 (+https://pui89.github.io/)"}
    last_error = ""
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(request_url, headers=headers, method=method)
        if method == "GET":
            req.add_header("Range", "bytes=0-1023")
        try:
            with urllib.request.urlopen(req, timeout=12) as response:
                status = response.status
                if status < 400:
                    return {"url": url, "status": str(status), "result": "pass"}
                last_error = f"HTTP {status}"
                if status not in (403, 405, 501):
                    break
        except urllib.error.HTTPError as exc:
            last_error = f"HTTP {exc.code}"
            if exc.code not in (403, 405, 501):
                if exc.code in (429,) or exc.code >= 500:
                    return {"url": url, "status": str(exc.code), "result": "inconclusive"}
                return {"url": url, "status": str(exc.code), "result": "fail"}
        except Exception as exc:
            last_error = type(exc).__name__ + ": " + str(exc)[:180]
            break
    return {"url": url, "status": last_error or "unknown", "result": "inconclusive"}


def main() -> int:
    argp = argparse.ArgumentParser()
    argp.add_argument("--external", action="store_true", help="check unique public HTTP(S) links")
    args = argp.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    pages = all_html_files()
    parsers: dict[Path, PageParser] = {}
    external_urls: set[str] = set()
    local_link_count = 0
    image_count = 0
    metadata_gaps = Counter()

    if not pages:
        errors.append("No HTML pages found.")

    for page in pages:
        parser, parse_error = parse_page(page)
        if parse_error:
            errors.append(f"{page.relative_to(ROOT)}: HTML parse error: {parse_error}")
            continue
        assert parser is not None
        parsers[page] = parser
        image_count += parser.images
        rel = page.relative_to(ROOT).as_posix()

        if not parser.lang:
            metadata_gaps["missing_lang"] += 1
            warnings.append(f"{rel}: missing html lang attribute")
        if not parser.title_seen or not parser.title_text:
            metadata_gaps["missing_title"] += 1
            warnings.append(f"{rel}: missing or empty title")
        if not parser.viewport_seen:
            metadata_gaps["missing_viewport"] += 1
            warnings.append(f"{rel}: missing viewport meta")
        if parser.h1_count == 0:
            metadata_gaps["missing_h1"] += 1
            warnings.append(f"{rel}: no H1 heading")
        elif parser.h1_count > 1:
            warnings.append(f"{rel}: {parser.h1_count} H1 headings; review heading hierarchy")
        if parser.images_without_alt:
            for src in parser.images_without_alt:
                errors.append(f"{rel}: image missing alt attribute: {src}")

        duplicates = [item for item, count in Counter(parser.ids).items() if count > 1]
        for duplicate in duplicates:
            errors.append(f"{rel}: duplicate id {duplicate!r}")

        for raw in parser.links:
            parsed = urllib.parse.urlsplit(raw)
            if parsed.scheme.lower() in ("http", "https") and parsed.netloc:
                external_urls.add(urllib.parse.urldefrag(raw)[0])
                continue
            target, fragment = resolve_local(page, raw)
            if target is None:
                continue
            local_link_count += 1
            if not target.exists() or not target.is_file():
                errors.append(f"{rel}: missing local target {raw!r}")
                continue
            if fragment and target.suffix.lower() in (".html", ".htm"):
                target_parser = parsers.get(target)
                if target_parser is None:
                    target_parser, target_error = parse_page(target)
                    if target_parser is None:
                        errors.append(f"{rel}: cannot parse fragment target {raw!r}: {target_error}")
                        continue
                    parsers[target] = target_parser
                if fragment not in target_parser.ids:
                    errors.append(f"{rel}: missing fragment target {raw!r}")

    # Verify every sitemap URL points to a local page in this repository.
    sitemap = ROOT / "sitemap.xml"
    sitemap_count = 0
    if not sitemap.is_file():
        errors.append("sitemap.xml is missing")
    else:
        try:
            root = ET.parse(sitemap).getroot()
            for loc in root.findall(".//{*}loc"):
                if not loc.text:
                    continue
                sitemap_count += 1
                parsed = urllib.parse.urlsplit(loc.text.strip())
                if parsed.scheme != "https" or parsed.netloc.lower() != SITE_HOST:
                    errors.append(f"sitemap.xml: unexpected canonical URL {loc.text!r}")
                    continue
                path = urllib.parse.unquote(parsed.path).lstrip("/") or "index.html"
                target = ROOT / path
                if not target.is_file():
                    errors.append(f"sitemap.xml: URL has no matching local file: {loc.text!r}")
        except Exception as exc:
            errors.append(f"sitemap.xml: invalid XML: {exc}")

    # Check QR asset files are present and structurally readable. Payload decoding
    # still requires an actual QR decoder or scan with a second device.
    qr_dir = ROOT / "qr"
    qr_assets = sorted(p for p in qr_dir.glob("*") if p.is_file()) if qr_dir.is_dir() else []
    png_count = svg_count = 0
    for path in qr_assets:
        if path.suffix.lower() == ".png":
            png_count += 1
            try:
                data = path.read_bytes()
                if len(data) < 33 or data[:8] != PNG_SIGNATURE or data[12:16] != b"IHDR":
                    errors.append(f"qr/{path.name}: invalid or incomplete PNG structure")
                else:
                    width = int.from_bytes(data[16:20], "big")
                    height = int.from_bytes(data[20:24], "big")
                    if width < 1 or height < 1:
                        errors.append(f"qr/{path.name}: invalid image dimensions")
            except OSError as exc:
                errors.append(f"qr/{path.name}: cannot read image: {exc}")
        elif path.suffix.lower() == ".svg":
            svg_count += 1
            try:
                ET.parse(path)
            except Exception as exc:
                errors.append(f"qr/{path.name}: invalid SVG/XML: {exc}")
    if not qr_assets:
        warnings.append("No files found in qr/; confirm QR assets are stored elsewhere.")

    external_report: list[dict[str, str]] = []
    if args.external and external_urls:
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            external_report = list(pool.map(check_external, sorted(external_urls)))
        for item in external_report:
            if item["result"] == "fail":
                errors.append(f"External link failed ({item['status']}): {item['url']}")
            elif item["result"] == "inconclusive":
                warnings.append(f"External link could not be verified ({item['status']}): {item['url']}")

    report = {
        "site": "https://pui89.github.io/",
        "html_pages_checked": len(pages),
        "local_references_checked": local_link_count,
        "images_checked": image_count,
        "sitemap_entries_checked": sitemap_count,
        "qr_assets_checked": len(qr_assets),
        "qr_png_files": png_count,
        "qr_svg_files": svg_count,
        "external_links_found": len(external_urls),
        "external_links_tested": len(external_report),
        "external_link_results": {
            key: sum(1 for item in external_report if item["result"] == key)
            for key in ("pass", "fail", "inconclusive")
        },
        "metadata_gaps": dict(metadata_gaps),
        "errors": errors,
        "warnings": warnings,
        "status": "failed" if errors else "passed_with_warnings" if warnings else "passed",
        "limitations": [
            "Static source checks do not render pages at mobile or desktop viewport sizes.",
            "PNG structure checks do not decode QR payloads; scan each code with a second device.",
            "External hosts may block automated requests; inconclusive results need manual review.",
            "No Lighthouse or full WCAG 2.2 audit is run by this dependency-free script."
        ]
    }
    report_text = json.dumps(report, indent=2, ensure_ascii=False)
    (ROOT / "pui89-site-qa-report.json").write_text(report_text + "\\n", encoding="utf-8")
    print(report_text)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
