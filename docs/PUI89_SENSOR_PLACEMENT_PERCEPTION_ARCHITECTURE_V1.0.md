# PUI89 Sensor Placement & Perception Architecture v1.0

**Status:** Design standard — proposed, not hardware-verified  
**Applies to:** Coconut Harvest AI, PUI89 Sentinel, AI HOME, AI NOMAD, AI Global SUV, AI Step-Through Scooter  
**Purpose:** Define how each product places sensors, describes what it can perceive, communicates uncertainty and blind zones, and presents observations through its own local Multimodal Interaction & Perception Console.

## 1. Core rule

Design perception from the product's real tasks and installed hardware—not from a generic human five-senses analogy. Every product must distinguish:
- **Installed and verified:** physically present and passed the stated check.
- **Planned:** selected in the design but not yet installed or tested.
- **Optional:** a possible configuration, not included by default.
- **Unavailable / faulted:** expected hardware or data is currently unavailable.
- **Not applicable:** not required for this product or task.

A sensor listed in this document is a candidate design element unless a build record and test evidence confirm it. No range, accuracy, coverage, autonomy, or safety capability is implied.

## 2. Sensor placement record

Every physical sensor position must have a record containing:
- Product and sensor identifier; sensor type, manufacturer/model when selected.
- Physical mounting location, orientation, height and adjustable range where applicable.
- Intended task and observable targets.
- Horizontal/vertical field of view, usable range and operating conditions from the actual datasheet.
- Occlusion sources, blind zones, overlap with adjacent sensors and environmental limitations.
- Calibration method, timestamp/freshness, health monitoring and contamination protection.
- Power/data interface, compute destination and failure response.
- Evidence: CAD revision, datasheet, installation photo, calibration record and test result.

Do not publish numeric FOV/range or claim coverage until supported by the selected component datasheet and product-level tests.

## 3. Product-specific candidate placement

### 3.1 Coconut Harvest AI
- Primary candidate: RGB camera on a stable, fruit-facing mount; position it to capture target bunches without unsafe operator positioning.
- Candidate adjustment: tilt/pan or repositioning mechanism only if the mechanical design supports it.
- Optional: depth sensor for distance/geometry; lighting for controlled capture.
- Console perception: image captured, target region visible/partly occluded, image quality, maturity estimate and confidence only when the model provides calibrated confidence.
- Must state: occluded fruit, poor lighting, motion blur, out-of-view bunches and unsupported maturity classes as unknown/needs review.
- No harvesting actuation or 0–30 m capability claim without separate engineering evidence.

### 3.2 PUI89 Sentinel — quadruped inspection robot
- Primary candidate: forward RGB camera on the upper front body, protected from direct impact and with a clear view over the front structure.
- Candidate depth/perception: forward depth camera or LiDAR mounted with an unobstructed view; choose based on the validated inspection task.
- Optional: rear/side cameras or proximity sensors for close-range awareness; IMU mounted rigidly near the body centre.
- Optional task sensors (for example thermal or gas) require a defined inspection use case, sensor specification and calibration plan.
- Console perception: visible scene, obstacles/terrain cues, sensor health, localization state if supported, and explicit unknown regions.
- Do not imply X-ray, chemical identification, universal hazard detection or autonomous safe navigation unless the relevant instrument and validation exist.

### 3.3 PUI89 AI HOME — indoor assistant
- Primary candidate: forward-facing RGB camera in the upper front body, with privacy-aware physical placement.
- Candidate near-field sensing: front/lower depth or proximity sensors to detect low objects and close obstacles.
- Optional: side/rear proximity coverage where movement tasks require it; IMU rigidly mounted to the chassis.
- Console perception: room scene cues, near-field obstacles, movement state and sensor availability.
- Explicitly identify areas hidden by furniture, the robot body, people, glare or low light. Do not claim person identification or fall detection unless separately designed and validated.

### 3.4 PUI89 AI NOMAD — outdoor/mobile assistant
- Primary candidate: forward RGB camera mounted high enough to reduce body occlusion while remaining protected.
- Candidate depth sensing: forward depth camera or LiDAR selected for the outdoor operating environment.
- Optional: side/rear proximity sensors, wheel/drive odometry and chassis IMU; GNSS only if outdoor location tasks require it and reception is assessed.
- Console perception: path/obstacle observations, surface or weather cues only when supported, localization quality and unavailable zones.
- Outdoor lighting, rain, dust, vegetation, reflective surfaces and GNSS loss must be represented as limitations—not silently treated as clear conditions.

