# DT Simulation Evidence Lineage Register

> **Factory:** Coo-Cah Personal Electronics Factory  
> **Date:** 2026-06-03  
> **Scope:** Mandatory pre-commissioning simulations for DT hard release rule Condition 2

---

## 1. Evidence Lineage Standard

Each simulation record includes:

- execution command and deterministic seed
- source runner path
- repository SHA at execution
- archived JSON output artifact path

Repository SHA at run time: `bb36d65d4557af4e6e5d20a4d847c93e9603c86c`

---

## 2. Mandatory Simulation Runs (3/3)

| Simulation Objective | Command | Output Artifact |
|---|---|---|
| Throughput baseline | `python dt-phase1/services/offline_simulation.py --hours 24 --phone-mix 0.60 --earbud-mix 0.25 --watch-mix 0.15 --seed 101 --out dt-phase1/evidence/simulations/2026-06-03-throughput-baseline.json` | `dt-phase1/evidence/simulations/2026-06-03-throughput-baseline.json` |
| Quality / maintenance stress baseline | `python dt-phase1/services/offline_simulation.py --hours 24 --phone-mix 0.45 --earbud-mix 0.40 --watch-mix 0.15 --seed 202 --out dt-phase1/evidence/simulations/2026-06-03-quality-maintenance-baseline.json` | `dt-phase1/evidence/simulations/2026-06-03-quality-maintenance-baseline.json` |
| Energy baseline | `python dt-phase1/services/offline_simulation.py --hours 24 --phone-mix 0.35 --earbud-mix 0.30 --watch-mix 0.35 --seed 303 --out dt-phase1/evidence/simulations/2026-06-03-energy-baseline.json` | `dt-phase1/evidence/simulations/2026-06-03-energy-baseline.json` |

---

## 3. Output Snapshot

| Objective | Avg Throughput/hr | Queue End Units | Energy Total (kWh) | AMR Utilization Avg (%) | Bottleneck Risk |
|---|---:|---:|---:|---:|---|
| Throughput baseline | 218.83 | 148 | 1430.86 | 73.36 | low |
| Quality / maintenance stress baseline | 232.58 | 178 | 1709.99 | 73.56 | low |
| Energy baseline | 203.21 | 19 | 1586.53 | 74.33 | low |

---

## 4. Approval Record

| Role | Decision | Date | Notes |
|---|---|---|---|
| DT Engineering Lead | Approved for pre-commissioning evidence lineage | 2026-06-03 | Evidence accepted as offline baseline only; recalibration required after commissioning |

