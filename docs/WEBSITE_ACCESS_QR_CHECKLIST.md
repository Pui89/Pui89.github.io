# PUI89 website access, responsive and QR verification

**Rule:** never mark a browser/device check as passed based only on source code. Record the exact page, date, viewport/device, browser, and evidence.

## Automated checks in the Pages workflow

The dependency-free `scripts/check_site.py` checks every HTML file in the repository for:
- HTML parseability, language/title/viewport/H1 metadata gaps, duplicate IDs and missing image alt attributes.
- Broken local page, fragment, stylesheet, script and image references.
- Sitemap URLs that do not map to local site files or use an unexpected canonical host.
- QR PNG file signature/IHDR integrity and QR SVG XML integrity.
- With `--external`, unique external HTTP(S) links using standard-library HTTP requests. A host that blocks automated checks is reported as inconclusive, not as a pass.

The Pages workflow runs these checks on pull requests and main-branch changes. A successful run validates source-level checks only; it does not prove that the deployed site renders correctly.

## Manual browser/device release gate

- [ ] Test the English and Thai homepages at 360px, 390px, 768px, 1024px and 1440px widths.
- [ ] Test all sitemap pages at narrow mobile and desktop widths; check horizontal overflow, clipped headings/cards, nav wrapping, footer and fixed elements.
- [ ] Test keyboard-only navigation, visible focus, skip links, menus, contrast, text zoom and screen-reader names.
- [ ] Test representative current Chrome, Firefox and Safari/ iOS Safari where available.
- [ ] Inspect browser console and network panel for JavaScript errors, failed fonts, missing images, mixed content and 404/403 resources.
- [ ] Confirm both language-switch directions for every bilingual page pair.

## QR release gate

Static QR files are checked for file integrity by CI, but that does **not** decode their payload or prove a camera can scan them.
- [ ] Scan every project QR from a second device at its intended screen and print size.
- [ ] Verify the decoded URL is the exact canonical HTTPS page for that project, not a branch, PR, redirect shortener or stale repository.
- [ ] Confirm the destination loads and its main project/repository link works.
- [ ] Keep a readable text URL beside each QR; do not require a user to scan a QR displayed on the same phone they are using.
- [ ] Recheck the seven project QR codes plus the English/Thai overview QR codes after any destination change.

## Lighthouse / accessibility gate

Use Google's PageSpeed Insights for both Mobile and Desktop on the homepage and each important landing page. It reports Lighthouse Performance, Accessibility, Best Practices and SEO categories; CrUX field data may be unavailable for low-traffic pages. Record report URLs, scores, date and key failed audits. A Lighthouse accessibility score is an automated subset, not proof of WCAG 2.2 conformance.

- Tool: https://pagespeed.web.dev/
- Google PSI methodology: https://developers.google.com/speed/docs/insights/v5/about

## Evidence log template

| Date/time | URL | Device / viewport | Browser | Mobile/desktop Lighthouse | QR scan / destination | Result / issue |
|---|---|---|---|---|---|---|
| Not yet recorded | All pages | Not tested | Not tested | Not run | Not decoded on a second device | Pending |

## Cost and privacy guard

No paid service, API key, subscription, QR shortener, new model or runtime dependency is required for the repository-side checks. PageSpeed Insights is an external Google service; submit only public page URLs. Browser/device and camera checks require an actual device.
