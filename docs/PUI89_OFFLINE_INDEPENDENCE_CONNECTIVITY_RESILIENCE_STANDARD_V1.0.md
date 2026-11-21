# PUI89 Offline Independence & Connectivity Resilience Standard v1.0

**Status:** approved development standard / proposed engineering requirements. This document does not claim that any product has implemented, tested, certified or validated these capabilities.
**Applies to:** all six active PUI89 products, their printed/digital manuals, packaging, service workflows and the proposed PUI89 Remote Companion.
**Core principle:** **The Product Must Work Without the App. Safety Must Work Without Connectivity.**

## 1. Customer promise and design rule

A customer must be able to access the product's documented basic operation, local controls, essential status and safety procedures without owning a smartphone, installing an app, creating an account, connecting Wi-Fi or accessing the internet. QR codes, websites, cloud services and the Remote Companion are optional enhancements. They must never be the only route to essential instructions, normal local operation, emergency stop, safe shutdown or recovery.

This is an offline-independence design requirement, not a claim that every advanced AI feature or remote service can operate without connectivity. Each product must publish a truthful capability matrix that separates offline functions, local-network functions and internet-dependent optional services.

## 2. Four connectivity levels

| Level | Environment | Required behaviour |
|---|---|---|
| L0 — Fully offline | No smartphone, app, Wi-Fi, Bluetooth, internet or cloud | Printed instructions, physical controls, essential local functions, local safety response and local fault indication remain available. |
| L1 — Direct/local connection | Optional direct Bluetooth, cable or local Wi-Fi connection; no cloud required | Supported local setup, diagnostics or data export may be provided. A smartphone is not mandatory for basic operation. |
| L2 — Internet connected | Internet available | Optional synchronisation, notifications, remote status and approved cloud services may be enabled by the owner. |
| L3 — Remote service | Authenticated service access | Explicitly authorised remote diagnostics/support with least privilege, expiry, revocation and audit. Hazardous remote actuation remains prohibited unless separately engineered and safety-validated. |

L0 is the baseline design target. Failure of a higher level must not silently disable L0 functions.

## 3. Mandatory design requirements

### 3.1 Physical and local human interface
- Provide product-appropriate physical controls for power, start/stop, acknowledgement and emergency stop where relevant to the machine's risk assessment.
- Emergency-stop devices must be physically accessible, clearly labelled and independent of the phone, app, Wi-Fi, internet and cloud.
- Provide local indicators for power, readiness, fault, battery/energy state and connectivity where applicable. Use understandable labels, pictograms, lights, tones or a local display.
- A local stop or safety interlock always takes precedence over a remote request.
- A reset must not automatically restart hazardous motion. Require deliberate re-arming and the prescribed local checks.

### 3.2 Local computation and AI boundaries
- Identify which AI inference and decision-support functions can run on the device's available CPU/GPU/NPU/MCU resources.
- Keep essential product controls and safety monitoring independent of external AI APIs and cloud availability.
- If a model, sensor, storage device or compute resource is unavailable, declare the affected function unavailable; do not fabricate a result or substitute stale output.
- Clearly distinguish local inference, local-only data, optional cloud processing and human-reviewed decisions.
- Define model/version, memory, compute, energy and thermal budgets before claiming offline AI capability.

### 3.3 Safe behaviour on loss of connectivity
- Detect loss of app, Bluetooth, local Wi-Fi, internet, cloud, remote operator or telemetry freshness separately.
- Reject delayed, duplicated, expired, unauthenticated or out-of-order commands. Never execute queued hazardous commands after reconnection.
- Mark remote data with source and last-updated time. Treat stale, missing, conflicting or uncertain state as unknown.
- Disable remote commands when the connection or authentication state is uncertain.
- Transition to the product-specific safe state based on hazard analysis. Do not use one generic response for robots and road vehicles.
- Reconnection must not resume movement or hazardous activity automatically. Require explicit local confirmation where risk assessment demands it.

