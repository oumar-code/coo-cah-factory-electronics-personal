# Personal Electronics Factory — EMS M1.9 Preconfiguration Baseline

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1
> **Document Version:** 1.0 | **Owner:** Energy + MES/SCADA + Facilities

---

## 1. Purpose and M1.9 Scope

This document defines the **policy-first, scenario-driven EMS preconfiguration baseline** for milestone **M1.9** (Solar + BESS commissioning).  
It is designed so commissioning is primarily validation and tuning, not first-time rule design.

This baseline applies to:

- Sungrow iSolarCloud integration
- Coo-Cah EMS policy engine
- ATS transfer logic and source-priority rules
- Energy dashboard and alerting controls
- Sandbox scenario validation before hardware handover

---

## 2. Governance, Ownership, and Success Criteria

### 2.1 Owner Set and Accountability

| Scope Area | Primary Owner | Co-Owners | Approval Required |
|---|---|---|---|
| EMS policy configuration | Energy Team Lead | MES/SCADA Lead, Facilities Electrical Lead | Yes |
| ATS/source-priority logic | Facilities Electrical Lead | Energy Team Lead, HSE | Yes |
| Dashboard and alert thresholds | MES/SCADA Lead | Energy Team Lead, Operations Control Tower | Yes |
| Production policy cutover | PMO + COO delegate | Energy, MES/SCADA, Facilities | Yes |

### 2.2 KPI and Alert Baseline (Locked Before Commissioning)

| KPI | M1.9 Commissioning Target | Steady-State Target | Warning | Critical |
|---|---|---|---|---|
| Solar self-sufficiency ratio | ≥ 75% (first 3 months) | ≥ 80% monthly | < 75% weekly trend | < 70% monthly |
| BESS SoC end-of-day | ≥ 25% | ≥ 25% | < 25% | < 20% |
| BESS SoH | ≥ 95% | ≥ 95% | < 95% | < 92% |
| Grid import share | ≤ 25% during stabilization | ≤ 20% monthly | > 25% | > 30% |
| Generator run hours | < 80 h/year trajectory | < 100 h/year | > monthly budget trajectory | Emergency-only policy breached |
| Energy intensity (phone) | ≤ 5.5 kWh during stabilization | ≤ 4.8 kWh | > 5.0 kWh | > 5.5 kWh |

### 2.3 Change-Control Matrix

| Configuration Class | Can Propose | Can Approve | Emergency Override | Audit Requirement |
|---|---|---|---|---|
| BESS dispatch policy | Energy Engineer | Energy Lead + MES/SCADA Lead | COO delegate + Facilities Lead | Ticket + before/after parameter snapshot |
| ATS priority/transfer timing | Facilities Engineer | Facilities Lead + HSE + Energy Lead | Facilities Lead + COO delegate | Test evidence + signed rollback path |
| Alert thresholds | MES/SCADA Analyst | MES/SCADA Lead + Energy Lead | MES/SCADA Lead | Alert tuning log + owner acknowledgement |

No policy change is promoted to production without sandbox replay evidence and rollback settings.

---

## 3. Load and Operating Profiles

### 3.1 Load-Tier Definition by Zone

| Tier | Priority | Representative Loads | EMS Rule Intent |
|---|---|---|---|
| Tier 1 | Critical | IT/MES servers, in-cycle RF test loads, fire/life safety systems | Must remain energized |
| Tier 2 | Essential | SMT lines, core phone assembly, battery QC/test | Maintain continuity through grid events |
| Tier 3 | Important | TWS/watch lines, packaging, warehousing | Sustain where capacity permits |
| Tier 4 | Deferrable | Non-critical HVAC zones, discretionary charging loads | Shed first under constraints |

### 3.2 Operating Profile Library

| Profile ID | Time/Condition | Expected Source Mix | Fallback State |
|---|---|---|---|
| `P01_NORMAL_PROD` | Standard production shift | Solar first, BESS peak-shaving/support, grid supplemental | Shed Tier 4 first |
| `P02_LOW_SOLAR` | Cloudy/low irradiance period | Grid + BESS reserve support | Restrict Tier 3/4 discretionary loads |
| `P03_NIGHT_BASELOAD` | Overnight base + prep ramp | BESS overnight support, controlled grid top-up | Protect emergency SoC floor |
| `P04_MAINTENANCE` | Planned maintenance windows | Grid-led with reduced dispatch | Force conservative BESS cycling |
| `P05_WEEKEND_LOWLOAD` | Weekend or low throughput | Solar charge-first, minimal dispatch | Maximize BESS reserve |
| `P06_GRID_OUTAGE_RECOVERY` | Utility outage and recovery | BESS immediate support; generator if reserve breached | Critical + essential loads only |

---

## 4. BESS Charging and Dispatch Policy

### 4.1 SoC Operating Bands

| Band | SoC Range | Operational Meaning | Allowed Actions |
|---|---|---|---|
| Normal operating band | 35–85% | Preferred daily dispatch range | Peak shaving, production support |
| Reserve protection band | 25–35% | Preserve backup readiness | Limited dispatch only |
| Emergency reserve band | 20–25% | Critical-load reserve only | Block non-critical dispatch |
| Critical floor | < 20% | Contingency state | Trigger generator/start emergency profile |

### 4.2 Charge/Discharge Windows and Priority

1. **Charge priority:** solar surplus first, then controlled grid top-up in approved windows.
2. **Dispatch priority:** peak shaving during production, overnight support only if reserve constraints are met.
3. **Outage policy:** reserve protection supersedes optimization policy.
4. **Top-up window:** pre-dawn or approved low-tariff window for reserve restoration where required.

### 4.3 Dispatch Modes

