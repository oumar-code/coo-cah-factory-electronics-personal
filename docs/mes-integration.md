# Personal Electronics Factory — MES Integration Specification

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1
> **Document Version:** 1.0 | **Owner:** MES / Digital Manufacturing Team

---

## 1. MES Architecture Overview

The Personal Electronics Factory MES is deployed as a Coo-Cah Platform module — a cloud-native MES with edge processing nodes on-site. The system handles production order management, real-time WIP tracking, full unit-level serialisation and traceability, quality management (including NCC type approval RF test result logging), energy monitoring, and AMR fleet dispatching.

```
                ┌─────────────────────────────────────────────┐
                │           Coo-Cah Cloud Platform            │
                │  ERP  |  AI Platform  |  DT  |  Analytics  │
                └────────────────┬────────────────────────────┘
                                 │ HTTPS / MQTT (TLS 1.3)
                ┌────────────────▼────────────────────────────┐
                │          MES Application Server             │
                │  (on-site primary + cloud-sync secondary)   │
                └──┬──────────┬────────────┬──────────────────┘
                   │          │            │
         ┌─────────▼──┐  ┌───▼────────┐  ┌▼────────────────┐
         │  Edge Node  │  │  Edge Node │  │  Edge Node       │
         │  (SMT Zone) │  │ (Assembly) │  │ (QC + RF Lab)   │
         └──┬──────────┘  └───┬────────┘  └┬────────────────┘
            │                 │             │
     OPC-UA / MQTT / Ethernet / Wi-Fi (IEEE 802.11ax)
            │                 │             │
  ┌─────────▼─────────────────▼─────────────▼──────────────┐
  │          Shop Floor — Industrial Control Network         │
  │  SMT Machines | Conveyors | Cobots | AMRs | Test Rigs   │
  └────────────────────────────────────────────────────────┘
```

---

## 2. MES Module Summary

| Module               | Functionality                                                     | Phase Available |
|----------------------|-------------------------------------------------------------------|-----------------|
| Production Order Mgmt | Work order creation, dispatch, progress tracking                 | Phase 1         |
| WIP Tracking          | Real-time unit-level WIP location by zone and station            | Phase 1         |
| Traceability          | Full unit serial number life history from PCB to dispatch        | Phase 1         |
| Quality Management    | SPC, in-line hold/release gates, NCR management                  | Phase 1         |
| NCC Test Logging      | RF test results, type approval sample tracking, certificate status| Phase 1        |
| AMR Fleet Dispatch    | MiR Fleet integration; work order → transport mission creation   | Phase 1         |
| Energy Monitoring     | Zone-level energy sub-metering; kWh per production order         | Phase 1         |
| Maintenance (CMMS)    | PM scheduling, work orders, spare parts inventory                | Phase 1         |
| Predictive Maintenance | AI vibration/temperature alert → maintenance work order          | Phase 2         |
| AI Scheduling         | Dynamic order sequencing based on real-time OEE and demand       | Phase 2         |
| Digital Twin Sync     | Live machine state feed to digital twin simulation model         | Phase 2         |

---

## 3. Serial Number & Traceability Architecture

Every unit produced in the factory receives a globally unique serial number at the point of IMEI/serial flash (phones) or equivalent identification point (TWS, watches, power banks). Traceability is maintained across the unit's full production life cycle.

### 3.1 Serial Number Format

```
Product Prefix + Factory Code + Year + Julian Day + Sequence
Example: CCE-SP-LITE-SAG-25-212-004501
   CCE        = Coo-Cah Electronics
   SP-LITE    = Product SKU abbreviation
   SAG        = Sagamu Factory
   25         = Year 2025
   212        = Julian day 212 (31 July)
   004501     = Daily sequence number (zero-padded 6 digits)
```

### 3.2 Traceability Data Captured per Unit

