# Digital Twin — Implementation Plan

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State
> **Document Version:** 1.0 | **Owner:** Digital Manufacturing & AI Team
> **Guiding Principle:** MES-First, Twin Second — the digital twin grows from the MES, not beside it.

---

## 1. Overview

This document is the master implementation plan for building the Coo-Cah Personal Electronics Factory
Digital Twin from pre-construction through to a fully prescriptive twin by 2030. It is the actionable
companion to [`digital-twin.md`](./digital-twin.md), which defines the architecture, asset registry,
and simulation use cases.

The plan is structured across four phases:

| Phase | Period      | DT Maturity Level        | Trigger                                          |
|-------|-------------|--------------------------|--------------------------------------------------|
| 0     | Now → Q1 2026 | Foundation Prep        | Pre-construction; no machines required           |
| 1     | Q2–Q4 2026  | Descriptive Twin         | Factory commissioning begins                     |
| 2     | 2027–2028   | Diagnostic + Predictive  | Automation Phase 2 (cobots, AI vision)           |
| 3     | 2029–2030   | Prescriptive Twin        | Automation Phase 3 (lights-out SMT)              |

The platform stack is already decided (InfluxDB + FastAPI + Grafana + MQTT + OPC-UA, edge node on-site
+ Rwanda cloud hub). This plan assumes that platform decision is fixed and focuses on **what to build,
in what order, and why**.

---

## 2. Phase 0 — Foundation Prep (Now → Q1 2026)

### Objective

Complete all zero-cost and low-cost preparatory work before a single physical machine arrives.
These tasks have outsized leverage: mistakes made here cost 10–100× more to fix after commissioning.

Phase 0 is run as a **foundation-freeze programme**, not as an open-ended technology build.
The primary objective is to lock the data contract, topic namespace, infrastructure baseline,
and facility requirements early enough that commissioning does not re-open core design decisions.

### Execution Model

Phase 0 is governed through three coordinated workstreams with one shared control register in
[`dt-phase0-governance.md`](./dt-phase0-governance.md):

| Workstream | Scope | Primary Purpose | Critical Output |
|---|---|---|---|
| A — Data Contract & Standards | Task 0.1 + Task 0.5 | Freeze naming, schema, and telemetry expectations | Locked manifest + locked MQTT namespace |
| B — Platform Proving | Task 0.2 | Prove the DT stack against synthetic data before machine arrival | Running Rwanda dev stack + signed-off dashboards |
| C — Physical & Facility Readiness | Task 0.3 + Task 0.4 | Eliminate retrofit risk in BIM and building services | Imported IFC model + signed building services spec |

### Execution Order and Dependency Rules

The execution order is intentional and is not calendar-driven alone:

1. Launch Phase 0 governance and track all five outputs in the Phase 0 control register.
2. Finalise the asset manifest first; it is the anchor deliverable for every downstream DT design choice.
3. Lock the MQTT namespace immediately after the manifest is stable enough to prevent schema drift.
4. Run the Rwanda dev stack in parallel only against the controlled manifest/namespace baseline.
5. Pull the edge node specification into building-services sign-off before fit-out procurement hardens.
6. Manage BIM delivery to civil cadence, but enforce zone and asset naming alignment from the start.

The following dependency rules are mandatory:

- [ ] Asset manifest reaches controlled baseline before MQTT namespace lock.
- [ ] Asset manifest + MQTT namespace align before full synthetic data generator design.
- [ ] Infrastructure and edge requirements are approved before fit-out procurement freeze.
- [ ] As-built BIM is required before spatial acceptance.
- [ ] All locked artifacts are required before first machine FAT and commissioning.

### Governance Output

The formal Phase 0 governance artifact is [`dt-phase0-governance.md`](./dt-phase0-governance.md).
It records workstreams, task ownership, blockers, approval criteria, dependency controls, and the
completion review structure for all five Phase 0 outputs.

