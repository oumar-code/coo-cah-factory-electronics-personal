# Digital Twin — Asset Data Manifest

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State
> **Document Version:** 1.0 | **Owner:** Digital Manufacturing & AI Team
> **Status:** CONTROLLED DRAFT — Phase 0 anchor deliverable; requires co-sign by MES Team Lead before locking

This manifest is the **contractual data schema** between the MES team and the Digital Twin team.
Every one of the 142 registered physical assets in the factory has a formally defined entry here:
Asset ID, zone, protocol, sensor list, data types, units, update frequency, and expected operating
ranges.

> **Lock Policy:** Once signed off and locked (see Version History), changes require a formal change
> request reviewed by both the Digital Manufacturing Team Lead and MES Team Lead. Any change must be
> applied simultaneously in InfluxDB, Grafana, and the MQTT topic namespace.

> **Phase 0 role:** This is the anchor deliverable for Phase 0. The MQTT namespace, InfluxDB bucket
> and measurement design, Telegraf topic mapping, Grafana dashboard structure, and synthetic data
> generators must all trace back to this manifest.

**Phase 0 control requirements**

- Complete asset coverage for all 142 registered asset IDs from [`digital-twin.md`](./digital-twin.md).
- Confirm primary protocol, update frequency, and expected operating range for every required metric.
- Co-sign with the MES Team Lead before changing document status from controlled draft to locked.
- Publish the approved version to the group MES integration standards path in Coo-Kah-Doks.
- Confirm alignment with [`dt-mqtt-namespace.md`](./dt-mqtt-namespace.md) and
  [`dt-infrastructure.md`](./dt-infrastructure.md) before lock.

---

## 1. Manifest Schema Reference

Each asset entry in Section 2 follows this schema:

```yaml
asset_id:          # Unique DT asset identifier (matches digital-twin.md asset registry)
name:              # Human-readable asset name
zone:              # Factory zone ID (Z1–Z12 or "site")
location:          # Descriptive sub-location
qty:               # Number of identical physical units under this asset ID group
protocol:          # Primary integration protocol
update_frequency_s: # Nominal data update interval in seconds
dt_phase:          # Phase in which this asset is first integrated (1, 2, or 3)
sensors:
  - id:            # Short metric identifier (used in MQTT topic and InfluxDB field key)
    name:          # Human-readable sensor/metric name
    data_type:     # float | int | string | bool
    unit:          # SI unit or descriptive unit; null if dimensionless
    expected_range: # [min, max] for numeric; null for string/bool; used for anomaly detection
```

---

## 2. Asset Manifest (YAML)

### 2.1 SMT & PCB Processing — Zone Z2 (SMT Line 1)

