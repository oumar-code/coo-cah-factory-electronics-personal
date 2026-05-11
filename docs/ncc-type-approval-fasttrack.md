# NCC Type Approval — Fast-Track Programme (M1.6 Recovery)

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1
> **Document Version:** 1.0 | **Owner:** Regulatory Affairs Lead + PMO Sponsor
> **Milestone:** M1.6 | **Original Target:** Q3 2025 | **Status:** ⚠️ Overdue — Recovery Active
> **Recovery Target:** Q3 2026 (CCE-FP-3G and CCE-SP-LITE certificates)

---

## 1. Programme Overview

Milestone M1.6 — NCC Type Approval for **CCE-FP-3G** and **CCE-SP-LITE** — was originally targeted for Q3 2025 and is now overdue. This document defines the recovery programme, operating model, and execution plan to achieve type approval for both priority SKUs as fast as possible.

NCC Type Approval is a hard commercial release gate. Neither CCE-FP-3G nor CCE-SP-LITE may be sold in Nigeria until the Nigerian Communications Commission (NCC) certificate is in hand and logged in MES. This programme is therefore treated as a **regulatory fast-track**, not an engineering project: the critical path is document completeness, lab access, and NCC portal submission — not hardware development.

### 1.1 Scope

| Item | Detail |
|---|---|
| In scope | CCE-FP-3G (GSM 900/1800, WCDMA B1/B8) and CCE-SP-LITE (LTE B1/B3/B8, Wi-Fi, BT) |
| Out of scope | CCE-FP-4G, CCE-TWS-01, CCE-SW-LITE (separate approval tracks; proceed after M1.6 closes) |
| Programme owner | Regulatory Affairs Lead |
| Programme sponsor | COO / PMO |
| Recovery start | 11 May 2026 |
| Recovery target | Certificates issued by Q3 2026 |

### 1.2 Re-Baseline Declaration

The Q3 2025 target for M1.6 is formally declared missed. A recovery baseline is established as follows:

| Event | Original Date | Recovery Date |
|---|---|---|
| CCE-FP-3G — application submitted to NCC MTBS portal | Q1 2025 | 10 June 2026 |
| CCE-SP-LITE — application submitted to NCC MTBS portal | Q1 2025 | 10 June 2026 |
| CCE-FP-3G — lab testing complete | Q2 2025 | August 2026 |
| CCE-SP-LITE — lab testing complete | Q2 2025 | August 2026 |
| CCE-FP-3G — NCC certificate issued (M1.6 closed) | Q3 2025 | September 2026 |
| CCE-SP-LITE — NCC certificate issued (M1.6 closed) | Q3 2025 | September 2026 |

All planning documents, master schedules, and commercial launch plans must be updated to align to the recovery dates above. The weekly governance review will report against recovery dates from the week commencing 11 May 2026.

---

## 2. Ownership and Accountability

| Role | Person / Team | Responsibility |
|---|---|---|
| Programme owner | Regulatory Affairs Lead | Day-to-day execution; dossier completeness; lab and NCC liaison |
| Programme sponsor | COO / PMO | Escalation authority; resource decisions; commercial alignment |
| RF Engineering | RF/Antenna Engineer | RF spec documents; pre-compliance test data; lab support during testing |
| Quality | QA Manager | Sample selection and release; test acceptance; MES certificate entry |
| Product Engineering | Product Lead | Hardware baseline freeze; firmware/modem build confirmation |
| Legal / Company Secretary | Legal Counsel | Local representative designation; manufacturer declaration sign-off |
| Finance | Finance Controller | Application fee payment; lab fee payment; budget provision |
| IT / MES | MES Admin | Certificate register entry; dispatch gate activation after certificate receipt |

All roles must be confirmed and confirmed in writing within **3 days of programme start** (by 14 May 2026). Any vacancy blocks the programme and is escalated to the COO immediately.

---

## 3. NCC Control Tower

The Regulatory Control Tower tracks both SKUs through the full application lifecycle from dossier assembly to certificate receipt. It is the single source of truth for M1.6 status.

### 3.1 Tracker Fields

For each SKU, the following fields are maintained and reviewed at every cadence:

