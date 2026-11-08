# PUI89 Hardware & Materials Intelligence

**Status:** Early-stage research and engineering planning  
**Scope:** Shared reference for current and future PUI89 projects  
**Procurement:** Research only; this document is not a purchase list or purchase approval.

## PUI89 positioning

PUI89 is an independent, early-stage AI and robotics R&D initiative. Current work focuses on software foundations, architecture, engineering concepts, research, simulation and documented verification. This programme describes candidate technologies; it does not imply that a physical robot has been manufactured, integrated, tested, certified or released commercially.

## Shared robot architecture

1. **Compute:** embedded computers, CPU/GPU/NPU, microcontrollers, memory and local storage.
2. **Perception:** RGB/depth/stereo/thermal cameras, LiDAR, radar, GNSS, microphones and environmental sensors.
3. **Control:** microcontrollers, motor controllers, encoders, CAN, Ethernet, USB and isolated I/O.
4. **Mobility/manipulation:** geared and BLDC motors, servos, linear actuators, wheels, tracks, joints, brakes and grippers.
5. **Power:** battery packs, BMS, fuses, contactors, DC-DC conversion, charging and thermal monitoring.
6. **Structure/protection:** frames, enclosures, seals, cable glands, connectors, impact and corrosion protection.
7. **Safety:** independent emergency stop, interlocks, watchdogs, safe-state design, manual override and fault reporting.

The shared AI Core should consume standardised observations and publish bounded action proposals. Physical actuation remains a separate, project-specific engineering and safety responsibility.

## Project-specific hardware research

| Project | Candidate materials and mechanical systems | Candidate electronics and sensors | Validation boundary |
|---|---|---|---|
| Coconut Harvest AI | Aluminium frame/arm; stainless fasteners; guarded cutter; compliant gripper; fruit-retention basket; protected wheels | RGB/depth camera, IMU, encoders, force sensing, motor drivers, safety switches | Reach, load, stability, cutting and worker/animal safety unvalidated |
| Flood Rescue AI | HDPE/composite hull; marine-compatible fittings; sealed propulsion; retractable wheel modules; flotation compartments | GNSS, IMU, water-level/depth, RGB/thermal cameras, leak sensors | Buoyancy, stability, current limits, ingress protection and rescue capability require tests |
| PUI89 Sentinel | Modular sensor mounts, protected mobile base, secure evidence interface | RGB/depth; optional certified X-ray equipment or validated chemical-sensor interfaces | No sensor integration or substance-detection performance implied; authorised human review required |
| AI HOME | ABS/polycarbonate enclosure; aluminium supports; bumpers; low-speed wheel base | Temperature/humidity, suitable smoke/CO sensors, water-leak, vibration and electrical monitoring | Calibration, alarm reliability, privacy and electrical safety require validation |
| AI NOMAD | Reinforced polymer/composite shell; aluminium frame; protected joints; weather seals; modular payload bay | RGB/depth/thermal, IMU, GNSS, environmental sensors, battery telemetry | Weather resistance, stability, mobility, endurance and payload remain design targets |
| AI Robot Car | Automotive-grade structure; suspension, steering, braking and crash-energy management | Cameras, radar/LiDAR, GNSS/IMU, wheel-speed and vehicle diagnostics | Simulation and closed-course testing precede road use; no autonomous-driving claim |
| AI Robot Motorcycle | Engineered frame; corrosion-resistant fasteners; suspension, tyres and brakes | IMU, wheel-speed, tyre-pressure, battery/thermal monitoring; camera/radar only if justified | Rider remains in control; roadworthiness and safety require professional validation |

## Materials under investigation

| Material family | Potential uses | Checks before selection |
|---|---|---|
| 6061-T6 aluminium | Frames, brackets, arms | Geometry, fatigue, joining and corrosion |
| Stainless steel 304/316 | Fasteners, shafts, exposed fittings | Grade, galvanic compatibility and environment |
| HDPE | Hulls, guards, water-exposed structures | Thickness, stiffness, impact and joining |
| Polycarbonate | Sensor windows, protective panels | Optical quality, UV ageing, scratching and chemicals |
| ABS / engineering polymers | Enclosures and fixtures | Heat, flame rating, UV and impact |
| Glass-fibre composites | Hulls and shaped enclosures | Lay-up, repair, fire behaviour and ingress |
| TPU / rubber | Wheels, bumpers, vibration isolation and seals | Hardness, wear, temperature and ageing |
| Carbon-fibre composites | Weight-sensitive parts where justified | Cost, impact damage, conductivity and repair |

A material name alone does not establish a safe load rating or fire/water resistance. Do not claim waterproof, fireproof, marine-grade or impact-rated performance without a defined test standard and evidence.

## Shared component categories

- **Compute:** embedded Linux computers, microcontrollers and edge accelerators.
- **Sensing:** cameras, depth sensors, LiDAR, radar, GNSS, IMUs, encoders and environmental sensors.
- **Actuation:** DC/BLDC motors, geared motors, servos, linear actuators, brakes and motor controllers.
- **Power:** cells/packs, BMS, fuses, contactors, DC-DC converters and charging systems.
- **Connectivity:** CAN, Ethernet, USB, serial, Wi-Fi and GNSS interfaces.
- **Mechanical:** bearings, gears, belts, chains, wheels, tracks, joints, grippers and quick-release mounts.
- **Protection:** enclosures, gaskets, cable glands, sealed connectors, thermal barriers and replaceable covers.
- **Safety:** hardwired E-stop, interlocks, watchdogs, isolation, manual override and fault indicators.

Examples such as Raspberry Pi, STM32, ESP32, NVIDIA Jetson and ROS 2 are research references only—not selected PUI89 components or purchase recommendations.

## Component evidence record

Each candidate should record: manufacturer and exact model; verifiable country of manufacture; primary datasheet and revision; interface, voltage/current, dimensions, mass and environmental limits; licence and firmware terms; cybersecurity/update policy; price and availability only when verified; compatibility; hazards and failure modes; repairability; and test evidence.

Use these statuses precisely:

`RESEARCHED` → `SHORTLISTED` → `DESIGNED` → `ACQUIRED` → `INTEGRATED` → `TESTED`

A planned part is not acquired. An acquired part is not integrated. An integrated part is not validated.

## Development sequence

1. Build a shared component/material registry.
2. Define reusable interfaces and project-specific mechanical/electrical constraints.
3. Prepare preliminary BOMs without purchase commitments.
4. Check datasheets, licences, provenance, resource requirements and safety risks.
5. Create CAD, wiring diagrams and simulation interfaces where useful.
6. Prototype only after explicit approval, budget review and a test plan.
7. Publish measured results, failures and limitations; never present plans or simulations as physical validation.

Prioritise open documentation, repairability, transparent provenance and verifiable supply chains. Verify origin at component level; do not infer it from a brand's headquarters.

**PUI89 | Intelligent Systems. Verifiable Decisions. Safer Outcomes.**