### Task 0.1 — Publish the Asset Data Manifest

**Owner:** Digital Manufacturing Team + MES Team
**Deadline:** Before factory civil works complete (M1.1)
**Output:** [`dt-asset-manifest.md`](./dt-asset-manifest.md) — promoted from controlled draft to locked standard

The asset manifest is the contractual schema between the MES team and the DT team. Every one of the
142 registered physical assets must have a formally defined data contract: Asset ID, zone, protocol,
sensor list, data types, units, update frequency, and expected operating ranges.

Key actions:

- [ ] Review all 142 asset IDs in the asset registry ([`digital-twin.md`](./digital-twin.md) §2).
- [ ] Assign a primary protocol and update rate to every asset.
- [ ] Define expected operating range for each sensor (used for anomaly detection baseline).
- [ ] Lock the manifest in version control. Any change after machine commissioning requires a formal
      change request — this prevents schema drift.
- [ ] Publish the manifest to the group MES integration standards path in Coo-Kah-Doks.

> **Why this matters first:** Every downstream step — MQTT topic design, InfluxDB schema, Grafana
> dashboard, predictive model inputs — depends on this manifest. Do it wrong and you rebuild
> everything.

---

### Task 0.2 — Deploy DT Infrastructure Stack in Dev Mode

**Owner:** IT/OT Infrastructure Team
**Deadline:** Q3 2025 (six months before commissioning)
**Output:** Running dev instance on Rwanda cloud hub; see [`dt-infrastructure.md`](./dt-infrastructure.md)

Stand up the full Coo-Cah DT Engine in a development environment on the Rwanda cloud hub
*before any machines exist*. Use synthetic data generators to simulate all 142 assets at the designed
update rates.

> **Entry condition:** Task 0.1 and Task 0.5 must be stable enough to provide the schema and topic
> baseline for synthetic publishers, Telegraf mappings, and Grafana panels.

Key actions:

- [ ] Provision Rwanda cloud hub compute node (minimum: 16 vCPU, 64 GB RAM, 4 TB NVMe).
- [ ] Deploy InfluxDB 2.x (OSS or Cloud) with bucket schema matching the asset manifest.
- [ ] Deploy FastAPI backend service with asset registry endpoint and time-series query proxy.
- [ ] Deploy Grafana (with InfluxDB and MQTT datasources configured).
- [ ] Stand up Mosquitto MQTT broker with TLS; configure topic namespace per
      [`dt-mqtt-namespace.md`](./dt-mqtt-namespace.md).
- [ ] Write synthetic data generators for all 11 production zones at correct update rates.
- [ ] Build the first Grafana dashboards against synthetic data; validate layout before real
      data arrives.
- [ ] Document the deployment runbook so the on-site edge node can be commissioned identically.

---

### Task 0.3 — Commission the BIM / 3D Spatial Model

**Owner:** Civil & Industrial Engineering Team
**Deadline:** Q1 2026 (as-built, concurrent with civil construction completion)
**Output:** IFC-format 3D model of 18,000 m² floor; registered in DT platform

The 3D spatial model must be built from the **as-built** civil drawings, not design drawings, to
capture actual column positions, aisle widths, and machine footprints accurately. This becomes the
persistent spatial reference for the DT floor visualisation and, in Phase 3, for simulation
collision detection.

> **Control rule:** Zone naming and asset footprint identifiers must stay aligned with the asset
> manifest and MQTT namespace from the start, even if final IFC acceptance waits for as-built issue.

Key actions:

- [ ] Commission BIM contractor during civil construction; deliverable is IFC + DWG format.
- [ ] Define zone boundaries (Z1–Z12) as named regions in the model, matching zone IDs in the
      asset manifest and MQTT namespace.
- [ ] Place all 142 asset footprints in the model at their as-built positions.
- [ ] Import model into DT platform spatial layer; verify zone/asset ID alignment.
- [ ] Establish a model update protocol: any equipment move triggers a BIM update within 5 business
      days.

---

### Task 0.4 — Embed DT Edge Node Requirements in Building Services Spec

**Owner:** Factory Engineering Team + IT/OT Infrastructure Team
**Deadline:** Before contractor appointment for fit-out (Q4 2025)
**Output:** DT Edge Node section added to Building Services Specification

The edge node cannot be retrofitted. It must be designed into the building services from day one:
dedicated rack space, power, cooling, and the OT/IT network segregation. See
[`dt-infrastructure.md`](./dt-infrastructure.md) §3 for the full edge node specification.

> **Priority rule:** Treat this as an early design-freeze task. If fit-out procurement hardens before
> the DT edge node requirements are embedded, retrofit cost and commissioning risk rise materially.

Key requirements to embed in the Building Services Spec:

| Requirement | Specification |
|---|---|
| Rack space | 1 × 42U rack in Z12 (MES/Engineering room); raised floor tile under rack |
| Power supply | Dual-feed UPS-backed circuits; 5 kVA minimum per rack |
| Cooling | Rack-inlet temp ≤ 22°C; Z12 HVAC independent of production zone HVAC |
| OT LAN ports | 2× 10 GbE uplinks from OT switch to MES/DT rack |
| Cloud WAN | Dedicated 100 Mbps WAN circuit (minimum); Starlink backup |
| Fibre backbone | Factory-wide single-mode fibre backbone; one drop per production zone |

---

### Task 0.5 — Define and Lock the MQTT Topic Namespace

**Owner:** Digital Manufacturing Team
**Deadline:** At least 4 weeks before first machine FAT (Factory Acceptance Testing)
**Output:** [`dt-mqtt-namespace.md`](./dt-mqtt-namespace.md) — promoted from controlled draft to locked and version-controlled

Changing MQTT topic names after machines are wired is operationally expensive: every subscriber
must be updated, and any gap creates data loss or duplication.

Key actions:

- [ ] Define the full topic hierarchy for all 142 assets using the canonical pattern:
      `cce/sag/{zone_id}/{asset_id}/{metric_id}`
- [ ] Assign QoS levels per asset type (QoS 1 for production data; QoS 0 for high-frequency
      telemetry like AMR position).
- [ ] Agree retained message policy with MES team (last known state should be retained for
      all production machine status topics).
- [ ] Lock the namespace document. Post-lock changes require a formal change request with
      impact assessment.
- [ ] Include MQTT topic map in the FAT checklist for every machine vendor.

---

### Phase 0 Completion Gate

Phase 0 is complete when all five tasks are done **and** verified:

- [ ] Asset manifest published and accepted by MES team lead.
- [ ] Dev DT stack running on Rwanda cloud hub; synthetic dashboards signed off.
- [ ] BIM model IFC file received from civil contractor and imported into DT platform.
- [ ] Edge node requirements signed off in Building Services Spec.
- [ ] MQTT namespace document locked in version control.

### Phase 0 Close-Out Review

Phase 0 closes only after a formal review chaired by the Digital Manufacturing Team Lead with the
MES Team Lead, IT/OT Infrastructure Lead, and Factory Engineering representative. The review must:

- [ ] confirm that all task outputs satisfy the approval criteria recorded in the Phase 0 governance register;
- [ ] confirm that the manifest, namespace, infrastructure baseline, and BIM naming model are mutually aligned;
- [ ] record any residual actions as post-Phase-0 carry-over items owned by named leads;
- [ ] issue a go / no-go decision for first-machine FAT readiness.

---

## 3. Phase 1 — Descriptive Twin (Q2–Q4 2026)

### Objective

A live, read-only mirror of the factory's physical state. All 142 assets are visible in the DT.
Data lag ≤ 1 second. The twin cannot yet act on anything; it only observes and reports.

This phase runs **concurrently with factory commissioning** — the DT is wired in zone by zone as
each production area comes live.

---

### Step 1.1 — SMT Lines 1 & 2 (Highest Priority, Highest Data Density)

**Trigger:** SMT Line 1 commissioned (Automation Milestone M1.2)
**Assets:** DT-SMT-L1-01 to -10, DT-SMT-L2-01 to -10 (20 assets, ~840 data points)
**Protocols:** SECS/GEM (DEK, JUKI, Koh Young), OPC-UA (Heller, Ersa), Ethernet API (Keysight)

The two SMT lines are the richest data source in the factory and the fastest path to demonstrating DT
value. Wiring the DT on Day 1 of SMT commissioning means the engineering team can see process health
on the same day a board comes off the line.

Key actions:

- [ ] Validate SECS/GEM connectivity for DEK screen printers and JUKI P&P machines at FAT.
- [ ] Confirm Heller oven OPC-UA server address space against asset manifest sensor list.
- [ ] Map all 420 data points per SMT line to their MQTT topics and InfluxDB measurements.
- [ ] Publish first production Grafana dashboard: SMT Line Health (zone temps, paste CPK,
      reflow profile, FPY per board, feeder error count).
- [ ] Validate data latency: ≤ 1 second from machine event to InfluxDB write to Grafana render.
- [ ] Repeat for SMT Line 2 at M1.2 or M1 Line 2 commissioning.

**Phase 1 Grafana Dashboards — SMT:**

| Dashboard | Panels | Audience |
|---|---|---|
| SMT Line 1 Overview | Reflow zone temps ×8, paste CPK, FPY trend, feeder error rate | Production engineer |
| SMT Line 2 Overview | Same layout as Line 1 | Production engineer |
| SMT Cross-Line Compare | Side-by-side Line 1 vs Line 2 OEE, FPY, changeover time | Shift supervisor |

---

### Step 1.2 — AMR Fleet Twin (Most Visually Compelling Stakeholder Demo)

**Trigger:** AMR fleet commissioned (Automation Milestone M1.3)
**Assets:** DT-AMR-MIR250-01 to -12, DT-AMR-MIR100-01 to -04, DT-AMR-DOCK-01 to -18 (34 assets)
**Protocol:** MiR Fleet Manager REST API → MQTT bridge

The live AMR position map is the single most compelling early DT demonstration for stakeholders,
investors, and operators. It makes the digital twin tangible to non-technical audiences immediately.

Key actions:

- [ ] Build MQTT bridge from MiR Fleet Manager API to the DT MQTT broker (1-second poll).
- [ ] Publish (x, y, θ), speed, battery SoC, mission ID, and mission status per AMR.
- [ ] Build the 2D floor plan overlay in Grafana (SVG background = factory floor layout from BIM)
      with AMR icons positioned at live coordinates.
- [ ] Build AMR Fleet Health dashboard: per-AMR battery SoC, mission success rate,
      dock occupancy map, daily mission count.
- [ ] Validate all 18 charging dock occupied/charging signals reach DT.

---

### Step 1.3 — Energy System Twin (Solar + BESS + Grid)

**Trigger:** Solar and BESS commissioned (Automation Milestone M1.9)
**Assets:** DT-EN-PV-01 to -03, DT-EN-BESS-01 to -02, DT-EN-INV-01 to -04, DT-EN-GEN-01,
           DT-EN-GRID-01, DT-EN-HVAC-01 to -02 (13 assets, ~400 data points)
**Protocol:** Sungrow iSolarCloud API → InfluxDB; Modbus TCP for grid meter and generator

Key actions:

- [ ] Configure iSolarCloud API integration; validate solar generation, BESS SoC, and inverter
      efficiency data flows into InfluxDB.
- [ ] Build the Energy Overview dashboard with the critical KPI tile: **Solar Self-Sufficiency
      Ratio** (solar generation ÷ total consumption × 100%, target ≥ 80%).
- [ ] Calculate and display **Energy Intensity per unit** (kWh/phone, kWh/earbud pair) by
      combining EMS energy data with MES production count data.
- [ ] Wire BESS SoC and SoH alerts: alert at SoC < 20% and SoH < 95%.

**Phase 1 Energy KPI Tile Targets:**

| KPI | Target | Alert Threshold |
|---|---|---|
| Solar Self-Sufficiency | ≥ 80% (monthly) | < 70% triggers review |
| BESS SoC (end of day) | ≥ 25% | < 20% = generator auto-start |
| Grid Import Share | ≤ 20% | > 25% triggers ops review |
| Energy/Phone | ≤ 4.8 kWh | > 5.5 kWh = production review |
| Generator Run Hours | < 100 hrs/year | > 80 hrs at any month triggers review |

---

### Step 1.4 — Phone & Test Assembly Zones

**Trigger:** Phone assembly lines live (Automation Milestone M1.5)
**Assets:** DT-PH-01 to -07, DT-TWS-01 to -03, DT-SW-01 to -02, DT-PB-01 to -03,
           DT-RF-01 to -06 (22 asset groups)
**Protocols:** OPC-UA (torque stations), REST API (flash, function test, battery tester),
               VISA/LAN (R&S CMW500), Ethernet API (Cognex, Chroma)

Key actions:

- [ ] Wire Atlas Copco torque station OPC-UA feeds; validate per-screw torque values appear
      in unit trace records within 2 seconds of tightening.
- [ ] Wire phone flash and function test fixture REST APIs; validate IMEI, firmware version,
      and all per-test pass/fail results populate MES trace and DT simultaneously.
- [ ] Wire R&S CMW500 RF test results into DT; verify NCC RF sample flagging appears in DT
      NCC Compliance dashboard.
- [ ] Build Phone Assembly Zone dashboard: live units/hour per line, flash yield, function
      test yield, torque NOK alert count.
- [ ] Build RF & NCC Lab dashboard: chamber utilisation %, RF test pass rate per band,
      NCC TA sample log with certificate status.

---

### Phase 1 Deliverables & Acceptance Criteria

| Deliverable | Acceptance Criterion |
|---|---|
| Factory-wide Grafana dashboard (all 11 zones) | All 142 assets show live status; data lag ≤ 1 second |
| AMR fleet 2D position map | All 16 AMRs visible; position updates ≤ 1 second |
| Energy self-sufficiency tile | Solar self-sufficiency KPI updates every 5 minutes |
| Per-unit serial trace in DT | SMT → Assembly → Test → Dispatch trace readable in DT within 1 second of each event |
| NCC RF test dashboard | Each R&S CMW500 RF test result appears in DT within 5 seconds of test completion |
| Alerting | All critical alerts (machine fault, BESS SoC, yield drop) fire within 30 seconds |

---

## 4. Phase 2 — Diagnostic + Predictive Twin (2027–2028)

### Objective

The twin not only mirrors reality — it explains *why* things are happening and forecasts
*what will happen next*. Phase 2 is gated by Automation Phase 2 milestones (cobots, AI vision,
predictive maintenance AI).

---

### Step 2.1 — Predictive Maintenance Models

**Trigger:** Phase 1 data baseline collected (minimum 6 months of Phase 1 data required)
**AI Platform:** Coo-Cah AI Platform (as defined in Coo-Kah-Doks `docs/ai/platform.md`)

Three predictive models are deployed in Phase 2:

**Model A — Reflow Oven Thermal Degradation (DT-SMT-L1-05, DT-SMT-L2-05)**

- Input features: Heating element current draw per zone, zone temperature delta vs. setpoint,
  oven age (hours since service), conveyor speed, N₂ consumption trend.
- Target: Predict heating element failure probability within next 72 hours.
- Alert action: Maintenance work order created in MES CMMS; DT displays predicted failure date.
- Success criterion: Unplanned SMT oven downtime < 2% (Automation Milestone M2.4).

