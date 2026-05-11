# Personal Electronics Factory — Immediate Priorities, Strategy & Execution Plan

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1
> **Document Version:** 1.0 | **Owner:** PMO + Operations + Quality + Regulatory

---

## 1. Strategic Direction (Next 12 Months)

**Operating strategy:** **compliance-first, yield-first, cash-disciplined ramp**.

Phase 1 execution prioritises regulatory readiness, stable process capability, and controlled volume ramp before broad SKU expansion.  
Phase 2/3 automation investment remains conditional on measurable Phase 1 KPI attainment.

### 1.1 Phase 1 Outcome Targets

| Outcome Area | Target |
|---|---|
| Regulatory readiness | All launch SKUs approved and sale-ready before mass ramp |
| Quality stability | Sustained FPY/OEE at gate thresholds before scale |
| Delivery reliability | On-time delivery performance at or above target |
| Cash discipline | Working capital and CapEx drawdown aligned to milestone gates |
| Operational resilience | Stable utilities/power quality and supply continuity |

---

## 2. Immediate Priorities by Time Horizon

## 2.1 First 2 Weeks — Re-Baseline Programme

| Priority | Deliverable | Accountable Owner | Completion Signal |
|---|---|---|---|
| Plan-vs-reality review | Consolidated status across site, financing, permits, equipment, certifications | PMO Lead | Signed baseline variance report |
| Integrated master schedule | One master schedule with critical path, dependencies, and named owners | PMO + Functional Heads | Approved schedule baseline v1 |
| Go-live sequence freeze | Launch wave decision (must-have SKUs first; wave 2 deferred) | COO + Commercial + Quality | Formal go-live memo |

## 2.2 Next 30–60 Days — Secure Gating Items

| Priority | Deliverable | Accountable Owner | Completion Signal |
|---|---|---|---|
| Regulatory gating | NCC/SON/NESREA/Factories Act submission tracker and fast-track actions | Regulatory Affairs | All launch SKU files submitted and acknowledged |
| Site/infrastructure gating | Civil/utilities readiness checklist with red/amber/green control | Engineering + Facilities | Commissioning-ready sign-off |
| Financing gating | Funding drawdown plan linked to equipment delivery milestones | Finance + Procurement | Drawdown and supplier-credit approvals issued |

## 2.3 12-Month Objective

Stabilise compliant output at required quality and delivery levels, then expand throughput and SKU mix in controlled waves.

---

## 3. Integrated Execution Workstreams

## 3.1 Workstream Register

| # | Workstream | Core Scope | Accountable Owner | Gate Metrics |
|---|---|---|---|---|
| WS1 | Programme Re-baseline | Reality check, critical path, ownership map | PMO | Baseline approved; >95% owner assignment |
| WS2 | Regulatory Fast-Track | NCC/SON/NESREA/Factories Act submissions, evidence packs | Regulatory Affairs | 100% launch SKU submission completeness |
| WS3 | Site & Utilities Readiness | Civil closure, utilities, EHS readiness | Engineering/Facilities | Commissioning checklist pass |
| WS4 | Financing & Commercial Controls | Drawdowns, supplier credit, payment gating | Finance | Milestone-linked cash release adherence |
| WS5 | Long-Lead Supply Control | Long-lead PO lock, safety stock, dual-source | Supply Chain | Safety stock coverage achieved by policy |
| WS6 | Staged Commissioning Ramp | MES software setup baseline → sandbox validation → SMT traceability → assembly pilot → RF/safety release | Operations + Quality | Software readiness sign-off and stage-gate KPIs met before next stage |
| WS7 | MES + Quality Traceability | Serial-level data integrity, dashboard governance, RBAC control, audit evidence | IT/MES + Quality | MES data completeness, access-control, and defect visibility gates met |
| WS8 | Energy & Uptime Resilience | Solar/BESS/ATS commissioning, power-quality validation, contingency plan | Energy + Maintenance | Uptime and power-quality acceptance report |
| WS9 | Workforce Readiness | Critical hires, certification, shift accountability | HR + Operations | Competency sign-off before scale-up |

## 3.2 Critical Path (Near-Term)

1. Re-baseline and schedule freeze  
2. Regulatory submission completeness for launch SKUs  
3. Site/utilities commissioning readiness  
4. Long-lead material and import compliance lock  
5. SMT commissioning and traceability validation  
6. Pilot production gate achievement and release to controlled ramp

Any delay in these six steps blocks launch readiness.

---

## 4. Master Schedule (Execution Baseline)

| Window | Key Activities | Primary Output |
|---|---|---|
| Weeks 1–2 | Re-baseline, integrated schedule issue, go-live wave freeze | Approved baseline package |
| Weeks 3–6 | Regulatory submission push, long-lead PO confirmation, MES software baseline deployment, utilities readiness closeout | Gating register reduced to controlled residuals |
| Weeks 7–10 | Sandbox production-order validation, SMT line commissioning, MES core traceability validation, incoming quality hardening | Stage-1 production readiness |
| Weeks 11–14 | Phone assembly pilot, RF/safety test release, containment loops | Stage-2 readiness decision |
| Months 4–6 | Narrow launch basket ramp under KPI gates | Stable compliant output |
| Months 7–12 | Controlled expansion (wave 2 SKUs) only after KPI stability | Throughput expansion with quality control |

