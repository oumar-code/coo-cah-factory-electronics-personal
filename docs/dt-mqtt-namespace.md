# Digital Twin — MQTT Topic Namespace

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State
> **Document Version:** 1.0 | **Owner:** Digital Manufacturing & AI Team
> **Status:** CONTROLLED DRAFT — lock required after manifest alignment and before first machine FAT

> **Lock Policy:** This namespace is locked once signed off. Post-lock changes require a formal
> change request reviewed by the Digital Manufacturing Team Lead. All subscribers must be notified
> before any topic rename takes effect. Changing topic names after machines are wired requires
> simultaneous updates to all subscribers, publishers, InfluxDB Telegraf configuration, and
> Grafana datasource queries — the cost is high; the namespace must be right the first time.

> **Phase 0 role:** This document freezes the telemetry contract after the asset manifest is stable
> enough to define canonical zone, asset, instance, and metric identifiers.

**Phase 0 lock preconditions**

- Confirm topic naming against the controlled asset manifest in
  [`dt-asset-manifest.md`](./dt-asset-manifest.md).
- Confirm QoS, retained-message policy, and vendor FAT checklist expectations with the MES team.
- Confirm Telegraf measurement mapping and synthetic publisher design against
  [`dt-infrastructure.md`](./dt-infrastructure.md).
- Lock the namespace before any vendor FAT, gateway build, or production dashboard hard-coding begins.

---

## 1. Canonical Topic Pattern

Every MQTT topic in the Coo-Cah DT Engine follows this structure:

```
cce/sag/{zone_id}/{asset_id}/{metric_id}
```

| Segment | Description | Examples |
|---|---|---|
| `cce` | Factory code — Coo-Cah Electronics | fixed |
| `sag` | Site code — Sagamu | fixed |
| `{zone_id}` | Production zone (lowercase) | `z2`, `z3`, `z4`, `z8`, `amr`, `energy`, `z1`, `z9`, `z10`, `z11` |
| `{asset_id}` | Asset identifier (lowercase, hyphens) | `smt-l1-reflow`, `amr-mir250-07`, `bess-01` |
| `{metric_id}` | Sensor/metric name (lowercase, underscores) | `zone8_temp_c`, `soc_pct`, `fpy_per_board` |

### Multi-Instance Assets

For assets with multiple physical units under a single asset group ID (e.g., 6× flash fixtures),
the instance number is inserted as a sub-segment between `{asset_id}` and `{metric_id}`:

```
cce/sag/{zone_id}/{asset_id}/{instance}/{metric_id}
```

Example: `cce/sag/z4/ph-flash/03/flash_result` — flash fixture instance 03.

---

## 2. Topic Directory by Zone

### 2.1 Zone Z2 — SMT Line 1

