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

## 9. Current implementation status

This document is a design baseline. Product-specific sensor hardware, mounting positions, CAD, coverage measurements, calibration, console integration and verification remain **not verified** unless supported by separate evidence. Do not convert candidate positions into installed-hardware claims.