| Field | Description |
|---|---|
| Dossier completeness (%) | Percentage of required dossier documents assembled and internally approved |
| Missing evidence items | Count and list of outstanding documents; owner and due date for each |
| Product baseline frozen | Yes / No — hardware revision, RF firmware, antenna configuration locked |
| Sample units ready | Number of test-ready units built and held; confirmation they match frozen baseline |
| Lab selected | Name of NCC-accredited lab engaged |
| Lab slot booked | Yes / No — date of booked test slot |
| NCC MTBS portal submission | Not started / Submitted / Acknowledged / Under review / Approved |
| Application fee paid | Yes / No — receipt reference |
| Lab fee paid | Yes / No — receipt reference |
| Open RFIs | Count of outstanding queries from lab or NCC; owner and due date per item |
| Certificate risk | 🟢 On track / 🟡 At risk / 🔴 Blocked |
| Next action | Owner, action, due date |

### 3.2 Review Cadence

| Phase | Cadence | Participants |
|---|---|---|
| Dossier assembly (Weeks 1–3) | Weekly | Regulatory Affairs Lead, RF Eng, Product Eng, QA, Finance |
| Application submission and lab testing | Twice weekly | Regulatory Affairs Lead, RF Eng, QA, PMO sponsor |
| NCC review and certificate | Weekly | Regulatory Affairs Lead, PMO sponsor |

Any item rated 🔴 Blocked or any item preventing lab booking or portal submission is escalated to the PMO sponsor **within 48 hours**.

---

## 4. Parallel Execution Streams

To avoid sequential delays, work is split into a **Common Stream** (shared across both SKUs) and a **SKU-Specific Stream** (parallel tracks per product).

### 4.1 Common Stream

| Task | Owner | Deadline |
|---|---|---|
| Appoint all programme owners and confirm in writing | PMO | 14 May 2026 |
| Issue complete dossier checklist to all owners | Regulatory Affairs Lead | 14 May 2026 |
| Select and shortlist NCC-accredited labs (primary + backup) | Regulatory Affairs Lead | 18 May 2026 |
| Request lab quotes: sample count, document checklist, fees, turnaround, retest policy | Regulatory Affairs Lead | 18 May 2026 |
| Confirm budget provision for application fees and lab fees | Finance | 18 May 2026 |
| Confirm local NCC-authorised representative designation | Legal / Company Secretary | 18 May 2026 |
| Set up NCC MTBS portal accounts and test document upload | Regulatory Affairs Lead | 21 May 2026 |
| Book lab slots (primary lab; both SKUs) | Regulatory Affairs Lead | 1 June 2026 |
| Book backup lab slot (contingency) | Regulatory Affairs Lead | 1 June 2026 |

### 4.2 CCE-FP-3G SKU Stream

| Task | Owner | Deadline |
|---|---|---|
| Confirm hardware revision and commercial model name | Product Engineering | 18 May 2026 |
| Freeze RF firmware/modem build | RF Engineering | 18 May 2026 |
| Freeze antenna configuration | RF Engineering | 18 May 2026 |
| Compile RF specifications: GSM 900/1800, WCDMA B1/B8 — frequency, max EIRP, modulation | RF Engineering | 21 May 2026 |
| Prepare antenna data: type, gain, radiation pattern reference | RF Engineering | 21 May 2026 |
| Prepare circuit diagrams and block diagrams | Product Engineering | 21 May 2026 |
| Prepare PCB/layout reference and RF architecture overview | RF Engineering | 21 May 2026 |
| Compile SAR evidence plan: band configuration, SAR measurement methodology | RF Engineering + QA | 21 May 2026 |
| Finalise user manual (English; Nigerian market) | Product Engineering | 25 May 2026 |
| Finalise product label and packaging artwork (NCC fields, SAR advisory) | Product Engineering | 25 May 2026 |
| Prepare Declaration of Conformity and manufacturer declarations | Legal / Company Secretary | 25 May 2026 |
| Compile pre-compliance test data from Z8 RF Lab | QA + RF Engineering | 28 May 2026 |
| Build and release minimum 5 test-ready sample units | QA + Production | 28 May 2026 |
| Internal dossier review and sign-off | Regulatory Affairs Lead | 1 June 2026 |
| Submit application via NCC MTBS portal | Regulatory Affairs Lead | 10 June 2026 |
| Hand over samples to lab | QA | Lab slot date |