```yaml
- asset_id: DT-SMT-L1-01
  name: DEK Horizon Screen Printer (Line 1)
  zone: Z2
  location: SMT Line 1 — Station 1
  qty: 1
  protocol: SECS/GEM
  update_frequency_s: 5
  dt_phase: 1
  sensors:
    - id: print_recipe
      name: Active Print Recipe Name
      data_type: string
      unit: null
      expected_range: null
    - id: paste_volume_pct
      name: Paste Volume (% of nominal)
      data_type: float
      unit: "%"
      expected_range: [85.0, 115.0]
    - id: stencil_life_cycles
      name: Stencil Life Remaining (cycles)
      data_type: int
      unit: cycles
      expected_range: [0, 50000]
    - id: alarm_active
      name: Alarm Active
      data_type: bool
      unit: null
      expected_range: null
    - id: machine_state
      name: Machine State (RUN/IDLE/ALARM/SETUP)
      data_type: string
      unit: null
      expected_range: null

- asset_id: DT-SMT-L1-02
  name: Koh Young KY8030-3 SPI (Line 1)
  zone: Z2
  location: SMT Line 1 — Station 2
  qty: 1
  protocol: SECS/GEM
  update_frequency_s: 5
  dt_phase: 1
  sensors:
    - id: paste_volume_3d_pct
      name: 3D Paste Volume (% of nominal)
      data_type: float
      unit: "%"
      expected_range: [80.0, 120.0]
    - id: cpk
      name: Process Capability Index (Cpk)
      data_type: float
      unit: null
      expected_range: [1.0, 3.0]
    - id: defect_count_per_board
      name: Defect Count per Board
      data_type: int
      unit: count
      expected_range: [0, 50]
    - id: board_id
      name: Board Panel ID (last inspected)
      data_type: string
      unit: null
      expected_range: null
    - id: pads_inspected
      name: Pads Inspected (last board)
      data_type: int
      unit: count
      expected_range: [100, 5000]

- asset_id: DT-SMT-L1-03
  name: JUKI FX-3R Pick-and-Place (Line 1)
  zone: Z2
  location: SMT Line 1 — Station 3
  qty: 1
  protocol: SECS/GEM
  update_frequency_s: 5
  dt_phase: 1
  sensors:
    - id: cph
      name: Components Per Hour (actual)
      data_type: int
      unit: cph
      expected_range: [10000, 45000]
    - id: feeder_error_count
      name: Feeder Error Count (current shift)
      data_type: int
      unit: count
      expected_range: [0, 50]
    - id: nozzle_state
      name: Active Nozzle State
      data_type: string
      unit: null
      expected_range: null
    - id: placement_count_shift
      name: Total Placements (current shift)
      data_type: int
      unit: count
      expected_range: [0, 500000]
    - id: machine_state
      name: Machine State
      data_type: string
      unit: null
      expected_range: null

- asset_id: DT-SMT-L1-04
  name: JUKI RX-7 Pick-and-Place (Line 1)
  zone: Z2
  location: SMT Line 1 — Station 4
  qty: 1
  protocol: SECS/GEM
  update_frequency_s: 5
  dt_phase: 1
  sensors:
    - id: cph
      name: Components Per Hour (actual)
      data_type: int
      unit: cph
      expected_range: [5000, 20000]
    - id: feeder_error_count
      name: Feeder Error Count (current shift)
      data_type: int
      unit: count
      expected_range: [0, 30]
    - id: placement_accuracy_um
      name: Placement Accuracy Trend (µm sigma)
      data_type: float
      unit: µm
      expected_range: [0.0, 50.0]
    - id: machine_state
      name: Machine State
      data_type: string
      unit: null
      expected_range: null

- asset_id: DT-SMT-L1-05
  name: Heller 1964 MK5 Reflow Oven (Line 1)
  zone: Z2
  location: SMT Line 1 — Station 5
  qty: 1
  protocol: OPC-UA
  update_frequency_s: 10
  dt_phase: 1
  sensors:
    - id: zone1_temp_c
      name: Zone 1 Temperature (°C)
      data_type: float
      unit: "°C"
      expected_range: [100.0, 320.0]
    - id: zone2_temp_c
      name: Zone 2 Temperature (°C)
      data_type: float
      unit: "°C"
      expected_range: [100.0, 320.0]
    - id: zone3_temp_c
      name: Zone 3 Temperature (°C)
      data_type: float
      unit: "°C"
      expected_range: [130.0, 320.0]
    - id: zone4_temp_c
      name: Zone 4 Temperature (°C)
      data_type: float
      unit: "°C"
      expected_range: [150.0, 320.0]
    - id: zone5_temp_c
      name: Zone 5 Temperature (°C)
      data_type: float
      unit: "°C"
      expected_range: [170.0, 320.0]
    - id: zone6_temp_c
      name: Zone 6 Temperature (°C)
      data_type: float
      unit: "°C"
      expected_range: [200.0, 320.0]
    - id: zone7_temp_c
      name: Zone 7 Temperature — Peak Zone (°C)
      data_type: float
      unit: "°C"
      expected_range: [230.0, 260.0]
    - id: zone8_temp_c
      name: Zone 8 Temperature — Cooling (°C)
      data_type: float
      unit: "°C"
      expected_range: [50.0, 200.0]
    - id: conveyor_speed_mm_min
      name: Conveyor Speed (mm/min)
      data_type: float
      unit: mm/min
      expected_range: [600.0, 1200.0]
    - id: n2_level_pct
      name: Nitrogen Level (% — optional atmosphere)
      data_type: float
      unit: "%"
      expected_range: [0.0, 100.0]
    - id: alarm_active
      name: Alarm Active
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-SMT-L1-06
  name: Koh Young Zenith AOI (Line 1)
  zone: Z2
  location: SMT Line 1 — Station 6
  qty: 1
  protocol: SECS/GEM
  update_frequency_s: 5
  dt_phase: 1
  sensors:
    - id: defect_code
      name: Last Defect Code
      data_type: string
      unit: null
      expected_range: null
    - id: fpy_per_board
      name: First-Pass Yield (last board — pass/fail)
      data_type: bool
      unit: null
      expected_range: null
    - id: defect_count_per_board
      name: Defect Count (last board)
      data_type: int
      unit: count
      expected_range: [0, 200]
    - id: image_ref
      name: Image Reference (last board)
      data_type: string
      unit: null
      expected_range: null
    - id: alarm_active
      name: Alarm Active
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-SMT-L1-07
  name: Unicomp AX8200 X-Ray Inspection (Line 1)
  zone: Z2
  location: SMT Line 1 — Station 7
  qty: 1
  protocol: Ethernet API
  update_frequency_s: 30
  dt_phase: 1
  sensors:
    - id: bga_void_pct
      name: BGA Void Analysis (% void — last board)
      data_type: float
      unit: "%"
      expected_range: [0.0, 25.0]
    - id: image_ref
      name: Image Reference (last board)
      data_type: string
      unit: null
      expected_range: null
    - id: pass_fail
      name: Pass / Fail (last board)
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-SMT-L1-08
  name: Ersa Versaflow Selective Solder (Line 1)
  zone: Z2
  location: SMT Line 1 — Station 8
  qty: 1
  protocol: OPC-UA
  update_frequency_s: 10
  dt_phase: 1
  sensors:
    - id: flux_level_pct
      name: Flux Level (% remaining)
      data_type: float
      unit: "%"
      expected_range: [10.0, 100.0]
    - id: solder_level_pct
      name: Solder Level (% remaining)
      data_type: float
      unit: "%"
      expected_range: [10.0, 100.0]
    - id: nozzle_temp_c
      name: Nozzle Temperature (°C)
      data_type: float
      unit: "°C"
      expected_range: [280.0, 380.0]
    - id: recipe_name
      name: Active Recipe Name
      data_type: string
      unit: null
      expected_range: null

- asset_id: DT-SMT-L1-09
  name: Keysight I1000D ICT (Line 1)
  zone: Z2
  location: SMT Line 1 — Station 9
  qty: 1
  protocol: Ethernet API
  update_frequency_s: 15
  dt_phase: 1
  sensors:
    - id: net_test_pass_fail
      name: Net Test Pass / Fail (last board)
      data_type: bool
      unit: null
      expected_range: null
    - id: shorts_count
      name: Shorts Detected (last board)
      data_type: int
      unit: count
      expected_range: [0, 20]
    - id: opens_count
      name: Opens Detected (last board)
      data_type: int
      unit: count
      expected_range: [0, 20]
    - id: fixture_id
      name: Test Fixture ID in Use
      data_type: string
      unit: null
      expected_range: null

- asset_id: DT-SMT-L1-10
  name: PCB Depanelling Router (Line 1)
  zone: Z2
  location: SMT Line 1 — Station 10
  qty: 1
  protocol: OPC-UA
  update_frequency_s: 15
  dt_phase: 1
  sensors:
    - id: cycle_count_shift
      name: Cycle Count (current shift)
      data_type: int
      unit: count
      expected_range: [0, 5000]
    - id: spindle_speed_rpm
      name: Spindle Speed (RPM)
      data_type: int
      unit: RPM
      expected_range: [10000, 60000]
    - id: alarm_state
      name: Alarm State
      data_type: bool
      unit: null
      expected_range: null
```

### 2.2 SMT & PCB Processing — Zone Z3 (SMT Line 2)