### 3.4 Local records, recovery and power resilience
- Buffer relevant events and diagnostic records locally with bounded storage, integrity checks and clear retention rules.
- Preserve event ordering and timestamps; disclose clock uncertainty if no trusted time source is available.
- Provide a documented response to storage-full, corrupt-log, low-battery, brownout, sudden power loss and restart.
- Use controlled shutdown, power-loss protection or a safe mechanical state where technically appropriate. Do not promise backup power unless designed and tested.
- After restart, recover into a known safe state; do not replay unsafe commands or automatically resume an interrupted mission.
- Provide an authorised local service/recovery route that does not require a cloud account. Protect service functions against unauthorised use.

### 3.5 Manuals, packaging and accessibility
- Every shipped unit must include a printed, product-specific Quick Start and Safety Guide in the destination-market language. Include essential controls, intended/prohibited use, setup, local operation, stop/emergency-stop, offline behaviour, common faults and support contact details.
- The complete user manual must be available as a printed or otherwise physically supplied offline-readable document, or a clearly identified offline package supplied with the product. It must not require QR, login, app or internet to read.
- QR code and a short human-readable URL are supplementary routes to the current digital manual, updates, app information and support. Never put a QR code in place of essential safety text.
- Provide a downloadable PDF and accessible HTML version, with version, product revision, language, release date and change history.
- Print critical safety information on durable labels on the product where the risk assessment requires it.
- Translation must be reviewed by a native-language technical reviewer and a competent product/safety reviewer. Machine translation alone is not release approval.
- The printed guide must state that the product's basic local functions and safety controls do not require the companion app or internet, where that is true for the released hardware.

### 3.6 Remote Companion boundaries
- Remote Companion is optional. No mandatory account or smartphone requirement for baseline local use.
- The app must show connection state, data freshness, device identity, firmware/software version and unavailable functions clearly.
- Provide manuals and previously downloaded support information offline inside the app, but do not make the app the only source.
- Remote access is opt-in, authenticated, encrypted, per-device authorised, least-privilege, revocable and auditable.
- No remote bypass of emergency stops, interlocks, local enable controls or human supervision.
- No dangerous remote steering, throttle, braking, ignition, cutting, harvesting or unattended robot movement under this standard.
- On loss of connection, stop accepting remote commands and apply the product-specific safe-state design. Do not infer that an internet connection is a safety channel.

## 4. Product-specific offline baseline and loss-of-link response

### Coconut Harvest AI
- Offline baseline: local image import/capture where supported, image-quality checks, local maturity-assessment workflow where model/runtime is available, human review, local result display and local record storage.
- If local AI resources are unavailable, allow manual image review/recording or clearly report the assessment function unavailable.
- Remote loss must not interrupt local safety controls or erase stored work. No remote cutting, harvesting or actuator command. Any future physical harvesting mechanism requires a separate hazard analysis, local enable and validated interlocks.

### PUI89 Sentinel — quadruped inspection robot
- Offline baseline: local operator controls, local stop/emergency stop, local status/fault indication and safe shutdown. Local supervised inspection may continue only if the mission risk assessment, onboard sensing and local operator link permit it.
- Loss of remote link must trigger a defined behaviour such as controlled stop, hold, return-to-safe-point or another validated response for the specific environment; do not assume return-to-home is always safe.
- No unattended hazardous movement or remote override of local safety controls.

### PUI89 AI HOME — indoor assistant
- Offline baseline: local start/stop, local safety sensing/control that is actually implemented, local status and essential user interaction. A phone or home Wi-Fi outage must not disable the physical stop or make the robot move unpredictably.
- On communication loss, stop or hold mobility as defined by the indoor hazard analysis; preserve locally available essential sensing/alerts. No movement into occupied or unsafe areas based solely on remote commands.