| Asset | Asset ID Segment | Metric | Full Topic Example |
|---|---|---|---|
| DEK Screen Printer L1 | `smt-l1-printer` | `paste_volume_pct` | `cce/sag/z2/smt-l1-printer/paste_volume_pct` |
| DEK Screen Printer L1 | `smt-l1-printer` | `stencil_life_cycles` | `cce/sag/z2/smt-l1-printer/stencil_life_cycles` |
| DEK Screen Printer L1 | `smt-l1-printer` | `alarm_active` | `cce/sag/z2/smt-l1-printer/alarm_active` |
| DEK Screen Printer L1 | `smt-l1-printer` | `machine_state` | `cce/sag/z2/smt-l1-printer/machine_state` |
| Koh Young SPI L1 | `smt-l1-spi` | `paste_volume_3d_pct` | `cce/sag/z2/smt-l1-spi/paste_volume_3d_pct` |
| Koh Young SPI L1 | `smt-l1-spi` | `cpk` | `cce/sag/z2/smt-l1-spi/cpk` |
| Koh Young SPI L1 | `smt-l1-spi` | `defect_count_per_board` | `cce/sag/z2/smt-l1-spi/defect_count_per_board` |
| JUKI FX-3R L1 | `smt-l1-pnp-hs` | `cph` | `cce/sag/z2/smt-l1-pnp-hs/cph` |
| JUKI FX-3R L1 | `smt-l1-pnp-hs` | `feeder_error_count` | `cce/sag/z2/smt-l1-pnp-hs/feeder_error_count` |
| JUKI FX-3R L1 | `smt-l1-pnp-hs` | `machine_state` | `cce/sag/z2/smt-l1-pnp-hs/machine_state` |
| JUKI RX-7 L1 | `smt-l1-pnp-fx` | `cph` | `cce/sag/z2/smt-l1-pnp-fx/cph` |
| JUKI RX-7 L1 | `smt-l1-pnp-fx` | `placement_accuracy_um` | `cce/sag/z2/smt-l1-pnp-fx/placement_accuracy_um` |
| Heller Reflow L1 | `smt-l1-reflow` | `zone1_temp_c` | `cce/sag/z2/smt-l1-reflow/zone1_temp_c` |
| Heller Reflow L1 | `smt-l1-reflow` | `zone2_temp_c` | `cce/sag/z2/smt-l1-reflow/zone2_temp_c` |
| Heller Reflow L1 | `smt-l1-reflow` | `zone3_temp_c` | `cce/sag/z2/smt-l1-reflow/zone3_temp_c` |
| Heller Reflow L1 | `smt-l1-reflow` | `zone4_temp_c` | `cce/sag/z2/smt-l1-reflow/zone4_temp_c` |
| Heller Reflow L1 | `smt-l1-reflow` | `zone5_temp_c` | `cce/sag/z2/smt-l1-reflow/zone5_temp_c` |
| Heller Reflow L1 | `smt-l1-reflow` | `zone6_temp_c` | `cce/sag/z2/smt-l1-reflow/zone6_temp_c` |
| Heller Reflow L1 | `smt-l1-reflow` | `zone7_temp_c` | `cce/sag/z2/smt-l1-reflow/zone7_temp_c` |
| Heller Reflow L1 | `smt-l1-reflow` | `zone8_temp_c` | `cce/sag/z2/smt-l1-reflow/zone8_temp_c` |
| Heller Reflow L1 | `smt-l1-reflow` | `conveyor_speed_mm_min` | `cce/sag/z2/smt-l1-reflow/conveyor_speed_mm_min` |
| Heller Reflow L1 | `smt-l1-reflow` | `n2_level_pct` | `cce/sag/z2/smt-l1-reflow/n2_level_pct` |
| Heller Reflow L1 | `smt-l1-reflow` | `alarm_active` | `cce/sag/z2/smt-l1-reflow/alarm_active` |
| Koh Young AOI L1 | `smt-l1-aoi` | `fpy_per_board` | `cce/sag/z2/smt-l1-aoi/fpy_per_board` |
| Koh Young AOI L1 | `smt-l1-aoi` | `defect_code` | `cce/sag/z2/smt-l1-aoi/defect_code` |
| Unicomp X-Ray L1 | `smt-l1-xray` | `bga_void_pct` | `cce/sag/z2/smt-l1-xray/bga_void_pct` |
| Unicomp X-Ray L1 | `smt-l1-xray` | `pass_fail` | `cce/sag/z2/smt-l1-xray/pass_fail` |
| Ersa Selective Solder L1 | `smt-l1-selective` | `flux_level_pct` | `cce/sag/z2/smt-l1-selective/flux_level_pct` |
| Ersa Selective Solder L1 | `smt-l1-selective` | `nozzle_temp_c` | `cce/sag/z2/smt-l1-selective/nozzle_temp_c` |
| Keysight ICT L1 | `smt-l1-ict` | `net_test_pass_fail` | `cce/sag/z2/smt-l1-ict/net_test_pass_fail` |
| Keysight ICT L1 | `smt-l1-ict` | `shorts_count` | `cce/sag/z2/smt-l1-ict/shorts_count` |
| PCB Router L1 | `smt-l1-router` | `spindle_speed_rpm` | `cce/sag/z2/smt-l1-router/spindle_speed_rpm` |
| PCB Router L1 | `smt-l1-router` | `alarm_state` | `cce/sag/z2/smt-l1-router/alarm_state` |