```yaml
# SMT Line 2 assets (DT-SMT-L2-01 to DT-SMT-L2-10) mirror the exact sensor schema
# of SMT Line 1 assets DT-SMT-L1-01 to DT-SMT-L1-10.
# The only differences are asset_id, location, and zone (Z3 instead of Z2).
#
# Summary entries — full sensor lists identical to Line 1 counterparts:

- asset_id: DT-SMT-L2-01
  name: DEK Horizon Screen Printer (Line 2)
  zone: Z3
  location: SMT Line 2 — Station 1
  qty: 1
  protocol: SECS/GEM
  update_frequency_s: 5
  dt_phase: 1
  sensors: # identical to DT-SMT-L1-01 sensor list

- asset_id: DT-SMT-L2-02
  name: Koh Young KY8030-3 SPI (Line 2)
  zone: Z3
  location: SMT Line 2 — Station 2
  qty: 1
  protocol: SECS/GEM
  update_frequency_s: 5
  dt_phase: 1
  sensors: # identical to DT-SMT-L1-02 sensor list

- asset_id: DT-SMT-L2-03
  name: JUKI FX-3R Pick-and-Place (Line 2)
  zone: Z3
  location: SMT Line 2 — Station 3
  qty: 1
  protocol: SECS/GEM
  update_frequency_s: 5
  dt_phase: 1
  sensors: # identical to DT-SMT-L1-03 sensor list

- asset_id: DT-SMT-L2-04
  name: JUKI RX-7 Pick-and-Place (Line 2)
  zone: Z3
  location: SMT Line 2 — Station 4
  qty: 1
  protocol: SECS/GEM
  update_frequency_s: 5
  dt_phase: 1
  sensors: # identical to DT-SMT-L1-04 sensor list

- asset_id: DT-SMT-L2-05
  name: Heller 1964 MK5 Reflow Oven (Line 2)
  zone: Z3
  location: SMT Line 2 — Station 5
  qty: 1
  protocol: OPC-UA
  update_frequency_s: 10
  dt_phase: 1
  sensors: # identical to DT-SMT-L1-05 sensor list (8 zone temps + conveyor + N2 + alarm)

- asset_id: DT-SMT-L2-06
  name: Koh Young Zenith AOI (Line 2)
  zone: Z3
  location: SMT Line 2 — Station 6
  qty: 1
  protocol: SECS/GEM
  update_frequency_s: 5
  dt_phase: 1
  sensors: # identical to DT-SMT-L1-06 sensor list

- asset_id: DT-SMT-L2-07
  name: UV Curing Oven — Dymax BlueWave 75 (Line 2)
  zone: Z3
  location: SMT Line 2 — Station 7
  qty: 1
  protocol: Modbus TCP
  update_frequency_s: 15
  dt_phase: 1
  sensors:
    - id: uv_intensity_mw_cm2
      name: UV Intensity (mW/cm²)
      data_type: float
      unit: mW/cm²
      expected_range: [50.0, 500.0]
    - id: conveyor_speed_mm_min
      name: Conveyor Speed (mm/min)
      data_type: float
      unit: mm/min
      expected_range: [100.0, 800.0]
    - id: lamp_hours
      name: Lamp Hours (cumulative)
      data_type: int
      unit: hours
      expected_range: [0, 2000]
    - id: alarm_active
      name: Alarm Active
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-SMT-L2-08
  name: Ersa Versaflow Selective Solder (Line 2)
  zone: Z3
  location: SMT Line 2 — Station 8
  qty: 1
  protocol: OPC-UA
  update_frequency_s: 10
  dt_phase: 1
  sensors: # identical to DT-SMT-L1-08 sensor list

- asset_id: DT-SMT-L2-09
  name: Takaya APT-1400F Flying Probe Tester (Line 2)
  zone: Z3
  location: SMT Line 2 — Station 9
  qty: 1
  protocol: Ethernet API
  update_frequency_s: 30
  dt_phase: 1
  sensors:
    - id: test_result
      name: Test Result (last board — PASS/FAIL)
      data_type: bool
      unit: null
      expected_range: null
    - id: fault_code
      name: Fault Code (last failure, if any)
      data_type: string
      unit: null
      expected_range: null
    - id: test_duration_s
      name: Test Duration (seconds — last board)
      data_type: float
      unit: s
      expected_range: [5.0, 180.0]

- asset_id: DT-SMT-L2-10
  name: PCB Depanelling Router (Line 2)
  zone: Z3
  location: SMT Line 2 — Station 10
  qty: 1
  protocol: OPC-UA
  update_frequency_s: 15
  dt_phase: 1
  sensors: # identical to DT-SMT-L1-10 sensor list
```

### 2.3 Phone Assembly — Zone Z4

