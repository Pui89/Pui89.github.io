# PUI89 Shared AI Safety Contract

**Status:** engineering contract for software tests and simulation only. It is not a safety certification, field validation, or proof of model accuracy.

This contract defines the minimum shared behavior expected across Coconut Harvest AI, Extreme Flood Rescue AI, and Multimodal Narcotics Screening AI. Each project may add stricter domain-specific rules, but must not weaken these minimums.

## 1. Required observation fields

Where applicable, each sensor or evidence observation should preserve:

- `source_id` and `modality` (do not collapse distinct sources into one value)
- `timestamp` and an explicit freshness result
- `quality` and `confidence`, with their meaning and scale documented
- `status`: `VALID`, `MISSING`, `STALE`, `INVALID`, `CONFLICTING`, or `UNKNOWN`
- `provenance_ref` and calibration/version information where relevant
- integrity/validation outcome and a reason code for rejected evidence

Do not invent missing readings, silently repair conflicts, treat an uncalibrated score as a probability, or convert unknown states into a positive/healthy state.

## 2. Required decision record

Every simulated decision should record:

- stable scenario/case ID and seed label (if applicable)
- code/model version and configuration hash
- input completeness, detected conflicts, uncertainty/abstention reason
- requested action, policy-gate outcome, actual simulated action/mode
- guard-rule trace, failure codes, simulated time and measured step latency
- human-review state where relevant
- expected versus actual outcome and any mismatch
- evidence limits, NOT RUN checks, and whether the result is synthetic or independently measured

Avoid storing unnecessary personal or sensitive data. Use hashes or minimal evidence references when the underlying evidence does not need to be copied into a report.

## 3. Conservative response rules

| Condition | Minimum software response |
|---|---|
| Emergency stop requested | `STOPPED`; block further simulated action until reset through the defined procedure |
| Required safety telemetry missing, stale, invalid, or conflicting | `SAFE_HOLD`; no action-capable step |
| State or evidence insufficient to support a conclusion | `UNKNOWN` or `ABSTAIN` |
| Human review required or requested | `REQUEST_HUMAN_REVIEW`; do not treat the proposal as approval |
| Configuration or operating limits missing/invalid | Fail closed; do not begin the action-capable simulation step |
| Report evidence missing or internally inconsistent | Mark evaluation invalid/failed; do not publish a success claim |

These are software-state requirements. A simulated `STOPPED` or `SAFE_HOLD` does **not** prove a physical emergency stop or certified safety function.

## 4. Minimum fault-injection matrix

Each project should maintain applicable deterministic tests for:

- missing, stale, malformed, out-of-range, and conflicting observations
- low-quality or uncertain perception and unknown world state
- communication loss and recovery
- emergency-stop request during an action-capable simulated step
- missing/invalid operating limits and malformed scenario configuration
- mismatch between expected and actual behavior
- absent, contradictory, or malformed evaluation evidence
- report status claiming success while failure records exist
- human-review missing, rejection, and override cases where relevant

Every injected fault must have an explicit expected response. Tests must fail if the system silently proceeds on unknown safety conditions.

## 5. Domain-specific safeguards

- **Coconut Harvest AI:** uncertain maturity, target geometry, worker/animal proximity, cutting/capture state, and operator approval must be represented explicitly. A scenario for a tree up to 30 m is a design challenge, not proof of reach or harvesting performance.
- **Extreme Flood Rescue AI:** unknown depth/current, degraded localisation, communication loss, and uncertain human/animal detection must block unsafe simulated approach. A 15 m scenario input does not prove buoyancy, pressure tolerance, or rescue capability.
- **Multimodal Narcotics Screening AI:** missing or disagreeing modalities must remain visible and produce abstention or authorised human review. An alert is not proof of chemical identity or guilt; it must not autonomously trigger search, seizure, detention, or enforcement. Ordinary RGB imagery or an ordinary baggage X-ray image alone does not establish chemical identity.

## 6. Evidence and release gates

1. Run deterministic, dependency-light checks before optional models or simulators.
2. Keep synthetic workflow tests separate from real-world performance evaluation.
3. Record exact commit, configuration, scenario/sample counts, failures, and measurement conditions.
4. Report precision/recall, false-positive/negative rates, calibration, abstention, or latency only when the relevant evaluation was actually run on appropriate, rights-cleared data with a defensible test split.
5. Label missing evidence **NOT RUN**; never infer a pass from tool presence or a green unrelated workflow.
6. Review model/data licences, privacy, installation footprint, and any recurring cost before optional adoption. No paid API, cloud GPU, automatic model download, or hardware connection is required by this contract.

## 7. Acceptance checklist

- [ ] Missing/stale/invalid/conflicting required inputs cannot pass as healthy.
- [ ] Emergency stop blocks further simulated actions.
- [ ] Unknown states remain explicit; no silent imputation.
- [ ] Every fault-injection case has a tested expected result.
- [ ] Reports preserve failures and reject contradictory success summaries.
- [ ] Synthetic results are labelled as synthetic and not as field validation.
- [ ] No real-world capability or accuracy claim exceeds the available evidence.

**Change policy:** project-specific adapters may add fields and stricter rules. Changes to this minimum contract should be reviewed across all three project repositories before adoption.