> **Wildcard subscription for all SMT Line 1 topics:** `cce/sag/z2/#`

---

### 2.2 Zone Z3 — SMT Line 2

SMT Line 2 topics mirror Line 1 exactly, with `z3` and `smt-l2` replacing `z2` and `smt-l1`:

| Pattern | Example |
|---|---|
| `cce/sag/z3/smt-l2-{asset}/{metric}` | `cce/sag/z3/smt-l2-reflow/zone7_temp_c` |

> **Wildcard subscription for all SMT Line 2 topics:** `cce/sag/z3/#`

> **Wildcard subscription for all SMT topics (both lines):**
> Use separate subscriptions: `cce/sag/z2/#` and `cce/sag/z3/#`

---

### 2.3 Zone Z4 — Phone Assembly

| Asset | Asset ID Segment | Instance | Metric | Full Topic Example |
|---|---|---|---|---|
| Screen Bonder | `ph-screen-bond` | `01`, `02` | `vacuum_level_mbar` | `cce/sag/z4/ph-screen-bond/01/vacuum_level_mbar` |
| Screen Bonder | `ph-screen-bond` | `01`, `02` | `cycle_time_s` | `cce/sag/z4/ph-screen-bond/02/cycle_time_s` |
| Autoclave | `ph-autoclave` | — | `pressure_bar` | `cce/sag/z4/ph-autoclave/pressure_bar` |
| Autoclave | `ph-autoclave` | — | `temperature_c` | `cce/sag/z4/ph-autoclave/temperature_c` |
| Torque Station | `ph-torque` | `01`–`04` | `torque_nm` | `cce/sag/z4/ph-torque/02/torque_nm` |
| Torque Station | `ph-torque` | `01`–`04` | `result_ok_nok` | `cce/sag/z4/ph-torque/03/result_ok_nok` |
| Flash Station | `ph-flash` | `01`–`06` | `serial_number` | `cce/sag/z4/ph-flash/04/serial_number` |
| Flash Station | `ph-flash` | `01`–`06` | `flash_result` | `cce/sag/z4/ph-flash/04/flash_result` |
| Flash Station | `ph-flash` | `01`–`06` | `firmware_version` | `cce/sag/z4/ph-flash/01/firmware_version` |
| Function Test | `ph-functest` | `01`–`06` | `test_camera_pass` | `cce/sag/z4/ph-functest/05/test_camera_pass` |
| Function Test | `ph-functest` | `01`–`06` | `overall_result` | `cce/sag/z4/ph-functest/05/overall_result` |
| Cognex Vision | `ph-vision` | `01`, `02` | `defect_class` | `cce/sag/z4/ph-vision/01/defect_class` |
| Cognex Vision | `ph-vision` | `01`, `02` | `pass_fail` | `cce/sag/z4/ph-vision/01/pass_fail` |
| Ultrasonic Welder | `ph-ultrasonic` | `01`–`03` | `weld_energy_j` | `cce/sag/z4/ph-ultrasonic/02/weld_energy_j` |
| RF Cal Station | `ph-rf-cal` | `01`–`04` | `cal_result_pass_fail` | `cce/sag/z4/ph-rf-cal/01/cal_result_pass_fail` |
| RF Cal Station | `ph-rf-cal` | `01`–`04` | `offset_applied_db` | `cce/sag/z4/ph-rf-cal/01/offset_applied_db` |

> **Wildcard for all Phone Assembly topics:** `cce/sag/z4/#`

---

### 2.4 Zone Z5 — TWS Earbuds Assembly

