# PUI89 Easy Direct Control Standard v1.0

**Status: Proposed shared product requirement — not a claim of completed implementation or validation.**

## Purpose

Make every PUI89 product straightforward to operate for older adults, first-time users and people who do not use smartphones or applications. The product itself must provide essential controls, status, settings and alerts.

## 1. Direct operation is the primary interface

- Essential setup, normal operation, mode selection, status checks, alerts, settings and safe recovery must be available on the product or its appropriate local operator station.
- No smartphone, application, account, pairing, internet connection or remote service may be required for essential operation.
- Remote dashboards and applications are optional supplementary interfaces. They may mirror information but must not become the only way to control, inspect or acknowledge an essential product state.

## 2. Shared physical control pattern

| Control | User meaning | Design requirement |
|---|---|---|
| POWER | Turn system on/off | Distinguish system power from motion stop; use a safe shutdown sequence |
| START | Begin the selected task or mode | Show the selected mode and confirm readiness before starting |
| STOP | Stop the current task normally | Distinct from power-off and emergency stop |
| MODE | Choose a working mode | Simple names, one-step selection where practical, visible current mode |
| STATUS / HELP | Check state or get guidance | Direct on-device explanation in plain language |
| EMERGENCY STOP | Stop hazardous motion/actuation | Prominent physical control where appropriate; engineering-specific safety design required |

Not every product should use identical hardware. Cars, scooters, quadruped robots, home robots and agricultural equipment must follow their own vehicle/machinery safety architecture and applicable standards. Do not add a generic emergency-stop button where it conflicts with established vehicle controls or creates a new hazard.

## 3. Inclusive and simple usability

- Large, legible labels and recognisable icons; high contrast and adequate spacing.
- Thai and English labels/instructions where supported.
- Tactilely distinguishable controls; never rely on colour alone.
- Clear feedback after every accepted input: on-screen text plus suitable light or sound.
- Plain language, short instructions and a small number of modes; avoid technical jargon.
- Prevent accidental activation of hazardous functions; use deliberate confirmation where risk requires it.
- Accessible placement for seated and standing users where relevant; test with older adults and people with differing abilities.
- Configurable alert sounds, display brightness and voice volume within safe limits.

## 4. On-device status and alerts

Show current state, selected mode, readiness, connectivity, relevant battery/power status, active warnings and recommended user action. Alerts should carry severity, timestamp and history where appropriate. Critical local warnings must remain available when disconnected.

## 5. Safe startup, stop and shutdown

- Startup performs required self-checks and reports ready, limited or blocked.
- START is accepted only when required conditions and interlocks are satisfied.
- STOP requests a controlled stop of the current task.
- POWER-off follows a product-specific safe shutdown sequence; it is not a substitute for emergency stopping.
- Emergency stopping and recovery are designed and validated for each product's hazards. AI software, remote commands and network connectivity must not be the sole safety mechanism.
- After a fault or emergency stop, require an appropriate local inspection/reset procedure; never restart hazardous motion automatically.

## 6. Local, remote and application verification

1. **Local:** physical controls, display, feedback, mode changes, safe stop, alerts and local history work without internet or application access.
2. **Remote:** when connected, status and alerts are transmitted with timestamps and connection-health indication; loss of connection is visible and does not disable local control.
3. **Application:** when an optional application exists, it accurately mirrors authorised status and alerts, marks stale/offline data, and cannot override product safety interlocks.

Verify reconnection, duplicate/out-of-order messages, clock differences, alert history continuity and safe behaviour during communication loss. Do not report a test as passed until evidence is recorded.

## 7. Product-specific adaptation

- **Coconut Harvest AI:** capture, maturity assessment and evidence review; future physical harvesting requires separate guarded machinery controls and safety validation.
- **PUI89 Sentinel:** supervised inspection/exploration; local operator stop and mission status; network loss must not remove local safe-stop capability.
- **PUI89 AI HOME:** simple home-assistance modes and accessible help/status; no unvalidated autonomous-following claims.
- **PUI89 AI NOMAD:** simple mobile-assistant modes and controls reachable while upright or handled; no unvalidated tracking/navigation claims.
- **PUI89 AI Global SUV:** vehicle-native controls and display; AI modes are advisory; driver retains all driving authority.
- **PUI89 AI Step-Through Scooter:** handlebar controls and integrated display; rider retains steering, throttle and braking authority; warnings are low-distraction.

## 8. Acceptance gates

| Gate | Evidence required | Initial status |
|---|---|---|
| G1 — Control map | Product-specific control layout and mode definitions reviewed | Proposed |
| G2 — Accessibility | Label, reach, visibility, tactile and usability review with representative users | Not tested |
| G3 — Local operation | Essential use without phone, app, account or internet | Not tested |
| G4 — Safe transitions | Startup, start, stop, shutdown, fault and emergency procedures tested | Not tested |
| G5 — Alerts | On-device status, severity, recommended action, timestamps and history verified | Not tested |
| G6 — Remote | Connection loss, recovery, stale data and alert delivery tested | Not tested |
| G7 — Application | Optional app parity and safety-boundary tests completed, if an app exists | Not tested |

**Release rule:** This document defines design requirements only. Each product must maintain its own control map, hazard analysis, test evidence and validation record. Do not describe any proposed mode as implemented, passed or certified without corresponding evidence.
