# Personal Electronics Factory — MES Phase 1 Software Setup

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1
> **Document Version:** 1.0 | **Owner:** MES / Digital Manufacturing Team

---

## 1. Purpose & Scope

This document defines the **deployable Phase 1 MES software baseline** for the Personal Electronics Factory. It is the operational companion to [`mes-integration.md`](./mes-integration.md), which remains the primary specification for MES architecture, interfaces, traceability, security, and cross-system integration.

Phase 1 software setup is designed to be fully deployed and validated **before live machine connection**. The scope covers:

- MES platform deployment topology
- Sandbox and production configuration boundaries
- Edge-node layout and sync rules
- Production-order workflow and WIP tracking rules
- Station identity, interface contracts, and traceability controls
- Role-based access, dashboards, and audit readiness
- Sandbox validation required before machine commissioning

---

## 2. Phase 1 Deployable Software Baseline

### 2.1 Environment Topology

| Layer | Phase 1 Baseline | Purpose | Deployment Rule |
|---|---|---|---|
| Cloud tenant | Coo-Cah shared platform tenant | Central governance, analytics, backup replication, API management | Active from day 1 |
| Site MES application server | On-site primary MES node | Executes production orders, WIP transactions, traceability, quality workflows | Mandatory before line commissioning |
| Cloud-sync secondary | Cloud recovery instance | Warm standby, configuration backup, non-real-time reporting continuity | Sync enabled after site acceptance |
| Edge node — SMT | Dedicated SMT edge runtime | Buffers machine events, handles local protocol adapters, queueing | Required for SMT Line 1 and SMT Line 2 |
| Edge node — Assembly | Dedicated assembly/runtime node | Handles flash, torque, function test, and line-side station traffic | Required before assembly pilot |
| Edge node — QC + RF Lab | Dedicated test/radio node | Handles RF, safety, cosmetic, acoustic, and packaging quality events | Required before release validation |
| Integration gateway | API and message broker layer | Controls REST, MQTT, OPC-UA, EMS, and AMR integrations | Shared service with explicit credential segregation |
| Reporting layer | Dashboards and audit exports | Go-live dashboards, exception review, KPI monitoring | Read-only access for most business users |

### 2.2 Sandbox vs Production Configuration

| Configuration Area | Sandbox Mode | Production Mode | Control Requirement |
|---|---|---|---|
| Tenant | Non-production tenant | Production tenant | No shared credentials |
| Work orders | Simulated and test-only orders | ERP-approved live orders | Distinct numbering series |
| Station events | Simulated payloads and operator test scans | Live equipment and operator transactions | Production stations reject sandbox traffic |
| AMR integration | Mission simulation and acknowledgement emulation | Live mission dispatch to fleet manager | Separate API base URLs and tokens |
| EMS integration | Sampled/simulated energy payloads | Live energy meter ingestion | Sandbox cannot overwrite production energy records |
| Serial numbers | Reserved test serial namespace | Live serial namespace | Duplicate prevention in both environments |
| User accounts | Test users with masked identities | Named production accounts | MFA mandatory for production admin roles |
| Dashboards | Validation dashboards with test banners | Operational dashboards | Clear environment banner on every screen |
| Backups | Daily snapshot retained 14 days | Daily incremental + weekly full retained per policy | Backup jobs isolated per environment |

### 2.3 Edge-Node Layout

| Edge Node | Connected Zones / Functions | Local Responsibilities | Minimum Availability Target |
|---|---|---|---|
| `EDGE-SMT-01` | SMT_L1, SMT_L2, incoming PCB traceability | Queue equipment events, map line telemetry, recover after brief network loss | 99.5% |
| `EDGE-ASM-01` | Phone assembly, TWS/watch assembly, flash, torque, function test | Station transaction caching, scan validation, routing to MES workflow engine | 99.5% |
| `EDGE-QA-01` | RF lab, safety test, acoustic test, packaging QA | Test result buffering, hold/release event forwarding, outbound quality record sync | 99.5% |