### 4.3 CCE-SP-LITE SKU Stream

| Task | Owner | Deadline |
|---|---|---|
| Confirm hardware revision and commercial model name | Product Engineering | 18 May 2026 |
| Freeze RF firmware/modem build | RF Engineering | 18 May 2026 |
| Freeze antenna configuration | RF Engineering | 18 May 2026 |
| Compile RF specifications: LTE B1/B3/B8, Wi-Fi 2.4 GHz, Bluetooth 5.0 — frequency, max EIRP, modulation | RF Engineering | 21 May 2026 |
| Prepare antenna data: type, gain, radiation pattern reference | RF Engineering | 21 May 2026 |
| Prepare circuit diagrams and block diagrams | Product Engineering | 21 May 2026 |
| Prepare PCB/layout reference and RF architecture overview | RF Engineering | 21 May 2026 |
| Compile SAR evidence plan: LTE bands + Wi-Fi, SAR measurement methodology | RF Engineering + QA | 21 May 2026 |
| Finalise user manual (English; Nigerian market) | Product Engineering | 25 May 2026 |
| Finalise product label and packaging artwork (NCC fields, SAR advisory, CE/UKCA if applicable) | Product Engineering | 25 May 2026 |
| Prepare Declaration of Conformity and manufacturer declarations | Legal / Company Secretary | 25 May 2026 |
| Compile pre-compliance test data from Z8 RF Lab | QA + RF Engineering | 28 May 2026 |
| Build and release minimum 5 test-ready sample units | QA + Production | 28 May 2026 |
| Internal dossier review and sign-off | Regulatory Affairs Lead | 1 June 2026 |
| Submit application via NCC MTBS portal | Regulatory Affairs Lead | 10 June 2026 |
| Hand over samples to lab | QA | Lab slot date |

---

## 5. Minimum Application Dossier

Each SKU application submitted to NCC must include all of the following. The checklist below is the **gate-2 completeness check** — no application may be submitted until every item is marked complete and internally approved.

| # | Dossier Item | CCE-FP-3G | CCE-SP-LITE | Notes |
|---|---|---|---|---|
| 1 | Product identification sheet (model name, SKU, hardware revision, commercial variant matrix) | ☐ | ☐ | |
| 2 | RF technology declaration (wireless technologies, frequency bands, standards) | ☐ | ☐ | |
| 3 | RF specifications: max transmit power (dBm), EIRP (dBm), modulation type per band | ☐ | ☐ | |
| 4 | Antenna data: antenna type, gain (dBi), radiation pattern reference | ☐ | ☐ | |
| 5 | Circuit diagram (RF section at minimum; full schematic preferred) | ☐ | ☐ | |
| 6 | Block diagram (system-level RF and baseband) | ☐ | ☐ | |
| 7 | PCB layout reference (RF traces, ground plane, antenna keep-out) | ☐ | ☐ | |
| 8 | RF architecture overview document | ☐ | ☐ | |
| 9 | SAR test plan and preliminary SAR evidence (head + body; ≤ 2.0 W/kg limit) | ☐ | ☐ | Mandatory for all phone products |
| 10 | User manual (English; NCC advisory language included) | ☐ | ☐ | |
| 11 | Product label artwork (showing NCC mark location, SAR advisory, model ID) | ☐ | ☐ | |
| 12 | Packaging artwork (regulatory panels) | ☐ | ☐ | |
| 13 | Declaration of Conformity (signed by authorised signatory) | ☐ | ☐ | |
| 14 | Manufacturer declaration (company details, registered address, contact) | ☐ | ☐ | |
| 15 | Local NCC-authorised representative letter | ☐ | ☐ | Coo-Cah Regulatory Affairs team acts as local representative |
| 16 | Pre-compliance test data from Z8 RF Lab (EMC radiated/conducted; RF output; spurious) | ☐ | ☐ | |
| 17 | Test parameter table (frequencies tested, limits, measured values, pass/fail) | ☐ | ☐ | |
| 18 | Application fee payment confirmation | ☐ | ☐ | ₦100,000–₦250,000 per product |

