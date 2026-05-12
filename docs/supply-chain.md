# Personal Electronics Factory — Supply Chain Management

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1
> **Document Version:** 1.0 | **Owner:** Supply Chain & Procurement Team

---

## 1. Supply Chain Overview

The Coo-Cah Personal Electronics Factory operates a hybrid supply chain: critical high-technology components (SoC chips, display modules, battery cells, bare PCBs) are imported primarily from China, while casings are supplied domestically by the Coo-Cah Plastics Factory, and packaging materials are sourced locally. The supply chain strategy balances cost, lead time, and Nigeria import duty exposure across all 13 product SKUs.

| Supply Category            | Origin           | % of BOM Cost | Lead Time | Duty Rate (approx.) | Key Risk             |
|----------------------------|------------------|---------------|-----------|----------------------|----------------------|
| SoC / Application Processor| China (MediaTek, Qualcomm) | 18% | 8–12 weeks | 5% (IT machinery) | Forex, global chip supply |
| Display Modules (LCD/AMOLED)| China (BOE, Tianma) | 15%    | 8–10 weeks| 5%                   | Display tech refresh |
| Battery Cells (Li-Po/Li-ion)| China (CATL, EVE) | 12%    | 6–8 weeks | 5%                   | Safety certification |
| Bare PCBs (multi-layer)    | China (TTM, Tripod) | 8%      | 4–6 weeks | 5%                   | FOB pricing          |
| Memory (LPDDR, eMMC/UFS)   | China / Taiwan (Kingston, Micron) | 7% | 6–8 weeks | 5%          | Supply allocation    |
| Camera Modules             | China (Sunny, OFilm) | 6%    | 8–10 weeks| 5%                   | IP + market supply   |
| Bluetooth/Wi-Fi Modules    | China (Realtek, Espressif) | 4% | 6–8 weeks | 5%                  | NCC qualification    |
| Casings & Plastic Parts    | **Coo-Cah Plastics Factory, Ogun State** | 10% | **1–2 weeks** | 0% (intra-group) | Internal capacity |
| Packaging (cartons, inserts)| Local (Lagos, Sagamu) | 4% | 1–2 weeks | — | Local paper price   |
| Cables, Chargers (bundled) | China / Coo-Cah Garage | 6%   | 4–6 weeks | 5–10%               | Intra-group supply   |
| Other EMS + Passives       | China (multi-supplier) | 6% | 4–8 weeks | 5%                   | Reel fragmentation   |
| Miscellaneous Accessories  | China / Local      | 4%            | 4–6 weeks | 5–20%               | Varied              |

---

## 2. Import Logistics

### 2.1 Inbound Freight Routes

| Route                       | Mode       | Port of Entry     | Transit Time (China → Sagamu) | Est. Cost (per 40ft HQ) |
|-----------------------------|------------|-------------------|-------------------------------|--------------------------|
| China (Shenzhen/Guangzhou)  | Sea FCL    | Apapa Port, Lagos | 22–28 days                    | ~$3,500–$4,500           |
| China (Shenzhen)            | Sea LCL    | Apapa Port, Lagos | 28–35 days                    | ~$180–$220/CBM           |
| China (Guangzhou/Shenzhen)  | Sea FCL    | Tin Can Island, Lagos | 24–30 days                | ~$3,200–$4,200           |
| China (Guangzhou)           | Air Freight| Lagos Murtala Muhammed Airport | 3–5 days           | ~$6.50–$9.00/kg          |
| UK/Europe (spare parts)     | Air Freight| Lagos MMIA        | 2–4 days                      | ~$8.00–$12.00/kg         |

> **Standard routing:** FCL sea via Tin Can Island (preferred — shorter average dwell time vs Apapa). Air freight used for urgent replenishment of critical components only.

### 2.2 Customs Clearance Process

