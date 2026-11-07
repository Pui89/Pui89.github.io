# PUI89 Website Security Policy

## Scope
This policy covers the public PUI89 website repository, static pages, assets, documentation and GitHub Actions workflows. It does not certify the security of any connected product, device or third-party service.

## Report a vulnerability
Do not publish exploitable details, credentials, personal data or attack payloads in public issues. Use GitHub private vulnerability reporting if enabled; otherwise contact the maintainer privately through the official PUI89 GitHub profile. Include the affected URL/file, commit, impact and safe reproduction steps. Allow coordinated remediation before public disclosure.

## Website security baseline
- Treat all user-submitted content, external links, downloaded assets and embedded media as untrusted.
- Avoid collecting sensitive personal data; do not request credentials or confidential case records through public pages or issues.
- Use HTTPS links for external resources; review third-party scripts, fonts, analytics, embeds and QR-code providers before use.
- Prefer static pages and minimise JavaScript, third-party dependencies and external request surfaces.
- Escape and validate any future user-generated content; never render untrusted HTML or execute uploaded files.
- Keep repository and Actions permissions least-privilege; use read-only permissions unless a reviewed workflow needs more.
- Do not expose secrets to untrusted pull-request workflows. Never store credentials in source, pages, workflow files or build logs.
- Review workflow actions, dependencies and downloaded artifacts for provenance and integrity; pin actions to immutable commit SHAs where practical.
- Protect the default branch with pull requests and required checks where repository settings permit.
- Keep a known-good source revision and verify deployment workflow results after changes.

## Incident response
1. Identify affected pages, commits, workflows and deployment runs.
2. Remove public exposure or disable the affected workflow where safe; do not destroy evidence.
3. Revoke exposed credentials and rotate them from a clean device. Do not paste secrets into an issue or chat.
4. Revert to a verified commit or deploy a reviewed fix; inspect recent dependency and workflow changes.
5. Verify the restored site, record the incident and follow up with a prevention change.

## Limitations
Automated checks and this policy reduce risk but cannot guarantee that the website is free of malware, vulnerabilities, compromise or service-provider incidents. No penetration test or security certification is claimed.
