# PUI89 Flood Resilience Test & Validation Plan v0.1

**Status:** Proposed test plan  
**Target:** Controlled exposure programme staged to 20 cm  
**Not a field-use instruction:** This document is not approval to expose, energise, drive, ride or operate any prototype in floodwater.

## 1. Test philosophy

Test from software to component to integrated product. Do not begin with a complete occupied vehicle or mobile robot. A successful software test does not establish water resistance or electrical safety.

## 2. Software test matrix

| ID | Scenario | Expected result |
|---|---|---|
| SW-01 | Valid, fresh water-level and health observations | Evaluate within configured envelope |
| SW-02 | Missing water-depth observation | Unknown / restrict |
| SW-03 | Stale observation | Unknown / restrict |
| SW-04 | Invalid quality or non-finite value | Unknown / restrict |
| SW-05 | Unit mismatch | Reject / restrict |
| SW-06 | Water depth above configured envelope | Restrict / human review |
| SW-07 | Conflicting water-level sensors | Unknown / restrict |
| SW-08 | Internal leak detected | Immediate safe-response proposal |
| SW-09 | Battery/electronics over-temperature | Immediate safe-response proposal |
| SW-10 | Emergency-stop asserted | Immediate safe-response proposal |
| SW-11 | Sensor health failure | Unknown / restrict |
| SW-12 | Synthetic 20 cm value | Evaluate only against explicit product envelope; never label as physical validation |

## 3. Component protection test matrix

Only after hardware selection and explicit purchase/build approval:
- enclosure seam, gasket compression and cable-gland inspection;
- connector mating/unmated exposure as relevant;
- spray/splash exposure using a defined method;
- controlled immersion only when the selected test method and enclosure are designed for it;
- condensation and post-drying inspection;
- corrosion/contamination review for the intended water type;
- electrical checks performed by qualified personnel using suitable procedures.

Do not improvise pressure or immersion tests on powered batteries, high-voltage systems or unreviewed electronics.

## 4. Controlled 20 cm test gate

Before any physical test, approve:
1. Exact test article, revision and bill of materials.
2. Hazard analysis and independent test supervisor.
3. Test tank/channel/facility and calibrated depth measurement.
4. Water type, temperature, contamination and flow/current condition.
5. Exposure duration, orientation, power state and motion state.
6. Emergency isolation, retrieval and spill/recovery plan.
7. Electrical inspection and acceptance procedure.
8. Stop criteria and post-test quarantine/return-to-service authority.

Recommended progression:
- **20A:** non-energised enclosure/component exposure;
- **20B:** instrumented component exposure under approved electrical-safety controls;
- **20C:** unoccupied integrated prototype, stationary;
- **20D:** controlled mobility trial only after earlier gates pass and a separate mobility hazard review approves it.

The 20 cm depth is a programme test point, not a safe flood-crossing depth. Flowing water, hidden drop-offs, contaminated water and unknown road conditions are separate hazards.

## 5. Product-specific notes

- **Coconut Harvest AI:** prioritise sealed electronics, connectors, motor/gearbox exposure, mud ingress and post-rain inspection.
- **Sentinel:** protect imaging and compute modules; ensure moisture does not compromise calibration, optics or evidence records.
- **AI HOME:** focus on leak detection and incidental splash; do not design it as an amphibious device by implication.
- **AI NOMAD:** test wet-floor traction and ingress separately; no mobility in floodwater until its mechanical/electrical architecture and hazard case are defined.
- **AI Global SUV:** advisory water-risk sensing only at current software stage; any wading validation belongs to a vehicle engineering programme.
- **AI Step-Through Scooter:** focus on electrical ingress and rider warnings; do not conduct rider-involved flood trials as an early validation step.

## 6. Result classification

- **PASS:** all predeclared acceptance criteria met for the exact test configuration.
- **FAIL:** one or more acceptance criteria not met.
- **INCONCLUSIVE:** instrumentation, procedure, evidence or conditions insufficient to decide.
- **NOT RUN:** no test execution evidence.

Every result must identify the procedure, configuration, date, responsible reviewer and supporting records. Do not report a test as passed based only on visual inspection or a software simulation.

## 7. Release gate

No public claim such as “IP67”, “waterproof”, “20 cm flood capable”, “submersible” or “amphibious” may be made unless the exact claim is supported by appropriate test evidence for the exact product configuration and conditions. Keep proposed targets visibly separate from verified capabilities.