| Step | Activity                                      | Timeline     | Responsible                  |
|------|-----------------------------------------------|--------------|------------------------------|
| 1    | Pre-arrival document submission to NCS        | 5 days before arrival | Freight forwarder        |
| 2    | Form M application and SON conformity assessment | 3–4 weeks pre-shipment | Trade Finance + Procurement |
| 3    | NAFDAC notification (battery cells, chargers) | 4–6 weeks pre-shipment | Regulatory Affairs      |
| 4    | Container terminal release + examination      | 2–5 days post-arrival | Licensed customs agent    |
| 5    | Duty payment (e-customs eServices portal)     | Same day     | Finance + customs agent      |
| 6    | Cargo release + bonded truck to Sagamu        | 1–2 days     | Logistics                    |
| 7    | Goods receipt + incoming QC scan (MES)        | Same day     | Stores + QC team             |

**Applicable Duties & Levies on Electronic Imports:**
- Import Duty: 5–20% depending on HS code (5% for IT equipment/components; 20% for finished consumer electronics)
- VAT: 7.5%
- Surcharge (CISS): 1%
- ETLS (ECOWAS tariff levy): 0.5%
- Port & terminal levies: ~₦15,000–₦50,000 per container depending on port

---

## 3. Intra-Group Supply Links

### 3.1 Coo-Cah Plastics Factory → Personal Electronics

| Component Supplied            | Spec / Standard              | Daily Volume (Phase 1) | Lead Time | Quality Spec          |
|-------------------------------|------------------------------|------------------------|-----------|-----------------------|
| Smartphone Rear Covers        | PC+ABS, textured or glossy finish; tolerance ±0.05mm | 2,000 pcs/day | 1–2 days | Dimensional + cosmetic COC |
| Feature Phone Housings        | ABS, moulded; colour matched to Pantone spec | 800 pcs/day | 1–2 days | Full dimensional + functional fit |
| TWS Charging Case Shells      | PC, gloss; hinge tolerance critical | 6,000 pcs/day | 1–2 days | Hinge life 5,000 open/close |
| Smartwatch Bezels & Case Back | PC+ABS or polycarbonate (Pro) | 600 pcs/day | 1–2 days | Surface finish Ra ≤ 0.8 μm |
| Power Bank Housings           | ABS, scratchproof coating     | 2,500 pcs/day | 1–2 days | Cosmetic class A          |
| Retail Packaging (plastic insert trays) | Recycled PET, food-safe | 3,000 pcs/day | 1–2 days | Dimension + print quality |

> *Transport: dedicated shuttle truck between Coo-Cah Plastics Factory and Personal Electronics Factory, 2 runs/day. Total distance: <5 km within Sagamu Industrial Estate.*

### 3.2 Coo-Cah Garage Power Electronics → Personal Electronics

| Component Supplied             | Spec                                     | Volume (Phase 1)   | Notes                      |
|--------------------------------|------------------------------------------|--------------------|----------------------------|
| Phone Charger Adapters (5W/18W/20W) | CE + NCC TA certified; USB-C, fused | 2,000 pcs/day   | Bundled with SP-LITE, SP-MID |
| USB-C Charging Cables          | 1m, 3A rated; TPE jacket; strain relief  | 2,500 pcs/day      | Bundled with phones + PBs  |
| Power Bank Internal PCB        | Custom BMS PCB spec from Personal Electronics factory design | 2,000 pcs/day | Designed here; built at Garage |

---

## 4. Safety Stock Policy

| Component Category          | Minimum Safety Stock | Reorder Point    | Basis                                   |
|-----------------------------|---------------------|------------------|-----------------------------------------|
| SoC Processors (phones)     | 6 weeks demand      | 4 weeks remaining| Long lead time; forex + allocation risk |
| Display Modules             | 4 weeks demand      | 3 weeks remaining| Moderate lead time; $US price-sensitive |
| Battery Cells               | 4 weeks demand      | 3 weeks remaining| Safety certification batch control      |
| Memory (LPDDR/eMMC)         | 4 weeks demand      | 3 weeks remaining| Periodic global supply volatility       |
| Camera Modules              | 4 weeks demand      | 3 weeks remaining| Long lead time; custom specs            |
| BT/Wi-Fi Modules            | 4 weeks demand      | 3 weeks remaining| NCC-qualified modules only              |
| Casings (Plastics Factory)  | 2 weeks demand      | 1 week remaining | Local supply; short transit (< 5 km)   |
| Packaging Materials         | 2 weeks demand      | 1 week remaining | Local supply; short lead time           |
| Cables & Chargers (Garage)  | 2 weeks demand      | 1 week remaining | Intra-group; daily runs                 |
| SMT Consumables (paste, flux)| 3 weeks demand     | 2 weeks remaining| Import; critical for SMT continuity    |

