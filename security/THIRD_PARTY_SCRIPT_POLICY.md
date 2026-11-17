# PUI89 Third-Party JavaScript Supply-Chain Policy

**Scope:** Every HTML page published by the PUI89 GitHub Pages website.
**Default:** Do not load executable JavaScript from third-party origins.

## Why this control exists

A website can be exposed when a trusted analytics, experimentation, tag-management, advertising, support, or other external platform is compromised. A remote script normally executes with the privileges of the page that loads it. HTTPS protects transport; it does not prove that the provider's current script is safe.

## Mandatory rules

1. Prefer first-party, version-controlled JavaScript or no JavaScript where static HTML is sufficient.
2. Do not add third-party script tags without an explicit owner review.
3. Every exception must use an exact HTTPS URL in `third_party_script_allowlist.json`; wildcards and broad host approvals are prohibited.
4. An approved external script must include a valid Subresource Integrity (SRI) hash and `crossorigin="anonymous"`.
5. Each exception must state its owner, purpose, review date, and expiry date. Expired approvals fail CI.
6. Review changes to script URLs, SRI hashes, CSP, HTML templates, JavaScript loaders, analytics, tag managers, and external integrations as security-sensitive.
7. Do not place payment forms, wallet operations, authentication secrets, or sensitive user data on pages that load unreviewed third-party scripts.
8. Do not automatically fetch, install, execute, or update remote JavaScript during the audit.

## CI enforcement

Run:

```sh
python3 scripts/check_third_party_scripts.py
```

The check scans local HTML files and fails on unapproved external script sources, non-HTTPS external script URLs, expired approvals, missing SRI, or missing anonymous CORS mode. It warns about inline executable scripts for manual CSP review.

## Limitations and next gate

This is a source-level guard, not runtime browser enforcement. It cannot detect a compromised first-party file, dynamically injected script paths that are assembled at runtime, DNS/account takeover, or a malicious browser extension. It does not configure HTTP response headers.

Before deploying an enforcing Content Security Policy, inventory all inline scripts, style attributes, images, fonts, frames, and required origins across the complete bilingual site. GitHub Pages does not provide arbitrary response-header configuration through a repository file; a `_headers` file is not assumed to be active. Do not claim CSP enforcement until the actual hosting layer returns and verifies the intended headers.

A passing CI check means only that the checked-out HTML meets this static policy at that commit.
