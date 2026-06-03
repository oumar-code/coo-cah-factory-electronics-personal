#!/usr/bin/env python3
import argparse
import json
import random
from statistics import mean


def run_scenario(hours: int, phone_mix: float, earbud_mix: float, watch_mix: float):
    queue = 0
    energy_kwh = 0.0
    amr_busy = []
    throughput = []

    for h in range(hours):
        demand = int(220 * phone_mix + 320 * earbud_mix + 90 * watch_mix)
        capacity = int(random.uniform(0.88, 1.08) * demand)
        produced = max(0, min(demand + queue, capacity))
        queue = max(0, queue + demand - produced)
        throughput.append(produced)

        energy_kwh += produced * random.uniform(0.18, 0.42)
        amr_busy.append(random.uniform(55, 92))

    return {
        "hours": hours,
        "avg_throughput_per_hour": round(mean(throughput), 2),
        "queue_end_units": queue,
        "energy_total_kwh": round(energy_kwh, 2),
        "amr_utilization_pct_avg": round(mean(amr_busy), 2),
        "bottleneck_risk": "high" if queue > 900 else "medium" if queue > 300 else "low",
    }


def main():
    parser = argparse.ArgumentParser(description="Offline design-spec simulation baseline")
    parser.add_argument("--hours", type=int, default=24)
    parser.add_argument("--phone-mix", type=float, default=0.5)
    parser.add_argument("--earbud-mix", type=float, default=0.35)
    parser.add_argument("--watch-mix", type=float, default=0.15)
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Deterministic random seed for reproducible simulations",
    )
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    random.seed(args.seed)
    result = run_scenario(args.hours, args.phone_mix, args.earbud_mix, args.watch_mix)
    payload = {
        "simulation_type": "design_spec_baseline",
        "note": "Calibrate with real production data after commissioning.",
        "inputs": {
            "hours": args.hours,
            "phone_mix": args.phone_mix,
            "earbud_mix": args.earbud_mix,
            "watch_mix": args.watch_mix,
            "seed": args.seed,
        },
        "lineage": {
            "runner": "dt-phase1/services/offline_simulation.py",
            "reproducibility": "Re-run with identical inputs and seed value.",
        },
        "outputs": result,
    }

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