| Asset | Asset ID Segment | Instance | Metric | Full Topic Example |
|---|---|---|---|---|
| HATS Acoustic Test | `tws-acoustic` | `01`–`06` | `sensitivity_db` | `cce/sag/z5/tws-acoustic/03/sensitivity_db` |
| HATS Acoustic Test | `tws-acoustic` | `01`–`06` | `thd_pct` | `cce/sag/z5/tws-acoustic/03/thd_pct` |
| HATS Acoustic Test | `tws-acoustic` | `01`–`06` | `pass_fail` | `cce/sag/z5/tws-acoustic/03/pass_fail` |
| R&S CMW500 BT | `tws-bt-tester` | `01`–`04` | `rssi_dbm` | `cce/sag/z5/tws-bt-tester/02/rssi_dbm` |
| R&S CMW500 BT | `tws-bt-tester` | `01`–`04` | `compliance_pass_fail` | `cce/sag/z5/tws-bt-tester/02/compliance_pass_fail` |
| IPX Spray Chamber | `tws-ipx` | `01`, `02` | `spray_pressure_bar` | `cce/sag/z5/tws-ipx/01/spray_pressure_bar` |
| IPX Spray Chamber | `tws-ipx` | `01`, `02` | `test_result` | `cce/sag/z5/tws-ipx/01/test_result` |

> **Wildcard for all TWS Assembly topics:** `cce/sag/z5/#`

---

### 2.5 Zone Z6 — Smartwatch Assembly

| Asset | Asset ID Segment | Instance | Metric | Full Topic |
|---|---|---|---|---|
| Pressure Test Chamber | `sw-pressure` | `01`, `02` | `pressure_bar` | `cce/sag/z6/sw-pressure/01/pressure_bar` |
| Pressure Test Chamber | `sw-pressure` | `01`, `02` | `pass_fail` | `cce/sag/z6/sw-pressure/01/pass_fail` |
| GPS Simulator | `sw-gps-sim` | `01`, `02` | `gnss_lock_time_s` | `cce/sag/z6/sw-gps-sim/01/gnss_lock_time_s` |
| GPS Simulator | `sw-gps-sim` | `01`, `02` | `position_error_m` | `cce/sag/z6/sw-gps-sim/01/position_error_m` |

> **Wildcard for all Smartwatch Assembly topics:** `cce/sag/z6/#`

---

### 2.6 Zone Z7 — Power Bank Assembly

| Asset | Asset ID Segment | Instance | Metric | Full Topic |
|---|---|---|---|---|
| Spot Welder | `pb-spotweld` | `01`–`04` | `pulse_energy_j` | `cce/sag/z7/pb-spotweld/02/pulse_energy_j` |
| Spot Welder | `pb-spotweld` | `01`–`04` | `weld_resistance_mohm` | `cce/sag/z7/pb-spotweld/02/weld_resistance_mohm` |
| Battery Tester | `pb-batt-tester` | `01`–`06` | `capacity_mah` | `cce/sag/z7/pb-batt-tester/04/capacity_mah` |
| Battery Tester | `pb-batt-tester` | `01`–`06` | `ir_mohm` | `cce/sag/z7/pb-batt-tester/04/ir_mohm` |
| Safety Tester | `pb-safety-tester` | `01`–`04` | `hipot_current_ua` | `cce/sag/z7/pb-safety-tester/01/hipot_current_ua` |
| Safety Tester | `pb-safety-tester` | `01`–`04` | `overall_result` | `cce/sag/z7/pb-safety-tester/01/overall_result` |

> **Wildcard for all Power Bank Assembly topics:** `cce/sag/z7/#`

---

### 2.7 Zone Z8 — RF & NCC Test Laboratory

