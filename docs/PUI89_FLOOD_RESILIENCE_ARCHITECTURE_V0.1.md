# PUI89 Flood Resilience Engineering v0.1

**Status:** Specified architecture and proposed software implementation  
**Scope:** Shared AI Core environmental-resilience capability for water exposure, flood awareness, system health, conservative warnings and evidence logging.  
**Evidence boundary:** The code in this change is a deterministic software reference implementation tested only with synthetic inputs. It does not establish ingress protection, vehicle wading capability, electrical safety, sensor accuracy, physical safety, IP rating, or field validation.

## 1. Purpose and engineering goals

PUI89 Flood Resilience combines two distinct goals:

1. **Flood resistance:** protect selected enclosures, connectors, wiring, sensors, batteries and mechanisms against defined exposure conditions.
2. **Flood intelligence:** detect water exposure, assess data quality and environmental risk, warn the operator, and request a product-specific safe response.

The shared sequence is:

**Protect → Detect → Assess → Warn → Safe Response → Recover**

A shared software module must not imply that all products have the same physical protection or operating envelope. Enclosure ratings apply to the tested enclosure/configuration, not automatically to the complete product.

## 2. Design target: 20 cm

The initial programme target is a **controlled shallow-water exposure test at up to 20 cm** for selected components and, only after separate safety reviews, selected product configurations.

This is a test target, not:
- permission or advice to drive or ride through floodwater;
- a validated operating depth for any PUI89 product;
- a statement that a product can operate while submerged;
- a substitute for measuring current, wave action, road condition, water contamination, hidden hazards, vehicle geometry or electrical isolation.

Depth alone is insufficient. Every physical test specification must also define exposure duration, water condition, flow/current, temperature, contamination, motion state, ingress inspection method, electrical checks and post-test acceptance criteria.

For vehicles, water can affect braking, traction, steering, intake paths, high-voltage components, stability and recovery. Unknown depth, moving water, hidden road edges or compromised visibility must be treated conservatively. The software in this PR is advisory and proposal-only; it does not control steering, throttle, propulsion or braking.

## 3. Internal exposure levels

These are PUI89 planning labels, not standards or certification marks.

| Internal level | Intended exposure | Evidence required |
|---|---|---|
| FR-1 | Humidity and rain | Defined humidity/rain test and post-test inspection |
| FR-2 | Splash and directed water exposure | Defined spray method, orientation, duration and ingress inspection |
| FR-3 | Controlled shallow-water exposure, staged to 20 cm | Depth and duration records, configuration control, ingress and electrical safety checks |
| FR-4 | Temporary immersion | Pressure/depth/time specification and appropriate enclosure testing |
| FR-5 | Underwater operation | Pressure-rated design, underwater communications/navigation and dedicated mission safety case |

Do not map FR levels directly to IP codes. Select the applicable standard and test method with a qualified test provider. An IP rating is specific to a tested enclosure/configuration and stated test conditions.

## 4. Shared architecture

### 4.1 Protection layer
- Sealed enclosures, gaskets and cable glands selected for the environment.
- Connectors, cable routing and strain relief designed for water exposure.
- Corrosion-resistant materials/coatings selected for actual contaminants.
- Drainage, condensation management and pressure equalisation only where compatible with the enclosure's protection design.
- Battery and power-system protection designed and reviewed independently.

### 4.2 Intelligence layer
- Water ingress/leak observations.
- External water-level/depth observations with units and mounting context.
- Current/flow observations only where a suitable sensor and validated method exist.
- IMU, wheel/motor feedback and sensor-health observations where product-relevant.
- Quality, freshness, calibration and disagreement checks.

### 4.3 Safety and recovery layer
- Conservative risk classification.
- Human-facing warnings and bounded action proposals.
- Independent deterministic safety controller for physical systems.
- Product-specific safe-stop/degraded behaviour from hazard analysis.
- Post-exposure inspection, fault diagnosis and explicit return-to-service approval.

## 5. Data and decision rules

The reference implementation uses typed observations with:
- sensor identifier and measurement kind;
- numeric value and explicit unit;
- timestamp and maximum permitted age;
- quality/validity state;
- optional calibration identifier.

The risk evaluator fails closed when required data is missing, stale, invalid, non-finite, unit-incompatible or outside the declared operating envelope. Conflicting evidence is not silently averaged.

