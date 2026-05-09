# Digital Twin — Infrastructure & Network Architecture

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State
> **Document Version:** 1.0 | **Owner:** IT/OT Infrastructure Team
> **Status:** CONTROLLED BASELINE — Phase 0 platform-proving and edge-spec reference
> **Related:** [Coo-Kah-Doks — platform/digital-twin-platform-architecture.md](https://github.com/oumar-code/Coo-Kah-Doks/blob/main/platform/digital-twin-platform-architecture.md)

---

## 1. Architecture Overview

The Coo-Cah Personal Electronics Factory Digital Twin uses the **Coo-Cah DT Engine** — a
group-standard hybrid platform combining on-site edge processing with a Rwanda cloud hub. The
platform was selected in the group architecture decision recorded in Coo-Kah-Doks.

**Phase 0 proving requirements**

- Use this document as the deployment baseline for Task 0.2 dev-mode proving on the Rwanda cloud hub.
- Keep the bucket schema, Telegraf topic mapping, and dashboard catalogue aligned to the controlled
  asset manifest and MQTT namespace before any synthetic data validation sign-off.
- Use Section 3 as the building-services reference for Task 0.4 so rack, power, cooling, WAN, and
  OT/IT segregation are embedded before fit-out procurement freeze.

```
┌─────────────────────────────────────────────────────────────┐
│                    RWANDA CLOUD HUB                         │
│                                                             │
│  ┌─────────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │  InfluxDB 2.x   │  │   FastAPI    │  │    Grafana    │  │
│  │  (time-series   │  │  (DT API     │  │  (dashboards  │  │
│  │   data store)   │  │   backend)   │  │   & alerts)   │  │
│  └────────┬────────┘  └──────┬───────┘  └───────┬───────┘  │
│           │                  │                  │           │
│  ┌────────▼──────────────────▼──────────────────▼────────┐  │
│  │          Mosquitto MQTT Broker (cloud — TLS 1.3)       │  │
│  └────────────────────────┬───────────────────────────────┘  │
│                           │  MQTT Bridge (TLS 1.3, port 8883)│
└───────────────────────────┼──────────────────────────────────┘
                            │
                    WAN (100 Mbps dedicated
                    + Starlink backup)
                            │
┌───────────────────────────┼──────────────────────────────────┐
│              SAGAMU FACTORY — EDGE NODE                      │
│                           │                                  │
│  ┌─────────────────────────▼─────────────────────────────┐   │
│  │       Mosquitto MQTT Broker (edge — OT LAN)            │   │
│  │       + Telegraf (MQTT subscriber → InfluxDB writer)  │   │
│  │       + FastAPI edge proxy (local dashboard fallback) │   │
│  └───┬──────────────────────────────────────────────┬────┘   │
│      │ OT Network (VLAN 10 — segregated)            │        │
│      │                                              │        │
│  ┌───▼──────────────┐                    ┌──────────▼──────┐ │
│  │  OPC-UA / SECS-  │                    │  MiR Fleet API  │ │
│  │  GEM Gateway     │                    │  MQTT Bridge    │ │
│  │  (per SMT zone)  │                    │  (AMR fleet)    │ │
│  └───┬──────────────┘                    └─────────────────┘ │
│      │                                                        │
│  ┌───▼──────────────────────────────────────────────────────┐ │
│  │         Shop Floor — OT Industrial Control Network        │ │
│  │  SMT Machines │ Heller Oven │ Torque │ Flash │ RF Test   │ │
│  │  Koh Young    │ Ersa Solder │ Chroma │ Cognex│ R&S CMW   │ │
│  └──────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

**Key architectural decisions:**

1. **Read-only OT → DT** in Phase 1: no DT action writes back to OT systems. The twin observes
   only. This preserves OT network safety and avoids IEC 62443 compliance complexity in Phase 1.
2. **Edge-first resilience**: if the WAN link to Rwanda drops, all factory dashboards continue
   to work from the local Grafana instance on the edge node. Buffered data syncs to cloud on
   reconnection.
3. **Single MQTT bus**: all machine data flows through one MQTT broker topology. No direct machine
   → InfluxDB writes; all writes go through Telegraf on the edge node.

---

## 2. Software Stack

### 2.1 Component Summary

| Component | Technology | Version | Deployment | Purpose |
|---|---|---|---|---|
| Time-Series Database | InfluxDB OSS 2.x | 2.7+ | Rwanda cloud + edge mirror | Stores all sensor time-series data |
| API Backend | FastAPI (Python) | 0.100+ | Rwanda cloud + edge fallback | DT REST API; asset registry; query proxy |
| Dashboards & Alerting | Grafana OSS | 10.x | Rwanda cloud + edge fallback | All DT dashboards and alert rules |
| MQTT Broker | Eclipse Mosquitto | 2.x | Rwanda cloud + edge (bridge pair) | Central message bus |
| MQTT → InfluxDB Writer | Telegraf | 1.28+ | Edge node | Subscribes `cce/sag/#`; writes to InfluxDB |
| OPC-UA → MQTT Gateway | Kepware KEPServerEX or Node-RED OPC-UA | — | Edge node | Translates OPC-UA machine data to MQTT |
| SECS/GEM → MQTT Gateway | Cogiscan TrackerCore or equivalent | — | Edge node (SMT zones) | Translates SECS/GEM to MQTT |
| MiR Fleet MQTT Bridge | Python service (custom) | — | Edge node | Polls MiR Fleet REST API; publishes to MQTT |
| Simulation Engine | DES module (integrated into FastAPI) | — | Rwanda cloud | Discrete-event simulation for Phase 2+ |
| Container Runtime | Docker + Docker Compose | — | All nodes | Service packaging and deployment |

### 2.2 InfluxDB Schema Design

InfluxDB organises data into **buckets**, **measurements**, and **fields**. The schema follows
the MQTT topic structure.

**Buckets:**

| Bucket Name | Retention Policy | Purpose |
|---|---|---|
| `cce-sag-raw` | 90 days | All raw sensor data from MQTT |
| `cce-sag-aggregated` | 10 years | Hourly/daily downsampled aggregates |
| `cce-sag-events` | 5 years | Alarm events, quality results, state changes |
| `cce-sag-models` | 10 years | Predictive model outputs (Phase 2+) |

**Measurement naming (follows asset ID segments):**

```
measurement: smt_l1_reflow
tags:        factory=cce-sag, zone=z2, asset=smt-l1-reflow
fields:      zone1_temp_c, zone2_temp_c, ..., zone8_temp_c,
             conveyor_speed_mm_min, n2_level_pct, alarm_active
time:        (nanosecond precision timestamp)
```

**Telegraf MQTT subscription configuration (excerpt):**

```toml
[[inputs.mqtt_consumer]]
  servers = ["tcp://edge-broker:1883"]
  topics  = ["cce/sag/#"]
  qos     = 1
  data_format = "json"

  # Topic → tag mapping
  # cce/sag/{zone}/{asset}/{metric} → measurement=zone_asset, field=metric
  topic_measurement_map = {
    "cce/sag/z2/smt-l1-reflow/+" = "smt_l1_reflow",
    "cce/sag/z3/smt-l2-reflow/+" = "smt_l2_reflow",
    "cce/sag/amr/mir250/+/+"      = "amr_mir250",
    "cce/sag/energy/bess-+/+"     = "energy_bess"
  }

[[outputs.influxdb_v2]]
  urls   = ["http://influxdb:8086"]
  token  = "${INFLUXDB_TOKEN}"
  org    = "coo-cah"
  bucket = "cce-sag-raw"
```

### 2.3 FastAPI Backend

The FastAPI backend exposes the DT REST API consumed by Grafana, the MES, and the Coo-Cah
AI Platform. Core endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/api/v1/assets` | List all registered assets with current state |
| `GET` | `/api/v1/assets/{asset_id}` | Get asset details and latest sensor values |
| `GET` | `/api/v1/assets/{asset_id}/history` | Query InfluxDB history for an asset |
| `GET` | `/api/v1/oee/realtime` | Factory-wide and per-line OEE (from MES via MQTT) |
| `GET` | `/api/v1/energy/summary` | Live solar self-sufficiency, BESS SoC, generation totals |
| `GET` | `/api/v1/amr/fleet` | All AMR positions, missions, and battery states |
| `POST` | `/api/v1/simulation/des/run` | Submit a DES scenario (Phase 2+) |
| `GET` | `/api/v1/alerts/active` | Current active alerts by severity |
| `GET` | `/api/v1/ncc/rf-log/{sku}` | NCC RF test log for a given product SKU |

All endpoints require JWT Bearer token authentication. Role-based access:

| Role | Permissions |
|---|---|
| `operator` | GET all read endpoints except simulation |
| `engineer` | GET all read endpoints; POST simulation |
| `admin` | Full access including asset manifest updates |
| `auditor` | GET `/api/v1/ncc/*` and `/api/v1/assets/*/history` only |

### 2.4 Grafana Dashboard Catalogue (Phase 1)

| Dashboard Name | Zone(s) | Primary Audience | Key Panels |
|---|---|---|---|
| Factory Overview | All | Plant Manager | Factory OEE gauge, active alerts count, solar self-sufficiency, AMR fleet summary |
| SMT Line 1 Health | Z2 | Production Engineer | Reflow zone temps ×8, paste CPK trend, FPY per board, feeder error count, changeover timer |
| SMT Line 2 Health | Z3 | Production Engineer | Same as Line 1 |
| SMT Cross-Line Compare | Z2, Z3 | Shift Supervisor | Side-by-side OEE, FPY, feeder error rate, changeover time |
| AMR Fleet Map | All | Shift Supervisor | 2D floor plan with live AMR positions, dock occupancy, fleet battery summary |
| Phone Assembly Status | Z4 | Line Supervisor | Units/hour per line, flash yield, function test yield, torque NOK alerts |
| TWS & Watch Assembly | Z5, Z6 | Line Supervisor | Units/hour, acoustic test yield, pressure test pass rate, BT compliance yield |
| Power Bank Assembly | Z7 | Line Supervisor | Units/hour, spot weld energy trend, battery capacity distribution, safety test yield |
| RF & NCC Lab | Z8 | RF Engineer | Chamber utilisation, RF test pass rate per band, NCC TA certificate status, sample count |
| Energy Overview | Site | Energy Manager | Total generation kW (live), BESS SoC ×2, solar self-sufficiency %, kWh/phone, grid import |
| Final QC & Packaging | Z9, Z10 | QC Manager | Vision defect escape rate, weight check reject rate, dispatch readiness |
| Warehouse & Stores | Z1, Z11 | Logistics Manager | VLM inventory levels, FG pallet count, AMR put-away rate |
| Alert Log | All | All roles | Chronological alert history, MTTR per asset, SLA compliance |

---

## 3. Edge Node Specification

The factory edge node is the critical on-site compute resource. It must be provisioned, racked,
and energised before machine commissioning begins.

### 3.1 Hardware Specification

| Component | Minimum Specification | Recommended |
|---|---|---|
| Server form factor | 1U rack server | 2U for better thermal headroom |
| CPU | 8-core Intel Xeon E-2300 series | 16-core |
| RAM | 32 GB ECC DDR4 | 64 GB |
| Primary storage | 2× 1 TB NVMe SSD (RAID-1) | 2× 2 TB NVMe SSD (RAID-1) |
| Network | 2× 1 GbE (OT LAN); 2× 1 GbE (IT/WAN) | 2× 10 GbE (OT); 2× 1 GbE (IT) |
| UPS runtime | 30 minutes at full load | 60 minutes |
| Operating system | Ubuntu Server 22.04 LTS | Same |
| Rack location | Z12 — Engineering/MES room | Dedicated 42U rack |

### 3.2 Edge Node Software Services (Docker Compose)

```yaml
version: "3.9"
services:

  mosquitto-edge:
    image: eclipse-mosquitto:2
    ports:
      - "1883:1883"     # Local OT LAN (plain TCP — OT VLAN only)
      - "8883:8883"     # External bridge (TLS)
    volumes:
      - ./mosquitto/config:/mosquitto/config
      - ./mosquitto/data:/mosquitto/data
      - ./mosquitto/log:/mosquitto/log

  telegraf:
    image: telegraf:1.28
    depends_on:
      - mosquitto-edge
    volumes:
      - ./telegraf/telegraf.conf:/etc/telegraf/telegraf.conf
    environment:
      - INFLUXDB_TOKEN=${INFLUXDB_TOKEN}
      - INFLUXDB_URL=https://influxdb.coo-cah.rw

  influxdb-edge:
    # Edge InfluxDB is a local 7-day cache for fallback dashboards
    image: influxdb:2.7
    ports:
      - "8086:8086"
    volumes:
      - influxdb-edge-data:/var/lib/influxdb2

  grafana-edge:
    # Edge Grafana serves factory dashboards when WAN is down
    image: grafana/grafana:10.2.0
    ports:
      - "3000:3000"
    depends_on:
      - influxdb-edge
    volumes:
      - grafana-edge-data:/var/lib/grafana

  opcua-gateway:
    # OPC-UA → MQTT gateway for Heller, Ersa, Atlas Copco, routers
    image: iobroker/iobroker:latest   # or Kepware if licensed
    depends_on:
      - mosquitto-edge

  secsgem-gateway:
    # SECS/GEM → MQTT gateway for DEK, JUKI, Koh Young
    image: cogiscan/trackercore:latest   # or equivalent
    depends_on:
      - mosquitto-edge

  mir-bridge:
    # Custom Python service — polls MiR Fleet REST API → publishes to MQTT
    build: ./services/mir-bridge
    depends_on:
      - mosquitto-edge
    environment:
      - MIR_FLEET_URL=http://mir-fleet-manager.local
      - MQTT_BROKER=mosquitto-edge

  energy-bridge:
    # Custom Python service — Sungrow iSolarCloud API → MQTT
    build: ./services/energy-bridge
    depends_on:
      - mosquitto-edge
    environment:
      - ISOLARCLOUD_API_KEY=${ISOLARCLOUD_API_KEY}
      - MQTT_BROKER=mosquitto-edge

volumes:
  influxdb-edge-data:
  grafana-edge-data:
```

### 3.3 Edge Node Physical Build Steps

- [ ] Rack server installed in Z12 42U rack; cabled to dual-feed UPS circuit.
- [ ] OT network interfaces connected to OT VLAN switch (VLAN 10 — segregated from corporate IT).
- [ ] IT/WAN network interfaces connected to factory WAN router (dedicated 100 Mbps circuit).
- [ ] Starlink backup terminal mounted on factory roof; failover configured in WAN router.
- [ ] Ubuntu Server 22.04 LTS installed; SSH hardened; automatic security updates enabled.
- [ ] Docker and Docker Compose installed; services brought up in order.
- [ ] Mosquitto bridge verified: test message published on edge broker, confirmed arriving
      on Rwanda cloud broker within 500 ms.
- [ ] Grafana edge dashboards confirmed operational against local InfluxDB edge cache.

---

## 4. Rwanda Cloud Hub Specification

| Component | Specification |
|---|---|
| Cloud provider | Preferred: AWS af-south-1 (Cape Town) or equivalent African region |
| Compute | 16 vCPU, 64 GB RAM instance (e.g., AWS m6i.4xlarge) |
| Primary storage | 4 TB NVMe / SSD (InfluxDB data volume) |
| Object storage | S3 / equivalent for InfluxDB backups and BIM model files |
| Network | 1 Gbps egress; dedicated MQTT listener on port 8883 with TLS |
| Backup | Daily InfluxDB snapshot to object storage; retained 30 days |
| Monitoring | Prometheus + Grafana Cloud for infrastructure health |
| Uptime target | ≥ 99.5% monthly (planned maintenance windows excluded) |

**Cloud services deployed (identical stack to edge node, minus OT gateways):**

- Mosquitto cloud broker (bridge pair with edge)
- InfluxDB 2.x (primary data store; 90-day raw retention; 10-year aggregate)
- FastAPI backend (behind Nginx reverse proxy; HTTPS with Let's Encrypt certificate)
- Grafana (primary dashboard server; accessed by all users with WAN access)

---

## 5. OT/IT Network Architecture

### 5.1 Network Segmentation

The factory operates three separated network planes, each with distinct security controls:

```
┌─────────────────────────────────────────────────────────┐
│  CORPORATE IT NETWORK (VLAN 20 — office, MES portal)    │
│  192.168.20.0/24                                        │
│  Internet-facing via factory firewall (Fortinet 60F)    │
└──────────────────────────┬──────────────────────────────┘
                           │  DMZ / Firewall rules
┌──────────────────────────▼──────────────────────────────┐
│  MES APPLICATION SERVER NETWORK (VLAN 30 — MES + DT)   │
│  10.10.30.0/24                                          │
│  MES server, DT edge node, ERP integration endpoint     │
└──────────────────────────┬──────────────────────────────┘
                           │  Strict allow-list firewall rules
┌──────────────────────────▼──────────────────────────────┐
│  OT CONTROL NETWORK (VLAN 10 — machines + AMRs)         │
│  10.10.10.0/24                                          │
│  SMT machines, Torque stations, Flash fixtures,         │
│  Test equipment, AMR fleet, Energy controllers          │
│  NO internet access; NO access to VLAN 20              │
└─────────────────────────────────────────────────────────┘
```

### 5.2 Firewall Rules (VLAN 10 OT → VLAN 30 MES/DT)

| Source (OT) | Destination (MES/DT) | Port/Protocol | Direction | Purpose |
|---|---|---|---|---|
| SMT OPC-UA gateway | OT VLAN broker | 1883 TCP | OT → MES/DT | MQTT publish |
| SECS/GEM gateway | OT VLAN broker | 1883 TCP | OT → MES/DT | MQTT publish |
| MiR Fleet Manager | MES VLAN broker | 1883 TCP | OT → MES/DT | AMR MQTT bridge |
| Torque stations (OPC-UA) | OPC-UA gateway | 4840 TCP | OT → MES/DT | Torque data |
| Flash fixtures (REST) | MES server | 443 HTTPS | OT → MES/DT | Flash results API |
| BESS / Energy controllers | Energy bridge service | 502 TCP (Modbus) | OT → MES/DT | Energy data |
| **Blocked** | All OT → Corporate IT | All | BLOCKED | OT isolation |
| **Blocked** | All internet → OT | All | BLOCKED | OT protection |

### 5.3 Physical Network Infrastructure

| Layer | Technology | Specification |
|---|---|---|
| Factory backbone | Single-mode fibre | OS2 single-mode; one zone drop per production zone; 10 GbE capable |
| OT zone switches | Managed industrial Ethernet | Cisco IE3300 or Hirschmann MACH; VLAN-aware; DIN-rail or 19" rack mount |
| OT endpoints | Ethernet (Cat6A or fibre) | ESD-shielded cable in production zones |
| AMR Wi-Fi | IEEE 802.11ax (Wi-Fi 6) | Dense AP layout: 1 AP per 400 m² production zone; 2.4 GHz + 5 GHz |
| Edge node to WAN | Dedicated 100 Mbps | Leased line from Lagos via Sagamu; Starlink terminal for backup |
| OT LAN IP addressing | 10.10.10.x/24 | Statically assigned to all OT devices; DHCP disabled on OT VLAN |

### 5.4 Wi-Fi Network for AMR Fleet

All 16 AMRs use Wi-Fi to communicate with the MiR Fleet Manager and the MQTT bridge service.
The Wi-Fi network in the factory is dedicated to AMR use on the 5 GHz band to avoid interference
with any future portable operator devices on 2.4 GHz.

| Parameter | Specification |
|---|---|
| SSID | `CCE-AMR-5G` (5 GHz, hidden) |
| Security | WPA3-Enterprise with RADIUS (certificate-based) |
| AP placement | 1 per 400 m² — minimum 12 APs for 18,000 m² floor |
| Roaming protocol | 802.11r (Fast BSS Transition) to enable seamless AMR roaming |
| Coverage target | -65 dBm minimum RSSI at all floor positions |
| IP addressing | 10.10.10.100–10.10.10.130 (reserved block for AMRs) |

---

## 6. Cyber Security Controls

The DT infrastructure follows IEC 62443 Zone and Conduit model principles.

| Control | Implementation |
|---|---|
| Network segmentation | Three VLANs (OT, MES/DT, IT) with explicit allow-list firewall rules |
| TLS everywhere | All MQTT connections TLS 1.3; all API connections HTTPS only |
| Certificate management | PKI managed by IT/OT team; certificates renewed ≥ 90 days before expiry |
| OT read-only in Phase 1 | No DT or MES action writes back to OT machines in Phase 1 |
| Software updates | Edge node: unattended security updates; application updates in maintenance windows |
| Logging | All MQTT broker connections logged; all FastAPI requests logged (no sensor payload logging in IT logs) |
| Annual pen test | Third-party penetration test annually; critical findings resolved within 30 days |
| Incident response | Defined playbook for: OT network compromise, ransomware, MQTT broker failure, WAN link failure |
| Physical security | Server rack in Z12 key-locked; access restricted to IT/OT team and authorised engineers |

---

## 7. Deployment Runbook Summary

### Dev → Production Promotion Path

```
1. DEV (Rwanda cloud hub — synthetic data)
        ↓  Validated dashboards, tested MQTT namespace
2. STAGING (Edge node — pre-commissioning, synthetic data)
        ↓  Hardware validated, network paths confirmed
3. PRODUCTION (Edge node + Rwanda cloud — live machine data)
        ↓  Phase 1 DT live
4. PHASE 2 EXPANSION (add cobot/AI vision topics, DES layer)
```

### Go-Live Checklist (Phase 1 — SMT Line 1 Pilot)

- [ ] SMT Line 1 OPC-UA and SECS/GEM gateways publishing to edge MQTT broker.
- [ ] Telegraf confirmed writing SMT L1 data to InfluxDB `cce-sag-raw` bucket.
- [ ] MQTT bridge confirmed: SMT L1 topics visible on Rwanda cloud broker within 1 second.
- [ ] Grafana SMT Line 1 Health dashboard live; zone temps updating ≤ 10 seconds.
- [ ] Data latency validated: machine event to Grafana render ≤ 1 second.
- [ ] Alert rules active: reflow zone temp out-of-range, feeder error count spike.
- [ ] Edge fallback tested: WAN link disconnected → edge Grafana confirmed operational.
- [ ] MQTT bridge queue tested: 1-minute WAN blackout → all messages recovered on reconnect.

---

## 8. Version History

| Version | Date | Description | Author |
|---|---|---|---|
| 1.0 | 2025 | Initial infrastructure spec — edge node, cloud hub, OT/IT network architecture | IT/OT Infrastructure Team |

---

*Implementation phases: [`dt-implementation-plan.md`](./dt-implementation-plan.md)*
*Asset manifest (sensor schema): [`dt-asset-manifest.md`](./dt-asset-manifest.md)*
*MQTT topic namespace: [`dt-mqtt-namespace.md`](./dt-mqtt-namespace.md)*
*MES integration protocols: [`mes-integration.md`](./mes-integration.md)*