---

## 5. Staged Go-Live Sequence (Frozen)

## 5.1 Launch Waves

| Wave | SKU Scope | Entry Condition | Exit Condition |
|---|---|---|---|
| Wave 1 (must-have) | CCE-FP-3G, CCE-FP-4G, CCE-SP-LITE, CCE-TWS-01 | Regulatory and commissioning gates cleared | Stable KPI performance over sustained review period |
| Wave 2 | Remaining Phase 1 SKUs (including MID/PRO variants) | Wave 1 stability and cash/supply readiness confirmed | Approved for scale by monthly governance board |

## 5.2 Commissioning Sequence

1. SMT lines commissioned and process-stable  
2. MES traceability and test data integrity verified  
3. Phone assembly pilot lots completed with containment controls  
4. RF/safety lab release and launch authorisation

## 5.3 MES Phase 1 Software Setup Gate

Phase 1 MES software setup must be accepted before live machine commissioning. The detailed baseline is defined in [`mes-phase1-software-setup.md`](./mes-phase1-software-setup.md); the execution plan treats it as a formal gate under WS6 and WS7.

| Validation Step | Required Output | Gate Owner |
|---|---|---|
| MES core deployed | Application, database, reporting, and identity services installed | IT/MES |
| Master data loaded | Approved SKU, route, station, user, and reason-code baseline | IT/MES + Operations |
| Sandbox orders simulated | Released test orders with full route execution evidence | Operations |
| Station events simulated | Entry, exit, hold, rework, and completion events validated | IT/MES + Quality |
| Traceability chain verified | PCB-to-shipment genealogy audit passed | Quality |
| AMR dispatch tested | Mission creation, acknowledgement, and failure handling proven | Logistics + IT/MES |
| EMS ingestion tested | Zone/order energy flow shown on dashboard | Energy + IT/MES |
| RBAC verified | Role matrix and approval routing signed off | IT/MES + Compliance |
| Dashboards reviewed | Operational and compliance dashboards accepted | Operations + Quality |
| Go/No-Go signed | Formal readiness decision recorded | PMO + COO |

No stage may proceed from sandbox to live station connection unless all critical software setup outputs are complete and signed off.

---

## 6. Control Towers (Operational Governance)

## 6.1 Regulatory Control Tower

Tracks submissions, evidence completeness, lab schedules, and certificate risk for launch SKUs.  
Escalates any submission slippage immediately to weekly governance.

## 6.2 Supply & Import Control Tower

Tracks long-lead PO status, shipment ETAs, Form M, SON CoC, NAFDAC-related documents, and customs bottlenecks.  
Maintains exception queue with owner, due date, and contingency action.

## 6.3 MES + Quality Control Tower

Monitors serial traceability, FPY, OEE, DPPM, downtime, and incoming quality escapes.  
Applies mandatory line-stop/escalation protocol for threshold breaches.

## 6.4 Energy & Uptime Control Tower

Monitors solar/BESS commissioning, ATS switching readiness, power quality for SMT/test assets, and backup mode drills.

---

## 7. KPI Gate Framework (Ramp Decisions)

Progression from each stage to the next is **metric-gated**, not calendar-gated.

| Gate Area | Required Condition for Progression |
|---|---|
| Compliance gate | Required approvals and certificates in place for release scope |
| Process capability gate | FPY/OEE/defect metrics at agreed thresholds |
| Traceability gate | Full serial-level MES and test data integrity |
| Software setup gate | MES baseline deployed, sandbox interfaces validated, RBAC and dashboards signed off |
| Supply gate | Long-lead and import coverage at policy levels |
| Uptime gate | Power-quality and contingency readiness validated |

If any gate fails, the programme holds at current stage with corrective action and revalidation.

---

## 8. Workforce Readiness Before Volume

| Priority | Action | Owner | Completion Signal |
|---|---|---|---|
| Critical staffing | Fill production engineering, quality/regulatory, SMT maintenance, MES admin, import/compliance roles | HR + Functional Heads | All critical positions staffed |
| Certification | Competency certification for line supervisors/operators before commissioning sign-off | Operations + Academy | Competency records complete |
| Shift accountability | Shift-level KPI ownership with named accountable leaders | Operations | Daily shift review in place |

---

## 9. Cadence & Decision Governance

| Cadence | Scope | Core Decisions |
|---|---|---|
| Daily | Line readiness, blockers, safety, quality escapes | Immediate containment and recovery actions |
| Weekly | Critical path, supplier risk, regulatory status, cash/budget variance | Escalations, re-prioritisation, owner resets |
| Monthly | Milestone reforecast, CapEx/OpEx control, launch and ramp gates | Go/No-Go decisions for next ramp stage |

---

## 10. Phase 2/3 Investment Rule

Phase 2/3 automation spend is released only when Phase 1 demonstrates sustained KPI performance across:

- OEE  
- FPY  
- DPPM  
- On-time delivery  
- Regulatory pass rate

This protects cash, prevents premature complexity, and ensures the factory scales from a stable base.

---

*This execution plan operationalises the factory strategy into accountable near-term actions, governance, and gate-based ramp controls.*