| Asset | Asset ID Segment | Instance | Metric | Full Topic |
|---|---|---|---|---|
| ETS-Lindgren Chamber | `rf-chamber-large` | `01`, `02` | `test_in_progress` | `cce/sag/z8/rf-chamber-large/01/test_in_progress` |
| Benchtop Chamber | `rf-chamber-bench` | `01`, `02` | `frequency_band` | `cce/sag/z8/rf-chamber-bench/01/frequency_band` |
| Benchtop Chamber | `rf-chamber-bench` | `01`, `02` | `test_result` | `cce/sag/z8/rf-chamber-bench/02/test_result` |
| R&S CMW500 NW | `rf-cmw500` | `01`, `02` | `trp_dbm` | `cce/sag/z8/rf-cmw500/01/trp_dbm` |
| R&S CMW500 NW | `rf-cmw500` | `01`, `02` | `tis_dbm` | `cce/sag/z8/rf-cmw500/01/tis_dbm` |
| R&S CMW500 NW | `rf-cmw500` | `01`, `02` | `pass_fail` | `cce/sag/z8/rf-cmw500/01/pass_fail` |
| Keysight Spectrum | `rf-spectrum` | — | `peak_frequency_mhz` | `cce/sag/z8/rf-spectrum/peak_frequency_mhz` |
| Keysight Spectrum | `rf-spectrum` | — | `emission_flag` | `cce/sag/z8/rf-spectrum/emission_flag` |
| CATR OTA | `rf-catr` | — | `trp_dbm` | `cce/sag/z8/rf-catr/trp_dbm` |
| CATR OTA | `rf-catr` | — | `pass_fail` | `cce/sag/z8/rf-catr/pass_fail` |

> **Wildcard for all RF Lab topics:** `cce/sag/z8/#`

---

### 2.8 AMR Fleet — All Zones

AMR topics use the `amr` zone segment rather than a production zone ID, as AMRs roam across
all zones.

```
cce/sag/amr/{amr-type}/{unit-id}/{metric}
```

| Fleet Type | Type Segment | Unit IDs | Metric | Full Topic Example |
|---|---|---|---|---|
| MiR250 Transport | `mir250` | `01`–`12` | `pos_x_m` | `cce/sag/amr/mir250/07/pos_x_m` |
| MiR250 Transport | `mir250` | `01`–`12` | `pos_y_m` | `cce/sag/amr/mir250/07/pos_y_m` |
| MiR250 Transport | `mir250` | `01`–`12` | `pos_theta_deg` | `cce/sag/amr/mir250/07/pos_theta_deg` |
| MiR250 Transport | `mir250` | `01`–`12` | `battery_soc_pct` | `cce/sag/amr/mir250/07/battery_soc_pct` |
| MiR250 Transport | `mir250` | `01`–`12` | `mission_status` | `cce/sag/amr/mir250/07/mission_status` |
| MiR250 Transport | `mir250` | `01`–`12` | `speed_m_s` | `cce/sag/amr/mir250/07/speed_m_s` |
| MiR100 Goods-to-Person | `mir100` | `01`–`04` | `pos_x_m` | `cce/sag/amr/mir100/02/pos_x_m` |
| MiR100 Goods-to-Person | `mir100` | `01`–`04` | `battery_soc_pct` | `cce/sag/amr/mir100/02/battery_soc_pct` |
| MiR100 Goods-to-Person | `mir100` | `01`–`04` | `mission_status` | `cce/sag/amr/mir100/02/mission_status` |
| Charging Dock | `dock` | `01`–`18` | `dock_occupied` | `cce/sag/amr/dock/09/dock_occupied` |
| Charging Dock | `dock` | `01`–`18` | `amr_soc_pct` | `cce/sag/amr/dock/09/amr_soc_pct` |
| Charging Dock | `dock` | `01`–`18` | `charge_current_a` | `cce/sag/amr/dock/09/charge_current_a` |

> **Wildcard for all AMR topics:** `cce/sag/amr/#`
> **Wildcard for all MiR250 positions:** `cce/sag/amr/mir250/+/pos_x_m` (+ single level wildcard)

---

### 2.9 Energy Systems