```yaml
- asset_id: DT-PH-01
  name: Screen Bonding Machine — Goman GM-90A
  zone: Z4
  location: Phone Assembly — Screen Bond Station
  qty: 2
  protocol: Ethernet API
  update_frequency_s: 10
  dt_phase: 1
  sensors:
    - id: vacuum_level_mbar
      name: Vacuum Level (mbar)
      data_type: float
      unit: mbar
      expected_range: [-900.0, -600.0]
    - id: oca_press_force_n
      name: OCA Press Force (N)
      data_type: float
      unit: N
      expected_range: [50.0, 500.0]
    - id: cycle_time_s
      name: Cycle Time (seconds)
      data_type: float
      unit: s
      expected_range: [15.0, 60.0]
    - id: alarm_active
      name: Alarm Active
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-PH-02
  name: Autoclave / OCA Debubble — Goman GDA-A60
  zone: Z4
  location: Phone Assembly — Debubble Station
  qty: 1
  protocol: Modbus TCP
  update_frequency_s: 30
  dt_phase: 1
  sensors:
    - id: pressure_bar
      name: Chamber Pressure (bar)
      data_type: float
      unit: bar
      expected_range: [0.0, 7.0]
    - id: temperature_c
      name: Chamber Temperature (°C)
      data_type: float
      unit: "°C"
      expected_range: [20.0, 100.0]
    - id: cycle_timer_s
      name: Cycle Timer Remaining (seconds)
      data_type: int
      unit: s
      expected_range: [0, 3600]
    - id: alarm_active
      name: Alarm Active
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-PH-03
  name: Atlas Copco QMX4 Torque Station
  zone: Z4
  location: Phone Assembly — Torque Stations (×4 across PH-1/2/3)
  qty: 4
  protocol: OPC-UA
  update_frequency_s: 1
  dt_phase: 1
  sensors:
    - id: torque_nm
      name: Torque Value (Nm — last tightening)
      data_type: float
      unit: Nm
      expected_range: [0.1, 2.5]
    - id: angle_deg
      name: Angle (degrees — last tightening)
      data_type: float
      unit: degrees
      expected_range: [0.0, 720.0]
    - id: result_ok_nok
      name: Tightening Result (OK/NOK)
      data_type: bool
      unit: null
      expected_range: null
    - id: sequence_step
      name: Tightening Sequence Step
      data_type: int
      unit: null
      expected_range: [1, 20]

- asset_id: DT-PH-04
  name: Phone Flash Station (6-up Android Flash Fixture)
  zone: Z4
  location: Phone Assembly — Flash Stations (×6)
  qty: 6
  protocol: REST API
  update_frequency_s: 5
  dt_phase: 1
  sensors:
    - id: serial_number
      name: Serial Number (unit under flash)
      data_type: string
      unit: null
      expected_range: null
    - id: firmware_version
      name: Firmware Version Flashed
      data_type: string
      unit: null
      expected_range: null
    - id: flash_result
      name: Flash Result (PASS/FAIL)
      data_type: bool
      unit: null
      expected_range: null
    - id: flash_duration_s
      name: Flash Duration (seconds)
      data_type: float
      unit: s
      expected_range: [15.0, 180.0]

- asset_id: DT-PH-05
  name: Phone Function Test Fixture
  zone: Z4
  location: Phone Assembly — Function Test Stations (×6)
  qty: 6
  protocol: REST API
  update_frequency_s: 5
  dt_phase: 1
  sensors:
    - id: test_camera_pass
      name: Camera Test — Pass/Fail
      data_type: bool
      unit: null
      expected_range: null
    - id: test_audio_pass
      name: Audio Test — Pass/Fail
      data_type: bool
      unit: null
      expected_range: null
    - id: test_touch_pass
      name: Touch Screen Test — Pass/Fail
      data_type: bool
      unit: null
      expected_range: null
    - id: test_nfc_pass
      name: NFC Test — Pass/Fail
      data_type: bool
      unit: null
      expected_range: null
    - id: test_charging_pass
      name: Charging Test — Pass/Fail
      data_type: bool
      unit: null
      expected_range: null
    - id: overall_result
      name: Overall Function Test Result (PASS/FAIL)
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-PH-06
  name: Cognex In-Sight 9000 AI Vision Camera
  zone: Z4
  location: Phone Assembly / Final QC (×2 — Z4 and Z9)
  qty: 2
  protocol: REST API
  update_frequency_s: 5
  dt_phase: 1
  sensors:
    - id: defect_class
      name: Defect Classification
      data_type: string
      unit: null
      expected_range: null
    - id: confidence_score
      name: AI Confidence Score (0–1)
      data_type: float
      unit: null
      expected_range: [0.0, 1.0]
    - id: image_ref
      name: Image Reference ID
      data_type: string
      unit: null
      expected_range: null
    - id: pass_fail
      name: Vision Inspection Result (PASS/FAIL)
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-PH-07
  name: Branson 2000X Ultrasonic Welder
  zone: Z4
  location: Phone Assembly — Ultrasonic Weld Stations (×3)
  qty: 3
  protocol: Ethernet API
  update_frequency_s: 5
  dt_phase: 1
  sensors:
    - id: weld_time_ms
      name: Weld Time (ms)
      data_type: float
      unit: ms
      expected_range: [100.0, 2000.0]
    - id: weld_energy_j
      name: Weld Energy (Joules)
      data_type: float
      unit: J
      expected_range: [5.0, 200.0]
    - id: amplitude_um
      name: Amplitude (µm)
      data_type: float
      unit: µm
      expected_range: [20.0, 120.0]
    - id: alarm_state
      name: Alarm State
      data_type: bool
      unit: null
      expected_range: null
```

### 2.4 TWS, Watch & Power Bank — Zones Z5, Z6, Z7

```yaml
- asset_id: DT-TWS-01
  name: Brüel & Kjær HATS Acoustic Test System
  zone: Z5
  location: TWS Assembly — Acoustic Test Stations (×6)
  qty: 6
  protocol: LAN API
  update_frequency_s: 10
  dt_phase: 1
  sensors:
    - id: freq_response_db
      name: Frequency Response at 1 kHz (dB)
      data_type: float
      unit: dB
      expected_range: [-20.0, 20.0]
    - id: thd_pct
      name: Total Harmonic Distortion (%)
      data_type: float
      unit: "%"
      expected_range: [0.0, 5.0]
    - id: sensitivity_db
      name: Sensitivity (dB SPL)
      data_type: float
      unit: dB SPL
      expected_range: [80.0, 110.0]
    - id: pass_fail
      name: Acoustic Test Pass/Fail
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-TWS-02
  name: R&S CMW500 Bluetooth Test System
  zone: Z5
  location: TWS Assembly / RF Lab (×4)
  qty: 4
  protocol: VISA/LAN
  update_frequency_s: 10
  dt_phase: 1
  sensors:
    - id: bt_channel
      name: Bluetooth Channel Under Test
      data_type: int
      unit: null
      expected_range: [0, 79]
    - id: rssi_dbm
      name: RSSI (dBm)
      data_type: float
      unit: dBm
      expected_range: [-90.0, 0.0]
    - id: latency_ms
      name: Audio Latency (ms)
      data_type: float
      unit: ms
      expected_range: [0.0, 100.0]
    - id: compliance_pass_fail
      name: Compliance Test Pass/Fail
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-TWS-03
  name: IPX Spray Chamber
  zone: Z5
  location: TWS Assembly — IPX Test (×2)
  qty: 2
  protocol: Modbus TCP
  update_frequency_s: 30
  dt_phase: 1
  sensors:
    - id: spray_pressure_bar
      name: Spray Pressure (bar)
      data_type: float
      unit: bar
      expected_range: [0.5, 3.0]
    - id: spray_duration_s
      name: Spray Duration (seconds)
      data_type: int
      unit: s
      expected_range: [60, 3600]
    - id: test_result
      name: IPX Test Result (PASS/FAIL)
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-SW-01
  name: Smartwatch Pressure Test Chamber
  zone: Z6
  location: Smartwatch Assembly — Pressure Test (×2)
  qty: 2
  protocol: Modbus TCP
  update_frequency_s: 30
  dt_phase: 1
  sensors:
    - id: pressure_bar
      name: Chamber Pressure (bar)
      data_type: float
      unit: bar
      expected_range: [0.0, 6.0]
    - id: soak_time_s
      name: Soak Time (seconds)
      data_type: int
      unit: s
      expected_range: [0, 1800]
    - id: pass_fail
      name: Pressure Test Pass/Fail
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-SW-02
  name: GPS Simulator (GNSS Replay)
  zone: Z6
  location: Smartwatch Assembly / RF Lab (×2)
  qty: 2
  protocol: VISA/LAN
  update_frequency_s: 15
  dt_phase: 1
  sensors:
    - id: gnss_lock_time_s
      name: GNSS Lock Time (seconds)
      data_type: float
      unit: s
      expected_range: [1.0, 60.0]
    - id: position_error_m
      name: Position Error (metres)
      data_type: float
      unit: m
      expected_range: [0.0, 10.0]
    - id: pass_fail
      name: GPS Simulation Test Pass/Fail
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-PB-01
  name: Sunstone Spot Welder
  zone: Z7
  location: Power Bank Assembly — Spot Weld Stations (×4)
  qty: 4
  protocol: Ethernet API
  update_frequency_s: 5
  dt_phase: 1
  sensors:
    - id: pulse_energy_j
      name: Pulse Energy (Joules)
      data_type: float
      unit: J
      expected_range: [1.0, 50.0]
    - id: voltage_v
      name: Weld Voltage (V)
      data_type: float
      unit: V
      expected_range: [0.0, 12.0]
    - id: weld_resistance_mohm
      name: Weld Resistance (mΩ)
      data_type: float
      unit: mΩ
      expected_range: [0.1, 5.0]
    - id: alarm_active
      name: Alarm Active
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-PB-02
  name: Chroma 17020 Battery Tester
  zone: Z7
  location: Power Bank Assembly — Battery Test Stations (×6)
  qty: 6
  protocol: Ethernet API
  update_frequency_s: 30
  dt_phase: 1
  sensors:
    - id: capacity_mah
      name: Measured Capacity (mAh)
      data_type: float
      unit: mAh
      expected_range: [4000.0, 22000.0]
    - id: ir_mohm
      name: Internal Resistance (mΩ)
      data_type: float
      unit: mΩ
      expected_range: [1.0, 200.0]
    - id: voltage_v
      name: Resting Voltage (V)
      data_type: float
      unit: V
      expected_range: [2.8, 4.35]
    - id: cycle_count
      name: Test Cycle Count
      data_type: int
      unit: count
      expected_range: [0, 10]

- asset_id: DT-PB-03
  name: Chroma 19053 Electrical Safety Tester
  zone: Z7
  location: Power Bank Assembly / Final QC (×4)
  qty: 4
  protocol: Ethernet API
  update_frequency_s: 10
  dt_phase: 1
  sensors:
    - id: hipot_voltage_v
      name: Hipot Test Voltage (V)
      data_type: float
      unit: V
      expected_range: [0.0, 3000.0]
    - id: hipot_current_ua
      name: Hipot Leakage Current (µA)
      data_type: float
      unit: µA
      expected_range: [0.0, 1000.0]
    - id: earth_bond_result
      name: Earth Bond Test Result (PASS/FAIL)
      data_type: bool
      unit: null
      expected_range: null
    - id: overall_result
      name: Safety Test Overall Result (OK/NOK)
      data_type: bool
      unit: null
      expected_range: null
```