| Mode | Primary Objective | Entry Condition | Exit Condition |
|---|---|---|---|
| Peak shaving | Reduce grid peaks and tariff exposure | Production demand exceeds target import band | Demand normalizes or reserve band reached |
| Backup reserve | Maintain outage readiness | Active profile requires resilience posture | SoC restored above reserve minimum |
| Overnight support | Carry base load before solar pickup | Night profile active and SoC in allowed band | Morning ramp or reserve protection threshold |
| Emergency-only | Preserve Tier 1/Tier 2 continuity | Grid outage + SoC near critical floor | Grid stable and SoC restored |

### 4.4 Anti-Thrashing Rules

- Minimum source hold time after transfer before next transfer evaluation.
- Hysteresis margins around SoC and load thresholds.
- Cooldown timer after generator stop before re-evaluation.
- Transfer inhibit when interlock state is not healthy.

---

## 5. ATS and Source-Priority Logic

### 5.1 Source-Priority Matrix by Mode

| Mode | Priority 1 | Priority 2 | Priority 3 | Priority 4 |
|---|---|---|---|---|
| Normal day | Solar | BESS | Grid | Generator |
| Low-solar | Grid | Solar | BESS | Generator |
| Grid failure | Solar (if available) | BESS | Generator | — |
| Black-start | BESS | Generator | Grid (on return) | Solar reintegration |
| Recovery | Grid stabilization | Solar rebalance | BESS recharge | Generator offload |

### 5.2 Transfer Conditions and Interlocks

| Condition Type | Rule |
|---|---|
| Timing guards | Validate source quality stability window before transfer close |
| Break-before-make | Enforce ATS interlock and anti-parallel protection |
| Rapid-transfer prevention | Block repeated toggles within configured cooldown window |
| Source-quality checks | Frequency/voltage thresholds must pass before acceptance |

### 5.3 Generator Trigger Policy

| Trigger | Start Rule | Stop Rule |
|---|---|---|
| Low reserve during outage | SoC < 20% and outage active | SoC recovered above reserve and preferred source stable |
| Extended outage | Outage duration exceeds configured threshold while Tier 1/2 demand active | Grid/solar recovered and load risk cleared |
| Critical demand spike | Tier 1+Tier 2 demand cannot be met by current source set | Demand stabilized and BESS reserve restored |

---

## 6. Dashboard and Alert Configuration

### 6.1 Required Dashboard Layers

| Layer | Audience | Minimum Views |
|---|---|---|
| Plant overview | COO, PMO, Energy Leads | source mix, self-sufficiency, grid import %, BESS SoC/SoH, generator status |
| Zone/load detail | Operations, Facilities, Energy Engineers | kWh by zone, kWh per order, load tier state, transfer events timeline |
| Alarms/events operations | Control tower, on-call responders | active alarms, severity, acknowledgement status, SLA breach queue |

### 6.2 Alerting Model and Escalation

| Alert Class | Example Trigger | Owner | Ack SLA | Escalation |
|---|---|---|---|---|
| Warning | BESS SoC < 25% trend | Energy Shift Engineer | 15 min | Energy Lead |
| Critical | BESS SoC < 20% or ATS repeated transfer block | Facilities Electrical On-Call | 5 min | Facilities Lead + COO delegate |
| Compliance/performance | Monthly self-sufficiency < target band | Energy Control Tower | 1 business day | PMO governance review |

All alerts require acknowledgement logging and closure notes.

---

## 7. Sandbox Validation Before Hardware Installation

### 7.1 Mandatory Scenario Tests

| Scenario | Expected Validation Output |
|---|---|
| Sunny day profile | Solar-first dispatch and normal reserve behavior confirmed |
| Cloudy/low-solar day | Grid/BESS fallback and reserve protection confirmed |
| Night peak | Overnight support behavior and reserve floor enforcement confirmed |
| Grid outage | Correct ATS/source switch sequence with no unsafe oscillation |
| Extended outage | Generator trigger policy and Tier 1/2 continuity confirmed |
| Recovery sequence | Controlled return to normal priority and recharge behavior confirmed |

### 7.2 Evidence Pack Required for Sign-Off

- Baseline parameter export (EMS, ATS, alerts)
- Scenario-by-scenario pass/fail log and timestamps
- Dashboard screenshot pack for each scenario
- Known limitations and operational constraints
- Rollback profile and restoration steps

---

## 8. M1.9 Cutover Package and Post-Commissioning Cadence

### 8.1 Field Parameter Sheet (Mandatory)

| Parameter Group | Required Fields |
|---|---|
| Metering | Meter IDs, zone mapping, calibration status |
| Power switching | Breaker mapping, ATS I/O map, interlock verification |
| Source assets | Inverter IDs, BESS IDs, generator control endpoints |
| Integration endpoints | iSolarCloud keys, EMS bridge endpoints, dashboard datasource IDs |

### 8.2 Baseline Freeze Set

| Profile Set | Intent |
|---|---|
| Day-1 baseline | Conservative commissioning profile prioritizing resilience |
| Day-30 optimization | Tuned policy set after first-month operating evidence |

### 8.3 M1.9 Review Cadence

| Window | Cadence | Focus |
|---|---|---|
| First 2 weeks post-commissioning | Daily | SoC/transfer events, reserve protection, alert hygiene |
| Weeks 3–12 post-commissioning | Weekly | KPI trend stability, dispatch efficiency, threshold retuning approvals |

---

*Related references: [`automation-roadmap.md`](./automation-roadmap.md), [`energy-profile.md`](./energy-profile.md), [`mes-phase1-software-setup.md`](./mes-phase1-software-setup.md), [`dt-implementation-plan.md`](./dt-implementation-plan.md).*