Energy topics use the `energy` zone segment.

```
cce/sag/energy/{asset-id}/{metric}
```

| Asset | Asset ID Segment | Metric | Full Topic |
|---|---|---|---|
| Solar Roof Main | `pv-roof-main` | `generation_kw` | `cce/sag/energy/pv-roof-main/generation_kw` |
| Solar Roof Main | `pv-roof-main` | `irradiance_w_m2` | `cce/sag/energy/pv-roof-main/irradiance_w_m2` |
| Solar Warehouse | `pv-warehouse` | `generation_kw` | `cce/sag/energy/pv-warehouse/generation_kw` |
| Solar Ground | `pv-ground` | `generation_kw` | `cce/sag/energy/pv-ground/generation_kw` |
| BESS Container 1 | `bess-01` | `soc_pct` | `cce/sag/energy/bess-01/soc_pct` |
| BESS Container 1 | `bess-01` | `soh_pct` | `cce/sag/energy/bess-01/soh_pct` |
| BESS Container 1 | `bess-01` | `charge_discharge_kw` | `cce/sag/energy/bess-01/charge_discharge_kw` |
| BESS Container 1 | `bess-01` | `cell_temp_max_c` | `cce/sag/energy/bess-01/cell_temp_max_c` |
| BESS Container 2 | `bess-02` | `soc_pct` | `cce/sag/energy/bess-02/soc_pct` |
| BESS Container 2 | `bess-02` | `soh_pct` | `cce/sag/energy/bess-02/soh_pct` |
| Inverter 1 | `inv-01` | `ac_output_kw` | `cce/sag/energy/inv-01/ac_output_kw` |
| Inverter 1 | `inv-01` | `efficiency_pct` | `cce/sag/energy/inv-01/efficiency_pct` |
| Inverter 2 | `inv-02` | `ac_output_kw` | `cce/sag/energy/inv-02/ac_output_kw` |
| Inverter 3 | `inv-03` | `ac_output_kw` | `cce/sag/energy/inv-03/ac_output_kw` |
| Inverter 4 | `inv-04` | `ac_output_kw` | `cce/sag/energy/inv-04/ac_output_kw` |
| Generator | `gen-01` | `running_status` | `cce/sag/energy/gen-01/running_status` |
| Generator | `gen-01` | `fuel_level_l` | `cce/sag/energy/gen-01/fuel_level_l` |
| Generator | `gen-01` | `output_kw` | `cce/sag/energy/gen-01/output_kw` |
| Grid Meter | `grid-01` | `import_kw` | `cce/sag/energy/grid-01/import_kw` |
| Grid Meter | `grid-01` | `tou_period` | `cce/sag/energy/grid-01/tou_period` |
| HVAC Chiller 1 | `hvac-01` | `cooling_kw` | `cce/sag/energy/hvac-01/cooling_kw` |
| HVAC Chiller 1 | `hvac-01` | `cop` | `cce/sag/energy/hvac-01/cop` |
| HVAC Chiller 2 | `hvac-02` | `cooling_kw` | `cce/sag/energy/hvac-02/cooling_kw` |

> **Wildcard for all energy topics:** `cce/sag/energy/#`
> **Wildcard for all BESS topics:** `cce/sag/energy/bess-+/#`

---

### 2.10 Supporting Zones — Z1, Z9, Z10, Z11