### 2.4 Database, Backup, and Sync Rules

| Data Domain | System of Record | Sync Rule | Backup / Retention Rule |
|---|---|---|---|
| Production orders | Site MES database | Real-time sync to cloud secondary after commit | Daily incremental; weekly full |
| WIP transactions | Site MES database | Async replication within 60 seconds | Retain operational history for trend analysis |
| Traceability genealogy | Site MES traceability store | Near-real-time sync; no destructive overwrite | Retain minimum 5 years |
| Quality and NCC records | Site MES quality/NCC modules | Near-real-time sync with audit checksum | Retain minimum 5 years |
| Dashboard aggregates | Reporting database | Refresh every 1–5 minutes by dashboard class | Rebuildable from source data |
| Integration logs | Gateway log store | Sync summary metrics to cloud; keep local detailed logs | Retain 12 months online |
| User/role assignments | Identity store + MES RBAC | Sync on change approval | Full audit trail retained |

### 2.5 User and Account Provisioning Model

| Account Class | Provisioning Rule | Approval Owner | Notes |
|---|---|---|---|
| Operator | Named account or controlled shared station account | Production Supervisor + MES Admin | Shared accounts allowed only on approved fixed terminals |
| Technician | Named account only | Functional Manager + MES Admin | Elevated device troubleshooting rights |
| Supervisor | Named account only | Department Head + MES Admin | Can manage holds, releases, and shift dashboards |
| Engineer | Named account only | Engineering Lead + MES Admin | Can configure mappings in approved scope |
| Admin | Named account only with MFA | IT/MES Manager | No generic admin accounts |
| Auditor | Time-bound named account | Quality/Compliance Lead | Read-only with export rights |

Provisioning controls:

- no account is created without role, department, and owner assignment
- all privilege changes require ticketed approval
- dormant accounts are disabled after defined inactivity
- production admin access is logged and reviewed weekly

### 2.6 Dashboard Scope

The Phase 1 deployment must enable the following dashboard families before go-live:

- **operations dashboards:** order progress, WIP by zone, station backlog, line status
- **quality dashboards:** FPY, defect pareto, hold queue, traceability completeness, RF/NCC status
- **logistics dashboards:** AMR mission requests, WIP transfer ageing, packaging and despatch readiness
- **energy dashboards:** kWh by zone, kWh per production order, utility alarm status
- **governance dashboards:** user access changes, integration health, backup status, sandbox validation evidence

---

## 3. Phase 1 Production-Order Workflow

### 3.1 Workflow States

| Stage | Business Meaning | Entry Trigger | Exit Trigger |
|---|---|---|---|
| Order Created | Order exists in MES but is not yet executable | ERP/API creation or approved manual creation | Material and routing review complete |
| Order Released | Order is approved for station execution | Supervisor/Planner release action | First station dispatch issued |
| Station Dispatch | Order or lot is assigned to a route step/station family | Release to SMT, assembly, QC, or packaging route | Unit/lot arrives and is scanned into station |
| In Process | Unit or lot is actively executing a route step | Station entry event recorded | Station exit, hold, or failure event |
| Hold | Unit/lot cannot continue pending decision | Quality, engineering, material, or system hold | Hold disposition approved |
| Rework | Unit/lot is routed to approved rework path | Rework disposition issued | Rework completion accepted or scrap confirmed |
| Completed | All mandatory route steps and quality gates are passed | Final pack or final test completion | Packaging closeout begins |
| Packaged | Unit is packed and linked to carton/pallet | Packaging station closeout | Despatch staging confirmed |
| Dispatch Closed | Goods are handed to WMS/distribution with full genealogy | Shipment/ASN confirmation | Order archived for reporting |

### 3.2 Workflow Rules

1. Orders cannot be released without approved BOM, route, and station-family mapping.
2. Station dispatch must point to a valid station ID and expected quantity or unit serial.
3. A hold blocks onward routing until an approved release, rework, or scrap disposition is posted.
4. Rework must preserve the original serial/genealogy record and append new event history; no overwrite is allowed.
5. Completion requires all mandatory traceability and quality checkpoints for the product family.
6. Packaging is a controlled route step, not an informal warehouse event.
7. Dispatch closeout requires carton/pallet/shipment linkage and active compliance status for the SKU.

