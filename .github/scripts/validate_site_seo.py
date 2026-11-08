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

# Only indexable HTML pages belong in the sitemap. Legacy compatibility
# redirects marked noindex,follow must remain reachable for old bookmarks,
# but should not be submitted as canonical search results.
indexable_html = set()
for page in Path(".").glob("*.html"):
    if page.name == "404.html":
        continue
    content = page.read_text(encoding="utf-8")
    robots = re.search(r"""<meta\s+name=["']robots["']\s+content=["']([^"']+)["']""", content, re.I)
    if robots and "noindex" in robots.group(1).lower():
        if page.name in sitemap_paths:
            errors.append(f"{page.name}: noindex page must not appear in sitemap")
        continue
    indexable_html.add(page.name)

missing = sorted(indexable_html - sitemap_paths)
extra = sorted(sitemap_paths - indexable_html)
if missing:
    errors.append("Indexable HTML pages missing from sitemap: " + ", ".join(missing))
if extra:
    errors.append("Sitemap paths are not indexable HTML pages: " + ", ".join(extra))

if not ROBOTS.is_file() or f"Sitemap: {ROOT}/sitemap.xml" not in ROBOTS.read_text(encoding="utf-8"):
    errors.append("robots.txt must reference the canonical sitemap URL")

# Every indexable page in the sitemap must expose basic discovery metadata.
for filename in sorted(indexable_html):
    content = Path(filename).read_text(encoding="utf-8")
    if not re.search(r'<title>\s*[^<]+\s*</title>', content, re.I):
        errors.append(f"{filename}: missing title")
    if not re.search(r'<meta\s+name=["\']description["\']\s+content=["\'][^"\']+["\']', content, re.I):
        errors.append(f"{filename}: missing meta description")
    if not re.search(r'<meta\s+name=["\']robots["\']\s+content=["\']index,\s*follow["\']', content, re.I):
        errors.append(f"{filename}: missing explicit index,follow directive")
    canonical = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', content, re.I)
    expected = ROOT + ("/" + filename if filename != "index.html" else "/")
    if not canonical or canonical.group(1) != expected:
        errors.append(f"{filename}: missing or incorrect canonical URL")

if errors:
    for error in errors:
        print("FAIL:", error)
    raise SystemExit(1)
print(f"PASS: sitemap XML, {len(sitemap_paths)} indexable HTML URLs, robots.txt, and page-level SEO metadata.")
print("NOTE: This validates repository files only; Google crawling, indexing, and ranking must be checked in Search Console.")
