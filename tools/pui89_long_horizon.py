#!/usr/bin/env python3
"""Deterministic, dependency-free long-horizon robustness evaluator.

This evaluates decision-policy behavior on explicitly synthetic scenarios.
It does not measure model accuracy, statistical calibration, or physical safety.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

VALID_STATES = {"CONTINUE", "SAFE_HOLD", "REQUEST_HUMAN_REVIEW", "STOPPED"}

def evaluate_sequence(sequence):
    state = "CONTINUE"
    uncertainty = 0.0
    trace = []
    failures = []
    for index, step in enumerate(sequence):
        faults = set(step.get("faults", []))
        confidence = step.get("confidence", 1.0)
        if not isinstance(confidence, (int, float)) or isinstance(confidence, bool) or not 0 <= confidence <= 1:
            failures.append({"step": index, "reason": "invalid_confidence"})
            state = "SAFE_HOLD"
            confidence = 0.0
        uncertainty = min(1.0, max(uncertainty, 1.0 - confidence))
        if "missing_evidence" in faults or "stale_sensor" in faults or "sensor_clock_skew" in faults:
            next_state = "SAFE_HOLD"
        elif "conflicting_evidence" in faults or "noisy_evidence" in faults or "ood_evidence" in faults:
            next_state = "REQUEST_HUMAN_REVIEW"
        elif "safety_critical_failure" in faults:
            next_state = "STOPPED"
        elif uncertainty >= step.get("review_uncertainty_threshold", 0.65):
            next_state = "REQUEST_HUMAN_REVIEW"
        else:
            next_state = "CONTINUE"
        # Fail-safe states persist until an explicit recovery step with fresh,
        # consistent evidence and operator approval is supplied.
        if state == "STOPPED":
            next_state = "STOPPED"
        elif state in {"SAFE_HOLD", "REQUEST_HUMAN_REVIEW"} and next_state == "CONTINUE":
            if not (step.get("recovery") is True and step.get("fresh_evidence") is True
                    and step.get("consistent_evidence") is True
                    and step.get("operator_approved") is True):
                next_state = state
        state = next_state
        trace.append({
            "step": index, "timestamp": step.get("timestamp"),
            "state": state, "uncertainty": round(uncertainty, 6),
            "faults": sorted(faults),
        })
    return {"steps": len(sequence), "trace": trace, "final_state": state,
            "failure_count": len(failures), "failures": failures,
            "uncertainty_increased": bool(trace and trace[-1]["uncertainty"] > trace[0]["uncertainty"])}

def build_report(scenarios, commit="unknown"):
    results = []
    for scenario in scenarios:
        result = evaluate_sequence(scenario.get("steps", []))
        expected = scenario.get("expected_final_state")
        result.update({"scenario_id": scenario.get("id", "unnamed"),
                       "expected_final_state": expected,
                       "expectation_met": expected is None or expected == result["final_state"]})
        results.append(result)
    failed = [r for r in results if not r["expectation_met"] or r["failure_count"]]
    return {
        "schema_version": "1.0",
        "benchmark": "PUI89 Long-Horizon Robustness (synthetic policy scenarios)",
        "commit": commit,
        "status": "PASS" if results and not failed else "FAIL",
        "scenario_count": len(results),
        "steps_total": sum(r["steps"] for r in results),
        "expectations_met": sum(bool(r["expectation_met"]) for r in results),
        "failed_scenarios": len(failed),
        "results": results,
        "limitations": [
            "Synthetic deterministic policy scenarios only; not trained-model evaluation.",
            "Uncertainty values are policy inputs, not statistically calibrated probabilities.",
            "No real-world accuracy, simulator realism, hardware safety, or physical capability is measured.",
            "Calibration metrics such as Brier score and ECE require independent labelled predictions and are intentionally not fabricated."
        ]
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--commit", default="unknown")
    args = parser.parse_args()
    scenarios = json.loads(args.input.read_text(encoding="utf-8"))
    report = build_report(scenarios, args.commit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\\n", encoding="utf-8")
    print(f"{report['status']}: {report['scenario_count']} scenarios, {report['steps_total']} steps")
    return 0 if report["status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