---

## 4. WIP Tracking Rules by Zone and Station

### 4.1 Mandatory WIP Event Model

| Event Type | Required At | Minimum Data Captured |
|---|---|---|
| Route dispatch | Every route step assignment | Order ID, route step, target station family, quantity/serial |
| Station entry | Every connected station | Station ID, unit/lot identifier, operator or device ID, timestamp |
| Station exit | Every connected station | Result, output quantity, next route step, timestamp |
| Transfer confirmation | All zone-to-zone moves | Source zone, destination zone, carrier ID or AMR mission, timestamp |
| Hold | All exception cases | Hold code, owner, reason, timestamp |
| Release / disposition | All held units/lots | Decision code, approver, next route, timestamp |

### 4.2 Zone-Level WIP Rules

| Zone | Required Scan / Event Points | Ownership Rule | Exception Handling |
|---|---|---|---|
| SMT receiving/start | PCB panel arrival, line assignment, first machine entry | SMT Supervisor owns WIP until downstream transfer accepted | Missing panel ID forces hold |
| SMT output buffer | Line completion, AOI disposition, tray creation | SMT to Assembly handoff only after tray ID confirmation | Failed AOI/X-ray/ICT routes to rework or hold |
| Phone / wearable assembly | Station entry and exit at each mandatory station family | Assembly Supervisor owns WIP from accepted tray to final test handoff | Blocked units move to containment queue |
| Flash / serialisation | Serial assignment, firmware result, uniqueness validation | MES enforces serial issuance before next step | Duplicate or failed flash forces hold |
| Functional / QC test | Test start, test result, repair disposition if failed | Quality owns units in test/repair queues | Failed units require rework or scrap decision |
| RF / safety lab | Sample selection, test result, release/hold event | Quality + Regulatory own compliance queue | Non-compliant results block release and despatch |
| Packaging | Pack confirmation, carton creation, pallet link | Packaging Lead owns WIP until warehouse handoff | Missing genealogy link blocks pack close |
| Despatch staging | Pallet scan, ASN/despatch event | Warehouse / Distribution interface owns staged goods | Any incomplete serial list blocks closeout |

### 4.3 Transfer-of-Ownership Rules

- SMT to Assembly: ownership changes only after destination zone acknowledges tray receipt.
- Assembly to QC/Test: ownership changes at station-entry confirmation in the receiving queue.
- QC/Test to Packaging: ownership changes only for units with passed mandatory quality gates.
- Packaging to Warehouse/Dispatch: ownership changes at pallet acceptance and ASN generation.

### 4.4 WIP Exception Rules

| Exception | Required MES Action | Outcome Rule |
|---|---|---|
| Rework required | Create rework route and reference original event | Unit remains visible in original order genealogy |
| Scrap confirmed | Capture scrap code, approver, and last good station | Unit closed from active WIP but retained in history |
| Blocked unit | Place unit on hold with owner and SLA | Cannot move until release or disposition |
| Missing scan | Force exception queue review | No manual completion without supervisor approval |
| Interface outage | Buffer locally on edge node and replay after recovery | Replay must preserve original timestamps |

---

## 5. Traceability Operational Matrix

### 5.1 Mandatory Data by Station Family

