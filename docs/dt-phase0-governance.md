# Digital Twin — Phase 0 Governance & Control Register

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State
> **Document Version:** 1.0 | **Owner:** Digital Manufacturing & AI Team
> **Status:** ACTIVE CONTROL REGISTER — Phase 0 Foundation Prep

---

## 1. Operating Rule

Phase 0 is run as a **foundation-freeze programme**, not as a broad technology build.
The purpose is to lock the data contract, telemetry namespace, infrastructure baseline,
spatial naming model, and facility requirements before machine commissioning begins.

The governing principle is simple:

- freeze foundational design decisions early;
- prove the platform stack only against the frozen baseline;
- treat sign-off as part of the deliverable, not as an afterthought.

---

## 2. Governance Structure

| Role | Primary Responsibility | Decision Rights |
|---|---|---|
| Digital Manufacturing Team Lead | Overall Phase 0 owner; chairs close-out review | Go / no-go recommendation for Phase 0 completion |
| MES Team Lead | Co-owner of the asset data contract and retained-message policy | Approves manifest lock and namespace alignment |
| IT/OT Infrastructure Lead | Owns dev stack proving and edge-node infrastructure baseline | Approves infrastructure readiness and dev-stack evidence |
| Factory Engineering Lead | Owns building-services integration for the edge node | Approves fit-out specification sign-off |
| Civil & Industrial Engineering Lead | Owns BIM / IFC delivery and spatial alignment | Approves BIM acceptance and update protocol |

---

## 3. Workstream Model

| Workstream | Scope | Purpose | Exit Condition |
|---|---|---|---|
| A — Data Contract & Standards | Task 0.1, Task 0.5 | Freeze naming, schema, and telemetry expectations | Manifest and MQTT namespace locked |
| B — Platform Proving | Task 0.2 | Prove architecture decisions before machine arrival | Rwanda dev stack running with synthetic dashboards signed off |
| C — Physical & Facility Readiness | Task 0.3, Task 0.4 | Remove retrofit risk from spatial and building-services design | IFC imported and building-services spec signed off |

**Critical path:** Workstream A is the gating path for the other two workstreams.

---

## 4. Dependency Controls

| Control Point | Rule | Why It Matters |
|---|---|---|
| Asset manifest → MQTT namespace | Do not lock the namespace before the manifest reaches controlled baseline | Prevents schema drift and topic renaming later |
| Manifest + namespace → synthetic data design | Do not hard-code publishers, Telegraf maps, or dashboards before both are aligned | Avoids rework in dev stack proving |
| Infrastructure baseline → building-services freeze | Do not freeze fit-out procurement before edge node requirements are embedded | Avoids costly retrofit of rack, power, cooling, and WAN |
| As-built BIM → spatial acceptance | Do not accept the spatial layer from design drawings alone | Prevents coordinate and footprint mismatch |
| All locked artifacts → first machine FAT | Do not enter FAT with unresolved foundational naming or infrastructure ambiguity | Protects commissioning readiness |

---

## 5. Phase 0 Control Register

| Task | Deliverable | Workstream | Owner | Current Status | Main Blocker to Clear | Approval Criteria |
|---|---|---|---|---|---|---|
| 0.1 | [`dt-asset-manifest.md`](./dt-asset-manifest.md) | A | Digital Manufacturing + MES | Controlled draft | Complete coverage and co-sign for all 142 asset IDs | Asset coverage complete; protocol/update/range fields complete; MES Team Lead acceptance recorded |
| 0.2 | Rwanda cloud-hub dev stack (see [`dt-infrastructure.md`](./dt-infrastructure.md)) | B | IT/OT Infrastructure | Planned | Controlled manifest/namespace baseline and deployment evidence not yet closed | Dev stack live; synthetic publishers active; first Grafana dashboards signed off; deployment runbook captured |
| 0.3 | IFC-format BIM / 3D spatial model | C | Civil & Industrial Engineering | Planned | Final as-built issue not yet available | IFC + DWG received; zones aligned; 142 asset footprints placed; model imported into DT platform |
| 0.4 | Building Services Specification update | C | Factory Engineering + IT/OT Infrastructure | Planned | Building-services sign-off pending before fit-out freeze | Rack, power, cooling, fibre, OT LAN, WAN, and backup requirements signed into building-services spec |
| 0.5 | [`dt-mqtt-namespace.md`](./dt-mqtt-namespace.md) | A | Digital Manufacturing | Controlled draft | Manifest alignment and retained-message policy sign-off pending | Topic hierarchy complete; QoS/retained policy agreed; FAT checklist references added; namespace locked in version control |

---

## 6. Sign-Off Matrix

| Deliverable | Required Approvers | Evidence Required |
|---|---|---|
| Asset manifest | Digital Manufacturing Team Lead, MES Team Lead | Completed manifest, coverage review, change-control statement |
| MQTT namespace | Digital Manufacturing Team Lead, MES Team Lead | Namespace document, QoS/retained policy agreement, FAT checklist reference |
| Rwanda dev stack | IT/OT Infrastructure Lead, Digital Manufacturing Team Lead | Running services, synthetic-data evidence, dashboard sign-off, runbook |
| BIM / spatial model | Civil & Industrial Engineering Lead, Digital Manufacturing Team Lead | IFC file, zone/asset alignment check, import confirmation |
| Building-services edge requirements | Factory Engineering Lead, IT/OT Infrastructure Lead | Issued building-services spec with DT edge node section |

---

## 7. Governance Cadence

| Cadence | Scope | Required Outcome |
|---|---|---|
| Weekly | Workstream status, blockers, dependency breaches | Owner reset and blocker escalation |
| Milestone-based | Manifest baseline review, namespace freeze, dev-stack proving review | Formal sign-off or corrective-action list |
| Phase close-out | All five Phase 0 outputs | Go / no-go decision for first-machine FAT readiness |

Any dependency breach that threatens manifest lock, namespace lock, dev-stack alignment, or fit-out freeze
must be escalated in the next weekly review or earlier if it affects procurement timing.

---

## 8. Completion Review Checklist

Phase 0 closes only when all of the following are true:

- [ ] Asset manifest published and accepted by the MES Team Lead.
- [ ] MQTT namespace locked in version control after manifest alignment.
- [ ] Rwanda dev stack running with synthetic dashboards signed off.
- [ ] BIM IFC file received, checked for zone/asset alignment, and imported into the DT platform.
- [ ] Edge node requirements signed off in the Building Services Specification.
- [ ] Residual carry-over items, if any, are assigned to named owners with due dates.

---

## 9. Related Controlled Documents

- [`dt-implementation-plan.md`](./dt-implementation-plan.md)
- [`dt-asset-manifest.md`](./dt-asset-manifest.md)
- [`dt-mqtt-namespace.md`](./dt-mqtt-namespace.md)
- [`dt-infrastructure.md`](./dt-infrastructure.md)