> **Total working capital in inventory at Phase 1 ramp:** ~₦4.2B (based on 4-week average cover across all categories at full production BOM values).

---

## 5. Supplier Management

### 5.1 Approved Supplier List (Key Categories)

| Category                  | Approved Supplier(s)                        | Country     | Tier | Qualification Basis         |
|---------------------------|---------------------------------------------|-------------|------|-----------------------------|
| SoC Processors            | MediaTek, Qualcomm (via authorised dist.)   | Taiwan/USA  | 1    | NCC-qualified chipset; production history |
| Display Modules           | BOE Technology, Tianma Microelectronics     | China       | 1    | Sample test + dimensional match          |
| Battery Cells (Li-Po)     | CATL, EVE Energy                            | China       | 1    | IEC 62133 COC required per batch         |
| PCBs (bare)               | TTM Technologies, Tripod Technology         | China/Taiwan | 1   | IPC-A-600 Class 2 min; Gerber sign-off   |
| Memory                    | Kingston, Micron (via distribution)         | Taiwan/USA  | 1    | Engineering sample + test programme      |
| Camera Modules            | Sunny Optical, OFilm (where permissible)    | China       | 1    | Resolution + low-light QC test           |
| BT/Wi-Fi Modules          | Realtek, Espressif (pre-qualified NCC)      | China       | 1    | NCC type approval evidence required      |
| Casings                   | Coo-Cah Plastics Factory                   | Nigeria     | 1    | Intra-group; daily dimensional audit     |
| Packaging                 | Local Lagos/Ogun suppliers (3 approved)    | Nigeria     | 2    | Print quality test; FSC paper preferred  |
| Logistics (customs/freight)| Kuehne+Nagel Nigeria, DHL Global Forwarding | Nigeria     | 1   | Performance SLA > 90% OTIF              |
| Customs Broker            | 2 approved licensed customs agents         | Nigeria     | 1    | NCS licensed; bond facility in place    |

### 5.2 Supplier Performance KPIs

| KPI                         | Target       | Measurement Frequency | Consequence of Failure         |
|-----------------------------|--------------|----------------------|--------------------------------|
| On-Time In-Full (OTIF)      | ≥ 92%        | Monthly              | Corrective Action Plan required|
| Incoming Quality Defect Rate | ≤ 500 PPM   | Per shipment         | Chargeback + re-inspection     |
| Lead Time Adherence         | ±5 days      | Per PO               | SLA review                     |
| Pricing Stability           | ±5% per quarter | Quarterly         | Commercial renegotiation        |
| Sustainability / RoHS COC   | 100% supplied | Per shipment        | Rejected without full docs     |

---

## 6. Finished Goods Distribution

### 6.1 Outbound Channels

| Channel                          | % of Volume (Phase 1) | Mode                  | Frequency      |
|----------------------------------|------------------------|-----------------------|----------------|
| Coo-Cah Distribution Hub (Sagamu)| 55%                   | Dedicated truck       | Daily          |
| E-Commerce (Jumia, Konga, etc.)  | 20%                   | 3PL parcel courier    | Daily          |
| Direct Retail (Lagos stores)     | 15%                   | Coo-Cah fleet vehicle | 3×/week        |
| Wholesale / Distributor Network  | 10%                   | Palletised FCL        | Weekly         |

### 6.2 Outbound Dispatch SLA

| Order Type                      | Cut-off Time | Dispatch Target  | Tracking Method      |
|---------------------------------|--------------|------------------|----------------------|
| E-Commerce (Jumia/Konga fulfil) | 14:00 daily  | Same day         | MES → 3PL WMS API    |
| Distribution Hub transfer       | 16:00 daily  | Next morning     | MES despatch note    |
| Retail direct delivery          | 10:00 for day's route | Same day | Route plan + driver app |
| Export (Phase 2)                | Per booking  | Per agreed ETD   | Bill of Lading       |

---

## 7. Supply Chain Risk Register

