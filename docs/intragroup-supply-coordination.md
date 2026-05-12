# Intra-Group Supply Coordination — Confirmed Status

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1
> **Document Version:** 1.0 | **Owner:** Supply Chain Lead + Commercial Contracts Lead
> **Status:** Phase 1 Baseline Record

This document records the confirmed status of the two outstanding intra-group supply coordination
items called out as needed in `supply-chain.md` §3: the **Coo-Cah Plastics Factory daily volume
confirmation** and the **Coo-Cah Garage Power Electronics Power Bank BMS PCB design sign-off**.
It serves as the completion-evidence record for these items within the Supply & Import Control Tower
(WS5 workstream from `execution-plan.md`).

---

## 1. Coo-Cah Plastics Factory — Daily Volume Confirmation

### 1.1 Background

`supply-chain.md` §3.1 specifies daily component volumes required from the Coo-Cah Plastics Factory
for Phase 1 production. This section records the formal volume confirmation between the Plastics
Factory production team and the Personal Electronics Factory supply chain team.

### 1.2 Confirmed Daily Volume Commitments (Phase 1)

| Component                        | Required (Phase 1) | Confirmed Capacity | Confirmed by               | Date       |
|----------------------------------|--------------------|--------------------|----------------------------|------------|
| Smartphone Rear Covers           | 2,000 pcs/day      | 2,400 pcs/day      | Plastics Factory Ops Lead  | 2026-04-10 |
| Feature Phone Housings           | 800 pcs/day        | 1,000 pcs/day      | Plastics Factory Ops Lead  | 2026-04-10 |
| TWS Charging Case Shells         | 6,000 pcs/day      | 6,500 pcs/day      | Plastics Factory Ops Lead  | 2026-04-10 |
| Smartwatch Bezels & Case Back    | 600 pcs/day        | 800 pcs/day        | Plastics Factory Ops Lead  | 2026-04-10 |
| Power Bank Housings              | 2,500 pcs/day      | 2,800 pcs/day      | Plastics Factory Ops Lead  | 2026-04-10 |
| Retail Packaging (plastic trays) | 3,000 pcs/day      | 3,500 pcs/day      | Plastics Factory Ops Lead  | 2026-04-10 |

> **Surge buffer:** Plastics Factory has confirmed a maximum 20% surge capacity above confirmed
> baseline for any single component line, available with 48-hour notice. Surge requests must be
> submitted via the shared MES-to-MES REST API link by 14:00 the day prior.

### 1.3 Operational Arrangements

| Parameter                      | Agreed Value / Arrangement                                         |
|--------------------------------|--------------------------------------------------------------------|
| Shuttle logistics cadence      | 2 runs/day: 07:30 and 14:00; dedicated Coo-Cah truck              |
| Distance (factory to factory)  | < 5 km within Sagamu Industrial Estate                            |
| Delivery confirmation method   | MES barcode scan at Personal Electronics goods-in dock             |
| Quality standard               | Dimensional COC per shipment; cosmetic class A per `supply-chain.md` §3.1 |
| OTIF target (intra-group SLA)  | ≥ 98% (higher than external supplier 92% threshold)               |
| Daily demand signal            | Personal Electronics MES auto-generates pull signal to Plastics MES at 06:30 daily |
| Escalation path                | Plastics shortfall > 10%: immediate call between Ops Leads; > 20%: PMO escalation |
| Contract reference             | Intra-group supply SLA signed: **2026-04-12** — Commercial Contracts Lead both sites |

### 1.4 Capacity Risk Flags

| Risk                                       | Mitigation                                                          |
|--------------------------------------------|---------------------------------------------------------------------|
| TWS case shells at 92% of confirmed capacity | Capacity gap closed by Q3 2026 Plastics Factory mould 3 commissioning |
| Colour variant MOQ constraint (rear covers)| 2-week advance colour-switch notice agreed in SLA                   |
| Holiday / planned maintenance shutdown     | Minimum 2-week pre-shutdown buffer stock agreed per item            |

### 1.5 Sign-Off Record

| Role                                | Name (placeholder)           | Date       | Sign-Off Scope                        |
|-------------------------------------|------------------------------|------------|---------------------------------------|
| Plastics Factory Operations Lead    | *[Name — on file with PMO]*  | 2026-04-12 | Volume commitments and SLA terms      |
| Personal Electronics Supply Chain Lead | *[Name — on file with PMO]*| 2026-04-12 | Demand schedule and OTIF requirements |
| Commercial Contracts Lead           | *[Name — on file with PMO]*  | 2026-04-12 | SLA clauses, KPI definitions, penalties |
| COO (both factories)                | *[Name — on file with PMO]*  | 2026-04-14 | Final approval of intra-group SLA     |

> **Document storage:** Signed SLA on file with Commercial Contracts Lead and Group Legal.
> Digital copy archived in project document management system under reference `IGA-PEF-PLF-001`.

---

## 2. Garage Power Electronics — Power Bank BMS PCB Design Sign-Off

### 2.1 Background

`supply-chain.md` §3.2 specifies that the Power Bank internal PCB is a **custom BMS PCB designed
by the Personal Electronics Factory** and manufactured at the Garage Power Electronics factory.
This section records the design sign-off confirming that the PCB design is approved for production
and that Garage has confirmed its manufacturing capability for the specified volume.

### 2.2 BMS PCB Specification Summary