| Station Family | Mandatory Data Fields | Capture Mode |
|---|---|---|
| SMT start | Work order, PCB panel ID, SMT line ID, recipe, timestamp | Automatic + scan |
| SMT inspection | Panel/board ID, SPI/AOI result, defect code, image reference if available | Automatic |
| ICT / probe / X-ray | Panel/board ID, test type, result, defect/ref code | Automatic or controlled upload |
| Assembly station | Unit/lot ID, station ID, operator ID, start/stop timestamp | Scan + manual confirmation |
| Torque station | Unit serial, station ID, program ID, torque/angle result | Automatic via OPC-UA |
| Flash / serialisation | Unit serial, IMEI/serial result, firmware version, flash result | Automatic via REST |
| Function / cosmetic / acoustic test | Unit serial, test result, defect class/reference, fixture ID | Automatic via REST/LAN |
| RF / safety lab | Unit serial, test result, certificate/sample link, approver if manual | Automatic + manual approval |
| Packaging | Unit serial, carton ID, pallet ID, operator ID, timestamp | Scan + manual confirmation |
| Dispatch | Pallet ID, shipment/ASN ID, despatch timestamp, destination | Scan + ERP/WMS event |

### 5.2 Automatic vs Manual Event Rules

| Data/Event Class | Automatic | Manual / Human-Assisted |
|---|---|---|
| Machine telemetry and test results | Yes | No |
| Station scan-in and scan-out confirmation | Device-assisted | Yes |
| Hold / release / scrap disposition | No | Yes |
| Rework authorisation | No | Yes |
| Carton / pallet linkage | Device-assisted | Yes |
| Audit note attachments | No | Yes |

### 5.3 Genealogy Link Requirements

Every shippable unit must support the following parent-child genealogy chain:

`PCB Panel ID -> Board ID -> Unit Serial / IMEI -> Carton ID -> Pallet ID -> Shipment / ASN ID`

Additional rules:

- rework events append to the same genealogy chain
- split lots must retain common parent references
- merged packaging groups must preserve each child serial membership
- any missing genealogy link blocks dispatch closeout

### 5.4 Retention Rules

| Record Type | Minimum Retention |
|---|---|
| Serial genealogy and quality/test history | 5 years |
| NCC/RF compliance records | 5 years |
| Production order and WIP transaction history | 5 years |
| User access and approval logs | 2 years online, archived thereafter |
| Integration error and replay logs | 12 months online, archived thereafter |

---

## 6. Phase 1 Station-ID and Interface Map

### 6.1 Station Naming Standard

Station IDs follow:

`<AREA>-<LINE OR CELL>-<STEP>-<NN>`

Examples:

- `SMT-L1-PRINT-01`
- `SMT-L2-AOI-01`
- `ASM-PH2-FLASH-01`
- `ASM-PH2-TORQUE-02`
- `QA-RF-CMW500-01`
- `PKG-LN1-PACK-01`
- `LOG-AMR-PICK-SMT01`

### 6.2 Connected Station and Endpoint Register

| Station / Endpoint Group | Example Station IDs | Primary Protocol | Direction | Notes |
|---|---|---|---|---|
| SMT printer / placement / reflow | `SMT-L1-PRINT-01`, `SMT-L1-PNP-01`, `SMT-L1-REFLOW-01` | SECS/GEM, Modbus TCP, OPC-UA | Bi-directional | Line recipe and execution telemetry |
| SMT inspection | `SMT-L1-SPI-01`, `SMT-L1-AOI-01` | SECS/GEM or REST | To MES | Quality result ingestion |
| Assembly stations | `ASM-PH1-BUILD-01`, `ASM-PH2-BUILD-04` | Barcode/terminal transaction | To MES | Operator-guided execution |
| Flash fixtures | `ASM-PH2-FLASH-01` | REST API | Bi-directional | Serial issue + firmware status |
| Torque stations | `ASM-PH2-TORQUE-01` to `ASM-PH3-TORQUE-04` | OPC-UA | To MES | Program result per screw channel |
| Function / cosmetic / acoustic test | `QA-PH2-FCT-01`, `QA-VIS-01`, `QA-AUD-01` | REST / LAN API | To MES | Test result + defect reference |
| RF / safety lab | `QA-RF-CMW500-01`, `QA-SAFE-CH19053-01` | VISA/LAN, Ethernet API | To MES | Compliance and release gate data |
| Packaging | `PKG-LN1-PACK-01`, `PKG-LN1-LABEL-01` | Scan terminal / Ethernet API | To MES | Carton, pallet, and label linkage |
| AMR pickup / drop | `LOG-AMR-PICK-SMT01`, `LOG-AMR-DROP-PH201` | REST API | Bi-directional | Mission creation and completion |
| EMS meters / energy points | `EMS-Z2-MTR-01`, `EMS-Z4-MTR-01` | OPC-UA / REST | To MES | Zone and order-level energy data |