The 20 cm programme target is **not** a universal safe threshold. Each product must provide its own approved operating envelope. Until one exists, the module returns an unknown/restrict response rather than assuming safe operation.

Leak detection, over-temperature, electrical fault and emergency-stop signals are treated as safety-critical inputs. This software may request a safe response but cannot replace a hardware safety circuit, BMS protection, fuse, contactor, emergency stop or qualified safety analysis.

## 6. Product application

| Product | Initial application | Boundary |
|---|---|---|
| Coconut Harvest AI | Rain/soil-moisture exposure awareness; enclosure and connector protection; leak and motor-health monitoring | No claim of harvesting operation in floodwater |
| PUI89 Sentinel | Protect inspection electronics and preserve evidence integrity under specified weather exposure | No water immersion claim; sensor calibration and inspection performance remain separate |
| AI HOME | Leak and indoor flood detection; protect selected electronics from incidental splash | Not a submerged or flood-mobile robot |
| AI NOMAD | Water ingress, wet-ground and traction-risk awareness; protect selected electronics | 20 cm remains a controlled component/product test target, not an approved route capability |
| AI Global SUV | Driver-facing water-risk warnings and authorised read-only health observations | Advisory only; no vehicle-control interface or wading-depth claim |
| AI Step-Through Scooter | Water ingress and electrical-risk warnings; protect selected electronics | No instruction to ride through floodwater; no autonomous throttle, steering or braking |

## 7. Validation plan and gates

### G0 — Requirements and hazard review
Define the exact component/product configuration, user, operating environment, hazards, exposure duration, water condition, acceptance criteria and stop criteria.

### G1 — Software verification
Run deterministic unit tests for missing/stale/invalid data, unit mismatch, sensor disagreement, leak detection, over-temperature, emergency stop and safe-response selection. Synthetic values test software behaviour only.

### G2 — Component-level protection
Only after explicit hardware approval: test enclosures, seals, glands, connectors and sensors using a defined method. Record configuration, depth/spray, duration, orientation, temperature, water condition, ingress findings and post-test electrical checks.

### G3 — Controlled 20 cm exposure
Requires a product-specific hazard review, qualified supervision, safe test facility, isolated test article, instrumentation, recovery plan and written approval. Begin with non-energised or appropriately protected component tests. Do not begin with a rider/driver or occupied vehicle.

### G4 — Product integration
Verify sensor installation, false alarms, detection latency, fail-safe behaviour, braking/traction implications where relevant, and post-exposure condition. Software tests alone cannot pass this gate.

### G5 — Field validation and claims review
Define a validated operating envelope and independent review. Publish only the exact configuration and conditions supported by evidence.

## 8. Evidence record

Each physical test record should include:
- product/component identifier and revision;
- enclosure, connector, cable and firmware versions;
- test procedure/version and responsible reviewer;
- water depth, duration, temperature, flow/current and contamination;
- test orientation and operating/power state;
- raw sensor readings and calibration references;
- photographs/video and inspection findings;
- electrical isolation/continuity checks as applicable;
- faults, warnings, pass/fail/inconclusive result;
- corrective actions and return-to-service approval.

Never convert synthetic test data into a physical test result. Never publish an IP rating, 20 cm wading capability or underwater capability without applicable test evidence.

## 9. Open-source-first implementation

The software reference uses Python standard-library modules only. Unit tests use `unittest`; no package installation, model download, cloud API, subscription or hardware purchase is required. Future ROS 2, Gazebo, OpenCV or sensor adapters must be evaluated separately for licence, provenance, resource needs and compatibility before adoption.

## 10. Definition of done for v0.1

- Shared typed observations and product operating-envelope configuration exist.
- Missing, stale, invalid and conflicting inputs fail conservatively.
- Leak, thermal and emergency-stop signals produce safe-response proposals.
- Tests cover normal, boundary and fault cases.
- Logs distinguish synthetic/software evidence from physical evidence.
- No actuator, vehicle-control, battery-management or electrical-isolation command path is included.
- Documentation states all unvalidated physical capabilities and test gates.

**Current maturity:** Specified / Implemented in this branch / Automated tests authored. Test execution and independent review must be recorded separately. No physical component or product validation is claimed.