| Data Point                  | Capture Stage            | Stored In               |
|-----------------------------|--------------------------|-------------------------|
| PCB Panel ID                | SMT line-start scan      | MES Traceability Module |
| SMT Line Used (L1 or L2)    | Automatic (station ID)   | MES                     |
| SPI paste volume result     | Koh Young → MES          | MES Quality Module      |
| AOI result (pass/fail/rework)| Koh Young → MES         | MES Quality Module      |
| X-Ray result (BGA)          | Manual upload or API      | MES Quality Module      |
| ICT / Flying Probe result   | Keysight / Takaya → MES  | MES Quality Module      |
| Assembly line + station      | Barcode scan per station  | MES Traceability        |
| Torque values (all screws)  | Atlas Copco → MES (OPC-UA)| MES Traceability        |
| IMEI / Serial Number        | Flash station → MES API  | MES + ERP               |
| Software version flashed    | Flash fixture → MES      | MES Traceability        |
| Phone function test result  | Test fixture → MES       | MES Quality Module      |
| RF calibration value        | RF calibration jig → MES | MES + NCC Log           |
| NCC RF test result          | R&S CMW500 → MES         | MES NCC Module          |
| IEC 62368-1 safety result   | Chroma 19053 → MES       | MES Quality Module      |
| AI cosmetic QC result       | Cognex IS9000 → MES      | MES Quality Module      |
| Packaged by operator ID     | Operator badge scan       | MES Traceability        |
| Carton ID / Pallet ID       | Label scan                | MES WMS                 |
| Dispatch date / batch        | Dispatch scan             | MES WMS                 |

---

## 4. NCC Type Approval Integration (Nigeria-Specific)

NCC Type Approval is a mandatory Nigerian Communications Commission requirement for all wireless devices placed on the Nigerian market. The MES NCC module manages the full type approval lifecycle, from sample selection through to certificate expiry tracking.

### 4.1 NCC Module Functionality

| Functionality                              | Description                                                               |
|--------------------------------------------|---------------------------------------------------------------------------|
| Type Approval Certificate Registry         | Stores NCC TA number, product SKU, certificate date, expiry date         |
| Production RF Sample Selection             | MES auto-flags every Nth unit per shift as "NCC RF Test Sample"          |
| RF Test Result Logging                     | R&S CMW500 test results (TRP, TIS, spurious emissions) stored per serial |
| Sample Certificate Linkage                 | Each production batch linked to the active NCC TA certificate            |
| Expiry Alert & Renewal Workflow            | Alert raised 6 months before expiry; auto-creates TA renewal task        |
| Blocked-Dispatch Gate                      | MES blocks dispatch of any product SKU without a valid NCC TA certificate|
| NCC Audit Report Generation                | One-click report of all RF test results for NCC audit/inspection          |

### 4.2 NCC Type Approval Certificate Register

| Product SKU       | NCC TA Number (placeholder) | Frequency Bands          | Certificate Date | Expiry Date | Status       |
|-------------------|-----------------------------|--------------------------|-----------------|-------------|--------------|
| CCE-FP-3G         | NCC/TA/2025/XXXX            | GSM 900/1800, WCDMA B1/B8| Q3 2025         | Q3 2030     | Pending (P1) |
| CCE-FP-4G         | NCC/TA/2025/XXXX            | GSM, WCDMA, LTE B1/B3/B8 | Q4 2025         | Q4 2030     | Pending (P1) |
| CCE-SP-LITE       | NCC/TA/2025/XXXX            | LTE B1/B3/B8, Wi-Fi 4    | Q3 2025         | Q3 2030     | Pending (P1) |
| CCE-SP-MID        | NCC/TA/2027/XXXX            | LTE B1/B3/B8, Wi-Fi 5, BT 5.3 | Q2 2027   | Q2 2032     | Pending (P2) |
| CCE-TWS-01        | NCC/TA/2025/XXXX            | Bluetooth 5.0            | Q4 2025         | Q4 2030     | Pending (P1) |
| CCE-TWS-PRO       | NCC/TA/2027/XXXX            | Bluetooth 5.3, ANC       | Q3 2027         | Q3 2032     | Pending (P2) |
| CCE-SW-LITE       | NCC/TA/2026/XXXX            | Bluetooth 5.1            | Q1 2026         | Q1 2031     | Pending (P1) |
| CCE-SW-PRO        | NCC/TA/2027/XXXX            | BT 5.3, GPS, Wi-Fi 5     | Q2 2027         | Q2 2032     | Pending (P2) |

---

## 5. Machine Interface Specifications

### 5.1 SMT Equipment Integration