---

## 7. Integration Contracts for Phase 1 Sandbox Validation

### 7.1 OPC-UA Namespace Baseline

| Namespace | Purpose | Example Tag |
|---|---|---|
| `ns=2;s=CCE/SMT/L1/Printer/Status` | SMT equipment runtime state | `RUNNING` |
| `ns=2;s=CCE/ASM/PH2/Torque01/Result` | Torque result payload | `{"serial":"...","ok":true}` |
| `ns=2;s=CCE/EMS/Z4/kWh` | Energy meter value | `1245.32` |
| `ns=2;s=CCE/AMR/Mission/Ack` | AMR bridge acknowledgement | `DISPATCHED` |

Rules:

- sandbox tags use the same namespace structure with a sandbox endpoint
- quality-critical tags must include timestamp and source identifier
- replayed events must preserve original event time

### 7.2 REST Contract Ownership

| Endpoint | Owner System | Consumer | Primary Purpose |
|---|---|---|---|
| `POST /api/v1/mes/orders` | MES | ERP / approved admin tooling | Create or update production orders |
| `POST /api/v1/mes/station-events` | MES | Edge nodes / station apps | Record station entry, exit, hold, rework events |
| `POST /api/v1/mes/traceability/pack` | MES | Packaging terminals | Link serials to cartons/pallets |
| `POST /api/v1/amr/dispatch` | AMR bridge | MES | Create WIP transfer missions |
| `POST /api/v1/ems/consumption` | EMS bridge | MES | Ingest zone/order energy data |
| `GET /api/v1/mes/dashboards/go-live` | MES | Dashboards / reporting | Return readiness KPI aggregates |

### 7.3 Request and Response Minimum Schema

| Contract | Required Request Fields | Required Response Fields |
|---|---|---|
| Production order create/update | `order_id`, `sku`, `route_id`, `planned_qty`, `due_date`, `source_system` | `order_id`, `status`, `accepted_at` |
| Station event | `event_id`, `station_id`, `event_type`, `unit_or_lot_id`, `timestamp`, `source` | `event_id`, `status`, `next_step` |
| AMR dispatch | `mission_type`, `source_zone`, `destination_zone`, `payload_description`, `work_order_id` | `mission_id`, `status`, `assigned_amr_id` |
| EMS ingestion | `meter_id`, `zone_id`, `timestamp`, `kwh`, `order_id` | `ingestion_id`, `status` |

### 7.4 Error Handling and Retry Rules

| Scenario | Required Behaviour |
|---|---|
| Validation error | Return 4xx with machine-readable error code and rejected field list |
| Temporary downstream outage | Return retryable 5xx or queue locally for replay |
| Duplicate event submission | Use idempotency key or `event_id` to return prior accepted result |
| Timeout | No silent drop; client retries using same idempotency key |
| Partial batch failure | Return per-record acceptance/rejection summary |

Retry controls:

- station and gateway events must be idempotent
- replay sequence must be ordered per source device
- maximum retry interval must be defined per connector
- failed replay queues require supervisor-visible alerting

### 7.5 Sandbox Simulated Payloads

**AMR dispatch simulation**

```json
{
  "mission_type": "WIP_TRANSFER",
  "source_zone": "SMT_L1_OUTPUT",
  "destination_zone": "ASM_PH2_INPUT",
  "payload_description": "CCE-SP-LITE Mainboards, Qty: 40, Tray-ID: TR-SBX-0007",
  "priority": "NORMAL",
  "requested_by": "MES_SANDBOX",
  "work_order_id": "WO-SBX-2026-0012"
}
```

**EMS energy ingestion simulation**

