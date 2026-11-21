# PUI89 Google Search Visibility Audit — 2026-11-22

## Executive result

The live English and Thai homepages currently present the correct six-product portfolio. The current live English homepage and Thai homepage both describe PUI89 as an independent, software-first initiative and clearly state that physical prototypes and field performance are not yet established.

A Google search result captured during this audit still displayed an older seven-project portfolio (including Extreme Flood Rescue AI, AI Robot Car and EasyRide AI Motorcycle). The live page differs from that search result. This is consistent with a stale indexed snapshot or search-result snippet, but only Google Search Console URL Inspection can confirm the actual indexed version and last crawl.

**Overall:** the site is publicly accessible and crawlable at the basic robots/sitemap level; the remaining work is metadata consistency, legacy link cleanup and requesting Google to refresh its index after the changes are reviewed and published.

## Scope and evidence

- Audited the GitHub Pages repository `Pui89/Pui89.github.io` on its `main` branch and the public live EN/TH homepages.
- Reviewed all 49 URL entries in `sitemap.xml`; each corresponding HTML source file was present in the repository.
- Checked `robots.txt`, sitemap URL/alternate-language structure, homepage portfolio copy, selected metadata, legacy product links and product-repository security-policy destinations.
- Google public search result: `https://pui89.github.io/` was still represented by an older seven-project result snapshot during this audit.
- Live English homepage: `https://pui89.github.io/` — six current products.
- Live Thai homepage: `https://pui89.github.io/th.html` — six current products.

This is a source and public-page audit, not an authenticated Search Console inspection. Search Console index status, impressions, clicks, crawl errors and ownership cannot be read from the public website alone.

## Findings

### Passed

1. `robots.txt` permits general crawling with `User-agent: * / Allow: /` and advertises `https://pui89.github.io/sitemap.xml`. The separate GPTBot rule does not block general Google crawling.
2. The sitemap contains 49 unique URL entries. 48 entries participate in EN/TH alternate-language pairs; `multimodal-console.html` is the single standalone URL.
3. The current live EN and TH homepages both show the six current products:
   - Coconut Harvest AI
   - PUI89 Sentinel
   - PUI89 AI HOME
   - PUI89 AI NOMAD
   - PUI89 AI Global SUV
   - PUI89 AI Step-Through Scooter
4. The homepage communicates the independent/software-first status and does not claim validated physical robots or field performance.
5. The homepage source includes a Google site-verification meta tag. Its presence does not prove that the property is currently verified in the owner's Search Console account.

### Corrected in this draft

1. Updated the Security & Trust EN/TH pages to link to the current repositories' `SECURITY.md` files for Sentinel, HOME, NOMAD, AI Global SUV and AI Step-Through Scooter. The target files were checked and found on the named repositories. Coconut's link was already current.
2. Corrected the English Materials page description from seven products to six active product projects.
3. Added a Thai meta description to `open-source-resources-th.html`.
4. Corrected the English Technical Visual Standard from seven products to six, updated the NOMAD description to the suitcase-form direction, and updated the scooter name.
5. Added self-canonical and reciprocal EN/TH alternate tags to both Technical Visual Standard pages.
6. Added a concise meta description and self-canonical URL to `multimodal-console.html`. The page remains a single URL with a bilingual interface; it is not represented as a separate Thai URL in the sitemap.
7. Updated `lastmod` in the sitemap for the seven HTML pages changed in this draft. Other dates were left unchanged rather than being artificially advanced.

### Remaining checks / owner actions

1. After reviewing and merging this draft, open Google Search Console for the `https://pui89.github.io/` property.
2. Use URL Inspection on the English and Thai homepages. Compare the indexed version and last crawl date with the live test.
3. Submit or resubmit `https://pui89.github.io/sitemap.xml` in the Sitemaps report.
4. Request indexing for the homepages and the highest-priority updated product, evidence, security and collaboration pages. Google does not guarantee immediate or eventual indexing from a request.
5. Monitor Search performance for branded queries such as `PUI89`, `PUI89 AI`, `Coconut Harvest AI`, `PUI89 Sentinel`, `PUI89 AI HOME`, `PUI89 AI NOMAD`, `PUI89 AI Global SUV` and `PUI89 AI Step-Through Scooter`.
6. Decide whether the single-URL Multimodal Console should remain bilingual at one URL or eventually receive a separate Thai URL. If it remains one bilingual URL, keep the single-URL sitemap entry.

## Draft scope and safety

- Documentation and SEO metadata/link corrections only.
- No homepage redesign, product claims, project scope changes, URL removals, redirects, analytics trackers or external scripts were added.
- No Google Search Console account was accessed; no sitemap was submitted and no indexing request was sent.
- No production `main` branch write, merge or deployment was performed.
- All changes are isolated on the draft branch for review.

## Google guidance

- URL Inspection distinguishes the indexed snapshot from a live test: https://support.google.com/webmasters/answer/9012289
- Requesting a recrawl or submitting a sitemap does not guarantee indexing or immediate search-result changes: https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl
