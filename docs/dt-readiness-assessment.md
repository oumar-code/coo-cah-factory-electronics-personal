# Digital Twin Readiness Assessment — Personal Electronics Factory

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1
> **Document Version:** 1.1 | **Owner:** Digital Manufacturing Team Lead + PMO
> **Assessment Date:** 2026-06-03
> **Master Standards Reference:** [Coo-Kah-Doks — docs/orchestration/dt-readiness-control-tower.md](https://github.com/oumar-code/Coo-Kah-Doks/blob/main/docs/orchestration/dt-readiness-control-tower.md)
> **DT Role:** **Primary DT Pilot Factory** — designated proving ground for group-wide Wave 0/1 rollout

---

## ⚠ DT-Ready Status: PRE-COMMISSIONING (NOT RELEASE READY)

The hard release rule in the group scorecard requires **all three** conditions below to be green.

| Condition | Status | Blocking Reason |
|---|---|---|
| All mandatory artifacts complete and validated | 🔴 Actionable (targeted close-out in progress) | `dt-asset-manifest.md` not yet co-signed; `sensor-map.md` full population pending vendor export; BIM IFC acceptance + GUID replacement pending contractor handover |
| Live data connectivity proven for critical assets | 🟠 Construction-gated (blocked by commissioning dependency) | No commissioned machines yet; unblock trigger set to first critical asset energization with Day-0/Day-7 protocol pre-approved in `dt-live-connectivity-commissioning-protocol.md` |
| ≥ 3 DT simulations with reproducible evidence lineage | 🟢 Met (offline pre-commissioning baseline) | Three deterministic simulation runs archived with lineage in `dt-simulation-evidence-lineage.md` and `dt-phase1/evidence/simulations/2026-06-03-*.json` |

Score alone cannot override this rule. This assessment reflects **documentation and execution readiness**,
not live-operational readiness.

---

## 0. Two-Gate Strategy (2026-06-03 Implementation)

The hard release rule is preserved with a two-gate operating model:

- **Gate A — Pre-Commissioning Readiness:** close all controllable documentation/simulation evidence now.
- **Gate B — Commissioning Runtime Proof:** execute live connectivity proof immediately when critical assets are energized.

### Gate A (Now)

- Condition 1 is tracked as active close-out (DOC-01, DOC-02, DOC-03, DOC-04).
- Condition 2 is closed with deterministic offline evidence lineage (3/3 mandatory simulations complete).

### Gate B (On Energization Trigger)

- Condition 3 remains construction-gated until commissioning.
- Execution and evidence requirements are locked in `dt-live-connectivity-commissioning-protocol.md`.
- Day-0 and Day-7 evidence packs are pre-defined to shorten time-to-green after machine arrival.

### Temporary Exception Governance Path

An exception request can be submitted **only for Condition 3** while the site is still under construction.
The request is valid only if:

1. Conditions 1 and 2 are actively controlled (with Condition 2 green).
2. Condition 3 includes owner, unblock trigger, and pre-approved commissioning protocol.
3. Waiver validity is time-bound to commissioning milestones and reviewed weekly in governance cadence.

---

## 1. DT Readiness Scorecard

Scored against the group standard from
[`docs/orchestration/dt-readiness-control-tower.md`](https://github.com/oumar-code/Coo-Kah-Doks/blob/main/docs/orchestration/dt-readiness-control-tower.md).

| Dimension | Weight | Score | Justification |
|---|---:|---:|---|
| Documentation foundation | 25 | **20** | All 5 required docs exist (`digital-twin.md`, `sensor-map.md`, `bim/zone-boundaries.md`, `bim/asset-anchors.md`, `mes-integration.md`) and are mutually cross-linked with version-controlled status. Deduction: `sensor-map.md` full population pending vendor export (2026-06-15); BIM docs in Controlled Draft pending as-built IFC acceptance (2026-06-30); `dt-asset-manifest.md` pending MES co-sign. |
| Asset + spatial coverage | 20 | **14** | 142 assets in manifest with full YAML schema (protocols, update frequencies, expected ranges). Zone definitions for Z1–Z12 with exact coordinates. Anchor X/Y/Z defined for all 142 assets. Deduction: IFC GUIDs all still `{GUID-<ASSET>-REPLACE}`; 3D model not yet imported into DT platform; sensor registry rows pending vendor delivery. |
| Integration design readiness | 20 | **15** | `mes-integration.md` comprehensive with factory-specific protocols (SECS/GEM, OPC-UA, REST API, MQTT per zone), architecture diagram, and connector ownership. `dt-infrastructure.md` provides deployment baseline; `dt-mqtt-namespace.md` in Controlled Draft. Deduction: Rwanda dev stack (Task 0.2) in Planned status — not yet live; no synthetic-data sign-off evidence archived. |
| Governance + ownership | 15 | **13** | Named owners across all Phase 0 workstreams. Weekly governance cadence defined (Tue steering + Thu working session). Sign-off matrix and exit-gate evidence ledger defined in `dt-phase0-governance.md`. Active programme control in `bim-simulation-readiness-program.md`. Due dates on all open items. Deduction: Phase 0 not yet closed — Tasks 0.2, 0.3, 0.4 still Planned; key sign-offs outstanding. |
| Simulation readiness | 10 | **7** | 14 use cases across 4 categories (production, predictive maintenance, energy optimisation, quality) in `digital-twin.md`, all with KPI linkage. Offline simulation baseline code at `dt-phase1/services/offline_simulation.py`. Deduction: no experiment design frozen per `dt-pilot-standards-and-templates.md`; acceptance gate checklist unchecked; zero runs with archived output. |
| Execution evidence | 10 | **7** | Comprehensive execution pack exists: `dt-implementation-plan.md`, `dt-phase1/` scaffold (docker-compose, synthetic publisher, coverage validator, offline sim), `gap-closure-report.md`, `bim-simulation-readiness-program.md`. Deduction: acceptance gate evidence not yet archived; Rwanda dev stack not live; no live telemetry to date. |
| **Total** | **100** | **76** | |

> **Interpretation:** Score of 76 reflects strong documentation and execution-planning maturity — the
> highest in the group portfolio at this stage of the pilot. Remaining gap is entirely runtime and
> commissioning-dependent: live connectivity, simulation evidence, and Phase 0 close-out.

---

## 2. Gap List

All open gaps are classified across the five triage buckets defined in the
[DT Readiness Control Tower](https://github.com/oumar-code/Coo-Kah-Doks/blob/main/docs/orchestration/dt-readiness-control-tower.md).
Severity: 🔴 Red (owner within 2 business days) | 🟡 Amber (closure plan within 5 business days) | 🟢 Green (monitor)

### 2.1 Documentation

| Gap ID | Gap Description | Severity | Named Owner | Due Date | Evidence / Source |
|---|---|---|---|---|---|
| DOC-01 | `sensor-map.md` full population (~2,800 rows): only zone summaries and representative entries present; rows for the full sensor inventory blocked on MES vendor export | 🔴 | MES Team Lead | 2026-06-15 | `gap-closure-report.md` Pass 8; `bim-simulation-readiness-program.md` Item 3 |
| DOC-02 | `bim/zone-boundaries.md` final Z-range and as-built coordinate confirmation: coordinates defined from design drawings, not accepted IFC | 🟡 | Civil & Industrial Engineering Lead | 2026-06-30 | `gap-closure-report.md` Pass 7; `bim-simulation-readiness-program.md` Item 1 |
| DOC-03 | `bim/asset-anchors.md` IFC GUID replacement for all 142 assets: all entries still carry `{GUID-<ASSET>-REPLACE}` controlled pending tags | 🟡 | Civil & Industrial Engineering Lead | 2026-06-30 | `bim/asset-anchors.md` Section 1.1; `bim-simulation-readiness-program.md` Item 2 |
| DOC-04 | `dt-asset-manifest.md` MES Team Lead co-sign pending — manifest in Controlled Draft status; lock cannot proceed without co-sign | 🔴 | Digital Manufacturing Team Lead + MES Team Lead | 2026-06-22 | `dt-phase0-governance.md` Task 0.1; `dt-asset-manifest.md` lock policy |
| DOC-05 | `dt-mqtt-namespace.md` lock pending: retained-message policy agreement and FAT checklist references not yet confirmed | 🟡 | Digital Manufacturing Team Lead | 2026-06-29 | `dt-phase0-governance.md` Task 0.5; dependency: DOC-04 must close first |
| DOC-06 | Building Services Specification (Task 0.4) not yet updated with edge node requirements (rack, power, cooling, fibre, OT LAN, WAN, backup) | 🟡 | Factory Engineering Lead | Before fit-out procurement freeze | `dt-phase0-governance.md` Task 0.4 |

### 2.2 Data Integration

| Gap ID | Gap Description | Severity | Named Owner | Due Date | Evidence / Source |
|---|---|---|---|---|---|
| INT-01 | Rwanda cloud hub dev stack (Task 0.2) not provisioned: `docker-compose.yml` is ready and `dt-infrastructure.md` defines the stack, but cloud hub not yet standing; no synthetic data flowing | 🔴 | IT/OT Infrastructure Lead | 2026-07-15 | `dt-phase0-governance.md` Task 0.2; `dt-phase1-software-infrastructure.md` |
| INT-02 | Synthetic telemetry sign-off evidence not archived: all acceptance gate checklist items in `dt-phase1-software-infrastructure.md` remain unchecked | 🟡 | IT/OT Infrastructure Lead | 2026-07-31 | `dt-phase1-software-infrastructure.md` acceptance-gate checklist |
| INT-03 | Live OT connector stubs unproven: SECS/GEM and OPC-UA mappings are documented in `dt-asset-manifest.md` and `sensor-map.md` but have not been exercised against actual machines | 🟡 | IT/OT Infrastructure Lead + Factory Engineering Lead | On commissioning (SMT Line 1: Q2 2026 target) | `dt-infrastructure.md`; `machinery.md` |
| INT-04 | AI platform production endpoints in stub state: `docs/ai-platform-status.md` confirms endpoint stubs are active but production model cutover and operational sign-off are pending | 🟡 | AI Platform Team Lead | 2026-06-30 | `gap-closure-report.md` Pass 10; `bim-simulation-readiness-program.md` Item 5 |
| INT-05 | MES ↔ DT event interoperability contract not yet jointly approved: shared event schema for OEE, FPY, and energy KPI calculation in the twin has not been jointly signed off by DT Lead and MES Product Owner | 🟡 | Digital Manufacturing Team Lead + MES Product Owner | 2026-07-31 | `docs/orchestration/post-gate-4-dt-execution.md` Section 7 |

### 2.3 Instrumentation

| Gap ID | Gap Description | Severity | Named Owner | Due Date | Evidence / Source |
|---|---|---|---|---|---|
| INS-01 | Zero physical sensors installed: factory under construction; no instruments on-site; all sensor entries in `sensor-map.md` and `dt-asset-manifest.md` represent design-baseline specification, not live hardware | 🟡 | Factory Engineering Lead | Phased per commissioning — SMT zones Q2 2026, full site Q4 2026 | `README.md` milestone checklist M5–M9 |
| INS-02 | Calibration baseline records not created: `sensor-map.md` defines calibration intervals (CAL-A through CAL-N) but CMMS calibration schedule has not been activated; no calibration records exist | 🟡 | Factory Engineering Lead + Quality Engineering | On commissioning per zone | `sensor-map.md` Section 2 |
| INS-03 | AMR positioning system not commissioned: MiR250/MiR100 fleet MQTT bridge fully documented in `digital-twin.md` and `dt-asset-manifest.md` but 16 AMR units not yet on-site | 🟡 | Factory Engineering Lead | Q4 2026 per roadmap | `README.md` milestone M9 |
| INS-04 | Energy submetering panel not installed: solar PV array (850 kWp), BESS (900 kWh), and grid meters are fully documented with sensor IDs and protocols, but physical hardware pending civil and electrical commissioning | 🟡 | Factory Engineering Lead | Q2 2026 (with solar commissioning) | `README.md` milestone M6; `digital-twin.md` Section 2.6 |
| INS-05 | IFC GUID extraction workflow staged but not yet executed: `scripts/extract-ifc-guids.py` pre-staged; cannot run until IFC file is delivered by contractor | 🟡 | Civil & Industrial Engineering Lead | 2026-06-30 | `gap-closure-report.md` Pass 7 |

### 2.4 Simulation Use-Cases

| Gap ID | Gap Description | Severity | Named Owner | Due Date | Evidence / Source |
|---|---|---|---|---|---|
| SIM-01 | Pilot charter not yet signed: the 14 simulation use cases require a frozen pilot charter (factory slice, scope boundary, locked value hypotheses, KPI formulas, baseline windows, confidence thresholds) per `dt-pilot-standards-and-templates.md` | 🔴 | Group CTO + PMO | Before first physical intervention | `dt-pilot-standards-and-templates.md` Section 1; `post-gate-4-dt-execution.md` Section 5 |
| SIM-02 | Experiment designs not frozen for any of the 14 use cases: no pre/post + matched-control design, no confounder controls, no minimum effect sizes, no statistical methods documented | 🟡 | DT Engineering Lead | 2026-08-31 | `dt-pilot-standards-and-templates.md` Section 2; `digital-twin.md` Section 4 |
| SIM-03 | Offline simulation results archived with deterministic inputs and seed lineage in dedicated evidence register | 🟢 | DT Engineering Lead | 2026-06-03 (closed) | `dt-simulation-evidence-lineage.md`; `dt-phase1/evidence/simulations/2026-06-03-*.json` |
| SIM-04 | Three mandatory simulation evidence records complete (throughput, quality/predictive maintenance proxy, energy) with reproducible command lineage | 🟢 | DT Engineering Lead | 2026-06-03 (closed) | `dt-simulation-evidence-lineage.md`; `dt-phase1/services/offline_simulation.py` |
| SIM-05 | KPI dictionary not yet versioned and change-controlled per `dt-pilot-standards-and-templates.md` Section 3: OEE, FPY, DPPM, energy intensity formulas are referenced across docs but not frozen in a change-controlled KPI dictionary | 🟡 | DT Engineering Lead + MES Product Owner | 2026-07-31 | `dt-pilot-standards-and-templates.md` Section 3 |

### 2.5 Ownership / Governance

| Gap ID | Gap Description | Severity | Named Owner | Due Date | Evidence / Source |
|---|---|---|---|---|---|
| GOV-01 | Phase 0 close-out not yet achieved: Tasks 0.2 (dev stack), 0.3 (BIM/IFC), and 0.4 (building-services spec) remain in Planned status; exit-gate evidence ledger empty | 🔴 | Digital Manufacturing Team Lead | 2026-07-31 | `dt-phase0-governance.md` Sections 5–8 |
| GOV-02 | Pentest not yet complete: kick-off was scheduled 2026-05-20; findings capture and remediation tracking are open; `docs/pentest-findings.md` stub not yet populated | 🟡 | IT/OT Security Lead | 2026-06-21 | `gap-closure-report.md` Pass 9; `bim-simulation-readiness-program.md` Item 4 |
| GOV-03 | Independent audit reviewer not yet assigned: governance checklist requires an independent reviewer assigned before pilot Day 61 | 🟡 | PMO | Before pilot Day 61 | `dt-pilot-standards-and-templates.md` Section 4 |
| GOV-04 | Carry-over log in `dt-phase0-governance.md` Section 8.1 unpopulated: table exists but no carry-over items have been formally entered with owner, due date, and tracking reference | 🟡 | Digital Manufacturing Team Lead | 2026-07-15 | `dt-phase0-governance.md` Section 8.1 |
| GOV-05 | Investor-ready DT proof track not yet initiated: `post-gate-4-dt-execution.md` requires a baseline capture pack, locked KPI formulas, and a DT Value & Funding Demand Brief before investor sessions begin | 🟡 | Group CTO + DT Engineering Lead | 2026-08-31 | `post-gate-4-dt-execution.md` Sections 3 and 8 |

---

## 3. Next 2-Week Deliverables

Window: **2026-06-02 to 2026-06-16**

| # | Deliverable | Owner | Completion Criterion |
|---|---|---|---|
| 1 | MES vendor sensor export received and validated against `sensor-map-vendor-template.md` (DOC-01 / INT-02 dependency) | MES Team Lead | Export file accepted; zone totals cross-checked against `sensor-map.md` control totals; discrepancy log raised |
| 2 | `dt-asset-manifest.md` co-sign initiated: MES Team Lead reviews manifest against sensor export and raises acceptance record or correction list (DOC-04) | Digital Manufacturing Team Lead + MES Team Lead | Acceptance record created or correction list raised with resolution deadline |
| 3 | Pentest execution window progress: findings capture in `pentest-findings.md` begun; SIEM triage alignment confirmed; first weekly findings review completed (GOV-02) | IT/OT Security Lead | At least initial findings entered in register; triage status confirmed in weekly steering review |
| 4 | Rwanda dev stack provisioning commenced: Rwanda cloud hub environment created; `docker-compose.yml` from `dt-phase1/` deployed to dev environment (INT-01) | IT/OT Infrastructure Lead | Cloud VM provisioned; Mosquitto, InfluxDB, Grafana, Telegraf, FastAPI containers running in dev mode |
| 5 | Weekly BIM-Simulation Steering Review (2026-06-03 and 2026-06-10, Tue 10:00 WAT) and Working Sessions (2026-06-05 and 2026-06-12, Thu 15:00 WAT) completed; RAID refreshed within 24 h of each | Documentation Integration Reviewer | Meeting minutes and refreshed RAID committed to programme record |

---

## 4. Template Improvements to Promote to Master

The following patterns developed in this factory are mature enough to be reviewed for promotion into
`factories/_template/` and group platform docs in [Coo-Kah-Doks](https://github.com/oumar-code/Coo-Kah-Doks).

| Pattern | Source in This Repo | Reusable As | Notes |
|---|---|---|---|
| Phase 0 governance control register (task model, sign-off matrix, exit-gate evidence ledger, no-bypass hold points, carry-over log) | `docs/dt-phase0-governance.md` | Template: `factories/_template/dt-phase0-governance.md` | Factory-specific task owners and deliverable names should be placeholders; the control structure, dependency graph, and exit-gate format are fully reusable |
| Machine-readable YAML asset manifest (schema: asset_id, zone, qty, protocol, update_frequency_s, dt_phase, per-sensor id/data_type/unit/expected_range) | `docs/dt-asset-manifest.md` | Template: `factories/_template/dt-asset-manifest.md` | The schema is the MES↔DT data contract — directly reusable. Remove factory-specific asset entries, retain schema and lock policy. |
| MQTT topic namespace design (zone/asset/instance/metric hierarchy, QoS policy, retained-message rules, FAT checklist references) | `docs/dt-mqtt-namespace.md` | Platform standard: `platform/mqtt-topic-schema.md` | Already aligned to group platform; promote the controlled-draft locking discipline and FAT checklist reference pattern |
| BIM asset anchors IFC GUID status control: `{GUID-<ASSET>-REPLACE}` convention with named owner, integration reviewer, and target closure date instead of free-form placeholders | `docs/bim/asset-anchors.md` Section 1.1 | Template: `factories/_template/docs/bim/asset-anchors.md` | Eliminates unmanaged placeholder text across factory repos; should become the group standard for pending-GUID tracking |
| Integrated BIM + Sensor + Pentest + AI Go-Live programme control format (owner matrix, weekly cadence, track-level closure gates, intake gate with SLA) | `docs/bim-simulation-readiness-program.md` | Template: `factories/_template/docs/bim-simulation-readiness-program.md` | The three-track closure board (Data Readiness, Security Assurance, AI Go-Live) and intake gate pattern will be needed in every factory |
| Pre-commissioning DT platform scaffold (docker-compose, synthetic publisher with operating-state drills, coverage validator, offline simulation baseline) | `dt-phase1/` | Replication package: include in Tier 1 rollout deployment playbook | Remove factory-specific `synthetic-profile.yaml` entries; retain scaffold, drill types, and acceptance gate checklist as the group standard proving kit |
| Offline simulation clearly marked as pre-commissioning baseline requiring recalibration (not presented as validated live model) | `dt-phase1/services/offline_simulation.py` header + `dt-phase1-software-infrastructure.md` | Template wording standard | Important guard against investor over-claiming. Should be enforced as a labelling rule in the master template. |

---

## 5. Evidence Traceability Index

| Topic | Primary Document |
|---|---|
| Asset registry (142 assets) | `docs/digital-twin.md` Section 2; `docs/dt-asset-manifest.md` |
| Sensor registry (~2,800 data points) | `docs/sensor-map.md` |
| Zone boundaries | `docs/bim/zone-boundaries.md` |
| Asset anchor points | `docs/bim/asset-anchors.md` |
| MQTT namespace | `docs/dt-mqtt-namespace.md` |
| Infrastructure stack | `docs/dt-infrastructure.md` |
| Phase 0 governance and control | `docs/dt-phase0-governance.md` |
| Implementation plan | `docs/dt-implementation-plan.md` |
| Phase 1 software scaffold | `docs/dt-phase1-software-infrastructure.md`; `dt-phase1/` |
| MES integration | `docs/mes-integration.md` |
| Simulation use cases | `docs/digital-twin.md` Section 4 |
| Gap closure status | `docs/gap-closure-report.md`; `docs/bim-simulation-readiness-program.md` |
| Group scorecard standard | [Coo-Kah-Doks/docs/orchestration/dt-readiness-control-tower.md](https://github.com/oumar-code/Coo-Kah-Doks/blob/main/docs/orchestration/dt-readiness-control-tower.md) |
| Pilot standards and templates | [Coo-Kah-Doks/docs/orchestration/dt-pilot-standards-and-templates.md](https://github.com/oumar-code/Coo-Kah-Doks/blob/main/docs/orchestration/dt-pilot-standards-and-templates.md) |
| Post-Gate 4 execution strategy | [Coo-Kah-Doks/docs/orchestration/post-gate-4-dt-execution.md](https://github.com/oumar-code/Coo-Kah-Doks/blob/main/docs/orchestration/post-gate-4-dt-execution.md) |

---

## Revision History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.1 | 2026-06-03 | Digital Manufacturing Team Lead + PMO | Implemented two-gate strategy: Condition 2 closed with reproducible simulation evidence lineage; Condition 3 reclassified as construction-gated with commissioning protocol and temporary exception controls |
| 1.0 | 2026-06-02 | Digital Manufacturing Team Lead + PMO | Initial DT readiness assessment — Wave 0 pilot scorecard, gap triage, 2-week deliverables, template promotion candidates |