### PUI89 AI NOMAD — mobile assistant
- Offline baseline: local power/stop, physical handling and transport use, local status and safe mobility control if a powered mobility version is implemented.
- Loss of remote link must not cause runaway movement. Stop/hold or another validated safe response; retain local manual handling and safe shutdown.
- No unattended hazardous remote driving. Travel/location sharing is optional and permission-controlled.

### PUI89 AI Global SUV
- Offline baseline: the vehicle's certified/approved primary driving controls, braking, steering, lighting and required safety systems must not depend on the companion app or internet. AI features must fail visibly and safely without compromising the driver’s control.
- Loss of connectivity must not cause automatic emergency braking, steering, throttle or propulsion changes solely because remote access was lost.
- No remote steering, throttle, braking, gear selection, ignition or motion activation through the companion app under this standard.

### PUI89 AI Step-Through Scooter
- Offline baseline: normal rider-operated vehicle controls and required safety functions must be independent of the app and internet. AI assistance may become unavailable with a clear local indication.
- Loss of connectivity must not cause unexpected throttle, steering, braking, ignition or motion activation.
- No remote throttle, steering, braking, ignition or unattended movement under this standard.

## 5. Mandatory failure-injection and acceptance tests

Each product must create a hazard-based test plan and record the exact hardware, firmware, software, model and configuration tested. At minimum test:
1. Operate without a smartphone or app installed.
2. Operate with Wi-Fi, Bluetooth and internet disabled.
3. Remove internet during startup, normal operation and shutdown.
4. Kill the app and disconnect remote service during an active task.
5. Inject stale, duplicated, delayed, expired and out-of-order remote messages.
6. Reconnect after link loss and verify no unsafe automatic resume or command replay.
7. Trigger local stop and emergency stop with all radios disabled.
8. Test low battery, brownout, sudden power loss and controlled restart.
9. Test full storage, corrupted local records and recovery.
10. Test missing sensor, failed sensor, unavailable model and compute/thermal limit.
11. Verify local fault indicators and printed troubleshooting steps.
12. Verify the complete manual can be read with no phone, QR scan, login or internet.
13. Verify printed quick-start, language, QR destination and short URL against the released product revision.
14. Conduct usability tests with intended users, including users unfamiliar with apps and users with limited connectivity.

Acceptance evidence must include test procedure, expected result, actual result, logs or observation, build/configuration ID, tester, date, unresolved defects and approval. A checklist in documentation is not proof that a test passed.

## 6. Release gates and evidence status

Do not claim a product is offline-capable, fail-safe, tested, certified or ready for sale until its applicable requirements are implemented and evidence is reviewed. Track each requirement as **planned**, **specified**, **implemented**, **tested**, **validated** or **not applicable**, with rationale and evidence reference.

Minimum release gates:
- Product offline capability matrix approved.
- Hazard analysis and product-specific safe states approved.
- Local controls and independent emergency-stop path verified where applicable.
- Offline user journey demonstrated without a smartphone or network.
- Connectivity-loss and recovery tests passed.
- Printed manual and safety guide approved in launch languages.
- App is demonstrably optional for basic use.
- Data, privacy, cybersecurity, service and country-specific regulatory reviews completed.
- Open safety-critical defects resolved before release.

## 7. Ownership and controlled change

The website portfolio standard defines shared minimum requirements. Each product repository owns its product-specific requirements, hazard analysis, interface design, tests and evidence. Shared AI Core may provide reusable contracts and test utilities but must not replace product-level safety engineering. Changes to hardware, firmware, model, radio, app, packaging or supported market trigger an impact review and manual/version update.

## 8. Customer-facing wording

Use only when true for the exact released product:
- “Works without the companion app for supported basic local functions.”
- “Essential controls and safety functions do not require an internet connection.”
- “QR code and online services are optional ways to access additional information.”
- “Remote features require a compatible connection and are not required for local operation.”

Never say “fully offline”, “fail-safe”, “all functions work offline” or “internet-independent AI” without product-specific test evidence.