All items must be approved by the Regulatory Affairs Lead before Gate 2 is declared passed.

---

## 6. Product Baseline Freeze

No application may proceed to NCC submission until the product baseline is frozen. A post-freeze change to any RF or antenna parameter requires formal change control review and may invalidate the application.

### 6.1 Freeze Checklist

| Baseline Item | Frozen By | Confirmed |
|---|---|---|
| Hardware revision (PCB and mechanical) | Product Engineering | ☐ |
| RF firmware / modem software build identifier | RF Engineering | ☐ |
| Antenna type and configuration | RF Engineering | ☐ |
| Charger / accessory configuration declared to NCC | Product Engineering | ☐ |
| Commercial model name and variant matrix | Product + Commercial | ☐ |
| NCC product category confirmed | Regulatory Affairs Lead | ☐ |

### 6.2 Post-Freeze Change Control

Any proposed change to a frozen item after Gate 1 must be reviewed by the Regulatory Affairs Lead before implementation. The review determines whether the change:

- Has no impact on the application (proceed without delay),
- Requires document update only (update dossier; re-approve; no retest),
- Requires retest by the accredited lab (mandatory before re-submission), or
- Requires full re-submission to NCC.

The review outcome is logged in the Control Tower tracker. No RF or antenna change may be made to production units without completing this review.

---

## 7. Five-Gate Execution Model

Progression through the application process is gate-controlled. No gate may be passed on assumption.

```
Gate 1: Product Baseline Frozen
│
├── All freeze checklist items confirmed
├── Baseline document versions recorded
└── Gate sign-off: Product Engineering + Regulatory Affairs Lead
                               │
                               ▼
Gate 2: Dossier 100% Complete
│
├── All 18 dossier items assembled and internally approved
├── Dossier reviewed against lab's own document checklist
└── Gate sign-off: Regulatory Affairs Lead
                               │
                               ▼
Gate 3: Lab Slot Booked and Samples Ready
│
├── NCC-accredited lab selected and slot confirmed in writing
├── Minimum 5 test-ready sample units per SKU available and matched to frozen baseline
├── Sample units pass internal pre-compliance check at Z8 RF Lab
└── Gate sign-off: QA Manager + Regulatory Affairs Lead
                               │
                               ▼
Gate 4: NCC Application Submitted and Acknowledged
│
├── Application submitted via NCC MTBS portal
├── Application fee paid; receipt logged in Control Tower
├── Submission acknowledgement received from NCC
└── Gate sign-off: Regulatory Affairs Lead
                               │
                               ▼
Gate 5: Lab Report Accepted and Certificate Issued
│
├── Accredited lab test complete; test report issued
├── NCC technical review complete; no outstanding RFIs
├── NCC Type Approval Certificate issued (CCE-FP-3G and CCE-SP-LITE)
├── Certificate logged in MES NCC Module; dispatch gate activated
└── Gate sign-off: Regulatory Affairs Lead + QA Manager + MES Admin
```

---

## 8. Thirty-Day Recovery Plan

The 30-day sprint brings both SKU applications to portal submission. Testing and NCC review continue after day 30.

| Week | Dates | Key Actions | Owner | Completion Signal |
|---|---|---|---|---|
| Week 1 | 11–18 May 2026 | Appoint and confirm all programme owners; re-baseline M1.6 dates; create and populate Control Tower tracker; confirm SKU variants and product categories; issue dossier checklist to all owners; contact shortlisted labs for quotes and slot availability | PMO + Regulatory Affairs Lead | All owners confirmed; tracker live; labs contacted |
| Week 2 | 18–25 May 2026 | Close all missing technical documents; complete RF spec and antenna data for both SKUs; freeze product baselines (Gate 1); collect label, manual, and packaging evidence; compare lab's document checklists against dossier; confirm SAR test methodology | RF Engineering + Product Engineering + Regulatory Affairs Lead | Gate 1 passed for both SKUs; dossier gap list reduced to zero |
| Week 3 | 25 May – 1 June 2026 | Select primary and backup labs; book test slots for both SKUs; build and release test samples; complete Declarations of Conformity; finalize portal-ready application packs; confirm fee payment readiness; complete dossier review (Gate 2) | Regulatory Affairs Lead + QA + Finance + Legal | Gate 2 and Gate 3 passed for both SKUs; lab slots confirmed in writing |
| Week 4 | 1–10 June 2026 | Submit both applications via NCC MTBS portal; pay application fees; receive acknowledgement; hand over samples to lab on booked test date; activate active follow-up cadence with lab and NCC | Regulatory Affairs Lead | Gate 4 passed for both SKUs; acknowledgements received; samples with lab |