| Risk                                  | Probability | Impact   | Mitigation Strategy                                        |
|---------------------------------------|-------------|----------|------------------------------------------------------------|
| Forex devaluation (₦/USD)            | High        | High     | USD forward contracts; local content increase road map     |
| Global semiconductor shortage         | Medium      | High     | 6-week SoC safety stock; dual-source qualification         |
| Port congestion (Apapa/Tin Can)       | High        | Medium   | Dual-port routing; pre-clearance; 4-week buffer stock      |
| Supplier quality failure              | Medium      | High     | Approved supplier list + IQC + incoming QC process        |
| Coo-Cah Plastics capacity constraint  | Low         | Medium   | Daily MES visibility; shared production planning meetings  |
| Customs duty regime changes           | Medium      | High     | Regulatory monitoring; bond store option; advocacy via MAN |
| Battery safety incident (import)      | Low         | High     | IEC 62133 COC required per batch; in-house IQC testing     |
| NCC type approval delay               | Medium      | High     | 6-month advance submission; pre-compliance EMC testing      |
| Air freight price spike               | Medium      | Low      | Minimise air-only dependency; 4-week sea buffer stock      |

---

## 8. Supply & Import Control Tower Implementation (M1.2, M1.3, M1.8)

This section operationalizes a single **Supply & Import Control Tower** that runs four parallel workstreams against milestone-driven gates for:

- **M1.2:** SMT Lines 1 & 2 installed, qualified, and running production
- **M1.3:** AMR fleet deployed and operational
- **M1.8:** TWS + Smartwatch lines at capacity with BT product approval readiness

### 8.1 Control Tower Scope and Owners

| Control Tower Function | Core Scope | Primary Owner | Supporting Functions |
|---|---|---|---|
| Milestone planning and gate control | Backward planning from M1.2/M1.3/M1.8, gate reviews, readiness decisions | PMO + Supply Chain Lead | Operations, Quality, Finance |
| Procurement execution | Long-lead PO/LC lock, shipment booking, supplier confirmation | Procurement Lead | Trade Finance, Engineering |
| Import compliance and duty control | HS classification, landed cost, Form M/SON/NAFDAC/NCC evidence, broker coordination | Logistics & Compliance Lead | Customs Brokers, Regulatory Affairs |
| MES/ERP supply onboarding | Vendor master data, workflow activation, sandbox flow validation | IT/MES Lead | ERP Admin, Stores, Quality |
| Intercompany and local contracts | Plastics and Packaging Hub SLAs, KPI clauses, contingencies | Commercial Contracts Lead | Legal, Operations, Quality |

### 8.2 Milestone-Backward Demand and Procurement Lock

| Milestone | Frozen Demand Package | Mandatory Commercial Lock | Exit Gate |
|---|---|---|---|
| M1.2 (SMT lines) | SMT line equipment balance, commissioning spares, SMT consumables | Signed PO/LC/TT, agreed Incoterm, confirmed ship window | All long-lead SMT items have supplier-confirmed ship dates aligned to commissioning sequence |
| M1.3 (AMR fleet) | 16 AMRs, charging docks, fleet licences, integration accessories | Signed PO/LC/TT, agreed Incoterm, confirmed delivery/installation window | AMR hardware and software package commercially locked with install-ready ETA |
| M1.8 (TWS/watch) | TWS/watch line components, fixtures, test assets, key imported modules | Signed PO/LC/TT, agreed Incoterm, confirmed ship window | Long-lead TWS/watch imports commercially locked with milestone-aligned ETA |

`TT` = Telegraphic Transfer.

Execution rules:

- Demand packs are frozen by milestone and only changed through formal change control
- Long-lead lines are released first and tracked on a daily expedite board
- Shipment mode (sea/air) is set by milestone criticality and contingency trigger

### 8.3 Import Compliance and Duty Optimisation Workstream

| Deliverable | Minimum Requirement | Owner | Gate Condition |
|---|---|---|---|
| Customs broker appointment | Two licensed brokers appointed (primary + backup) | Logistics & Compliance | Both appointments approved before first critical shipment |
| HS code matrix | Every imported line item mapped to HS code and duty band | Logistics & Compliance + Brokers | Zero unknown HS code lines |
| Landed-cost model | Duty, VAT, CISS, ETLS, and port/terminal costs validated | Finance + Logistics | Finance sign-off completed |
| Pre-clearance document pack | Form M, SON CoC, pre-shipment inspection, NAFDAC documents where required, NCC evidence where required | Regulatory Affairs + Trade Finance | Full pre-arrival checklist signed per shipment |

