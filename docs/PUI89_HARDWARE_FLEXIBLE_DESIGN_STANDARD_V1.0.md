# PUI89 Hardware-Flexible Design Standard v1.0

**Status:** Proposed engineering standard  
**Applies to:** Coconut Harvest AI, PUI89 Sentinel, AI HOME, AI NOMAD, AI Global SUV, AI Step-Through Scooter  
**Purpose:** Keep each product developable when a preferred component is unavailable, unaffordable, unsupported, delayed, or discontinued.

> Design around required capabilities and stable interfaces, not around one specific vendor or part number.

## 1. Core rule

No single non-essential hardware part should become a project-wide blocker. For every hardware-dependent capability, document:
1. Preferred component or architecture.
2. Compatible alternative(s).
3. Low-cost prototype option.
4. Temporary substitute for continued development.
5. No-hardware path, such as simulation, recorded data, synthetic fixtures, or manual input.
6. The capability lost or degraded by each substitution.
7. Verification required before the substitute can be used in a real product.

A fallback is not automatically equivalent. Never represent simulated, recorded, manually entered, or lower-performance data as live sensor capability.

## 2. Component status vocabulary

Use exactly one status per candidate:
- **Installed & verified** — physically installed and passed the named verification.
- **Installed, not verified** — physically present, but not yet validated.
- **Selected, not purchased** — chosen for a design, not acquired.
- **Candidate** — under evaluation; no selection commitment.
- **Alternative** — possible substitute, compatibility not yet proven.
- **Temporary development substitute** — only for development, not approved for operational use.
- **Simulation / recorded-data only** — no live hardware capability.
- **Unavailable** — cannot currently be sourced or used.
- **Not applicable** — capability is not required for this product.

Never use “supported”, “available”, “working”, or “validated” without evidence and a defined test.

## 3. Hardware registry record

Create one record for every required hardware function with these fields:

| Field | Required information |
|---|---|
| Product / subsystem | Which product and subsystem use it |
| Required capability | User or engineering outcome, not a brand name |
| Component class | Camera, IMU, range sensor, compute, actuator, display, etc. |
| Preferred candidate | Exact model only when researched |
| Alternatives | Other candidates and their differences |
| Development substitute | Simulation, dataset, manual fixture, or none |
| Interfaces | USB, CSI, Ethernet, UART, I2C, SPI, CAN, GPIO, etc. |
| Electrical needs | Voltage, current, peak load, connector, protection |
| Compute needs | CPU/GPU/NPU/MCU, RAM, storage, bandwidth |
| Mechanical needs | Size, mass, mounting, vibration, ingress protection |
| Software support | OS, driver, SDK, licence, maintenance status |
| Cost / sourcing | Price, seller, country, lead time, source date |
| Limitations | Range, field of view, lighting, weather, latency, precision |
| Failure response | Detect failure, report uncertainty, safe fallback |
| Status / evidence | Status vocabulary above, test record, date, reviewer |

Do not fill price, availability, driver support, or compatibility from assumptions. Mark unknown fields **Not yet researched**.

## 4. Design for replaceability

- Define a product-owned interface between hardware drivers and the shared AI Core.
- Keep vendor-specific SDK calls inside replaceable adapters.
- Normalize sensor data into timestamped observations with units, coordinate frame, calibration state, provenance, and quality.
- Keep actuator commands behind product-specific safety controllers and validated limits.
- Separate sensing, perception, decision support, user interaction, and actuation.
- Make optional sensors truly optional in configuration; missing optional hardware must not crash the product.
- On missing or stale critical sensors, explicitly degrade capability, show the reason, and inhibit unsafe actions.
- Do not silently substitute one sensor modality for another.
- Avoid unnecessary sensor duplication; justify each component by coverage, reliability, or safety need.
- Prefer documented, maintainable interfaces and replaceable mounts/cables.

## 5. Six product baseline capability maps

These are planning profiles, not selected or installed hardware.

### 5.1 Coconut Harvest AI

| Capability | Preferred class to evaluate | Alternatives / development path | Key limitation to disclose |
|---|---|---|---|
| Fruit and canopy image capture | RGB camera | Different USB/CSI/network RGB camera; recorded licensed images | Image quality depends on optics, light, distance, motion |
| Maturity classification | RGB image pipeline | Human-labelled images; recorded-data evaluation | Not a hardware sensor; accuracy requires representative labels and testing |
| Distance / spatial context | Depth camera or stereo | ToF or ultrasonic for limited point/range tasks; manual measured setup; simulation | Alternatives do not provide equivalent dense 3D information |
| Illumination | Controlled visible lighting | Diffuse lamps / daylight capture protocol | Weather and shadows can change image quality |
| Edge processing | CPU-first computer | Lower-power SBC/desktop during development; offline batch processing | Throughput and latency may change |
| Operator interaction | Local screen, physical controls, audio/light as fitted | Laptop/local operator station during prototype | Prototype station is not proof of final integrated interface |

