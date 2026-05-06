# Personal Electronics Factory — Regulatory Compliance

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1
> **Document Version:** 1.0 | **Owner:** Regulatory Affairs & Quality Team

---

## 1. Regulatory Framework Summary

The Coo-Cah Personal Electronics Factory is subject to a multi-layered regulatory framework that spans product safety, wireless type approval, environmental compliance, worker safety, and import/export licensing. NCC Type Approval is the most product-critical Nigerian regulatory requirement — no wireless device may be sold in Nigeria without it.

| Regulatory Body          | Primary Jurisdiction            | Key Requirement                          | Impact Level |
|--------------------------|---------------------------------|------------------------------------------|--------------|
| NCC (Nigerian Communications Commission) | All wireless devices | Type Approval before sale | **Critical**  |
| SON (Standards Organisation of Nigeria) | All manufactured products | NIS certification / product registration | High     |
| NAFDAC                   | Battery cells, chargers, health devices | Product registration (batteries/health) | Medium   |
| NESREA                   | Environmental compliance        | EIA approval, e-waste management, effluent | High     |
| Nigeria Customs Service  | Imports                         | Form M, import duty payment, SON CoC    | High         |
| FIRS / Ogun State IRS    | Tax compliance                  | Corporate tax, WHT, VAT                  | High         |
| Ministry of Labour       | Workers' welfare                | Factories Act compliance, labour law     | High         |
| Ogun State Government    | Land, construction, planning    | Building permit, operational licence     | Medium       |
| IEC / ISO (International) | Product safety and quality     | IEC 62368-1, ISO 9001:2015              | High         |

---

## 2. NCC Type Approval — Detailed Process

### 2.1 What is NCC Type Approval?

NCC Type Approval is the mandatory certification under the Nigerian Communications Act 2003 (as amended) that every telecommunications or wireless device — including mobile phones, Bluetooth earbuds, smartwatches with wireless connectivity, and Wi-Fi accessories — must obtain before being imported, sold, or used commercially in Nigeria.

The approval confirms that a device meets Nigerian RF emission limits, does not cause harmful interference to licensed telecommunications networks, and complies with relevant ITU Radio Regulations.

### 2.2 NCC Type Approval Process Flowchart

```
Step 1: Pre-Submission Engineering
│
├── Confirm device RF parameters (frequency bands, max EIRP, modulation)
├── Conduct pre-compliance EMC + RF scan in Coo-Cah RF Lab (Zone Z8)
├── Confirm device complies with NCC Spectrum Management Regulations
└── Prepare Technical File (User Manual, Declaration of Conformity, circuit diagrams, antenna data)
                              │
                              ▼
Step 2: Formal Application to NCC (MTBS Portal)
│
├── Submit online application via NCC Mobile Terminal and Broadcasting Services portal
├── Pay non-refundable application fee (₦100,000–₦250,000 per product per standard category)
├── Upload technical file, user manual, circuit diagrams, antenna gain data
└── Designate an NCC-authorised local representative (Coo-Cah Regulatory Affairs team)
                              │
                              ▼
Step 3: NCC Laboratory Testing (NITDA-accredited or NCC-designated lab)
│
├── NCC schedules device testing at an approved laboratory (in Lagos or Abuja)
├── Tests performed: EMC (radiated/conducted emissions), RF output, spurious emissions, SAR (phones)
├── Pre-compliance test data from Coo-Cah Z8 RF Lab submitted alongside formal lab submission
└── Timeline: 4–12 weeks depending on lab queue and product complexity
                              │
                              ▼
Step 4: NCC Technical Review & Decision
│
├── NCC reviews lab test report; may request supplementary data or technical clarification
├── If approved: Type Approval Certificate issued (valid 5 years; renewable)
└── If rejected: Modification required; resubmission with updated product/antenna
                              │
                              ▼
Step 5: Certificate Issued — Production Authorised
│
├── NCC TA Number logged in Coo-Cah MES NCC Module
├── NCC mark applied to product label and packaging (per NCC labelling guidance)
├── All production units batch-linked to certificate in MES
└── Certificate monitored for expiry; renewal initiated 6 months before expiry
```

### 2.3 NCC Type Approval Fee Schedule

| Activity                        | Approximate Fee      | Notes                               |
|---------------------------------|----------------------|-------------------------------------|
| Application fee (per product)   | ₦100,000–₦250,000   | Depends on device category          |
| Laboratory testing fee           | ₦500,000–₦1,500,000 | Per product; external accredited lab|
| Annual Type Approval levy        | ₦50,000–₦150,000/year | Charged during certificate validity |
| Renewal fee (at 5-year expiry)  | ₦150,000–₦350,000   | Full re-test usually required       |

