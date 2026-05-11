# Personal Electronics Factory — Workforce Training Academy (6-Week Onboarding)

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1
> **Document Version:** 1.0 | **Owner:** HR + Operations + Academy
> **Workstream:** WS9 Workforce Readiness (see [`execution-plan.md`](./execution-plan.md))

---

## 1. Programme Overview

The Coo-Cah Manufacturing Academy delivers a machine-independent 6-week onboarding programme for all direct production staff before production starts. The programme can run immediately in parallel with other workstreams because it depends on classroom, sandbox MES, and training assets rather than live machine commissioning.

This page is the single source of truth for:

- Academy programme structure and cohort schedule
- Weekly module content and assessment method
- Trainer roles and accountabilities
- Competency sign-off gate required before line access
- Governance tracker and retest/refresher controls

The MES training modules use the deployed sandbox baseline and role model defined in [`mes-phase1-software-setup.md`](./mes-phase1-software-setup.md).

---

## 2. Scope and Throughput Plan

| Item | Requirement |
|---|---|
| Total direct staff in scope | ~450 |
| Cohort size | ~50 trainees per cohort |
| Parallel cohorts | 2 cohorts at once |
| Throughput per 6-week cycle | ~100 trainees |
| Estimated cycles required | ~5 cycles |
| Delivery model | Rolling cohorts with ~2-week stagger |

### 2.1 Cohort Priority Order

1. Line supervisors  
2. SMT operators  
3. Phone assembly operators  
4. TWS/watch/power-bank operators  
5. Quality/QC personnel  
6. Warehouse/logistics operators

---

## 3. Phase 0 Foundation Setup (Before Week 1)

### 3.1 Academy Staffing

| Role | Accountability |
|---|---|
| Academy Programme Manager (HR + Operations) | Owns schedule, capacity, tracker reporting, and sign-off governance |
| Safety/ESD Trainer | Delivers Week 1 safety induction and ESD handling module |
| 5S/Lean Trainer | Delivers Week 2 5S module and zone-audit practicals |
| MES Trainer | Delivers Week 3–4 sandbox MES modules and practical assessments |
| Quality/IPC Trainer | Delivers Week 5 quality awareness and IPC standards module |
| External IPC-A-610 Class 2 Trainer (contract) | Supports standards content and assessment quality calibration |

### 3.2 Training Infrastructure

- Designate classroom space (training hall/conference rooms)
- Prepare 2–3 MES sandbox workstations per classroom
- Prepare ESD demonstration kits (wrist straps, ESD mats, ionisers, handling trays)
- Print safety signage, 5S visual guides, and IPC Class 2 visual standards

### 3.3 Document Governance

| Record | Rule |
|---|---|
| Competency Record | One record per trainee, linked to employee ID and MES user account |
| Module Sign-Off Form | One sign-off per module, signed by trainer and line supervisor |
| Competency Register | Maintained in MES and HR systems for auditability |
| Gate Rule | No live production line access until all 4 module sign-offs are complete |

---

## 4. Six-Week Curriculum and Assessment

## 4.1 Week 1 — Safety Induction and ESD Handling

**Core content**

- Ogun State Factories Act obligations and emergency response
- PPE requirements by zone (including SMT HEPA/ESD policy)
- ESD fundamentals and production risk impact
- ESD controls: strap testing, mat use, tray discipline, ioniser awareness
- ESD zone demarcation (SMT and assembly zones)
- ESD equipment check-in/check-out routine
- Incident and near-miss reporting flow

**Assessment**

- Written safety quiz (minimum pass mark 80%)
- Practical ESD wrist-strap test demonstration

## 4.2 Week 2 — 5S Methodology

**Core content**

- Sort, Set in Order, Shine, Standardise, Sustain with electronics examples
- Visual management standards: labels, floor tape, shadow boards, andon
- Weekly zone 5S audit scoring method
- Before/after floor-layout practical exercises
- Supervisor accountability for corrective action tracking
- Shift handover expectations for 5S sustainment

**Assessment**

- Practical walk-through of a mock station with 5 planted defects to identify and remediate

## 4.3 Week 3 — MES Core Navigation and Production Orders (Sandbox)

**Core content**

- Login and role model orientation (Operator, Technician, Supervisor, Engineer, Auditor)
- Work order read/execute flow and WIP routing basics
- Station scan-in/scan-out/hold transactions in sandbox
- Hold/release gate purpose and authority boundaries
- Rework event and reason-code capture
- Shift dashboard interpretation (OEE, FPY, downtime)

## 4.4 Week 4 — MES Role-Specific Deep Dives (Sandbox)

**Core content**

- SMT flow interpretation for SPI/AOI result handling and escalation
- Assembly flow events: torque confirmation, serial registration, function-test acknowledgement
- QC flow: NCR lifecycle, RF sample flag handling, hold/release control
- Supervisor flow: release approvals, escalation routing, shift review
- Audit-trail integrity and zero-workaround policy for all users

**Assessment (Weeks 3–4 combined)**

- Simulated production-order lifecycle in sandbox:
  - create order
  - route 10 units through scan events
  - hold 1 unit for rework
  - release unit after rework
  - close order with complete records

## 4.5 Week 5 — Quality Awareness and IPC Standards

**Core content**

- Quality KPI awareness: FPY, DPPM, OEE
- IPC-A-610 Class 2 acceptability criteria and defect recognition
- Visual inspection method (lighting, magnification, sequence discipline)
- Cosmetic defect classification using AI-assist context
- NCC compliance awareness and MES dispatch-block implications
- IEC 62368-1 safety awareness near test operations
- Defect escalation and line-stop protocol
- Packaging quality checks and carton/weight validation controls

**Assessment**

- Visual inspection practical (minimum 8/10 correct classifications)
- 10-question IPC recognition quiz

## 4.6 Week 6 — Integration, Final Assessment, and Sign-Off

**Core content**

- End-to-end simulated shift across safety, 5S, MES, and quality workflows
- Role-based scenarios (including supervisor containment/escalation)
- Common failure modes and prevention controls
- Escalation map recap and ownership confirmation

**Final assessment**

- Written integrated exam (minimum pass mark 80%)
- Practical station simulation scored by trainer + line supervisor
- Live sandbox scenario completed independently

**Completion output**

- Competency record co-signed by trainer and supervisor
- Record uploaded to MES profile and HR competency register
- Access gate remains closed until all module sign-offs are complete

---

## 5. Governance and Tracking Controls

| Control | Rule |
|---|---|
| Weekly Academy Tracker | Report cohort progress, pass/fail by module, retakes, and completion forecast vs ramp needs |
| Competency Register | Keep synchronized records in MES and HR for regulatory and customer audit evidence |
| Retest Policy | 1st failure: retest within 5 days; 2nd failure: supervisor-led remediation before third attempt |
| Refresher Policy | Annual refresher for MES and IPC modules; extra refresher triggered on role/RBAC changes |

---

## 6. Readiness Dependencies

| Dependency | Status |
|---|---|
| MES sandbox deployed | Met |
| MES RBAC model and user accounts defined | Met |
| Classroom and training space | Met (designation required) |
| External IPC trainer engagement | Met (procurement action) |
| ESD demo kit availability | Met (consumable preparation) |
| Competency record template linkage to MES IDs | Met (HR/MES governance action) |

---

*This Academy plan operationalises WS9 workforce readiness into a controlled, auditable onboarding path before production volume ramp.*