No harvesting mechanism or autonomous cutting capability is implied by this profile.

### 5.2 PUI89 Sentinel — quadruped inspection robot

| Capability | Preferred class to evaluate | Alternatives / development path | Key limitation to disclose |
|---|---|---|---|
| Scene perception | RGB camera | USB/CSI/network camera; recorded inspection data | No depth from a single RGB image without additional estimation |
| Range / obstacle awareness | 2D/3D LiDAR or depth camera | Stereo, ToF, ultrasonic for constrained zones; simulation | Different range, resolution, sunlight and surface limitations |
| Motion state | IMU | Alternative IMU module; simulated motion logs | Calibration, drift, vibration and mounting orientation matter |
| Localization | LiDAR/camera/IMU fusion with suitable platform support | Fiducials, mapped test area, operator-supervised localization | GNSS may fail indoors or near structures; no universal substitute |
| Environmental monitoring | Product-specific temperature, humidity, gas or other sensor | Separate sensor modules; omit unsupported hazards | A sensor detects only specified substances/ranges; never claim general chemical detection |
| Robot mobility | Platform-specific motor drivers and actuators | Bench rig, hardware-in-loop or simulator | A substitute actuator is not field-operational approval |

Do not claim quadruped mobility, autonomous navigation, or hazard detection until the complete platform is built and tested.

### 5.3 PUI89 AI HOME — indoor assistant

| Capability | Preferred class to evaluate | Alternatives / development path | Key limitation to disclose |
|---|---|---|---|
| Human/object scene input | RGB camera | Different camera; recorded indoor scenes | Privacy, lighting, occlusion |
| Near-field obstacle detection | ToF / depth / proximity sensors | Ultrasonic or contact bumper in constrained roles | No single low-cost sensor covers all materials and geometries |
| Motion / tilt state | IMU | Lower-cost IMU; stationary prototype without motion functions | Not a substitute for obstacle sensing |
| Indoor localization | Camera/depth/odometry fusion | Fiducials, mapped test space, supervised manual positioning | Wheel slip and changing furniture affect localization |
| Mobility | Wheel motors, encoders, motor controller | Static mock-up or bench motor test | Bench testing does not validate human-safe mobile operation |
| User interaction | Integrated display and physical controls | Local laptop/operator console during development | Final product must remain usable without a phone |

Respect the current HOME target envelope: 8 kg target, 10 kg maximum; verify all component mass and power budgets against it.

### 5.4 PUI89 AI NOMAD — outdoor/mobile assistant

| Capability | Preferred class to evaluate | Alternatives / development path | Key limitation to disclose |
|---|---|---|---|
| Outdoor scene perception | RGB camera with suitable optics/protection | Different weather-protected camera; recorded outdoor data | Rain, glare, dust, low light and lens contamination |
| Obstacle/range awareness | Depth or LiDAR class sensor | Stereo, ToF, ultrasonic for limited zones; simulation | Outdoor sunlight and surface reflectivity affect modalities differently |
| Motion state | IMU and wheel odometry | Alternative IMU/encoder; recorded logs | Drift, wheel slip and vibration |
| Outdoor localization | GNSS plus visual/odometry fusion where appropriate | Fiducial or mapped-site supervised trials | GNSS is not reliable in every environment |
| Environmental protection | Enclosure, connectors, thermal monitoring | Prototype enclosure and controlled test | IP rating must be tested/certified, not assumed from appearance |
| Mobility | Four-wheel drive platform and motor control | Static mock-up, bench rig, simulator | No outdoor autonomy claim without validated braking, traction and stability |

Respect the NOMAD target envelope: 8–10 kg target, 10 kg maximum. Keep it distinct from AI HOME.

### 5.5 PUI89 AI Global SUV

