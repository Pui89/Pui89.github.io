# PUI89 Structural & Environmental Intelligence v0.1

**Status:** Proposed architecture + dependency-light reference rules. Not a deployed monitoring system.

## Purpose

Provide a reusable Shared AI Core capability for observing vibration, building movement, visible crack change, and humidity. It is intended for condition awareness, trend monitoring, and conservative human-facing alerts—not structural diagnosis, earthquake prediction, or certification of building safety.

## Monitoring domains

1. **Object and equipment vibration** — monitor measured acceleration/vibration indicators against a commissioned baseline and equipment-specific limits.
2. **Building shaking** — identify unusual measured movement or sustained vibration. Describe this as a *shaking event indicator*, not a confirmed earthquake alert. Use an authoritative seismic-warning source for public earthquake alerts.
3. **Wall and surface cracks** — compare timestamped, calibrated images or human-entered measurements; track crack width/length changes and image quality. Computer vision may propose candidate crack regions, but a person must review them.
4. **Humidity and moisture** — monitor relative humidity, surface moisture, condensation/leak indicators, and trends. Air humidity alone cannot establish moisture inside a wall.
5. **Cross-sensor anomaly review** — correlate vibration, crack change, humidity, leaks, and sensor health without assuming causation.

## Reference architecture

- **Sensor adapters:** accelerometer / vibration sensor; calibrated camera or crack gauge; temperature and relative-humidity sensor; surface-moisture or leak sensor where appropriate.
- **Observation layer:** timestamp, source ID, location/asset ID, units, calibration status, quality, and provenance.
- **Baseline and configuration:** site- and asset-specific baselines, installation orientation, sampling rate, calibration history, and limits approved by a qualified person.
- **Signal processing:** filtering, RMS/peak/frequency features, event duration, trend comparison, and image registration before crack comparison. Processing methods and sampling rates must be documented per sensor.
- **Risk assessment:** conservative rules; stale, missing, uncalibrated, or conflicting inputs produce an unknown/degraded state rather than a safe result.
- **Alert and evidence:** severity, triggering observations, uncertainty, timestamps, acknowledgement, and review history. Alerts are advisory and must not imply a diagnosis.

## Threshold policy

There are **no universal vibration, crack-width, crack-growth, or humidity thresholds** in this reference implementation. Values must be configured for the particular building, material, sensor, mounting, environment, and monitoring objective. A structural engineer or other appropriately qualified professional must define and review structural limits. Sensor calibration and installation must be recorded.

## Product relevance

- **AI HOME:** primary candidate for indoor building-condition awareness and humidity/leak monitoring, subject to privacy-by-design.
- **AI NOMAD:** optional monitoring of its own enclosure, vibration exposure, and environmental condition; not a building inspector.
- **Sentinel:** optional supervised infrastructure inspection with calibrated imaging and vibration observations; no autonomous safety verdict.
- **SUV / Step-Through Scooter:** optional component vibration and environmental-health monitoring through authorised read-only sensors; no vehicle control.
- **Coconut Harvest AI:** optional machinery/robot vibration and moisture monitoring where it supports maintenance and safe operation.

## Safety and limitations

- Do not claim earthquake prediction. A local accelerometer can indicate shaking at its installation point; it cannot reliably identify the source or provide authoritative regional warning.
- Do not claim a building is safe, unsafe, structurally sound, or at risk of collapse from this software alone.
- Crack detection from images is sensitive to lighting, scale, camera angle, focus, surface texture, and calibration. Apparent change must be verified.
- Humidity is not the same as wall moisture. Use suitable surface/material sensors and qualified inspection where needed.
- On suspected structural damage, unusual severe shaking, rapidly changing cracks, falling debris, or other immediate danger, people should move to safety and follow local emergency guidance; do not wait for an AI alert.
- Keep recordings local where practical, minimise image capture, avoid recording people/private spaces, and require explicit consent and access controls.

## Validation gates

- **G0 — Requirements:** define asset, sensor location/orientation, sampling, units, baseline, hazards, privacy, and alert recipients.
- **G1 — Software:** test units, timestamp handling, stale/missing/conflicting data, sensor faults, thresholds, and fail-closed behaviour.
- **G2 — Bench calibration:** compare sensors against traceable references; verify mounting and repeatability.
- **G3 — Controlled trials:** safe vibration-table / reference-shaker tests and controlled humidity tests; no intentional damage to occupied structures.
- **G4 — Crack measurement:** calibrated scale, fixed camera geometry, image registration, repeatability and human review.
- **G5 — Site validation:** qualified professional review, documented operating envelope, false-alarm/missed-event analysis, maintenance plan, and emergency procedures.

## Evidence status

This document and its reference rules are design-stage software assets. They do not establish installed sensors, live monitoring, model accuracy, calibrated measurements, building inspection, earthquake-warning capability, or validated structural safety. No hardware purchase, installation, cloud service, or physical test is included.