**Model B — JUKI P&P Feeder Vibration Model (DT-SMT-L1-03/04, DT-SMT-L2-03/04)**

- Input features: Per-feeder vibration signature (FFT), feeder age (cycles), miss-pick rate
  trend, component type.
- Target: Flag feeder wear pattern before first miss-pick event; predict replacement window.
- Alert action: Feeder-level maintenance alert in MES; DT displays feeder health heatmap.
- Success criterion: SMT FPY maintained ≥ 98.5% (Phase 2 target).

**Model C — AMR Battery State-of-Health (DT-AMR-MIR250-01 to -12, DT-AMR-MIR100-01 to -04)**

- Input features: SoC trajectory per charge cycle, charge acceptance rate, ambient temperature,
  missions per day, age in calendar days and cycle count.
- Target: Predict per-AMR battery replacement window 30 days in advance.
- Alert action: Scheduled replacement order raised in MES CMMS; DT displays SoH trend and
  predicted end-of-life date.
- Success criterion: AMR availability ≥ 98.5% (Phase 2 target); zero surprise AMR failures.

---

### Step 2.2 — Cobot & SCARA Kinematics Model

**Trigger:** UR20 cobots commissioned at Z4 (Automation Milestone M2.1–M2.2)
**New Assets:** UR20 cobot joints ×(number deployed), Epson SCARA G-Series joints ×(number deployed)

Key actions:

- [ ] Add cobot joint angle (θ1–θ6), joint torque, TCP speed, and cycle time to asset manifest
      (Phase 2 extension).
- [ ] Import UR20 URDF kinematic model into DT spatial layer; link to live joint angle feed.
- [ ] Build Cobot Cell dashboard: cycle time trend, joint torque vs. nominal, collision zone
      violation alerts.
- [ ] Enable "virtual commissioning" mode: engineers can simulate a cobot path change in the
      DT before executing on the live machine.
- [ ] Validate Phase 2 DT data lag ≤ 500 ms (Automation Milestone M2.9).

---

### Step 2.3 — AI Vision Inference Twin

**Trigger:** AI Vision 100% QC deployed (Automation Milestone M2.3)
**Asset:** DT-PH-06 (Cognex IS9000 ×2), Z9 Final QC cameras

The Phase 1 twin already streams defect class and confidence scores from Cognex IS9000 to the DT.
In Phase 2, this data is correlated with upstream process parameters:

Key actions:

- [ ] Build a correlation analysis pipeline: for each cosmetic defect class, automatically
      query the upstream SMT paste volume, reflow profile, and assembly torque records for
      that unit's serial number.
- [ ] Display defect root-cause correlation matrix in DT (defect class → most likely upstream
      cause → confidence).
- [ ] Set up automated alert: if cosmetic escape rate trends above 150 PPM, the DT auto-generates
      a root-cause investigation task in MES.
- [ ] Target: cosmetic defect escape ≤ 200 PPM (Automation Milestone M2.3).

---

### Step 2.4 — Discrete Event Simulation (DES) Layer

**Trigger:** Minimum 9 months of Phase 1 production data collected (used as DES calibration input)
**Tool:** Integrated into Coo-Cah DT Engine simulation framework (DES + process physics models)

Key actions:

- [ ] Calibrate DES model using Phase 1 actual cycle times, yield rates, changeover times,
      and AMR travel times.
- [ ] Build production ramp simulation: simulate ramp from 500k to 1M phones/year; identify
      bottleneck stations before committing to a schedule change.
- [ ] Run product mix scenario planning: model factory OEE for different phone/earbud/watch
      volume mix combinations.
- [ ] Build NPI simulation: for each new product introduction, simulate cycle time and yield
      before physical first article runs.
- [ ] Gate: all DES simulation results must be reviewed and signed off by Factory Manager and
      Industrial Engineering before being used for live production planning decisions.

---

### Phase 2 Deliverables & Acceptance Criteria

