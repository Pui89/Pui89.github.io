"""Reproducible synthetic three-floor building scenario."""
from __future__ import annotations

import argparse
import json
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path

from homeguard_ai.core import Baseline, SensorObservation, evaluate_observations


def build_demo(seed: int = 89) -> dict:
    rng = random.Random(seed)
    now = datetime.now(timezone.utc).replace(microsecond=0)
    metrics = {
        "temperature_c": Baseline("temperature_c", 25.0, 1.0, "degC", 120,
                                  (now - timedelta(days=30)).isoformat(), now.isoformat()),
        "relative_humidity_pct": Baseline("relative_humidity_pct", 55.0, 5.0, "%RH", 120,
                                          (now - timedelta(days=30)).isoformat(), now.isoformat()),
        "wall_moisture_pct": Baseline("wall_moisture_pct", 8.0, 1.5, "%", 120,
                                      (now - timedelta(days=30)).isoformat(), now.isoformat()),
        "current_a": Baseline("current_a", 12.0, 2.0, "A", 120,
                              (now - timedelta(days=30)).isoformat(), now.isoformat()),
        "vibration_rms": Baseline("vibration_rms", 0.02, 0.005, "m/s2", 120,
                                  (now - timedelta(days=30)).isoformat(), now.isoformat()),
        "sound_level_db": Baseline("sound_level_db", 38.0, 4.0, "dBA", 120,
                                   (now - timedelta(days=30)).isoformat(), now.isoformat()),
    }
    floors = ["FLOOR-01", "FLOOR-02", "FLOOR-03"]
    observations = []
    index = 0
    for floor in floors:
        for metric, baseline in metrics.items():
            index += 1
            value = baseline.mean + rng.gauss(0, baseline.standard_deviation * 0.25)
            if floor == "FLOOR-02" and metric == "wall_moisture_pct":
                value = 15.5
            if floor == "FLOOR-02" and metric == "relative_humidity_pct":
                value = 74.0
            if floor == "FLOOR-03" and metric == "temperature_c":
                value = 30.0
            if floor == "FLOOR-01" and metric == "current_a":
                value = 20.5
            observations.append(SensorObservation(
                observation_id=f"SIM-{index:03d}",
                sensor_id=f"SYN-{floor}-{metric}",
                domain=metric.split("_")[0].upper(),
                metric=metric,
                value=round(value, 4),
                unit=baseline.unit,
                timestamp=(now - timedelta(seconds=60 * (index % 7))).isoformat(),
                location=f"SIMULATED_BUILDING/{floor}",
                quality="VALID",
                calibration="CURRENT",
                uncertainty=round(baseline.standard_deviation * 0.05, 5),
            ))
    report = evaluate_observations(observations, metrics)
    report["system"]["scenario"] = "SYNTHETIC_THREE_FLOOR_BUILDING"
    report["system"]["random_seed"] = seed
    report["system"]["data_status"] = "SIMULATION_ONLY"
    report["assessment"]["floors_simulated"] = floors
    report["assessment"]["baseline_status"] = "SYNTHETIC_REFERENCE"
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the HOMEGUARD synthetic building scenario.")
    parser.add_argument("--seed", type=int, default=89)
    parser.add_argument("--output", type=Path, default=Path("homeguard-report.json"))
    args = parser.parse_args()
    report = build_demo(args.seed)
    args.output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Wrote {args.output}; findings={report['assessment']['findings_count']}; SIMULATION_ONLY")


if __name__ == "__main__":
    main()
