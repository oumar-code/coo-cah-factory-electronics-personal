# BIM & Simulation Readiness Program — Personal Electronics Factory

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**  
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1  
> **Document Version:** 1.0 | **Owner:** Documentation Integration Reviewer  
> **Status:** Active Programme Control — dependency-driven closure of BIM & simulation readiness gaps

This document operationalises the open readiness items tracked in
[`gap-closure-report.md`](./gap-closure-report.md) as one integrated programme with three tracks:

1. **Data Readiness (BIM + Sensor)**
2. **Security Assurance**
3. **AI Go-Live**

---

## 1. Integrated Closure Board

### 1.1 Weekly Governance Cadence

| Item | Cadence |
|---|---|
| Steering review | Weekly, every Tuesday 10:00 WAT |
| Working session | Weekly, every Thursday 15:00 WAT |
| RAID refresh | Within 24h of each session |
| Evidence pack publish | Weekly after steering review |

### 1.2 Owner Matrix

| Function | Primary Owner | Scope |
|---|---|---|
| Civil/BIM | Civil & Industrial Engineering Lead | IFC delivery, zone geometry, asset anchors |
| Digital Manufacturing | Digital Manufacturing Team Lead | DT import, sensor/asset harmonization, integration evidence |
| MES Vendor Interface | MES Team Lead | Sensor inventory export delivery, schema compliance |
| IT/OT Security | IT/OT Security Lead | Pentest execution, remediation governance, retest tracking |
| AI Platform | AI Platform Team Lead | STUB→LIVE-PROD readiness, cutover, rollback and monitoring |
| Integration QA | Documentation Integration Reviewer | Evidence completeness, sign-off traceability, closure gating |

### 1.3 Open-Item Board with Hard Due Dates

| Item | Track | Dependency | Due Date | Gate Status |
|---|---|---|---|---|
| 1. Zone boundary coordinates | Data Readiness | IFC handover accepted | 2026-06-30 | ⏳ Open |
| 2. Asset anchors + IFC GUIDs (142) | Data Readiness | IFC handover accepted | 2026-06-30 | ⏳ Open |
| 3. Sensor registry full population (~2,800) | Data Readiness | MES vendor export accepted | 2026-06-15 | ⏳ Open |
| 4. Penetration test execution | Security Assurance | Kick-off complete, test window executed | 2026-06-21 | ⏳ Open |
| 5. AI platform production go-live | AI Go-Live | Production data and model readiness | 2026-06-30 | ⏳ Open |

> **Top dependency risks:** IFC delivery and MES sensor export are treated as P1 risks and escalated in every steering review until closed.

---

## 2. Critical Path A — IFC Model Delivery (Unlocks Items 1 & 2)

### 2.1 IFC Handover Package Lock

| Required Field | Requirement |
|---|---|
| IFC schema | IFC4 |
| Origin/CRS | Must match [`bim/zone-boundaries.md`](./bim/zone-boundaries.md) Section 1 |
| Naming | Zone and asset naming aligned with DT IDs and BIM labels |
| Integrity | SHA-256 hash recorded in governance register |
| Delivery metadata | Contractor issue date, revision ID, transmittal reference |

### 2.2 Intake Gate (Receipt Check)

- [ ] CRS/origin alignment verified against zone-boundaries reference
- [ ] Zone entities present and named for Z1–Z12 + UTIL/AMEN/CIRC
- [ ] Storey/Z-range consistency validated (ground and mezzanine where applicable)
- [ ] GUID extraction test successful for all required entity classes
- [ ] Intake evidence and reviewer sign-off recorded

### 2.3 Intake Failure SLA

If any intake check fails:

- Raise contractor correction request within **1 business day**
- Require corrected IFC resubmission within **3 business days**
- Re-run full intake gate before accepting downstream closure tasks

---

## 3. Item 1 Closure Gate — Zone Boundary Coordinates

Closure requires all controls below:

- [ ] Z1–Z12 + UTIL/AMEN/CIRC boundaries reconciled to accepted IFC geometry
- [ ] Coordinate system and local origin references confirmed in-zone documentation
- [ ] Z min/max ranges populated and validated for all zones/storeys in scope
- [ ] Tolerance checks completed per boundary acceptance controls
- [ ] DT platform import verification passed with zone resolution in UI
- [ ] Evidence package includes source IFC revision, sign-off names, and closure date

---

## 4. Item 2 Closure Gate — Asset Anchors + IFC GUIDs (142 Assets)

Closure requires all controls below:

- [ ] Anchor X/Y/Z populated for all 142 assets
- [ ] IFC GUID status converted from pending tags to assigned IDs for all 142 assets
- [ ] Mapping evidence links recorded for each assignment batch
- [ ] Physical verification completed against commissioning/as-built locations
- [ ] Deviations recorded, approved, and closed through change control
- [ ] DT render/import verification confirms anchor placements in 3D view

---

## 5. Critical Path B — MES Sensor Inventory Export (Unlocks Item 3)

### 5.1 Schema Freeze & Mandatory Fields

- [ ] Sensor vendor template frozen and versioned
- [ ] Mandatory fields locked (zone, asset ID, sensor ID, protocol, calibration class, location)
- [ ] ID harmonization rules agreed with DT asset manifest ownership

### 5.2 Staged Ingest Quality Gates

- [ ] Schema validation pass
- [ ] ID harmonization pass (manifest ↔ sensor export)
- [ ] Protocol and calibration rule validation pass
- [ ] Duplicate and null-value checks within acceptable threshold
- [ ] Zone totals and global totals reconcile to control counts

---

## 6. Item 3 Closure Gate — Full Sensor Registry Population

Closure requires all controls below:

- [ ] Remaining placeholder rows replaced with validated sensor inventory rows
- [ ] Zone-level totals and global totals reconciled in `sensor-map.md`
- [ ] Gate 3 thresholds and calibration/CMMS requirements met
- [ ] Data completeness and drop/null thresholds evidenced
- [ ] Integration reviewer sign-off and closure date recorded

---

## 7. Item 4 Closure Gate — Penetration Test Execution

Closure requires all controls below:

- [ ] Test executed within approved engagement window and rules of engagement
- [ ] Findings entered into `pentest-findings.md` with severity and owners
- [ ] Remediation plans and SLAs assigned and tracked
- [ ] Retest evidence captured for critical/high findings
- [ ] Governance board receives closure package and signs readiness status

---

## 8. Item 5 Closure Gate — AI Platform Production Go-Live

Closure requires all controls below:

- [ ] Per-endpoint STUB→LIVE-PROD readiness evidence complete
- [ ] Production data validation and model acceptance complete
- [ ] Latency/fallback/cutover checks complete
- [ ] Rollback readiness and production monitoring baseline validated
- [ ] AI Platform Team Lead and MES Team Lead provide operational sign-off

---

## 9. Cross-Cutting Evidence and Change-Control Rules

- Every closure decision must include **source artifact, reviewer sign-off, and closure date**
- Coordinate, sensor, and endpoint status changes must be propagated across linked docs in the same change window
- Final integrated readiness review is mandatory before programme completion

---

## 10. Execution Sequencing

1. Start governance cadence and dependency escalation immediately
2. Run Security Assurance (Item 4) and AI Go-Live (Item 5) in parallel
3. On IFC acceptance, execute Item 1 then Item 2 closure gates
4. On MES export acceptance, execute Item 3 closure gate
5. Conduct integrated readiness review and close programme

---

## Related Documents

- [`gap-closure-report.md`](./gap-closure-report.md)
- [`bim/zone-boundaries.md`](./bim/zone-boundaries.md)
- [`bim/asset-anchors.md`](./bim/asset-anchors.md)
- [`sensor-map.md`](./sensor-map.md)
- [`sensor-map-vendor-template.md`](./sensor-map-vendor-template.md)
- [`pentest-scoping.md`](./pentest-scoping.md)
- [`pentest-findings.md`](./pentest-findings.md)
- [`ai-platform-status.md`](./ai-platform-status.md)