```json
{
  "meter_id": "EMS-Z4-MTR-01",
  "zone_id": "Z4_PHONE_ASSEMBLY",
  "timestamp": "2026-05-11T10:15:00Z",
  "kwh": 18.6,
  "order_id": "WO-SBX-2026-0012",
  "source": "EMS_SANDBOX"
}
```

---

## 8. Roles and Access Model

| Role | Orders | WIP Edits | Holds / Releases | Quality Records | Dashboards | Audit Export |
|---|---|---|---|---|---|---|
| Operator | View assigned orders only | Record station transactions only | No | Enter limited defect / completion confirmations | Line/shift views only | No |
| Technician | View assigned and local-area orders | Correct local station transactions with reason code | Can request hold; cannot approve release | Add repair/test detail in assigned area | Area dashboards | No |
| Supervisor | Release orders, re-sequence local dispatch | Approve controlled WIP corrections | Approve hold, release, rework in assigned area | Approve dispositions and sign off shift quality actions | Area and shift dashboards | Limited operational exports |
| Engineer | View and analyse all orders | Controlled engineering corrections | Can place engineering hold/release | View and annotate engineering investigations | Factory engineering dashboards | No |
| Admin | Full order administration | Full correction rights with audit trail | Full rights | Full rights | All dashboards incl. system health | Controlled export rights |
| Auditor | Read-only | No | No | Read-only | Compliance and traceability dashboards | Yes |

Role rules:

- no role may delete production history
- all override actions require reason codes and audit logging
- access to sandbox and production is segregated by role assignment
- auditors remain read-only at all times

---

## 9. Go-Live Dashboard Requirements

| Dashboard | Minimum Required Views |
|---|---|
| Production Order Status | order backlog, released vs in-process, completion by shift, overdue orders |
| WIP by Zone | live WIP count by zone/station family, ageing, blocked queue, transfer wait time |
| Line Stoppage / Alarms | current status, downtime reason, acknowledgement status, top recurring faults |
| FPY / OEE | line OEE, yield trend, defect pareto, throughput vs plan |
| Traceability Completeness | missing scan count, genealogy breaks, serial uniqueness exceptions |
| NCC / RF Test Status | sample queue, pass/fail trend, certificate linkage, blocked-release count |
| AMR Mission Status | open missions, ageing, success rate, stuck mission alerts |
| Energy by Zone / Order | kWh by zone, kWh per order, abnormal consumption alerts |
| System Readiness | interface health, backup completion, edge queue depth, user access changes |

---

## 10. Phase 1 Sandbox Validation and Go/No-Go

### 10.1 Validation Sequence

| Step | Validation Activity | Required Evidence |
|---|---|---|
| 1 | Deploy MES core application, database, reporting, and identity services | Installed environment checklist |
| 2 | Load master data (SKUs, routes, station IDs, users, reason codes) | Master-data sign-off |
| 3 | Create simulated production orders in sandbox | Order creation and release evidence |
| 4 | Simulate station entry/exit, hold, rework, and completion events | Event log and queue replay evidence |
| 5 | Validate serial genealogy from PCB through shipment object | Traceability audit report |
| 6 | Validate AMR dispatch requests and acknowledgements | Mission test log |
| 7 | Validate EMS/energy ingestion by zone and order | Energy dashboard evidence |
| 8 | Verify role-based access and approval routing | Access test matrix |
| 9 | Review dashboards, alerts, backups, and sync status | Go-live readiness dashboard pack |
| 10 | Run formal go/no-go sign-off | Signed readiness decision |

### 10.2 Go/No-Go Criteria

- production order workflow executes end-to-end in sandbox without manual database intervention
- mandatory WIP scan points are captured for all Phase 1 route families
- genealogy chain is complete from PCB panel to shipment object
- AMR and EMS interfaces pass contract and retry tests
- role-based access matches approved matrix
- dashboards expose the minimum operational and compliance views
- open critical defects are zero; major defects have accepted workaround and owner

---

*This document defines the Phase 1 MES software setup gate that must be passed before live station integration and controlled production ramp.*
