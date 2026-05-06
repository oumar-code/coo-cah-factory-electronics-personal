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

*For regulatory compliance requirements affecting supply chain, refer to [`regulatory.md`](./regulatory.md).*
*For MES supply chain integration, refer to [`mes-integration.md`](./mes-integration.md).*
*For CapEx and working capital analysis, refer to [`capex-opex.md`](./capex-opex.md).*
