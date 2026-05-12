# Sensor Registry — MES Vendor Export Schema Template

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1
> **Document Version:** 1.0 | **Owner:** Digital Manufacturing & AI Team Lead
> **Purpose:** Schema specification and sample template for the MES vendor sensor inventory export
> **Sent to:** MES Vendor / Configuration Team — request date: **2026-05-12**
> **Required by:** 2026-06-15 (Gate 3 sensor coverage acceptance — see `sensor-map.md` §14)

This document is the formal schema specification for the MES vendor sensor inventory export
required to complete `docs/sensor-map.md` (Pass 8 of the gap-closure programme).  The vendor
must return one row per data point — approximately **2,800 rows total** across 12 zones —
using the column definitions in Section 1.  Sections 2 through 4 provide example rows,
validation rules, and the delivery checklist.

---

## 1. Required Export Schema

The export must be delivered as either a **UTF-8 CSV file** or a **Markdown table** matching
the column order below exactly.  Do not merge or reorder columns.

| Column # | Column Header              | Data Type    | Required | Description |
|----------|---------------------------|-------------|----------|-------------|
| 1  | `sensor_id`                       | String       | ✅       | Unique sensor identifier as used in the MES configuration.  Must match the existing IDs in `sensor-map.md` where rows already exist, or follow the naming convention described in §1.1 for new rows. |
| 2  | `asset_id`                        | String       | ✅       | DT asset identifier — must match an asset ID in `dt-asset-manifest.md` (e.g. `DT-SMT-L1-01`). |
| 3  | `zone`                            | String       | ✅       | Zone identifier: one of Z1–Z11 or `Site`. |
| 4  | `description`                     | String       | ✅       | Human-readable description of the measured parameter (e.g. `Squeegee pressure (N)`). |
| 5  | `sensor_model`                    | String       | ⚠️ if known | Manufacturer and model of the physical sensor or source (e.g. `Sensirion SHT31`).  Use `MES internal` for software-derived values, `SECS/GEM internal` for protocol-native counters. |
| 6  | `protocol`                        | String       | ✅       | Integration protocol: one of `SECS/GEM`, `OPC-UA`, `Modbus TCP`, `REST API`, `Ethernet API`, `VISA/LAN`, `LAN API`, `MQTT`, `dry-contact`. |
| 7  | `data_type`                       | String       | ✅       | Value data type: one of `float`, `int`, `bool`, `string`, `array`. |
| 8  | `unit`                            | String       | ⚠️ if applicable | Engineering unit (e.g. `°C`, `kW`, `mbar`, `Nm`).  Use `—` for dimensionless or boolean values. |
| 9  | `cal_interval`                    | String       | ✅       | Calibration interval code from `sensor-map.md` §2: one of `CAL-A` through `CAL-H`, or `CAL-N` (not applicable). |
| 10 | `influxdb_bucket`                 | String       | ✅       | Target InfluxDB bucket name (e.g. `factory-smt`, `factory-energy`). |
| 11 | `influxdb_measurement`            | String       | ✅       | InfluxDB measurement name (e.g. `screen_printer`, `reflow_oven`). |
| 12 | `influxdb_field_key`              | String       | ✅       | InfluxDB field key (snake_case, e.g. `squeegee_pressure_n`). |
| 13 | `mqtt_topic_or_opcua_node`        | String       | ✅       | MQTT topic path **or** OPC-UA node ID, as applicable.  For SECS/GEM sources, use the SECS message reference (e.g. `SECS/GEM S6F11`).  For REST/Ethernet API sources, use the endpoint path (e.g. `/api/v1/sensor/result`). |
| 14 | `telegraf_plugin`                 | String       | ⚠️ if known | Telegraf input plugin to use (e.g. `modbus`, `mqtt_consumer`, `opcua`, `http`).  Leave blank if unknown; DT team will determine. |
| 15 | `notes`                           | String       | —        | Any supplementary information (firmware dependency, polling interval override, known limitations). |

### 1.1 Sensor ID Naming Convention

Sensor IDs must follow the pattern already established in `sensor-map.md`:

```
<ZONE-ASSET>-<PARAMETER>
```

Examples:
- `SMT-L1-01-SQUEEGEE_PRESS` — SMT Line 1, DEK Screen Printer, squeegee pressure
- `PH-03-2-TORQUE_NM` — Phone Assembly, Torque Station unit 2, torque value
- `EN-PV-1-GEN_KW` — Energy, PV Array 1, generation power

Where an asset has multiple identical units (e.g. ×6 flash stations), the unit index `n` is
appended as a numeric suffix on the asset segment: `PH-04-1-FLASH_RESULT`, `PH-04-2-FLASH_RESULT`, etc.

---

## 2. Example Rows

The following sample rows illustrate the required format for each major protocol type.
The vendor export must replicate this structure for all ~2,800 data points.

### 2.1 SECS/GEM source (SMT)

| sensor_id | asset_id | zone | description | sensor_model | protocol | data_type | unit | cal_interval | influxdb_bucket | influxdb_measurement | influxdb_field_key | mqtt_topic_or_opcua_node | telegraf_plugin | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `SMT-L1-01-SQUEEGEE_PRESS` | `DT-SMT-L1-01` | Z2 | Squeegee pressure (N) | Built-in load cell | SECS/GEM | float | N | CAL-C | factory-smt | screen_printer | squeegee_pressure_n | SECS/GEM S6F11 | secs | — |
| `SMT-L1-01-MACHINE_STATE` | `DT-SMT-L1-01` | Z2 | Machine state (RUN/IDLE/ALARM/SETUP) | SECS/GEM EQST | SECS/GEM | string | — | CAL-N | factory-smt | screen_printer | machine_state | SECS/GEM EQST | secs | — |

### 2.2 Modbus TCP source (Energy)

| sensor_id | asset_id | zone | description | sensor_model | protocol | data_type | unit | cal_interval | influxdb_bucket | influxdb_measurement | influxdb_field_key | mqtt_topic_or_opcua_node | telegraf_plugin | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `EN-PV-1-GEN_KW` | `DT-EN-PV-01` | Site | Real-time PV generation (kW) | Sungrow SH250HX inverter | Modbus TCP | float | kW | CAL-H | factory-energy | solar_pv | gen_kw | holding_register:40083 | modbus | Sungrow Modbus register map v3.2 |
| `EN-BESS-1-SOC_PCT` | `DT-EN-BESS-01` | Site | BESS State of Charge (%) | BMS internal | Modbus TCP | float | % | CAL-H | factory-energy | bess | soc_pct | holding_register:30101 | modbus | — |

### 2.3 OPC-UA source (Assembly)

| sensor_id | asset_id | zone | description | sensor_model | protocol | data_type | unit | cal_interval | influxdb_bucket | influxdb_measurement | influxdb_field_key | mqtt_topic_or_opcua_node | telegraf_plugin | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `PH-01-1-VAC_LEVEL_MBAR` | `DT-PH-01` | Z4 | Vacuum level unit 1 (mbar) | Pirani vacuum sensor | OPC-UA | float | mbar | CAL-C | factory-assembly | screen_bonding | vac_level_mbar | ns=2;s=ScreenBonder1.VacuumLevel | opcua | — |
| `PH-02-TEMP_C` | `DT-PH-02` | Z4 | Autoclave chamber temperature (°C) | PT100 | OPC-UA | float | °C | CAL-E | factory-assembly | autoclave | chamber_temp_c | ns=2;s=Autoclave1.ChamberTemp | opcua | — |

### 2.4 REST API source (QC / Vision)

| sensor_id | asset_id | zone | description | sensor_model | protocol | data_type | unit | cal_interval | influxdb_bucket | influxdb_measurement | influxdb_field_key | mqtt_topic_or_opcua_node | telegraf_plugin | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `SMT-L1-06-FPY` | `DT-SMT-L1-06` | Z2 | AOI first pass yield per board (%) | Koh Young Zenith REST API | REST API | float | % | CAL-G | factory-smt | aoi | first_pass_yield_pct | /api/v1/board/result | http | Polled per board; 200 ms max latency |
| `PH-04-1-FLASH_RESULT` | `DT-PH-04` | Z4 | Flash result unit 1 (OK/NOK) | Flash station REST API | REST API | bool | — | CAL-N | factory-assembly | phone_flash | flash_result | /api/v1/flash/result | http | — |