| Asset | Topic |
|---|---|
| VLM 1–4 (Z1 Stores) | `cce/sag/z1/vlm/{01-04}/pick_count_shift` |
| VLM 1–4 (Z1 Stores) | `cce/sag/z1/vlm/{01-04}/inventory_level_pct` |
| Drop Test (Z9) | `cce/sag/z9/drop-test/pass_fail` |
| Thermal Chamber (Z9) | `cce/sag/z9/thermal-chamber/chamber_temp_c` |
| Battery Cycle Sampling (Z9) | `cce/sag/z9/batt-cycle/capacity_retention_pct` |
| Checkweigher (Z10) | `cce/sag/z10/checkweigh/01/weight_g` |
| Checkweigher (Z10) | `cce/sag/z10/checkweigh/01/pass_fail` |
| Barcode Scanner (Z10) | `cce/sag/z10/barcode-scan/{01-02}/scan_result` |
| Label Printer (Z10) | `cce/sag/z10/label-print/{01-02}/ribbon_level_pct` |
| Temp/Humidity (Z11) | `cce/sag/z11/env-sensor/{01-04}/temperature_c` |
| Temp/Humidity (Z11) | `cce/sag/z11/env-sensor/{01-04}/humidity_pct` |
| Pallet Scanner (Z11) | `cce/sag/z11/pallet-scan/pallet_id` |

---

## 3. System Topics (Non-Asset)

System and control topics that are not mapped to a specific physical asset:

| Topic | Type | Purpose |
|---|---|---|
| `cce/sag/system/oee/factory_blended` | Published by MES | Factory blended OEE (0–1) — updated every minute |
| `cce/sag/system/oee/smt-l1` | Published by MES | SMT Line 1 OEE |
| `cce/sag/system/oee/smt-l2` | Published by MES | SMT Line 2 OEE |
| `cce/sag/system/oee/ph-1` | Published by MES | Phone Assembly Line 1 OEE |
| `cce/sag/system/oee/ph-2` | Published by MES | Phone Assembly Line 2 OEE |
| `cce/sag/system/oee/ph-3` | Published by MES | Phone Assembly Line 3 OEE |
| `cce/sag/system/energy/solar_self_sufficiency_pct` | Published by DT | Calculated KPI: solar ÷ total × 100 |
| `cce/sag/system/energy/total_generation_kw` | Published by DT | Sum of all PV arrays |
| `cce/sag/system/energy/total_consumption_kw` | Published by DT | Factory total consumption |
| `cce/sag/system/alerts/{severity}/{asset_id}` | Published by DT | Alert payloads (severity: `critical`, `warning`, `info`) |
| `cce/sag/system/amr/fleet_summary` | Published by DT | Fleet: active count, avg SoC, missions in progress |

---

## 4. QoS and Retention Policy

### 4.1 QoS Assignments

| Data Category | QoS Level | Rationale |
|---|---|---|
| High-frequency position telemetry (AMR pos, conveyor speed) | QoS 0 | High volume; stale data has no value; drop is acceptable |
| Machine state and alarm flags | QoS 1 | At-least-once delivery; loss of an alarm is not acceptable |
| Quality test results (pass/fail, serial, defect code) | QoS 1 | Regulatory traceability; must not be lost |
| NCC RF test results | QoS 1 | Regulatory requirement; must reach InfluxDB |
| BESS SoC and SoH | QoS 1 | Safety-critical; loss not acceptable |
| System OEE and alert topics | QoS 1 | Operational decisions depend on these |
| Energy generation KPIs | QoS 0 | Calculated metrics; re-derivable from raw data |

### 4.2 Retained Message Policy

| Topic Pattern | Retained | Rationale |
|---|---|---|
| `cce/sag/+/+/machine_state` | Yes | New subscribers immediately see current state |
| `cce/sag/amr/+/+/mission_status` | Yes | AMR position map needs last-known state on connect |
| `cce/sag/energy/bess-+/soc_pct` | Yes | Energy dashboard needs last SoC on page load |
| `cce/sag/system/+` | Yes | OEE and fleet summary retained for dashboard hydration |
| All other production metrics | No | High-frequency; retained message would be stale |

---

## 5. Broker Configuration

### 5.1 Broker Topology