| Capability | Preferred class to evaluate | Alternatives / development path | Key limitation to disclose |
|---|---|---|---|
| Forward scene awareness | Automotive-grade camera; radar where justified | Camera-only prototype, recorded driving datasets | Camera-only is not equivalent to radar and is not a safety-rated ADAS |
| Rear awareness | Rear camera and/or parking sensors | Camera or proximity sensors in a limited prototype role | A camera does not measure distance reliably in all conditions |
| Side awareness | Side cameras / radar / proximity sensors | Mirrors and driver observation for non-automated concept studies | Do not imply a blind-spot warning function without validated coverage |
| Vehicle state | Read-only vehicle data interface | Bench CAN simulator or synthetic data | Never inject commands into vehicle control systems during early prototypes |
| Position / navigation context | GNSS and map data | Recorded routes / simulated position | Position accuracy and map freshness vary |
| Driver information | Integrated display, tones and status lights | Bench display / local development console | Driver retains control; AI is advisory |

Do not connect prototype AI directly to throttle, steering, braking, or other safety-critical vehicle controls.

### 5.6 PUI89 AI Step-Through Scooter

| Capability | Preferred class to evaluate | Alternatives / development path | Key limitation to disclose |
|---|---|---|---|
| Forward road awareness | Road-facing camera | Alternative camera; recorded road scenes | Rain, vibration, glare, lens obstruction |
| Rear awareness | Rear camera or limited-range proximity sensor | Mirror/visual operator checks for prototype studies | Do not claim full rear/side coverage from one sensor |
| Motion state | IMU and vehicle speed data | Alternative IMU; bench or recorded data | Requires calibration and correct mounting |
| Position / navigation context | GNSS | Recorded routes / simulated position | GNSS can be unavailable or inaccurate |
| Vehicle information | Read-only vehicle data interface | Bench simulator / manually entered data | No unvalidated connection to control bus |
| Rider interaction | Display, physical buttons, tones and warning lights | Bench console during development | Rider retains steering, throttle and braking authority |

Do not make autonomous throttle, steering, or braking part of this architecture.

## 6. Shared console and alert requirements

Every product should expose a local, plain-language status and perception console. Show:
- What the product is currently sensing or receiving.
- Which sensor/source produced each observation.
- When the observation was captured and whether it is fresh.
- Confidence or uncertainty only when the pipeline can justify it.
- What is unknown, blocked, degraded, or outside sensor coverage.
- Which components are missing, disconnected, uncalibrated, or faulted.
- Recommended user action and alert history.

Use clear states: **Detected**, **Suspected**, **Not detected**, **Unable to determine**, and **Sensor unavailable**. Never convert “not detected” into “not present”.

Voice, tones, lights, vibration/haptics, text and icons are complementary outputs. Only show a modality as available when the relevant hardware is actually fitted and verified. Local operation must not depend on a smartphone or internet connection.

## 7. Procurement and selection gates

Before selecting or buying any component:
1. Confirm the capability and measurable requirement.
2. Search at least two independent sourcing options where practical.
3. Record current price, shipping, taxes, lead time, seller and date.
4. Check country of origin and manufacturer provenance when relevant.
5. Check licence, driver, OS and long-term software support.
6. Check voltage, peak current, connector, bandwidth, compute and thermal budget.
7. Check physical dimensions, mounting, mass and environmental limits.
8. Compare the preferred option with at least one alternative.
9. Define a bench test before integration.
10. Obtain explicit approval before any purchase, download, installation, or paid service.

If a component is expensive or unavailable, first ask whether the requirement can be met by a simpler architecture. Do not downgrade a safety-critical capability without a hazard review and explicit acceptance.

## 8. Verification gates

- **G0 — Requirement defined:** capability and failure consequences documented.
- **G1 — Candidate researched:** datasheet, source, cost, interface and limitations checked.
- **G2 — Bench verified:** electrical, driver and data-path tests passed.
- **G3 — Integrated:** mechanically and electrically integrated; health monitoring works.
- **G4 — Environment tested:** tested under representative lighting, weather, vibration, range and user conditions.
- **G5 — Product validated:** system-level performance, usability, fault response and safety evidence reviewed.

A component must not be labelled validated based only on a datasheet, simulation, or successful software import.

## 9. Current portfolio implementation rule

At the start of this standard, no exact component model, price, vendor, availability, or installed status is asserted for any of the six products. Each project registry must be populated from current evidence before purchase or hardware commitment.

The first practical implementation sequence is:
1. Build the common registry and interfaces.
2. Establish a low-cost, stationary software/bench prototype.
3. Evaluate the Coconut Harvest AI image-capture pipeline as an early perception testbed.
4. Reuse only verified common modules across HOME, NOMAD and Sentinel where requirements genuinely match.
5. Develop separate automotive-grade constraints for SUV and Scooter; do not assume consumer robotics components are vehicle-safe.
6. Update the registry, console and project READMEs with evidence and blockers.

**PUI89 rule:** Hardware may change. Capability contracts, safety boundaries, honest status reporting, and evidence must remain.