### 2.4 Phase 1 NCC Type Approval Schedule

| Product SKU     | Wireless Technology         | NCC Category               | Target Submission | Target Certificate |
|-----------------|-----------------------------|----------------------------|-------------------|--------------------|
| CCE-FP-3G       | GSM 900/1800, WCDMA B1/B8  | Mobile Handset             | Q1 2025           | Q3 2025            |
| CCE-FP-4G       | LTE B1/B3/B8                | Mobile Handset             | Q2 2025           | Q4 2025            |
| CCE-SP-LITE     | LTE B1/B3/B8, Wi-Fi, BT    | Smartphone                 | Q1 2025           | Q3 2025            |
| CCE-TWS-01      | Bluetooth 5.0               | Short Range Device         | Q2 2025           | Q4 2025            |
| CCE-SW-LITE     | Bluetooth 5.1               | Short Range Device / Watch | Q3 2025           | Q1 2026            |
| CCE-PB-5K/10K/20K | USB-C PD (no wireless)   | N/A — no NCC TA required   | —                 | —                  |
| CCE-ACC (USB-C Hub) | USB 3.1 (no wireless)   | N/A — no NCC TA required   | —                 | —                  |

> **SAR Testing:** All mobile phones (CCE-FP-3G, CCE-FP-4G, CCE-SP-LITE) must comply with NCC SAR limits ≤ 2.0 W/kg (head + body). SAR testing conducted by accredited laboratory and included in the Type Approval Technical File.

---

## 3. SON Product Registration & NIS Certification

The Standards Organisation of Nigeria (SON) requires that all manufactured products comply with relevant Nigerian Industrial Standards (NIS) and that applicable products are registered in the SON Product Registration portal before market placement.

### 3.1 SON Requirements by Product Category

| Product Category          | Relevant NIS Standard                  | SON Action Required                       | Timeline     |
|---------------------------|----------------------------------------|-------------------------------------------|--------------|
| Mobile phones             | NIS 62368-1:2022 (Audio/Video/IT)     | Product registration + CoC               | Per product  |
| TWS Earbuds               | NIS 60268-7 (Headphones)              | Product registration                      | Per product  |
| Smartwatches              | NIS 62368-1:2022                      | Product registration + CoC               | Per product  |
| Power Banks               | NIS 62133:2017 (Battery safety)       | Product registration + battery safety CoC | Per product |
| USB Chargers / Adapters   | NIS 62368-1 + NIS 61851               | Product registration + NAFDAC if medical  | Per product  |

### 3.2 SON Conformity Assessment (Import)

All imported components that are themselves SON-regulated products (e.g., imported finished chargers, battery cells) require a SON Conformity Assessment Programme (MANCAP) Certificate of Conformity before they may clear Nigerian Customs. The Procurement team ensures all relevant COC documents are obtained from suppliers before shipment.

---

## 4. IEC 62368-1 Product Safety

IEC 62368-1 (Audio/Video, Information and Communications Technology Equipment — Safety) is the primary international product safety standard applicable to all Coo-Cah Personal Electronics Factory outputs. It supersedes IEC 60950-1 and IEC 60065.

### 4.1 IEC 62368-1 Compliance Activities

| Activity                             | Responsible          | Frequency          | Evidence                         |
|--------------------------------------|----------------------|--------------------|----------------------------------|
| Design-stage safety analysis (HBSE)  | R&D / Product Engineer | Per new product  | Safety analysis report           |
| Pre-production sample test (accredited lab) | Quality / Regulatory | Per product     | Full test report                |
| Production hipot test (Chroma 19053) | QC / Operators       | 100% of units      | MES safety test record per serial|
| Annual surveillance audit            | Quality Manager      | Annually           | Audit report + corrective actions|
| Customer complaint safety review     | Quality / Regulatory | As needed          | Complaint + investigation report |

---

## 5. NESREA & Environmental Compliance

The National Environmental Standards and Regulations Enforcement Agency (NESREA) has jurisdiction over environmental compliance at the factory site.

### 5.1 Environmental Authorisations

| Requirement                          | Detail                                                              | Status       |
|--------------------------------------|---------------------------------------------------------------------|--------------|
| Environmental Impact Assessment (EIA) | Full EIA required before construction under NESREA Act 2007       | Required (P1)|
| EIA Approval (Federal NESREA)        | Issued by NESREA after review; required before commissioning        | Required (P1)|
| Ogun State Environmental Permit      | State-level environmental operating permit                          | Required (P1)|
| Effluent Discharge Permit            | Applicable if factory has process effluent; SMT flux cleaning water | Required     |
| Air Emission Permit                  | Generator exhaust; reflow oven VOC (if non-nitrogen)               | Required     |

### 5.2 E-Waste Management (WEEE)