```
                    ┌──────────────────────────────┐
                    │   Rwanda Cloud Hub            │
                    │   Eclipse Mosquitto 2.x       │
                    │   (cloud broker — primary)    │
                    │   TLS 1.3, port 8883          │
                    └──────────┬───────────────────┘
                               │ MQTT Bridge (TLS 1.3)
                    ┌──────────▼───────────────────┐
                    │   Edge Node — Sagamu Factory  │
                    │   Eclipse Mosquitto 2.x       │
                    │   (edge broker — primary OT)  │
                    │   TLS 1.3, port 8883          │
                    │   Local only, port 1883       │
                    └──────────┬───────────────────┘
                               │ MQTT over OT LAN
              ┌────────────────┼──────────────────┐
              │                │                  │
     Machine MQTT         MiR Fleet          Sensor Adapters
     Adapters (OPC-UA      MQTT Bridge        (energy, env)
     → MQTT gateways)
```

- **Edge broker** handles all machine-side publishing. It bridges all topics matching
  `cce/sag/#` to the Rwanda cloud broker.
- **Cloud broker** is the single authoritative source for Grafana and the FastAPI backend.
- If the WAN link drops, the edge broker buffers messages locally (Mosquitto persistence enabled).
  On reconnect, buffered messages bridge to the cloud broker. Maximum bridge queue: 500,000 messages.

### 5.2 Authentication & Authorisation

| Client Type | Auth Method | ACL |
|---|---|---|
| Machine adapters (OPC-UA gateway, MiR bridge) | TLS client certificate | Publish to `cce/sag/{zone}/#` only; no subscribe |
| DT edge node services (Telegraf, FastAPI) | Username + password; TLS | Subscribe `cce/sag/#`; publish `cce/sag/system/#` |
| Grafana dashboards | Username + password | Subscribe `cce/sag/#` read-only |
| MES server | TLS client certificate | Subscribe `cce/sag/#`; publish `cce/sag/system/oee/#` |
| Cloud broker bridge | Mutual TLS | Full `cce/sag/#` bridge |

### 5.3 Broker Sizing

| Parameter | Edge Broker | Cloud Broker |
|---|---|---|
| Expected message rate (peak) | ~3,500 msg/sec | ~3,500 msg/sec |
| Concurrent clients | ~60 | ~30 |
| Persistence (QoS 1 queue) | 500,000 messages, 2 GB | 100,000 messages |
| Log retention | 7 days | 30 days |

> **Estimated peak rate derivation:** ~2,800 sensor data points at an average update rate of
> 1.25 messages/second = ~3,500 messages/second. This is comfortably within Mosquitto's
> sustained throughput of >1 million messages/second on the specified hardware.

---

## 6. Topic Governance

### 6.1 Naming Rules (Enforced)

1. All segments lowercase.
2. Hyphens (`-`) for compound asset names; underscores (`_`) for metric names.
3. Zone segments are always the two-character zone code (`z2`, `z4`, etc.) or a functional
   zone (`amr`, `energy`).
4. Instance numbers are always zero-padded to two digits (`01`, `02`, not `1`, `2`).
5. No spaces, no special characters other than `-` and `_`.
6. Metric names must match the `id` field in the asset manifest exactly.

### 6.2 Change Request Process

Any proposed topic change after namespace lock must follow this process:

1. Raise a change request in the project issue tracker with: topic(s) affected, reason for
   change, list of all publishers and subscribers affected.
2. Change reviewed and approved by Digital Manufacturing Team Lead and MES Team Lead.
3. Approved change: all publishers and subscribers updated simultaneously in a maintenance window.
4. Update this document and the asset manifest in the same commit; increment version number.

---

## 7. Version History

| Version | Date | Description | Author |
|---|---|---|---|
| 1.0 | 2025 | Initial namespace definition — all zones, Phase 1 assets | Digital Manufacturing Team |

---

*Asset manifest: [`dt-asset-manifest.md`](./dt-asset-manifest.md)*
*Implementation plan: [`dt-implementation-plan.md`](./dt-implementation-plan.md)*
*Infrastructure & broker deployment: [`dt-infrastructure.md`](./dt-infrastructure.md)*