| Equipment            | Protocol    | Data Points                                              | Direction    |
|----------------------|-------------|----------------------------------------------------------|--------------|
| DEK Screen Printer   | SMEMA + SECS/GEM | Print recipe, paste volume, stencil life, alarms   | Bidirectional|
| Koh Young SPI/AOI    | SECS/GEM or REST API | Inspection result, defect codes, 3D images per board | To MES  |
| JUKI P&P (FX-3R, RX-7)| SECS/GEM  | Placement result, feeder error, CPH, component reels    | Bidirectional|
| Heller Reflow Oven   | Modbus TCP or OPC-UA | Zone temps, conveyor speed, alarm, recipe name    | Bidirectional|
| Ersa Selective Solder| OPC-UA      | Solder level, flux level, nozzle position, recipe        | Bidirectional|

### 5.2 Assembly & Test Equipment Integration

| Equipment                     | Protocol     | Data Points                                              | Direction    |
|-------------------------------|--------------|----------------------------------------------------------|--------------|
| Atlas Copco Torque Station    | OPC-UA       | Torque value, angle, OK/NOK per screw channel            | To MES       |
| Phone Flash Station           | REST API     | Serial number, firmware version, flash result OK/NOK     | Bidirectional|
| Phone Function Test Fixture   | REST API     | Per-test pass/fail: touch, audio, camera, NFC, charge    | To MES       |
| R&S CMW500 (RF tester)        | VISA / LAN   | RF test parameters, TRP/TIS, frequency deviation         | To MES       |
| Chroma 17020 (Battery tester) | Ethernet API | Capacity (mAh), IR, voltage, charge curve               | To MES       |
| Chroma 19053 (Safety tester)  | Ethernet API | Hipot voltage/current, earth bond result, OK/NOK         | To MES       |
| Cognex In-Sight 9000 (Vision) | REST API     | Pass/fail, defect class, image reference                 | To MES       |
| Mettler Toledo Checkweigher   | Ethernet API | Weight, pass/fail, serial ref                            | To MES       |
| Brüel & Kjær Acoustic System  | LAN API      | Frequency response, THD, sensitivity OK/NOK per channel  | To MES       |

---

## 6. AI Service API Integration

The Coo-Cah AI Platform exposes REST API endpoints consumed by the MES for AI-driven quality and operational decisions.

### 6.1 SMT Defect Prediction API

**Endpoint:** `POST /api/v1/ai/smt-defect-predict`

**Request Payload:**
```json
{
  "factory_id": "CCE-SAG-PERSONAL",
  "line_id": "SMT_L1",
  "board_id": "PANEL-2025-212-0045",
  "paste_volume_3d": {
    "mean_volume_percent": 98.4,
    "cpk": 1.45,
    "pads_inspected": 1280,
    "pads_failed": 0
  },
  "reflow_profile": {
    "peak_temp_c": 248,
    "tac_time_s": 62,
    "zone_8_temp_c": 241,
    "conveyor_speed_mm_min": 900
  },
  "placement_data": {
    "total_components": 312,
    "placement_misses": 0,
    "feeder_errors": 0
  }
}
```

**Response:**
```json
{
  "prediction_id": "SMT-PRED-20250731-0045",
  "defect_risk_score": 0.06,
  "risk_level": "LOW",
  "flagged_concerns": [],
  "recommended_action": "PROCEED",
  "model_version": "smt-predict-v2.3",
  "timestamp": "2025-07-31T08:14:22Z"
}
```

---

### 6.2 RF Calibration & NCC Compliance AI API

**Endpoint:** `POST /api/v1/ai/rf-calibration`

**Request Payload:**
```json
{
  "unit_serial": "CCE-SP-LITE-SAG-25-212-004501",
  "sku": "CCE-SP-LITE",
  "ncc_ta_number": "NCC/TA/2025/0042",
  "rf_test_results": {
    "band_b1_power_dbm": 23.1,
    "band_b3_power_dbm": 22.8,
    "band_b8_power_dbm": 32.5,
    "wifi_24_tx_dbm": 18.2,
    "wifi_24_rx_sensitivity_dbm": -88,
    "spurious_emissions_pass": true
  },
  "calibration_applied": {
    "b1_offset_db": 0.2,
    "b3_offset_db": 0.0,
    "b8_offset_db": -0.3
  }
}
```

**Response:**
```json
{
  "unit_serial": "CCE-SP-LITE-SAG-25-212-004501",
  "rf_calibration_status": "PASS",
  "ncc_compliance": "COMPLIANT",
  "ncc_ta_certificate": "NCC/TA/2025/0042",
  "result_stored": true,
  "dispatch_cleared": true,
  "timestamp": "2025-07-31T09:22:11Z"
}
```

---