| Deliverable | Acceptance Criterion |
|---|---|
| Predictive maintenance models live (3 models) | M2.4: Unplanned SMT downtime < 2%; AMR availability ≥ 98.5% |
| Cobot kinematics model in DT | M2.9: DT data lag ≤ 500 ms |
| AI vision root-cause correlation | Cosmetic escape ≤ 200 PPM; auto-investigation trigger working |
| DES production ramp simulation | First DES scenario reviewed and accepted by Factory Manager |

---

## 5. Phase 3 — Prescriptive Twin (2029–2030)

### Objective

The twin recommends actions; humans approve and execute. Phase 3 supports near-lights-out SMT
operation and adaptive AI-driven production scheduling.

---

### Step 3.1 — Lights-Out SMT Simulation

**Trigger:** Lights-out SMT trial preparation (Automation Milestone M3.2, Q2 2029)

Before any unmanned overnight SMT run, run thousands of simulated scenarios in the DT to find
the edge cases that would cause an unplanned stop without a human present to intervene.

Key actions:

- [ ] Run 1,000+ overnight scenario simulations in DES: vary reflow oven health state, feeder
      wear state, board warpage probability, N₂ supply pressure fluctuations, power grid
      interruptions.
- [ ] Identify the top-5 failure modes from simulation; verify each has an automated recovery
      path or auto-halt procedure defined in the MES.
- [ ] Only proceed to physical lights-out trial (M3.2) when DT simulation shows ≥ 95% of
      scenarios complete successfully (< 1 unplanned stop per simulated 8-hour run).
- [ ] Success criterion: Physical overnight OEE ≥ 87% vs daytime baseline (M3.2).

---

### Step 3.2 — Adaptive WIP AI

**Trigger:** Adaptive WIP AI deployment (Automation Milestone M3.3, Q3 2029)

The DT feeds real-time queue depths, machine states, and downstream order priorities into the
AI scheduling engine, which prescribes the optimal production sequence. The MES executes the
recommendation after supervisor approval.

Key actions:

- [ ] Connect DT real-time WIP queue depth data to the AI scheduling API
      (see `mes-integration.md` §6.3).
- [ ] Build the Scheduling Recommendation dashboard: shows current vs. recommended production
      sequence, predicted OEE impact of the recommendation, one-click "Accept" action.
- [ ] Implement supervisor approval workflow: no AI recommendation executes without
      Supervisor-level MES approval.
- [ ] Gate: AI scheduling must demonstrate ≥ 94% on-time completion in simulation (M2.7)
      before being enabled in prescriptive mode.

---

### Step 3.3 — BESS Dispatch Optimisation

**Trigger:** Phase 3 energy optimisation (concurrent with M3.3–M3.6)

Move from reactive energy management (the EMS responds to conditions as they occur) to proactive
(the DT prescribes the optimal BESS charge/discharge schedule 24 hours in advance).

Key actions:

- [ ] Integrate weather forecast API (72-hour solar irradiance forecast for Sagamu, Ogun State).
- [ ] Integrate NERC/DisCo ToU tariff schedule (time-of-use pricing periods).
- [ ] Build BESS Dispatch Optimiser: DES simulation of 24-hour BESS dispatch scenarios;
      outputs optimal charge/discharge schedule to minimise grid import cost.
- [ ] Publish daily BESS dispatch recommendation to EMS; EMS operator reviews and approves
      before implementation.
- [ ] Target: generator run hours < 100 hrs/year; grid import ≤ 15% (Phase 3 stretch target).

---

### Phase 3 Deliverables & Acceptance Criteria

| Deliverable | Acceptance Criterion |
|---|---|
| Lights-out SMT simulation complete | 1,000+ scenarios run; top-5 failure modes identified and mitigated |
| Adaptive WIP AI live | M3.3: WIP turns > 8×/day; no starvation events; schedule adherence ≥ 94% |
| BESS dispatch optimisation live | Generator run hours < 100 hrs/year; grid import ≤ 15% |
| Phase 3 OEE | M3.6: Blended OEE ≥ 88%; SMT OEE ≥ 92% |

