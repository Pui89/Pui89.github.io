# PUI89 website access and QR verification

**Purpose:** a release checklist for website availability, project navigation, contact routes, mobile layout, and static QR codes. Items are not marked passed until a real browser/device check is recorded.

## Canonical entry point

- Preferred portfolio URL: https://pui89.github.io/
- Custom domain to check separately: https://pui89.com/
- Alternate hostname to check separately: https://www.pui89.com/
- Do not print or publish a QR code until its exact HTTPS destination has been opened and checked.

## Link checks

- [ ] HTTPS canonical URL resolves without a certificate warning.
- [ ] www and apex custom-domain behavior is understood; any redirect ends at the canonical URL.
- [ ] Each project card opens the intended canonical repository:
  - https://github.com/Pui89/Coconut-Harvest-AI
  - https://github.com/Pui89/Extreme-Flood-Rescue-AI
  - https://github.com/Pui89/Multimodal-Narcotics-Screening-AI
- [ ] Contact links have valid destinations and do not expose private information.
- [ ] Broken links, mixed-content resources, missing images, and browser-console errors are checked.

## Mobile and accessibility

- [ ] Test at narrow phone width and desktop width; no horizontal overflow.
- [ ] Navigation and project/contact links are keyboard reachable with visible focus.
- [ ] Every informative image has meaningful alt text; decorative images have empty alt text.
- [ ] Text contrast and tap target size are adequate; links are not distinguished by colour alone.
- [ ] Thai and English copy fit without clipping; language choice is clear if a language switch is provided.

## QR code rules

- Use a static QR code encoding the complete canonical HTTPS URL directly; avoid subscription-dependent dynamic QR services and third-party shorteners.
- Prefer a stable project landing page for project-specific QR codes; do not use a temporary branch, pull-request URL, or tracking-heavy URL.
- Place a readable text URL next to each QR code and provide useful alt text.
- Test scanning from another device, at intended display/print size and contrast. A successful decode is not sufficient: verify the destination and complete the visitor journey.
- Keep QR codes hidden on small/mobile layouts when the person is already using the same device and cannot scan their own screen.

## Verification log template

Record date/time, tester, device/browser, exact URL, HTTP/redirect result, mobile viewport, contact-link result, QR payload, scan result, and outstanding failures. Use NOT TESTED where no actual check was performed; do not infer a pass from the source code alone.

## Cost guard

Prefer direct links, static hosting, and locally generated static QR images. No paid QR subscription, analytics service, or third-party shortener is required.