### 3.5 PUI89 AI Global SUV
- Candidate forward perception: front camera and automotive-rated radar/sensing selected for the intended driver-assistance function.
- Candidate rear perception: reversing camera and rear proximity sensing.
- Candidate side perception: side cameras/radar for blind-spot assistance where the vehicle architecture supports it.
- Optional: surround-view cameras, wheel-speed/vehicle-state signals and IMU.
- Console perception: driver-facing status, detected objects/alerts, sensor blockage and system availability.
- AI is advisory. The driver retains control. Do not claim autonomous driving, collision avoidance or full blind-spot coverage without automotive-grade design, integration and validation.

### 3.6 PUI89 AI Step-Through Scooter
- Candidate forward perception: road-facing front camera positioned clear of rider, handlebar and bodywork occlusion.
- Candidate rear awareness: rear camera or appropriate proximity sensing if the design and power budget support it.
- Candidate motion state: chassis IMU and validated vehicle signals; GNSS optional for navigation context.
- Console perception: forward/rear awareness status, road-context observations, sensor obstruction and warning status.
- Rider retains steering, throttle and braking. No autonomous control. Rain, vibration, helmet/rider occlusion, glare and camera contamination must be addressed in validation.

## 4. Perception coverage map

Each product must have its own top/front/side/rear placement views and a coverage overlay. The map must visually distinguish:
- Sensor location and orientation.
- Measured/validated coverage versus estimated design coverage.
- Overlap zones and known blind zones.
- Occlusion by chassis, payload, rider/operator, furniture or environment.
- Sensor fault or blocked state.

Use a legend and text labels; never rely on colour alone. A conceptual drawing is not a measured coverage map. CAD/FOV simulation and physical tests are required before coverage is labelled validated.

## 5. Local Multimodal Interaction & Perception Console

Every product has a built-in local display/control surface or an appropriate local operator station. Core operation must not require a smartphone, account, app or internet connection.

Required console sections:
1. **Overview:** product identity, current state, selected working mode, power and connectivity/offline state.
2. **What I perceive:** plain-language observations, source sensor, observation time, quality and uncertainty.
3. **Coverage:** sensor positions, current health, blocked/faulted sensors and known blind zones.
4. **Alerts:** severity, concise title, complete sentence, timestamp, recommended user action and history.
5. **Controls:** physical start/stop, mode selection and product-specific emergency control where appropriate.
6. **Help & recovery:** simple instructions, sensor cleaning/check guidance and safe recovery steps.

Important information must be written as readable text and complete sentences. Tones, spoken voice, lights, icons, vibration/haptics and optional remote notifications supplement—not replace—text. Only show a modality as delivered when the hardware confirms delivery.

## 6. Shared perception/event message

A perception or alert event should carry:
- event_id, product_id, event_type and severity;
- title and plain-language sentence;
- source sensor identifiers and observation timestamp;
- data freshness and quality;
- confidence/uncertainty only when meaningfully supported;
- recommended user action;
- sensor/system state and whether the observation is partial;
- modalities available and modalities actually delivered;
- acknowledgement state and event-history reference.

Use explicit states: **Detected**, **Suspected**, **Not detected**, **Unable to determine**, **Sensor unavailable**, and **Stale observation**. “Not detected” must never be presented as proof that a hazard or object is absent.

## 7. Human factors and safety
- Thai and English text where supported; simple wording, large text and clear physical controls.
- Do not use colour alone to communicate severity.
- Separate normal STOP, POWER OFF and emergency stop; define product-specific safe behaviour.
- Avoid alert overload; prioritize actionable warnings and explain what the user should do.
- Provide a clear acknowledgement flow without allowing acknowledgement to disable a safety function.
- Define fallback behaviour for sensor loss, disagreement, stale data, compute overload and power interruption.
- Keep a timestamped local event history; protect privacy and minimize stored imagery.

## 8. Verification gates

A product cannot mark a sensor position or perception capability as verified until evidence exists for:
1. Component selection and datasheet review.
2. CAD placement, mounting, vibration and environmental assessment.
3. FOV/coverage and occlusion analysis.
4. Calibration and sensor-health checks.
5. Representative tests across lighting, weather, motion and target conditions.
6. Fault injection: disconnected, blocked, stale, noisy and contradictory sensor data.
7. Console text correctness, Thai/English usability and alert-delivery checks.
8. Safe fallback and recovery tests.


## 10. Hardware-flexible and easy-to-source design

PUI89 products must be designed to remain buildable when a preferred component is unavailable, expensive, difficult to import, out of stock or discontinued. Define capability requirements first and select hardware second.

### 10.1 Capability-first architecture
For every function, specify:
- The user need and operational task.
- Required observation or output (for example: capture a fruit image, detect a nearby obstacle, show a warning).
- Minimum acceptable performance and the test that proves it.
- Environmental, power, compute, interface, mounting and cost constraints.
- What the product must do when the function is absent or fails.