### 2.5 MQTT source (AMR fleet)

| sensor_id | asset_id | zone | description | sensor_model | protocol | data_type | unit | cal_interval | influxdb_bucket | influxdb_measurement | influxdb_field_key | mqtt_topic_or_opcua_node | telegraf_plugin | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `WH-AMR-01-BATTERY_PCT` | `DT-AMR-MIR250-01` | Z11 | AMR battery SoC (%) | MiR Fleet MQTT | MQTT | float | % | CAL-N | factory-warehouse | amr_fleet | battery_pct | mir/robot/1/status/battery | mqtt_consumer | MiR250 fleet broker topic |

---

## 3. Validation Rules

The Digital Manufacturing team will validate the vendor export against the following rules
before importing into `sensor-map.md`:

| Rule | Description |
|------|-------------|
| **V1 — Row count** | Total rows must equal the zone subtotals in `sensor-map.md` §1: Z1=80, Z2=420, Z3=420, Z4=280, Z5=200, Z6=160, Z7=200, Z8=260, Z9=180, Z10=120, Z11=80, Site=400. Grand total = 2,800. |
| **V2 — Asset ID validity** | Every `asset_id` value must exist in `dt-asset-manifest.md`.  Unrecognised asset IDs will be rejected. |
| **V3 — Zone consistency** | The `zone` column must match the zone recorded in `dt-asset-manifest.md` for the given `asset_id`. |
| **V4 — Protocol validity** | `protocol` must be one of the permitted values listed in §1. |
| **V5 — Cal interval validity** | `cal_interval` must be one of `CAL-A` through `CAL-H` or `CAL-N`. |
| **V6 — InfluxDB key format** | `influxdb_field_key` must be `snake_case` (lowercase letters, digits, underscores; no spaces or hyphens). |
| **V7 — Sensor ID uniqueness** | Every `sensor_id` must be unique across the entire file. |
| **V8 — Required fields** | Columns 1–3, 6–9, 10–13 must not be empty. |
| **V9 — Cross-reference consistency** | Sensor IDs already present in `sensor-map.md` must match; any change in existing IDs requires a documented change request. |
| **V10 — Duplicate check** | No two rows may have the same (`asset_id`, `mqtt_topic_or_opcua_node`) combination. |

---

## 4. Delivery Checklist

Before returning the export to the Digital Manufacturing team:

- [ ] All ~2,800 rows present with no missing assets
- [ ] Zone subtotals verified (V1)
- [ ] All asset IDs cross-checked against the asset list provided in Attachment A
- [ ] Validation rules V2–V10 self-checked by vendor
- [ ] File delivered as UTF-8 CSV **or** as a Markdown table in this document's format
- [ ] File named `sensor-export-coo-cah-factory-<date>.csv` (e.g. `sensor-export-coo-cah-factory-2026-06-15.csv`)
- [ ] Signed-off by MES Configuration Lead before delivery

---

## 5. Delivery and Contacts

| Item | Detail |
|------|--------|
| Requested by | Digital Manufacturing & AI Team Lead |
| Request date | 2026-05-12 |
| Required by | **2026-06-15** |
| Deliver to | Digital Manufacturing & AI Team Lead + Documentation Integration Reviewer |
| Delivery method | Encrypted email attachment or secure project file share |
| Questions | Contact Digital Manufacturing & AI Team Lead (cc: MES Team Lead) |

---

## Related Documents

- Canonical sensor registry (target document): [`sensor-map.md`](./sensor-map.md)
- DT asset identifiers: [`dt-asset-manifest.md`](./dt-asset-manifest.md)
- MQTT topic namespace: [`dt-mqtt-namespace.md`](./dt-mqtt-namespace.md)
- Gap closure tracking: [`gap-closure-report.md`](./gap-closure-report.md)