Nigeria's Extended Producer Responsibility (EPR) framework, guided by the National Environmental (Electrical/Electronic Sector) Regulations 2011, places obligations on manufacturers to establish or participate in e-waste collection and recycling programmes.

| Obligation                           | Description                                                         | Implementation         |
|--------------------------------------|---------------------------------------------------------------------|------------------------|
| Product EPR Registration             | Register with NESREA as an electronic product producer              | Q2 2025                |
| Take-Back Programme                  | Establish or join a SON/NESREA-recognised take-back scheme          | Q4 2025                |
| Annual E-Waste Report                | Report tonnage of products placed on market vs. waste recovered     | Annual (from Year 2)   |
| Factory Waste Segregation            | SMT waste (solder dross, paste, flux, PCB offcuts) segregated and disposed via licensed hazardous waste contractor | Ongoing |
| Battery Cell Disposal                | All rejected Li-ion cells sent to NESREA-certified recycler          | Per occurrence         |

---

## 6. Labour & Workers' Welfare Compliance

### 6.1 Applicable Laws

| Law / Regulation                          | Key Requirement                                                    |
|-------------------------------------------|--------------------------------------------------------------------|
| Labour Act (Cap L1, LFN 2004)             | Written contracts, notice periods, termination procedures         |
| Employees' Compensation Act 2010          | Compulsory workers' compensation insurance (NSITF)                 |
| National Minimum Wage Act 2019 (amended)  | Minimum wage compliance; current minimum ₦70,000/month (2024)     |
| Factories Act (Cap F1, LFN 2004)          | Machine guarding, ventilation, sanitation, accident reporting      |
| Pension Reform Act 2014                   | Contributory pension scheme (employer 10% + employee 8% of salary)|
| Health and Safety at Work (OSHA guidelines) | HSE policy, PPE provision, incident register, emergency plan     |
| Nigeria Social Insurance Trust Fund (NSITF) | Monthly contribution; workers' compensation                       |

### 6.2 Factory Act Compliance Checklist

| Requirement                      | Status       | Details                                                   |
|----------------------------------|--------------|-----------------------------------------------------------|
| Factory Registration with FMOL   | Required     | Register under Factories Act before production commencement|
| Machinery Guarding               | In design    | All conveyors, press tools, and welders comply with ISO 14119 + ISO 13857 |
| First Aid Facilities             | Planned      | Staffed first aid room; 4 trained first aiders per shift  |
| Fire Safety Equipment            | Planned      | Sprinklers (battery zone), extinguishers, smoke detection throughout |
| Incident Reporting System        | Planned      | OSHA-style incident register; report to FMOL within 24h for LTI |
| Personal Protective Equipment    | Planned      | ESD wrist straps, safety shoes, lab coats provided; stored at lockers |
| Canteen & Welfare Facilities     | Planned      | Subsidised canteen, prayer room, changing rooms, nurse station|

---

## 7. Import Regulatory Compliance

| Compliance Item                      | Responsible Body          | Documentation Required                        |
|--------------------------------------|---------------------------|-----------------------------------------------|
| Form M (import declaration)          | CBN / Commercial Bank     | Pro-forma invoice, LC or TT                   |
| SON CoC for regulated products       | SON via MANCAP            | SON CoC per HS code per shipment              |
| Pre-shipment Inspection              | SON-recognised inspection body | Inspection certificate                   |
| Import duty payment                  | Nigeria Customs Service   | Customs assessment, duty payment receipt      |
| NAFDAC import notification (batteries)| NAFDAC                  | Product registration + import permit          |
| NCC approval for wireless modules    | NCC                       | Module-level NCC TA or system-level TA        |

---

## 8. Phase 2 Export Compliance (Outlook)

Phase 2 includes planned export to West African ECOWAS markets. The following additional certifications will be required:

| Market            | Standard / Certification     | Description                                          | Target Phase |
|-------------------|------------------------------|------------------------------------------------------|--------------|
| ECOWAS Region     | ECOWAS Technical Regulation  | Mutual recognition under ECOWAS type approval MRA    | Phase 2      |
| UK                | UKCA Marking                 | Replaces CE for UK market; IoT/radio regulations     | Phase 2      |
| EU                | CE Marking (RED Directive)   | Radio Equipment Directive 2014/53/EU                 | Phase 2      |
| Global (export)   | RoHS 2 compliance            | Restriction of hazardous substances in electronics   | Phase 2      |
| Global (export)   | REACH compliance             | Chemical compliance for EU market                    | Phase 2      |

---

*For MES regulatory data tracking (NCC test result logging), refer to [`mes-integration.md`](./mes-integration.md).*
*For supply chain import process documentation, refer to [`supply-chain.md`](./supply-chain.md).*