After week 4, the programme transitions to:

| Phase | Period | Actions |
|---|---|---|
| Lab testing | June–August 2026 | Twice-weekly follow-up with lab; rapid response to lab queries (target: 48h turnaround); keep backup samples ready; engineering contact available for lab clarifications |
| NCC review | August–September 2026 | Weekly follow-up with NCC; RFI response within 48 hours; no open blocking items |
| Certificate receipt | Q3 2026 | Update MES certificate register; activate dispatch gate; update product labels; notify commercial and operations |

---

## 9. Lab Engagement Requirements

When requesting quotes and booking slots, the following information must be obtained from each candidate lab:

| Information Required | Purpose |
|---|---|
| Earliest available test slot for mobile handset / smartphone category | Schedule planning |
| Number of sample units required per product | Sample production planning |
| Exact document checklist required for submission | Dossier completeness validation |
| Fee schedule (per product, per test category, SAR separately) | Finance provision |
| Expected turnaround from sample receipt to test report | Schedule planning |
| Retest policy and fee if first test fails | Risk planning |
| NCC accreditation certificate reference and expiry date | Lab qualification check |

A minimum of two labs must be shortlisted. The backup lab slot must be booked no later than the date the primary lab slot is booked.

---

## 10. Query Management

During lab testing and NCC technical review, queries and requests for information (RFIs) must be resolved rapidly to avoid delays.

| Query Type | Lead Responder | Support | Target Turnaround |
|---|---|---|---|
| RF test parameter or measurement query (from lab) | RF Engineering | QA | 24 hours |
| Documentation or product description query (from lab or NCC) | Regulatory Affairs Lead | Product Engineering | 24 hours |
| SAR methodology or measurement query (from lab) | RF Engineering + QA | Regulatory Affairs Lead | 24 hours |
| Product identity or manufacturer information query | Legal / Company Secretary | Regulatory Affairs Lead | 48 hours |
| Commercial / import / distribution query from NCC | Regulatory Affairs Lead | Legal / Finance | 48 hours |

All RFIs are logged in the Control Tower tracker with the date received, owner, response deadline, and date resolved. Any RFI open beyond its target turnaround is escalated to the PMO sponsor.

---

## 11. Physical Testing Preparation

Physical RF testing at the NCC-accredited lab is the critical path item for certificate issuance. The following preparation is required before handing samples to the lab:

| Preparation Item | Owner | Deadline |
|---|---|---|
| Pre-compliance test at Z8 RF Lab (EMC radiated/conducted; RF output; spurious emissions) | QA + RF Engineering | Before lab slot |
| SAR pre-compliance check (confirm value within margin of NCC limit) | QA + RF Engineering | Before lab slot |
| Sample units verified against frozen baseline (hardware revision, firmware build, antenna config) | QA | Before lab slot |
| Sample units labelled with correct model name, hardware revision, and serial number | QA | Before lab slot |
| Dossier hard copy and/or digital pack prepared for handover to lab | Regulatory Affairs Lead | Before lab slot |
| Backup samples available (minimum 3 per SKU) | QA + Production | Before lab slot |
| RF engineering point of contact confirmed to lab (available during testing for clarifications) | RF Engineering | Before lab slot |
| Return logistics arranged for samples after testing | QA | Before lab slot |

---

