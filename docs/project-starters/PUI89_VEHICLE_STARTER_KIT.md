# PUI89 Vehicle Project Starter Kit — SHIELD

This starter kit prepares the PUI89 AI Robot Car and AI Robot Motorcycle projects to inherit the Universal SHIELD standard. It is a documentation/configuration starter only. It does not create the two GitHub repositories, implement vehicle control, or validate physical safety.

## Shared AI Core contracts
Both future repositories must reuse the existing PUI89 Shared AI Core contracts:
- `WorldState`
- `Observation`
- `ActionProposal`
- `FailureReport`
- evidence provenance and uncertainty
- safety gates and human override
- simulation/benchmark records
- automated tests and security checks

Do not fork or duplicate the Shared AI Core. Keep vehicle-specific dynamics, operating envelopes, hazard thresholds and safety cases separate.

## Mandatory development order
1. Create the repository and apply the project-specific profile.
2. Audit the existing Shared AI Core and reuse contracts.
3. Build software-only observation, warning and evidence interfaces.
4. Add unit tests for missing, stale, conflicting and adversarial observations.
5. Add simulation scenarios and reproducible benchmarks.
6. Complete threat modeling and security checks.
7. Define hardware safety requirements only after software/simulation evidence.
8. Require separate engineering review and authorization before hardware or road testing.

## Non-negotiable limits
- Strict zero-cost: no paid APIs, cloud GPU, subscription, billable service or unapproved hardware purchase.
- Check licences and resource requirements before adding dependencies.
- No physical actuation, autonomous road operation or deployment is authorized by this starter.
- Keep physical validation as `NOT_VERIFIED` until suitable tests and evidence exist.
- A software warning is not a brake, steering, isolation or fire-protection mechanism.
- No claim of waterproof, fireproof, crash-safe, autonomous-safe or standards compliance without appropriate independent evidence.

## Project-specific differences
- Car: four-wheel vehicle dynamics, steering/braking, pedestrian/cyclist safety, driver override and minimal-risk condition.
- Motorcycle: two-wheel balance, lean angle, traction, rider fall, braking/throttle and rider override. Begin with rider-assistance research, not full autonomy.