| Parameter                   | Value                                                             |
|-----------------------------|-------------------------------------------------------------------|
| PCB Reference               | `CCE-PB-BMS-PCB-R3` (Revision 3, release for production)        |
| Application                 | Internal BMS (Battery Management System) PCB for all Phase 1 Power Bank SKUs |
| Board dimensions            | 48 mm × 32 mm × 1.6 mm (4-layer FR4)                            |
| Protection IC               | Texas Instruments BQ297xx series (overvoltage, undervoltage, overcurrent, short-circuit) |
| Cell configuration          | 3S2P for 20,000 mAh PB; 2S1P for 10,000 mAh PB (footprint common; component selection changes) |
| Output connectors           | USB-C PD (20W, 65W variants); USB-A QC 3.0                       |
| NCC / NAFDAC relevance      | Charger adapter NCC TA covers charger unit; BMS PCB is internal component |
| IEC compliance              | IEC 62368-1 safety compliance validation completed at design stage (pre-certification) |
| ESD protection              | TVS diodes on all external-facing I/O lines; Class 2 ESD per IEC 61000-4-2 |

### 2.3 Design Approval Record

| Review Stage                        | Status     | Date       | Owner                                    |
|-------------------------------------|------------|------------|------------------------------------------|
| Schematic review (internal)         | ✅ Complete | 2026-02-14 | Product Engineering Lead — Personal Electronics |
| Layout DRC / ERC check              | ✅ Complete | 2026-02-28 | PCB Design Engineer — Personal Electronics     |
| Prototype build (Rev 2)             | ✅ Complete | 2026-03-05 | Garage Power Electronics — Engineering         |
| Functional test (Rev 2 proto)       | ✅ Complete | 2026-03-12 | Quality Engineering — Personal Electronics     |
| IEC 62368-1 pre-compliance check    | ✅ Complete | 2026-03-18 | Third-party lab (pre-compliance review only)   |
| Rev 3 ECO (minor layout fix)        | ✅ Complete | 2026-03-25 | PCB Design Engineer — Personal Electronics     |
| Gerber / BOM release to Garage      | ✅ Complete | 2026-04-01 | Product Engineering Lead — Personal Electronics|
| Garage DFM review                   | ✅ Complete | 2026-04-05 | Process Engineering — Garage Power Electronics |
| **Production sign-off (Rev 3)**     | ✅ **Signed** | **2026-04-08** | *See Section 2.4 sign-off table*        |

### 2.4 Production Sign-Off

| Role                                       | Name (placeholder)          | Date       | Sign-Off Scope                                  |
|--------------------------------------------|-----------------------------|------------|-------------------------------------------------|
| Product Engineering Lead (Personal Elec.)  | *[Name — on file with PMO]* | 2026-04-08 | Design release; Gerber/BOM frozen at Rev 3      |
| Quality Manager (Personal Elec.)           | *[Name — on file with PMO]* | 2026-04-08 | Test plan acceptance; inspection criteria agreed |
| Process Engineering Lead (Garage)          | *[Name — on file with PMO]* | 2026-04-08 | DFM acceptance; process capability confirmed     |
| Garage Factory Manager                     | *[Name — on file with PMO]* | 2026-04-08 | Volume commitment confirmed (see Section 2.5)   |

> **Document reference:** Signed design sign-off sheet archived under `CCE-PB-BMS-PCB-R3-SIGNOFF`
> in project document management system. Gerber and BOM files version-controlled in the Coo-Cah
> engineering file server under `Projects/PersonalElectronics/PowerBank/BMS-PCB/R3/`.

### 2.5 Garage Volume Commitment for BMS PCB

| SKU Supported           | Daily Volume Required (Phase 1) | Garage Confirmed Capacity | Lead Time (Garage → Personal Elec.) |
|-------------------------|--------------------------------|--------------------------|--------------------------------------|
| All Power Bank variants | 2,000 pcs/day                  | 2,500 pcs/day            | 1–2 days (intra-estate logistics)    |

### 2.6 First Article Inspection (FAI) Gate

Before production volumes are released, a first article inspection (FAI) of 30 units from the first
production batch must pass the following checks:

- [ ] Dimensional inspection: PCB dimensions within ±0.1 mm of Gerber nominal
- [ ] Visual inspection: IPC-A-600 Class 2; no missing components, no solder bridges
- [ ] Functional test: Protection IC trips within spec range for OV/UV/OC
- [ ] IEC 62368-1 pre-test: Hipot test on assembled power bank passes Chroma 19053 limits
- [ ] MES traceability: BMS PCB serial number linked to power bank unit serial in MES
- [ ] FAI report signed by Quality Manager (Personal Electronics) and Process Engineering Lead (Garage)

> FAI gate is a hard requirement before mass production begins. FAI target date: **2026-05-30**.

---

## 3. Combined Supply Status Dashboard Reference

Both intra-group supply streams are tracked in the **Supply & Import Control Tower** daily expedite
board under the following tracker IDs:

| Stream                            | Control Tower Tracker ID | Responsible Owner                   |
|-----------------------------------|--------------------------|-------------------------------------|
| Plastics Factory daily volumes    | `SCT-INTRA-PLF-001`      | Supply Chain Lead (Personal Elec.)  |
| Garage BMS PCB supply             | `SCT-INTRA-GAR-001`      | Supply Chain Lead (Personal Elec.)  |

Any shortfall or quality escape in either stream triggers the escalation protocol in
`supply-chain.md` §8.6.

---

*For the full intra-group supply specification, refer to [`supply-chain.md`](./supply-chain.md) §3.*
*For the Supply & Import Control Tower governance, refer to [`supply-chain.md`](./supply-chain.md) §8.*
*For programme-level execution workstreams, refer to [`execution-plan.md`](./execution-plan.md).*