## 12. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Incomplete dossier at time of submission | Medium | High — NCC returns application | Complete Gate 2 checklist before submission; compare against lab's own checklist |
| Product / sample mismatch (sample differs from documents) | Medium | High — invalidates application | Gate 1 baseline freeze; QA sample verification against frozen baseline |
| RF or antenna change after submission | Low | High — may require retest or resubmission | Post-freeze change control; no RF/antenna changes without regulatory review |
| SAR value exceeds NCC limit (≤ 2.0 W/kg) | Low | Critical — application failed; redesign required | SAR pre-compliance measurement at Z8 before submission; plan antenna/power margin |
| Lab queue slippage (primary lab unavailable) | Medium | Medium — delays testing | Backup lab slot booked in parallel; lab booking confirmed by Gate 3 |
| Lab test failure (product fails EMC or RF limits) | Low | High — retest required; 4–12 week delay | Pre-compliance testing at Z8 RF Lab; resolve marginal results before submission |
| Slow NCC clarification response | Medium | Medium — delays certificate | Establish NCC relationship before submission; assign NCC liaison; respond to RFIs within 24–48 h |
| Key owner vacancy (RF Eng, Regulatory Lead, QA) | Low | High — programme stalls | Confirm owners by 14 May 2026; escalate any vacancy to COO within 48 h |
| Conflicting internal engineering schedule | Medium | Medium — delays dossier completion | Programme sponsor priority protection; any resource conflict escalated to COO |
| Application fee payment delay | Low | Medium — submission blocked | Finance approval obtained by Week 2; payment readiness confirmed at Gate 2 |

---

## 13. Post-Certificate Actions

Once the NCC Type Approval Certificate is issued for each SKU, the following actions are mandatory before any commercial dispatch:

| Action | Owner | Timing |
|---|---|---|
| Log certificate number, issue date, and expiry date in MES NCC Module (see [`mes-integration.md`](./mes-integration.md) §4.2) | MES Admin + QA | Within 24 hours of receipt |
| Activate dispatch gate in MES for each certified SKU | MES Admin | Same day as certificate logging |
| Apply NCC mark to product label and packaging (per NCC labelling guidance) | Product Engineering | Before first commercial batch |
| Update commercial launch confirmation for Wave 1 SKUs | PMO + Commercial | Same week as certificate receipt |
| Set expiry reminder: 6 months before expiry date (renewal initiation alert) | MES Admin | At certificate logging |
| Notify all cross-factory dependencies (Distribution Hub, Plastics Factory) that SKU is cleared for dispatch | Supply Chain | Same week as certificate receipt |
| File original certificate in regulatory document management system | Regulatory Affairs Lead | Within 24 hours of receipt |
| Report M1.6 closure to weekly governance board | PMO | Next governance meeting after certificate receipt |

---

## 14. Success Criteria

M1.6 is closed when **all** of the following are satisfied:

- [ ] NCC Type Approval Certificate issued for **CCE-FP-3G** (GSM 900/1800, WCDMA B1/B8)
- [ ] NCC Type Approval Certificate issued for **CCE-SP-LITE** (LTE B1/B3/B8, Wi-Fi, BT)
- [ ] Both certificates logged in MES NCC Module with expiry tracking active
- [ ] Dispatch gates activated in MES for both SKUs
- [ ] Product labels and packaging updated with NCC mark
- [ ] No open critical dossier gaps or RFIs
- [ ] M1.6 closure reported to and accepted by the governance board

---

## 15. Links and References

| Document | Relevance |
|---|---|
| [`regulatory.md`](./regulatory.md) | NCC Type Approval process detail, fee schedule, SAR requirements, SON/NESREA framework |
| [`mes-integration.md`](./mes-integration.md) | MES NCC Module: certificate registry, dispatch gate, RF test logging, audit report |
| [`execution-plan.md`](./execution-plan.md) | WS2 Regulatory Fast-Track workstream; overall programme governance cadence |
| [`automation-roadmap.md`](./automation-roadmap.md) | M1.6 milestone definition and Phase 1 milestone table |
| [`machinery.md`](./machinery.md) | Z8 RF Lab equipment (R&S CMW500, shielded chambers, pre-compliance test rig) |
| [`floor-plan.md`](./floor-plan.md) | Z8 RF Lab layout, shielded chamber specification |
| [`supply-chain.md`](./supply-chain.md) | NCC delay risk mitigation in supply chain risk register |

---

*This document is the master reference for M1.6 NCC Type Approval fast-track execution. All status updates are maintained in the Regulatory Control Tower tracker and reported at weekly programme governance.*