### 2.5 RF & NCC Type Test Laboratory — Zone Z8

```yaml
- asset_id: DT-RF-01
  name: ETS-Lindgren 7000 Shielded Chamber
  zone: Z8
  location: RF & NCC Lab — Full-Phone OTA Chambers (×2)
  qty: 2
  protocol: REST API (booking system)
  update_frequency_s: 60
  dt_phase: 1
  sensors:
    - id: chamber_booking_status
      name: Chamber Booking Status (FREE/OCCUPIED)
      data_type: string
      unit: null
      expected_range: null
    - id: test_in_progress
      name: Test In Progress (bool)
      data_type: bool
      unit: null
      expected_range: null
    - id: alarm_active
      name: Alarm Active
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-RF-02
  name: Benchtop RF Shielded Chamber
  zone: Z8
  location: RF & NCC Lab — BT/Wi-Fi Chambers (×2)
  qty: 2
  protocol: REST API
  update_frequency_s: 30
  dt_phase: 1
  sensors:
    - id: test_result
      name: Test Result (PASS/FAIL)
      data_type: bool
      unit: null
      expected_range: null
    - id: frequency_band
      name: Frequency Band Under Test
      data_type: string
      unit: null
      expected_range: null

- asset_id: DT-RF-03
  name: R&S CMW500 Network / RF Analyser
  zone: Z8
  location: RF & NCC Lab (×2)
  qty: 2
  protocol: VISA/LAN
  update_frequency_s: 10
  dt_phase: 1
  sensors:
    - id: trp_dbm
      name: Total Radiated Power — TRP (dBm)
      data_type: float
      unit: dBm
      expected_range: [-20.0, 35.0]
    - id: tis_dbm
      name: Total Isotropic Sensitivity — TIS (dBm)
      data_type: float
      unit: dBm
      expected_range: [-110.0, -60.0]
    - id: band
      name: Band Under Test
      data_type: string
      unit: null
      expected_range: null
    - id: pass_fail
      name: RF Test Pass/Fail
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-RF-04
  name: Keysight N9020B Spectrum Analyser
  zone: Z8
  location: RF & NCC Lab
  qty: 1
  protocol: VISA/LAN
  update_frequency_s: 60
  dt_phase: 1
  sensors:
    - id: peak_frequency_mhz
      name: Peak Emission Frequency (MHz)
      data_type: float
      unit: MHz
      expected_range: [0.0, 18000.0]
    - id: emission_flag
      name: Emission Limit Exceedance Flag
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-RF-05
  name: Mini CATR OTA Test Range
  zone: Z8
  location: RF & NCC Lab
  qty: 1
  protocol: VISA/LAN
  update_frequency_s: 30
  dt_phase: 1
  sensors:
    - id: trp_dbm
      name: TRP (dBm)
      data_type: float
      unit: dBm
      expected_range: [-20.0, 35.0]
    - id: tis_dbm
      name: TIS (dBm)
      data_type: float
      unit: dBm
      expected_range: [-110.0, -60.0]
    - id: theta_deg
      name: Theta Scan Angle (degrees)
      data_type: float
      unit: degrees
      expected_range: [0.0, 360.0]
    - id: phi_deg
      name: Phi Scan Angle (degrees)
      data_type: float
      unit: degrees
      expected_range: [0.0, 360.0]
    - id: pass_fail
      name: OTA Pass/Fail
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-RF-06
  name: RF Calibration Station
  zone: Z4
  location: Phone / TWS / Watch Assembly RF Cal Stations (×4)
  qty: 4
  protocol: REST API
  update_frequency_s: 10
  dt_phase: 1
  sensors:
    - id: cal_result_pass_fail
      name: Calibration Result (PASS/FAIL)
      data_type: bool
      unit: null
      expected_range: null
    - id: band
      name: Band Calibrated
      data_type: string
      unit: null
      expected_range: null
    - id: offset_applied_db
      name: Calibration Offset Applied (dB)
      data_type: float
      unit: dB
      expected_range: [-3.0, 3.0]
    - id: serial_number
      name: Unit Serial Number
      data_type: string
      unit: null
      expected_range: null
```

### 2.6 AMR Fleet — All Zones

