#!/usr/bin/env python3
"""Validate PUI89's public sitemap and the recently completed SEO page pairs.

Uses only Python's standard library. It does not contact Google or claim indexing.
"""
from datetime import date
from pathlib import Path
from urllib.parse import urlparse
import re
import xml.etree.ElementTree as ET

ROOT = "https://pui89.github.io"
SITEMAP = Path("sitemap.xml")
ROBOTS = Path("robots.txt")
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
errors = []

if not SITEMAP.is_file():
    raise SystemExit("FAIL: sitemap.xml is missing")
try:
    tree = ET.parse(SITEMAP)
except ET.ParseError as exc:
    raise SystemExit(f"FAIL: sitemap.xml is invalid XML: {exc}")

entries = tree.findall("sm:url", NS)
sitemap_paths = set()
for entry in entries:
    loc = entry.findtext("sm:loc", default="", namespaces=NS)
    lastmod = entry.findtext("sm:lastmod", default="", namespaces=NS)
    parsed = urlparse(loc)
    if parsed.scheme != "https" or parsed.netloc != "pui89.github.io":
        errors.append(f"Invalid sitemap URL: {loc}")
        continue
    path = parsed.path.lstrip("/") or "index.html"
    if parsed.query or parsed.fragment:
        errors.append(f"Unexpected query or fragment in sitemap URL: {loc}")
    if not Path(path).is_file():
        errors.append(f"Sitemap URL has no matching file: {loc}")
    sitemap_paths.add(path)
    if lastmod:
        try:
            date.fromisoformat(lastmod)
        except ValueError:
            errors.append(f"Invalid lastmod date for {loc}: {lastmod}")

expected_html = {p.name for p in Path(".").glob("*.html") if p.name != "404.html"}
missing = sorted(expected_html - sitemap_paths)
extra = sorted(sitemap_paths - expected_html)
if missing:
    errors.append("Public HTML pages missing from sitemap: " + ", ".join(missing))
if extra:
    errors.append("Sitemap paths not matching public HTML pages: " + ", ".join(extra))

if not ROBOTS.is_file() or f"Sitemap: {ROOT}/sitemap.xml" not in ROBOTS.read_text(encoding="utf-8"):
    errors.append("robots.txt must reference the canonical sitemap URL")

# These four pages were newly brought into the sitemap and need complete
# reciprocal English/Thai discovery metadata.
pairs = {
    "development.html": ("en", ROOT + "/development.html", ROOT + "/development-th.html"),
    "development-th.html": ("th", ROOT + "/development-th.html", ROOT + "/development.html"),
    "security.html": ("en", ROOT + "/security.html", ROOT + "/security-th.html"),
    "security-th.html": ("th", ROOT + "/security-th.html", ROOT + "/security.html"),
}
for filename, (language, canonical, peer) in pairs.items():
    content = Path(filename).read_text(encoding="utf-8")
    if not re.search(r"<title>\s*[^<]+\s*</title>", content, re.I):
        errors.append(f"{filename}: missing title")
    if not re.search(r'<meta\s+name="description"\s+content="[^"]+"', content, re.I):
        errors.append(f"{filename}: missing meta description")
    if f'<meta name="robots" content="index,follow">' not in content:
        errors.append(f"{filename}: missing index,follow directive")
    if f'<link rel="canonical" href="{canonical}">' not in content:
        errors.append(f"{filename}: incorrect canonical URL")
    expected_en = canonical if language == "en" else peer
    expected_th = canonical if language == "th" else peer
    for lang, href in (("en", expected_en), ("th", expected_th), ("x-default", ROOT + "/development.html" if filename.startswith("development") else ROOT + "/security.html")):
        if f'<link rel="alternate" hreflang="{lang}" href="{href}">' not in content:
            errors.append(f"{filename}: missing or incorrect {lang} alternate")

if errors:
    for error in errors:
        print("FAIL:", error)
    raise SystemExit(1)
print(f"PASS: sitemap XML, {len(sitemap_paths)} public HTML URLs, robots.txt, and four bilingual SEO page pairs.")
print("NOTE: This validates repository files only; Google crawling, indexing, and ranking must be checked in Search Console.")