Software must communicate through stable capability interfaces rather than depending directly on one sensor brand or model. Examples include `ImageSource`, `RangeObservation`, `MotionState`, `PositionEstimate`, `AudioOutput`, `VisualIndicator` and `TextDisplay`. These are interface concepts, not a claim that every product contains every device.

### 10.2 Three hardware tiers
Each capability should have a deliberately designed configuration tier:

1. **Minimum / Starter:** the simplest affordable and obtainable hardware that can perform the essential, non-safety-critical task. The product must clearly disclose reduced coverage or performance.
2. **Standard / Preferred:** the recommended balance of availability, performance, power, maintainability and cost.
3. **Enhanced / Optional:** additional sensors or compute for wider coverage or advanced functions. The product must still operate safely if this tier is not installed.

A tier is product- and task-specific. Do not assume a cheap component is suitable merely because it has a similar name.

### 10.3 Approved substitution rules
When a component cannot be sourced:
1. Keep the capability requirement and acceptance test unchanged.
2. Search the approved parts list for an equivalent component.
3. Compare electrical interface, protocol, driver support, dimensions, mounting, voltage/current, thermal load, data quality, latency, environmental rating and supply continuity.
4. Update the mechanical adapter or cable harness where possible, instead of redesigning the whole product.
5. Run interface, calibration, coverage, environmental and fault tests.
6. Record the substituted part, reason, trade-offs, evidence and approved configuration.
7. Update the BOM, wiring diagram, CAD, software configuration and user-facing capability list together.

Never silently replace a sensor or claim equivalent performance without tests.

### 10.4 Modular mechanical and electrical design
- Use replaceable sensor brackets and documented mounting patterns where practical.
- Keep sensor modules physically serviceable without dismantling unrelated assemblies.
- Use labelled connectors, keyed connections where appropriate, strain relief and documented pinouts.
- Separate sensor power and data interfaces where practical; protect against incorrect voltage and polarity.
- Prefer common, documented interfaces and maintainable open drivers, while checking actual compatibility.
- Provide a safe blanking cover or sealed unused mounting point where an optional sensor is not fitted.
- Design cable routes, enclosure space, thermal paths and compute capacity for realistic future upgrades without promising that every upgrade will fit.

### 10.5 Capability degradation and graceful fallback
The console must show the actual installed configuration and change its language when a capability is missing:
- **Available:** hardware is detected and has passed its current health check.
- **Limited:** the function works with reduced coverage or quality; explain the limitation.
- **Unavailable:** hardware is absent, disconnected or faulted.
- **Not configured:** optional capability has not been installed or enabled.
- **Needs service:** inspection, cleaning or repair is required.

Examples:
- If depth sensing is unavailable, show that depth-based distance information is unavailable; do not invent distance from an RGB image.
- If a rear camera is not fitted, state that rear visual awareness is not provided.
- If GNSS is unavailable, state that satellite positioning is unavailable; do not display a fabricated location.
- If voice output is not fitted, keep the text and visual alert available; do not claim a spoken warning was delivered.
- If network connectivity is absent, retain local controls, status and event history wherever the product design supports them.

A missing optional sensor may reduce a feature. A missing safety-critical sensor must trigger the product-specific safe state defined by hazard analysis; it must never be bypassed simply to keep the product moving.

### 10.6 Cost and sourcing register
Maintain a per-product BOM with:
- Function/capability and required tier.
- Preferred part and at least one technically assessed alternative where feasible.
- Supplier/source, country of origin when known, availability date and lead-time notes.
- Unit cost and currency only when supported by a current quote or listing.
- Open-source driver/licence and operating-system compatibility.
- Power, compute, mechanical and environmental requirements.
- Substitution status: unassessed, candidate, tested, approved or rejected.
- Evidence link and last review date.

Do not invent prices or claim a part is available without a current source check. Avoid making a product dependent on a single proprietary cloud, paid API, app or vendor-specific service for essential local operation.

### 10.7 Easy-build design gate
Before freezing a product design, ask:
- Can the essential version be assembled with obtainable components?
- Can a beginner or technician replace a module using clear instructions and ordinary tools?
- Can the system identify a missing, wrong or failed module?
- Can the software boot and show a useful status when optional modules are absent?
- Are wiring, pinouts, brackets, drivers and calibration steps documented?
- Are safe degraded modes defined and tested?
- Can future sourcing changes be handled by a module-level substitution rather than a complete redesign?

If not, simplify the architecture before adding more sensors or features.


## 11. Current implementation status

This document is a design baseline. Product-specific sensor hardware, mounting positions, CAD, coverage measurements, calibration, console integration and verification remain **not verified** unless supported by separate evidence. Do not convert candidate positions into installed-hardware claims.
