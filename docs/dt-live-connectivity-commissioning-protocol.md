# DT Live Connectivity Commissioning Protocol (Condition 3)

> **Factory:** Coo-Cah Personal Electronics Factory  
> **Status:** Pre-approved for commissioning execution  
> **Date:** 2026-06-03

---

## 1. Purpose

This protocol defines the exact execution and evidence required to move hard release rule
Condition 3 (**Live data connectivity proven for critical assets**) from construction-gated
to green once machines are commissioned.

---

## 2. Construction-Gated Rule

- Condition 3 remains **not green** until live telemetry is proven.
- Current status is **Blocked by commissioning dependency** (not blocked by documentation execution).
- Unblock trigger: first critical asset energized with stable telemetry path to DT stack.

---

## 3. Critical Assets for Day-0 Verification

| Asset Group | Minimum Live Asset | Required Telemetry |
|---|---|---|
| SMT production | SMT Line 1 (Z2 or Z3) | machine state, cycle count, alarm code, throughput counters |
| Quality / test | AOI or ICT station | defect/fail counters, test pass/fail events |
| Energy | Main feeder / energy meter | real-time kW, cumulative kWh, timestamped interval readings |

---

## 4. Day-0 Evidence Pack (Initial Connectivity Proof)

- asset energized record and commissioning timestamp
- connector and topic mapping sheet (asset tag ↔ namespace path)
- 60-minute continuity capture per critical asset
- message integrity checks (timestamp monotonicity, payload schema validity, null/drop rate)
- ingestion proof in broker and downstream storage
- incident log for any packet loss or mapping mismatch

---

## 5. Day-7 Evidence Pack (Stability Proof)

- seven-day uptime summary for each critical asset path
- continuity window report with hourly completeness
- quality checks: duplicates, stale timestamps, malformed payload count
- alerting evidence for outage/recovery events
- approved closure record signed by IT/OT Infrastructure Lead and Factory Engineering Lead

---

## 6. Pass/Fail Criteria

Condition 3 turns green only when all are true:

- Day-0 pack complete for all three critical asset groups
- Day-7 stability pack complete and signed
- no open critical telemetry defects without approved mitigation

---

## 7. Ownership

| Control Item | Accountable Owner | Due Trigger |
|---|---|---|
| Day-0 execution | IT/OT Infrastructure Lead | First critical asset energization |
| Day-7 stability validation | IT/OT Infrastructure Lead + Factory Engineering Lead | 7 days after Day-0 |
| Final Condition 3 sign-off | Digital Manufacturing Team Lead | After Day-7 pass criteria |