Acronyms: `SON` = Standards Organisation of Nigeria; `NAFDAC` = National Agency for Food and Drug Administration and Control; `NCC` = Nigerian Communications Commission.

Control requirement: no shipment may move to customs submission without a complete document pack and approved HS classification.

### 8.4 MES/ERP Supplier Onboarding Workstream

| Onboarding Area | Required Setup | Validation Output |
|---|---|---|
| Vendor master data | Approved supplier profile, lead time, MOQ, Incoterm, payment terms, compliance docs | Supplier record approved in ERP/MES |
| Route/station linkage | Product route and receiving/IQC mapping for each supplier family | Receiving and traceability map validated |
| Transaction workflows | PO, ASN/receipt, GRN, IQC hold/release, exception and escalation flow | Workflow test evidence archived |
| Cross-system traceability | ERP ↔ MES data continuity from PO through receipt to release | End-to-end traceability pass |

Sandbox gate before live commissioning:

- `PO -> receipt -> IQC -> release to production` flow passes end-to-end
- No manual database intervention is required
- Traceability chain is complete and auditable

### 8.5 Intercompany and Local Contract Finalisation Workstream

| Contract Counterparty | Mandatory Clauses | Acceptance Gate |
|---|---|---|
| Coo-Cah Plastics Factory | Daily/weekly capacity, quality specs, OTIF target, PPM threshold, escalation path, penalties, change-control | Signed SLA with measurable KPI clauses and operating playbook |
| Packaging Hub suppliers | Artwork/version control, service level, OTIF, defect threshold, contingency capacity, logistics cadence | Signed SLA with release/version governance and backup capacity commitment |

Required alignment:

- Shuttle/milk-run logistics cadence must be contractually defined
- KPI definitions must match MES dashboard metrics used in monthly governance

### 8.6 Governance Cadence and Escalation

| Cadence | Forum | Core Focus | Required Output |
|---|---|---|---|
| Daily | Expedite board | PO status, shipment booking, customs blockers, onboarding blockers | Updated blocker log with owner and due date |
| Weekly | Milestone risk review | M1.2/M1.3/M1.8 readiness, cost/risk deltas, gate risk | Escalation and recovery actions approved |
| Monthly | Go/No-Go readiness board | Supply readiness gate decision per milestone | Formal go/no-go record |

Escalation rule: any line item that threatens milestone date triggers immediate contingency action (alternate supplier, airfreight, or sequencing change) with owner and decision deadline.

### 8.7 First 6 Weeks Execution Sequence

| Window | Mandatory Activities | Completion Signal |
|---|---|---|
| Week 1 | Freeze demand packs, appoint brokers, launch HS/duty matrix, issue contract redlines | Demand baseline approved; brokers appointed; HS matrix active |
| Week 2 | Issue critical PO/LC/TT packages, submit first Form M/SON/NAFDAC packs, begin MES/ERP vendor master loads | Critical long-lead awards placed; first compliance packs submitted |
| Weeks 3–4 | Complete supplier sandbox onboarding, sign Plastics/Packaging contracts, confirm shipment bookings | Sandbox onboarding evidence complete; contracts signed; bookings confirmed |
| Weeks 5–6 | Run end-to-end inbound simulation (import docs -> customs -> GRN -> IQC -> MES traceability), close residual risks | Simulation pass with closed critical gaps |

---

*For regulatory compliance requirements affecting supply chain, refer to [`regulatory.md`](./regulatory.md).*
*For MES supply chain integration, refer to [`mes-integration.md`](./mes-integration.md).*
*For CapEx and working capital analysis, refer to [`capex-opex.md`](./capex-opex.md).*
*For programme-level control tower governance, refer to [`execution-plan.md`](./execution-plan.md).*
*For confirmed intra-group supply coordination status (Plastics volume confirmation + BMS PCB design sign-off), refer to [`intragroup-supply-coordination.md`](./intragroup-supply-coordination.md).*