```yaml
# MiR250 Transport AMRs — 12 units (main material transport)
- asset_id: DT-AMR-MIR250-01
  name: MiR250 Transport AMR — Unit 01
  zone: all
  location: Roaming — all production zones
  qty: 1
  protocol: MiR Fleet REST API
  update_frequency_s: 1
  dt_phase: 1
  sensors:
    - id: pos_x_m
      name: Position X (metres — factory coordinate)
      data_type: float
      unit: m
      expected_range: [0.0, 150.0]
    - id: pos_y_m
      name: Position Y (metres — factory coordinate)
      data_type: float
      unit: m
      expected_range: [0.0, 120.0]
    - id: pos_theta_deg
      name: Heading Angle θ (degrees)
      data_type: float
      unit: degrees
      expected_range: [0.0, 360.0]
    - id: speed_m_s
      name: Speed (m/s)
      data_type: float
      unit: m/s
      expected_range: [0.0, 1.5]
    - id: battery_soc_pct
      name: Battery State of Charge (%)
      data_type: float
      unit: "%"
      expected_range: [0.0, 100.0]
    - id: mission_status
      name: Mission Status (IDLE/EXECUTING/COMPLETE/ERROR)
      data_type: string
      unit: null
      expected_range: null
    - id: payload_weight_kg
      name: Payload Weight (kg)
      data_type: float
      unit: kg
      expected_range: [0.0, 250.0]

# Units DT-AMR-MIR250-02 through DT-AMR-MIR250-12: identical schema to DT-AMR-MIR250-01.

# MiR100 Goods-to-Person AMRs — 4 units (SMT component kitting)
- asset_id: DT-AMR-MIR100-01
  name: MiR100 Goods-to-Person AMR — Unit 01
  zone: Z1
  location: Stores to SMT Line feeder trolleys
  qty: 1
  protocol: MiR Fleet REST API
  update_frequency_s: 1
  dt_phase: 1
  sensors:
    - id: pos_x_m
      name: Position X (metres)
      data_type: float
      unit: m
      expected_range: [0.0, 150.0]
    - id: pos_y_m
      name: Position Y (metres)
      data_type: float
      unit: m
      expected_range: [0.0, 120.0]
    - id: speed_m_s
      name: Speed (m/s)
      data_type: float
      unit: m/s
      expected_range: [0.0, 1.2]
    - id: battery_soc_pct
      name: Battery State of Charge (%)
      data_type: float
      unit: "%"
      expected_range: [0.0, 100.0]
    - id: mission_status
      name: Mission Status
      data_type: string
      unit: null
      expected_range: null

# Units DT-AMR-MIR100-02 through DT-AMR-MIR100-04: identical schema to DT-AMR-MIR100-01.

# AMR Charging Docks — 18 docks
- asset_id: DT-AMR-DOCK-01
  name: AMR Charging Dock 01
  zone: Z12
  location: AMR Charging Bay — Engineering Zone
  qty: 1
  protocol: MiR Fleet REST API
  update_frequency_s: 30
  dt_phase: 1
  sensors:
    - id: dock_occupied
      name: Dock Occupied (true/false)
      data_type: bool
      unit: null
      expected_range: null
    - id: amr_id
      name: AMR ID Currently Docked
      data_type: string
      unit: null
      expected_range: null
    - id: charge_current_a
      name: Charge Current (A)
      data_type: float
      unit: A
      expected_range: [0.0, 25.0]
    - id: amr_soc_pct
      name: Docked AMR SoC (%)
      data_type: float
      unit: "%"
      expected_range: [0.0, 100.0]

# Docks DT-AMR-DOCK-02 through DT-AMR-DOCK-18: identical schema to DT-AMR-DOCK-01.
```

### 2.7 Energy Systems — Site-Wide