---

## 6. Immediate Actions — Top 5 (Do Now)

These five actions cost almost nothing and have the highest leverage. They must be completed
before any factory construction or commissioning begins.

| # | Action | Owner | Deadline | Document |
|---|---|---|---|---|
| 1 | Publish the asset data manifest (YAML schema for all 142 assets) | Digital Mfg Team | 2 weeks | [`dt-asset-manifest.md`](./dt-asset-manifest.md) |
| 2 | Deploy DT infrastructure stack in dev mode on Rwanda cloud hub | IT/OT Infra Team | 6 weeks | [`dt-infrastructure.md`](./dt-infrastructure.md) |
| 3 | Define and lock the MQTT topic namespace | Digital Mfg Team | 4 weeks | [`dt-mqtt-namespace.md`](./dt-mqtt-namespace.md) |
| 4 | Embed DT edge node requirements into building services spec | Factory Eng Team | Before contractor appt | [`dt-infrastructure.md`](./dt-infrastructure.md) §3 |
| 5 | Wire SMT Line 1 DT integration as the Phase 1 pilot | Digital Mfg + MES | At SMT FAT (M1.2) | This document §3 Step 1.1 |

---

## 7. Key Risk Register

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| OT connectivity failure at commissioning — machine vendor does not provide working SECS/GEM or OPC-UA interface | High | High | DT team present at machine FAT; connectivity verified before machines ship to Sagamu; protocol fallback (Modbus TCP) pre-agreed with vendor |
| Schema drift — asset manifest not maintained after initial publication | Medium | High | Manifest locked in version control; change request process enforced; quarterly manifest audit by Digital Mfg team lead |
| Data volume exceeds edge node storage — InfluxDB retention policy not set correctly | Medium | Medium | Phase 0 Task 0.2 includes retention policy configuration; 90-day raw edge cache as per DT data governance spec |
| Rwanda cloud hub WAN link failure — DT loses cloud sync | Low | Low | Edge node operates autonomously for up to 72 hours; local Grafana dashboards remain live; cloud sync resumes when link restored |
| Phase 2 DES calibration inaccurate — DES model not trusted by Factory Manager | Low | High | DES calibrated on minimum 9 months Phase 1 data; calibration validation report produced before DES used for planning decisions |
| MQTT topic namespace changed after machine commissioning | Low | High | Namespace locked in Phase 0; formal change request required post-lock; all changes logged and announced to all subscribers |

---

## 8. Roles & Responsibilities

| Role | Responsibilities |
|---|---|
| Digital Manufacturing Team Lead | Owns this document; governs asset manifest and MQTT namespace; approves Phase gate completions |
| MES Team Lead | Owns machine-to-MES data flows; must co-sign asset manifest; validates MES → DT sync |
| IT/OT Infrastructure Lead | Owns DT infrastructure stack deployment and operation; edge node and Rwanda cloud hub |
| Factory Engineering Manager | Embeds DT edge node requirements in building services spec; manages FAT attendance plan |
| AI Platform Lead (Coo-Kah Group) | Owns Phase 2 predictive models; integrates with Coo-Kah AI Platform |
| Factory Manager | Approves Phase gate completions; signs off DES recommendations before live use |

---

*Asset manifest: [`dt-asset-manifest.md`](./dt-asset-manifest.md)*
*MQTT namespace: [`dt-mqtt-namespace.md`](./dt-mqtt-namespace.md)*
*Infrastructure & network architecture: [`dt-infrastructure.md`](./dt-infrastructure.md)*
*Digital twin architecture & asset registry: [`digital-twin.md`](./digital-twin.md)*
*Automation milestones: [`automation-roadmap.md`](./automation-roadmap.md)*
*MES integration protocols: [`mes-integration.md`](./mes-integration.md)*