### 6.3 Production OEE & Scheduling API

**Endpoint:** `GET /api/v1/mes/oee/realtime`

**Response:**
```json
{
  "factory_id": "CCE-SAG-PERSONAL",
  "timestamp": "2025-07-31T09:30:00Z",
  "oee_summary": {
    "factory_blended_oee": 0.743,
    "availability": 0.891,
    "performance": 0.872,
    "quality": 0.956
  },
  "lines": [
    {
      "line_id": "SMT_L1",
      "oee": 0.781,
      "status": "RUNNING",
      "current_product": "CCE-SP-LITE-MAINBOARD",
      "units_completed_shift": 1420
    },
    {
      "line_id": "PH-2",
      "oee": 0.718,
      "status": "RUNNING",
      "current_product": "CCE-SP-LITE",
      "units_completed_shift": 612
    }
  ]
}
```

---

### 6.4 AMR Fleet Mission Dispatch API

**Endpoint:** `POST /api/v1/amr/dispatch`

**Request Payload:**
```json
{
  "mission_type": "WIP_TRANSFER",
  "source_zone": "SMT_L1_OUTPUT",
  "destination_zone": "PH2_STATION_01",
  "payload_description": "CCE-SP-LITE Mainboards, Qty: 200, Tray-ID: TR-2025-212-0089",
  "priority": "HIGH",
  "requested_by": "MES_AUTO",
  "work_order_id": "WO-2025-212-0312"
}
```

**Response:**
```json
{
  "mission_id": "AMR-MISS-20250731-0312",
  "assigned_amr_id": "MIR250-07",
  "estimated_completion_time": "2025-07-31T09:47:33Z",
  "status": "DISPATCHED",
  "timestamp": "2025-07-31T09:44:00Z"
}
```

---

## 7. MES Data Governance & Security

| Requirement                     | Implementation                                                   |
|---------------------------------|------------------------------------------------------------------|
| Data Residency                  | Production data stored on-site (edge nodes); synced to Coo-Cah cloud (Lagos DC) |
| Encryption in Transit           | TLS 1.3 for all MES ↔ cloud, MES ↔ machine API connections      |
| Encryption at Rest              | AES-256 for all MES databases and trace data archives            |
| Role-Based Access Control       | Roles: Operator, Technician, Supervisor, Engineer, Admin, Auditor |
| NCC Audit Data Retention        | NCC test records retained for minimum 5 years (NCC requirement) |
| IMEI/Serial Data                | Linked to NIN (National Identity Number) verification at point of sale — Phase 2 |
| Backup                          | Daily incremental + weekly full backup; offsite copy to Coo-Cah Lagos DC |
| IT/OT Network Segregation       | MES on OT VLAN; isolated from corporate IT; DMZ for ERP integration|
| Penetration Testing             | Annual third-party pen test; critical finding resolution within 30 days |

---

## 8. MES Integration with Cross-Factory Systems

| System                              | Integration Type          | Data Exchanged                                         | Frequency     |
|-------------------------------------|---------------------------|--------------------------------------------------------|---------------|
| Coo-Cah ERP (SAP or equivalent)     | REST API / SAP RFC        | Production orders, BOM, inventory, costing, despatch   | Real-time     |
| Coo-Cah AI Platform                 | MQTT + REST API            | OEE, quality events, maintenance alerts, predictions   | Real-time     |
| Coo-Cah Plastics Factory MES        | REST API (factory link)    | Casing production schedule, WIP status, delivery ETA   | Hourly        |
| Garage Power Electronics MES        | REST API (factory link)    | PCB delivery schedule, internal PCB order status       | Hourly        |
| Coo-Cah Distribution / WMS          | REST API                  | Finished goods despatch notes, serial lists, ASN       | Per despatch  |
| NCC Type Approval Portal (external) | Manual + CSV export        | RF test summary reports for TA submission              | Per submission |
| SON NAFDAC Product Registry         | Manual submission + portal | Product registration data for NIS certification        | Per product    |
| Coo-Cah Digital Twin                | MQTT (streaming)           | Real-time machine states, sensor readings, WIP flow    | 1-second poll |

---

*For digital twin architecture, refer to [`digital-twin.md`](./digital-twin.md).*
*For regulatory data requirements, refer to [`regulatory.md`](./regulatory.md).*
*For supply chain ERP integration, refer to [`supply-chain.md`](./supply-chain.md).*