```yaml
- asset_id: DT-EN-PV-01
  name: Solar PV Array — Roof Main (620 kWp)
  zone: site
  location: Factory Main Roof
  qty: 1
  protocol: Sungrow iSolarCloud API
  update_frequency_s: 60
  dt_phase: 1
  sensors:
    - id: generation_kw
      name: Real-Time Generation (kW)
      data_type: float
      unit: kW
      expected_range: [0.0, 650.0]
    - id: cumulative_kwh_today
      name: Cumulative Generation Today (kWh)
      data_type: float
      unit: kWh
      expected_range: [0.0, 3000.0]
    - id: irradiance_w_m2
      name: Irradiance (W/m²)
      data_type: float
      unit: W/m²
      expected_range: [0.0, 1200.0]
    - id: string_iv_flag
      name: String IV Anomaly Flag (any underperforming string)
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-EN-PV-02
  name: Solar PV Array — Warehouse Roof (110 kWp)
  zone: site
  location: Warehouse Block Roof
  qty: 1
  protocol: Sungrow iSolarCloud API
  update_frequency_s: 60
  dt_phase: 1
  sensors:
    - id: generation_kw
      name: Real-Time Generation (kW)
      data_type: float
      unit: kW
      expected_range: [0.0, 120.0]
    - id: cumulative_kwh_today
      name: Cumulative Generation Today (kWh)
      data_type: float
      unit: kWh
      expected_range: [0.0, 550.0]
    - id: irradiance_w_m2
      name: Irradiance (W/m²)
      data_type: float
      unit: W/m²
      expected_range: [0.0, 1200.0]

- asset_id: DT-EN-PV-03
  name: Solar PV Array — Ground Mount (120 kWp)
  zone: site
  location: East Yard
  qty: 1
  protocol: Sungrow iSolarCloud API
  update_frequency_s: 60
  dt_phase: 1
  sensors:
    - id: generation_kw
      name: Real-Time Generation (kW)
      data_type: float
      unit: kW
      expected_range: [0.0, 130.0]
    - id: temperature_c
      name: Panel Surface Temperature (°C)
      data_type: float
      unit: "°C"
      expected_range: [20.0, 80.0]
    - id: irradiance_w_m2
      name: Irradiance (W/m²)
      data_type: float
      unit: W/m²
      expected_range: [0.0, 1200.0]

- asset_id: DT-EN-BESS-01
  name: LFP BESS Container 1 (450 kWh)
  zone: site
  location: North Yard — BESS Enclosure 1
  qty: 1
  protocol: Sungrow iSolarCloud API / Modbus TCP
  update_frequency_s: 30
  dt_phase: 1
  sensors:
    - id: soc_pct
      name: State of Charge (%)
      data_type: float
      unit: "%"
      expected_range: [10.0, 100.0]
    - id: soh_pct
      name: State of Health (%)
      data_type: float
      unit: "%"
      expected_range: [70.0, 100.0]
    - id: charge_discharge_kw
      name: Charge (+) / Discharge (-) Power (kW)
      data_type: float
      unit: kW
      expected_range: [-450.0, 450.0]
    - id: cell_temp_max_c
      name: Maximum Cell Temperature (°C)
      data_type: float
      unit: "°C"
      expected_range: [15.0, 45.0]
    - id: pack_voltage_v
      name: Pack Voltage (V)
      data_type: float
      unit: V
      expected_range: [550.0, 680.0]

- asset_id: DT-EN-BESS-02
  name: LFP BESS Container 2 (450 kWh)
  zone: site
  location: North Yard — BESS Enclosure 2
  qty: 1
  protocol: Sungrow iSolarCloud API / Modbus TCP
  update_frequency_s: 30
  dt_phase: 1
  sensors: # identical to DT-EN-BESS-01

- asset_id: DT-EN-INV-01
  name: Sungrow SH250HX Hybrid Inverter 1
  zone: site
  location: Inverter / PCS Room
  qty: 1
  protocol: Sungrow iSolarCloud API
  update_frequency_s: 30
  dt_phase: 1
  sensors:
    - id: ac_output_kw
      name: AC Output Power (kW)
      data_type: float
      unit: kW
      expected_range: [0.0, 260.0]
    - id: dc_input_kw
      name: DC Input Power from Solar (kW)
      data_type: float
      unit: kW
      expected_range: [0.0, 260.0]
    - id: efficiency_pct
      name: Inverter Efficiency (%)
      data_type: float
      unit: "%"
      expected_range: [90.0, 99.0]
    - id: alarm_active
      name: Alarm Active
      data_type: bool
      unit: null
      expected_range: null

# DT-EN-INV-02, DT-EN-INV-03, DT-EN-INV-04: identical schema to DT-EN-INV-01.

- asset_id: DT-EN-GEN-01
  name: Perkins 500 kVA Backup Generator
  zone: site
  location: North-East Corner — Generator Pad
  qty: 1
  protocol: Modbus TCP
  update_frequency_s: 30
  dt_phase: 1
  sensors:
    - id: running_status
      name: Running Status (RUNNING/STOPPED/FAULT)
      data_type: string
      unit: null
      expected_range: null
    - id: output_kw
      name: Output Power (kW)
      data_type: float
      unit: kW
      expected_range: [0.0, 420.0]
    - id: fuel_level_l
      name: Fuel Tank Level (litres)
      data_type: float
      unit: L
      expected_range: [0.0, 2000.0]
    - id: run_hours_total
      name: Total Run Hours (cumulative)
      data_type: float
      unit: hours
      expected_range: [0.0, 50000.0]

- asset_id: DT-EN-GRID-01
  name: Grid Supply AMI Smart Meter
  zone: site
  location: HV/LV Intake Substation
  qty: 1
  protocol: Modbus TCP
  update_frequency_s: 60
  dt_phase: 1
  sensors:
    - id: import_kw
      name: Grid Import Power (kW)
      data_type: float
      unit: kW
      expected_range: [0.0, 620.0]
    - id: cumulative_kwh_today
      name: Cumulative Grid Import Today (kWh)
      data_type: float
      unit: kWh
      expected_range: [0.0, 5000.0]
    - id: tou_period
      name: Time-of-Use Tariff Period (PEAK/OFF-PEAK/SHOULDER)
      data_type: string
      unit: null
      expected_range: null

- asset_id: DT-EN-HVAC-01
  name: Carrier Chiller 1
  zone: site
  location: Utility Room
  qty: 1
  protocol: BACnet/IP or Modbus TCP
  update_frequency_s: 60
  dt_phase: 1
  sensors:
    - id: cooling_kw
      name: Cooling Output (kW)
      data_type: float
      unit: kW
      expected_range: [0.0, 200.0]
    - id: inlet_temp_c
      name: Chilled Water Inlet Temperature (°C)
      data_type: float
      unit: "°C"
      expected_range: [5.0, 25.0]
    - id: outlet_temp_c
      name: Chilled Water Outlet Temperature (°C)
      data_type: float
      unit: "°C"
      expected_range: [5.0, 18.0]
    - id: cop
      name: Coefficient of Performance (COP)
      data_type: float
      unit: null
      expected_range: [2.5, 6.0]
    - id: alarm_active
      name: Alarm Active
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-EN-HVAC-02
  name: Carrier Chiller 2
  zone: site
  location: Utility Room
  qty: 1
  protocol: BACnet/IP or Modbus TCP
  update_frequency_s: 60
  dt_phase: 1
  sensors: # identical to DT-EN-HVAC-01
```

### 2.8 Supporting Zones — Z1, Z9, Z10, Z11

```yaml
# Zone Z1 — Component Stores
- asset_id: DT-Z1-VLM-01
  name: Modula Vertical Lift Module 1
  zone: Z1
  location: Component Stores — VLM Bay 1
  qty: 1
  protocol: Modula API (REST/OPC-UA)
  update_frequency_s: 10
  dt_phase: 1
  sensors:
    - id: pick_count_shift
      name: Pick Count (current shift)
      data_type: int
      unit: count
      expected_range: [0, 2000]
    - id: inventory_level_pct
      name: Inventory Level (% of capacity)
      data_type: float
      unit: "%"
      expected_range: [5.0, 100.0]
    - id: temp_c
      name: Internal Temperature (°C)
      data_type: float
      unit: "°C"
      expected_range: [18.0, 30.0]
    - id: alarm_active
      name: Alarm Active
      data_type: bool
      unit: null
      expected_range: null

# DT-Z1-VLM-02, DT-Z1-VLM-03, DT-Z1-VLM-04: identical schema to DT-Z1-VLM-01.

# Zone Z9 — Final QC & Safety Test Lab
- asset_id: DT-Z9-DROP-01
  name: Drop Test System
  zone: Z9
  location: Final QC Lab
  qty: 1
  protocol: Ethernet API
  update_frequency_s: 60
  dt_phase: 1
  sensors:
    - id: drop_height_mm
      name: Drop Height (mm)
      data_type: int
      unit: mm
      expected_range: [500, 2000]
    - id: pass_fail
      name: Drop Test Pass/Fail
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-Z9-THERM-01
  name: Thermal Cycling Chamber
  zone: Z9
  location: Final QC Lab
  qty: 1
  protocol: Modbus TCP
  update_frequency_s: 60
  dt_phase: 1
  sensors:
    - id: chamber_temp_c
      name: Chamber Temperature (°C)
      data_type: float
      unit: "°C"
      expected_range: [-40.0, 85.0]
    - id: cycle_count
      name: Thermal Cycle Count
      data_type: int
      unit: count
      expected_range: [0, 200]
    - id: alarm_active
      name: Alarm Active
      data_type: bool
      unit: null
      expected_range: null

- asset_id: DT-Z9-BATT-CYCLE-01
  name: Battery Cycle Sampling Station
  zone: Z9
  location: Final QC Lab
  qty: 1
  protocol: Ethernet API
  update_frequency_s: 60
  dt_phase: 1
  sensors:
    - id: cycle_count
      name: Cycles Completed
      data_type: int
      unit: count
      expected_range: [0, 500]
    - id: capacity_retention_pct
      name: Capacity Retention (%)
      data_type: float
      unit: "%"
      expected_range: [70.0, 100.0]

# Zone Z10 — Packaging Lines
- asset_id: DT-Z10-CHECKWEIGH-01
  name: Mettler Toledo Checkweigher
  zone: Z10
  location: Packaging Line 1
  qty: 1
  protocol: Ethernet API
  update_frequency_s: 5
  dt_phase: 1
  sensors:
    - id: weight_g
      name: Measured Weight (grams)
      data_type: float
      unit: g
      expected_range: [50.0, 2000.0]
    - id: pass_fail
      name: Weight Check Pass/Fail
      data_type: bool
      unit: null
      expected_range: null
    - id: reject_count_shift
      name: Rejects Count (current shift)
      data_type: int
      unit: count
      expected_range: [0, 200]

- asset_id: DT-Z10-BARCODE-01
  name: Barcode Verification Scanner — Packaging
  zone: Z10
  location: Packaging Lines (×2)
  qty: 2
  protocol: Ethernet API
  update_frequency_s: 5
  dt_phase: 1
  sensors:
    - id: serial_number
      name: Serial Number Scanned
      data_type: string
      unit: null
      expected_range: null
    - id: scan_result
      name: Scan Result (MATCH/NO_READ/MISMATCH)
      data_type: string
      unit: null
      expected_range: null

- asset_id: DT-Z10-LABEL-01
  name: Carton Label Printer
  zone: Z10
  location: Packaging Lines (×2)
  qty: 2
  protocol: Ethernet API
  update_frequency_s: 10
  dt_phase: 1
  sensors:
    - id: label_count_shift
      name: Labels Printed (current shift)
      data_type: int
      unit: count
      expected_range: [0, 5000]
    - id: ribbon_level_pct
      name: Ribbon Level (%)
      data_type: float
      unit: "%"
      expected_range: [0.0, 100.0]
    - id: alarm_active
      name: Alarm Active
      data_type: bool
      unit: null
      expected_range: null

# Zone Z11 — Finished Goods Warehouse
- asset_id: DT-Z11-TEMP-01
  name: Warehouse Ambient Temperature & Humidity Sensor
  zone: Z11
  location: FG Warehouse — distributed sensors
  qty: 4
  protocol: MQTT (wireless sensor)
  update_frequency_s: 60
  dt_phase: 1
  sensors:
    - id: temperature_c
      name: Ambient Temperature (°C)
      data_type: float
      unit: "°C"
      expected_range: [15.0, 35.0]
    - id: humidity_pct
      name: Relative Humidity (%)
      data_type: float
      unit: "%"
      expected_range: [30.0, 70.0]

- asset_id: DT-Z11-PALLET-SCAN-01
  name: Pallet Barcode Scanner — FG Warehouse
  zone: Z11
  location: FG Warehouse — rack entry points
  qty: 1
  protocol: Ethernet API
  update_frequency_s: 10
  dt_phase: 1
  sensors:
    - id: pallet_id
      name: Pallet ID Scanned
      data_type: string
      unit: null
      expected_range: null
    - id: scan_event
      name: Scan Event Type (PUT_AWAY/PICK/DISPATCH)
      data_type: string
      unit: null
      expected_range: null
```

---

## 3. Asset Count Summary

| Zone | Zone Name | Asset IDs (Groups) | Physical Units (qty) |
|------|---|---|---|
| Z2 | SMT Line 1 | 10 | 10 |
| Z3 | SMT Line 2 | 10 | 10 |
| Z4 | Phone Assembly | 7 | 24 |
| Z5 | TWS Assembly | 3 | 12 |
| Z6 | Smartwatch Assembly | 2 | 4 |
| Z7 | Power Bank Assembly | 3 | 14 |
| Z8 | RF & NCC Lab | 6 | 12 |
| Z1 | Component Stores | 4 | 4 |
| Z9 | Final QC Lab | 4 | 5 |
| Z10 | Packaging | 5 | 6 |
| Z11 | FG Warehouse | 2 | 5 |
| AMR | Fleet (all zones) | 34 | 34 |
| Site | Energy Systems | 13 | 16 |
| **Total** | | **103 Asset ID groups** | **156 physical units** |

> **Count reconciliation:**
>
> - **103 logical Asset ID groups** — the number of distinct `asset_id` entries in this manifest.
>   Multi-instance assets (e.g., 6× flash fixtures under `DT-PH-04`) are counted once here.
>
> - **156 physical units** — the total when every `qty` field is expanded. This is the sum of
>   all individual machines, sensors, and devices on the factory floor.
>
> - **142 registered physical assets** — the count stated in [`digital-twin.md`](./digital-twin.md)
>   §1. That number represents production-critical assets originally enumerated in the DT asset
>   registry (Sections 2.1–2.6 of that document), which covers SMT, phone, TWS/watch/PB,
>   RF lab, AMR fleet, and energy assets. The 14-unit difference from 156 reflects the supporting
>   zone assets (Z1 VLMs, Z9 test equipment, Z10 packaging stations, Z11 warehouse sensors)
>   that are fully defined in this manifest but were not individually enumerated in the initial
>   digital-twin.md registry tables. The combined total across all zones is 156 physical units.

---

## 4. Version History

| Version | Date | Description | Author |
|---|---|---|---|
| 1.0 | 2026 | Initial manifest — all 101 asset ID groups; Phase 1 sensors | Digital Manufacturing Team |

---

*For phase build steps, see [`dt-implementation-plan.md`](./dt-implementation-plan.md)*
*For MQTT topic assignments, see [`dt-mqtt-namespace.md`](./dt-mqtt-namespace.md)*
*For infrastructure deployment, see [`dt-infrastructure.md`](./dt-infrastructure.md)*
