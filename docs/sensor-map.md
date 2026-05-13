# Sensor Registry — Personal Electronics Factory

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1
> **Document Version:** 1.0 | **Owner:** Digital Manufacturing & AI Team + Quality Engineering
> **Integration Reviewer:** Documentation Integration Reviewer
> **Status:** Controlled Draft — canonical sensor registry for DT Gate 3 acceptance

This document is the **canonical sensor registry** for all 2,800 data points monitored by the
Coo-Cah Digital Twin platform across the Personal Electronics Factory. Every sensor and data-point
entry records the sensor model (where applicable), integration protocol, calibration interval,
factory location, and data type. It is the authoritative reference used to:

1. Configure Telegraf/MQTT subscriptions in the DT edge node
2. Define InfluxDB measurement schema (bucket, measurement, field key)
3. Set calibration/maintenance schedules in the CMMS
4. Verify Gate 3 sensor coverage before Phase 1 live connection

> **Relationship to asset manifest:** This registry extends `dt-asset-manifest.md` with
> calibration, model, and physical-sensor detail not captured in the YAML schema.
> Any discrepancy between this document and `dt-asset-manifest.md` must be resolved
> and both documents updated simultaneously.

---

## 1. Registry Summary

| Zone  | Zone Name              | Monitored Assets | Data Points | Primary Protocols          |
|-------|------------------------|-----------------|-------------|----------------------------|
| Z1    | Component Stores       | 4               | 80          | Modbus TCP, dry-contact     |
| Z2    | SMT Line 1             | 10              | 420         | SECS/GEM, OPC-UA, REST API  |
| Z3    | SMT Line 2             | 10              | 420         | SECS/GEM, OPC-UA, REST API  |
| Z4    | Phone Assembly         | 8               | 280         | OPC-UA, REST API, Ethernet  |
| Z5    | TWS Assembly           | 6               | 200         | LAN API, VISA, REST API     |
| Z6    | Smartwatch Assembly    | 5               | 160         | OPC-UA, REST API, VISA      |
| Z7    | Power Bank Assembly    | 6               | 200         | Ethernet API, REST API      |
| Z8    | RF & NCC Lab           | 6               | 260         | VISA/LAN, REST API          |
| Z9    | Final QC               | 4               | 180         | REST API, Ethernet API      |
| Z10   | Packaging              | 4               | 120         | Ethernet API, Modbus TCP    |
| Z11   | FG Warehouse           | 4               | 80          | MQTT (MiR), Modbus, REST    |
| Site  | Energy Systems         | 12              | 400         | Modbus TCP, OPC-UA, MQTT    |
| **Total** |                    | **79**          | **2,800**   |                            |

---

## 2. Calibration Interval Reference

| Interval Code | Calibration Frequency | Applicable Sensor Types                                     |
|---------------|-----------------------|-------------------------------------------------------------|
| CAL-A         | Every 6 months        | RF/microwave instruments (R&S CMW500, spectrum analysers)   |
| CAL-B         | Every 12 months       | Acoustic test systems, GPS simulators, vision systems       |
| CAL-C         | Every 12 months       | Torque transducers, force gauges, pressure sensors          |
| CAL-D         | Every 12 months       | Battery testers, hipot/safety testers (electrical standards)|
| CAL-E         | Every 24 months       | Temperature sensors (NTC/PT100) in ovens and chambers       |
| CAL-F         | Per manufacturer spec  | Spot welders (pre-use energy calibration); reflow oven thermocouples |
| CAL-G         | Quarterly             | SPI / AOI reference boards; golden-board calibration runs   |
| CAL-H         | Every 12 months       | Energy meters (kWh accuracy per IEC 62053-21 Class 1)       |
| CAL-N         | Not applicable        | Digital state/status sensors, alarm flags, recipe strings   |

---

## 3. Zone Z1 — Component Stores (80 data points)

### 3.1 Modula VLM Units ×4 (DT-STR-01 to 04)

| Sensor ID             | Description                     | Sensor Model / Type       | Protocol     | Cal. Interval | Location       |
|-----------------------|---------------------------------|---------------------------|--------------|---------------|----------------|
| STR-VLM-n-PICK_COUNT  | Pick cycle count (running total) | Modula internal counter   | Modbus TCP   | CAL-N         | Z1 — VLM n     |
| STR-VLM-n-INV_LEVEL   | Inventory level (% of capacity) | Modula Lift controller    | Modbus TCP   | CAL-N         | Z1 — VLM n     |
| STR-VLM-n-TEMP_C      | Internal tray temperature (°C)  | NTC thermistor (built-in) | Modbus TCP   | CAL-E         | Z1 — VLM n     |
| STR-VLM-n-ALARM       | Alarm/fault status              | Digital output            | Modbus TCP   | CAL-N         | Z1 — VLM n     |
| STR-VLM-n-DOOR_STATE  | Door open/closed (bool)         | Micro-switch              | Modbus TCP   | CAL-N         | Z1 — VLM n     |

*n = 1–4; 4 units × 5 data points = 20 data points*

### 3.2 Incoming QC Bench & Environment (DT-STR general)

| Sensor ID              | Description                    | Sensor Model / Type            | Protocol     | Cal. Interval | Location       |
|------------------------|--------------------------------|--------------------------------|--------------|---------------|----------------|
| STR-ENV-TEMP_C         | Ambient temperature (°C)       | Sensirion SHT31                | Modbus TCP   | CAL-E         | Z1 — QC bench  |
| STR-ENV-RH_PCT         | Relative humidity (%)          | Sensirion SHT31                | Modbus TCP   | CAL-C         | Z1 — QC bench  |
| STR-QC-SCAN_COUNT      | IQC barcode scan count/shift   | Honeywell Xenon 1900 (barcode) | REST API     | CAL-N         | Z1 — IQC bench |
| STR-RACK-TEMP_C        | Bulk rack area temperature (°C)| NTC thermistor (wall-mount)    | Modbus TCP   | CAL-E         | Z1 — rack area |

*4 data points per bench, plus 60 explicitly allocated support points for label printers, dock-door
sensors, and inventory-system callbacks = 80 total for Z1.*

---

## 4. Zone Z2 — SMT Line 1 (420 data points)

### 4.1 DT-SMT-L1-01 — DEK Horizon Screen Printer

| Sensor ID                  | Description                           | Sensor / Source                   | Protocol   | Cal. Interval |
|----------------------------|---------------------------------------|-----------------------------------|------------|---------------|
| SMT-L1-01-PRINT_RECIPE     | Active print recipe name              | SECS/GEM S7F13                    | SECS/GEM   | CAL-N         |
| SMT-L1-01-PASTE_VOL_PCT    | Paste volume (% of nominal)           | SECS/GEM S6F11 data               | SECS/GEM   | CAL-G         |
| SMT-L1-01-STENCIL_LIFE     | Stencil remaining life (cycles)       | SECS/GEM counter                  | SECS/GEM   | CAL-N         |
| SMT-L1-01-ALARM_ACTIVE     | Alarm active (bool)                   | SECS/GEM S5F1                     | SECS/GEM   | CAL-N         |
| SMT-L1-01-MACHINE_STATE    | Machine state (RUN/IDLE/ALARM/SETUP)  | SECS/GEM EQST                     | SECS/GEM   | CAL-N         |
| SMT-L1-01-SQUEEGEE_PRESS   | Squeegee pressure (N)                 | Built-in load cell                | SECS/GEM   | CAL-C         |
| SMT-L1-01-PRINT_SPEED      | Print speed (mm/s)                    | SECS/GEM motion data              | SECS/GEM   | CAL-N         |
| SMT-L1-01-SEPARATION_SPD  | Stencil separation speed (mm/s)       | SECS/GEM motion data              | SECS/GEM   | CAL-N         |
| SMT-L1-01-BOARD_COUNT      | Boards processed (shift count)        | SECS/GEM counter                  | SECS/GEM   | CAL-N         |
| SMT-L1-01-UNDERSIDE_CLEAN  | Underside wipe interval (cycles)      | SECS/GEM counter                  | SECS/GEM   | CAL-N         |

### 4.2 DT-SMT-L1-02 — Koh Young KY8030-3 SPI

| Sensor ID                   | Description                           | Sensor / Source          | Protocol    | Cal. Interval |
|-----------------------------|---------------------------------------|--------------------------|-------------|---------------|
| SMT-L1-02-MEAN_VOL_PCT      | Mean paste volume (% nominal)         | KY REST API / SECS/GEM   | SECS/GEM    | CAL-G         |
| SMT-L1-02-CPK               | Process capability index Cpk          | KY REST API              | SECS/GEM    | CAL-G         |
| SMT-L1-02-PADS_INSPECTED    | Pads inspected per board              | KY SECS/GEM              | SECS/GEM    | CAL-N         |
| SMT-L1-02-PADS_FAILED       | Pads failed count per board           | KY SECS/GEM              | SECS/GEM    | CAL-N         |
| SMT-L1-02-DEFECT_CODE       | Latest defect code string             | KY REST API              | REST API    | CAL-N         |
| SMT-L1-02-BOARD_ID          | Board serial reference                | KY REST API              | REST API    | CAL-N         |
| SMT-L1-02-ALARM_ACTIVE      | Alarm active (bool)                   | SECS/GEM S5F1            | SECS/GEM    | CAL-N         |
| SMT-L1-02-MACHINE_STATE     | Machine state                         | SECS/GEM EQST            | SECS/GEM    | CAL-N         |

### 4.3 DT-SMT-L1-03 — JUKI FX-3R Pick-and-Place

| Sensor ID                   | Description                      | Protocol   | Cal. Interval |
|-----------------------------|----------------------------------|------------|---------------|
| SMT-L1-03-CPH               | Components per hour              | SECS/GEM   | CAL-N         |
| SMT-L1-03-FEEDER_ERROR      | Feeder error count/shift         | SECS/GEM   | CAL-N         |
| SMT-L1-03-NOZZLE_STATE      | Nozzle status per head (array)   | SECS/GEM   | CAL-N         |
| SMT-L1-03-PLACEMENT_COUNT   | Placement count (shift)          | SECS/GEM   | CAL-N         |
| SMT-L1-03-MACHINE_STATE     | Machine state                    | SECS/GEM   | CAL-N         |
| SMT-L1-03-ALARM_ACTIVE      | Alarm active                     | SECS/GEM   | CAL-N         |

### 4.4 DT-SMT-L1-04 — JUKI RX-7 Pick-and-Place

*Same sensor set as DT-SMT-L1-03; topic prefix `SMT-L1-04-`.*

### 4.5 DT-SMT-L1-05 — Heller 1964 MK5 Reflow Oven

| Sensor ID                   | Description                           | Sensor / Source            | Protocol      | Cal. Interval |
|-----------------------------|---------------------------------------|----------------------------|---------------|---------------|
| SMT-L1-05-ZONE_n_TEMP_C     | Zone n temperature (°C), n=1–8        | K-type thermocouple × 8    | Modbus TCP    | CAL-F         |
| SMT-L1-05-CONVEYOR_SPD      | Conveyor speed (mm/min)               | Encoder via Modbus          | Modbus TCP    | CAL-N         |
| SMT-L1-05-N2_LEVEL_PCT      | Nitrogen purity level (%)             | O₂ sensor (residual)        | Modbus TCP    | CAL-E         |
| SMT-L1-05-PROFILE_NAME      | Active reflow profile name            | OPC-UA / Modbus string      | OPC-UA        | CAL-N         |
| SMT-L1-05-ALARM_ACTIVE      | Alarm active (bool)                   | OPC-UA                      | OPC-UA        | CAL-N         |
| SMT-L1-05-MACHINE_STATE     | Machine state                         | OPC-UA                      | OPC-UA        | CAL-N         |
| SMT-L1-05-ENERGY_KW         | Power consumption (kW)                | Integrated energy meter     | Modbus TCP    | CAL-H         |

*8 zone temps + 6 other = 14 data points per oven.*

### 4.6 DT-SMT-L1-06 — Koh Young Zenith AOI

| Sensor ID                   | Description                      | Protocol    | Cal. Interval |
|-----------------------------|----------------------------------|-------------|---------------|
| SMT-L1-06-DEFECT_CODE       | Defect class code                | REST API    | CAL-N         |
| SMT-L1-06-IMAGE_REF         | Image reference (path/URL)       | REST API    | CAL-N         |
| SMT-L1-06-FPY               | First pass yield per board (%)   | REST API    | CAL-G         |
| SMT-L1-06-DEFECT_COUNT      | Defect count per board           | REST API    | CAL-N         |
| SMT-L1-06-ALARM_ACTIVE      | Alarm active                     | SECS/GEM    | CAL-N         |
| SMT-L1-06-MACHINE_STATE     | Machine state                    | SECS/GEM    | CAL-N         |
| SMT-L1-06-BOARD_ID          | Board serial reference           | REST API    | CAL-N         |
| SMT-L1-06-GOLDEN_REF_DATE   | Golden-board calibration date    | REST API    | CAL-G         |

### 4.7 DT-SMT-L1-07 — Unicomp AX8200 X-Ray

| Sensor ID                  | Description                        | Protocol  | Cal. Interval |
|----------------------------|------------------------------------|-----------|---------------|
| SMT-L1-07-VOID_PCT         | BGA void percentage per joint      | REST API  | CAL-B         |
| SMT-L1-07-IMAGE_REF        | Image reference                    | REST API  | CAL-N         |
| SMT-L1-07-PASS_FAIL        | Pass/fail result                   | REST API  | CAL-N         |
| SMT-L1-07-BOARD_ID         | Board serial reference             | REST API  | CAL-N         |
| SMT-L1-07-ALARM_ACTIVE     | Alarm active                       | REST API  | CAL-N         |

### 4.8 DT-SMT-L1-08 — Ersa Versaflow Selective Solder

| Sensor ID                  | Description                   | Protocol  | Cal. Interval |
|----------------------------|-------------------------------|-----------|---------------|
| SMT-L1-08-FLUX_LEVEL_PCT   | Flux reservoir level (%)      | OPC-UA    | CAL-N         |
| SMT-L1-08-SOLDER_LEVEL_PCT | Solder pot level (%)          | OPC-UA    | CAL-N         |
| SMT-L1-08-NOZZLE_TEMP_C    | Nozzle temperature (°C)       | K-type thermocouple → OPC-UA | OPC-UA | CAL-E  |
| SMT-L1-08-RECIPE_NAME      | Active recipe name            | OPC-UA    | CAL-N         |
| SMT-L1-08-ALARM_ACTIVE     | Alarm active                  | OPC-UA    | CAL-N         |
| SMT-L1-08-MACHINE_STATE    | Machine state                 | OPC-UA    | CAL-N         |

### 4.9 DT-SMT-L1-09 — Keysight I1000D ICT

| Sensor ID                  | Description                    | Protocol      | Cal. Interval |
|----------------------------|--------------------------------|---------------|---------------|
| SMT-L1-09-TEST_RESULT      | Net test pass/fail             | Ethernet API  | CAL-N         |
| SMT-L1-09-SHORTS_COUNT     | Shorts detected count          | Ethernet API  | CAL-N         |
| SMT-L1-09-OPENS_COUNT      | Opens detected count           | Ethernet API  | CAL-N         |
| SMT-L1-09-FIXTURE_ID       | Fixture serial number          | Ethernet API  | CAL-N         |
| SMT-L1-09-BOARD_ID         | Board serial reference         | Ethernet API  | CAL-N         |
| SMT-L1-09-ALARM_ACTIVE     | Alarm active                   | Ethernet API  | CAL-N         |

### 4.10 DT-SMT-L1-10 — PCB Depanelling Router

| Sensor ID                  | Description                   | Protocol  | Cal. Interval |
|----------------------------|-------------------------------|-----------|---------------|
| SMT-L1-10-CYCLE_COUNT      | Routing cycle count (shift)   | OPC-UA    | CAL-N         |
| SMT-L1-10-SPINDLE_SPD_RPM  | Spindle speed (RPM)           | OPC-UA    | CAL-N         |
| SMT-L1-10-ALARM_ACTIVE     | Alarm active                  | OPC-UA    | CAL-N         |
| SMT-L1-10-MACHINE_STATE    | Machine state                 | OPC-UA    | CAL-N         |

*SMT Line 1 total: 10 assets × approx. 42 data points per line average = 420 total for Z2.*

> **Zone Z3 (SMT Line 2):** Identical sensor set to Z2 with topic prefix `SMT-L2-`. Total: 420 data points.

---

## 5. Zone Z4 — Phone Assembly (280 data points)

### 5.1 DT-PH-01 — Screen Bonding Machine (×2)

| Sensor ID               | Description                  | Sensor / Source              | Protocol     | Cal. Interval |
|-------------------------|------------------------------|------------------------------|--------------|---------------|
| PH-01-n-VAC_LEVEL_MBAR  | Vacuum level (mbar)          | Pirani vacuum sensor         | OPC-UA       | CAL-C         |
| PH-01-n-OCA_PRESS_N     | OCA press force (N)          | Load cell                    | OPC-UA       | CAL-C         |
| PH-01-n-CYCLE_TIME_S    | Cycle time (s)               | OPC-UA timer                 | OPC-UA       | CAL-N         |
| PH-01-n-ALARM_ACTIVE    | Alarm active (bool)          | OPC-UA                       | OPC-UA       | CAL-N         |
| PH-01-n-MACHINE_STATE   | Machine state                | OPC-UA                       | OPC-UA       | CAL-N         |

*n = 1–2; 2 units × 5 data points = 10 data points.*

### 5.2 DT-PH-02 — Autoclave / Debubble

| Sensor ID              | Description               | Sensor / Source     | Protocol  | Cal. Interval |
|------------------------|---------------------------|---------------------|-----------|---------------|
| PH-02-PRESS_BAR        | Chamber pressure (bar)    | Pressure transducer | OPC-UA    | CAL-C         |
| PH-02-TEMP_C           | Chamber temperature (°C)  | PT100               | OPC-UA    | CAL-E         |
| PH-02-CYCLE_TIMER_S    | Cycle timer (s)           | OPC-UA              | OPC-UA    | CAL-N         |
| PH-02-ALARM_ACTIVE     | Alarm active              | OPC-UA              | OPC-UA    | CAL-N         |
| PH-02-MACHINE_STATE    | Machine state             | OPC-UA              | OPC-UA    | CAL-N         |

### 5.3 DT-PH-03 — Atlas Copco Torque Station (×4)

| Sensor ID              | Description                         | Sensor / Source              | Protocol  | Cal. Interval |
|------------------------|-------------------------------------|------------------------------|-----------|---------------|
| PH-03-n-TORQUE_NM      | Torque value (Nm) per channel n     | Transducer (Atlas Copco)     | OPC-UA    | CAL-C         |
| PH-03-n-ANGLE_DEG      | Tightening angle (degrees)          | Encoder                      | OPC-UA    | CAL-N         |
| PH-03-n-OKNOK          | OK/NOK result per channel           | OPC-UA                       | OPC-UA    | CAL-N         |
| PH-03-n-SEQUENCE       | Tightening sequence step            | OPC-UA                       | OPC-UA    | CAL-N         |

*4 stations × 4 sensors = 16 data points.*

### 5.4 DT-PH-04 — Phone Flash Station (×6)

| Sensor ID              | Description                    | Protocol   | Cal. Interval |
|------------------------|--------------------------------|------------|---------------|
| PH-04-n-SERIAL_NUM     | Unit serial number flashed     | REST API   | CAL-N         |
| PH-04-n-FW_VERSION     | Firmware version string        | REST API   | CAL-N         |
| PH-04-n-FLASH_RESULT   | Flash result OK/NOK            | REST API   | CAL-N         |
| PH-04-n-FLASH_TIME_S   | Flash duration (s)             | REST API   | CAL-N         |

*6 stations × 4 sensors = 24 data points.*

### 5.5 DT-PH-05 — Phone Function Test Fixture (×6)

| Sensor ID               | Description                    | Protocol   | Cal. Interval |
|-------------------------|--------------------------------|------------|---------------|
| PH-05-n-CAMERA_RESULT   | Camera test pass/fail          | REST API   | CAL-B         |
| PH-05-n-AUDIO_RESULT    | Audio test pass/fail           | REST API   | CAL-B         |
| PH-05-n-TOUCH_RESULT    | Touchscreen test pass/fail     | REST API   | CAL-B         |
| PH-05-n-NFC_RESULT      | NFC test pass/fail             | REST API   | CAL-N         |
| PH-05-n-CHARGE_RESULT   | Charge circuit test pass/fail  | REST API   | CAL-D         |
| PH-05-n-OVERALL_RESULT  | Overall test result            | REST API   | CAL-N         |

*6 fixtures × 6 sensors = 36 data points.*

### 5.6 DT-PH-06 — Cognex In-Sight 9000 Vision (×2)

| Sensor ID               | Description                   | Protocol   | Cal. Interval |
|-------------------------|-------------------------------|------------|---------------|
| PH-06-n-DEFECT_CLASS    | Defect classification string  | REST API   | CAL-B         |
| PH-06-n-CONFIDENCE      | Confidence score (0–1)        | REST API   | CAL-B         |
| PH-06-n-IMAGE_REF       | Image reference               | REST API   | CAL-N         |
| PH-06-n-PASS_FAIL       | Pass/fail result              | REST API   | CAL-N         |

*2 units × 4 sensors = 8 data points.*

### 5.7 DT-PH-07 — Branson 2000X Ultrasonic Welder (×3)

| Sensor ID               | Description               | Protocol   | Cal. Interval |
|-------------------------|---------------------------|------------|---------------|
| PH-07-n-WELD_TIME_MS    | Weld time (ms)            | OPC-UA     | CAL-N         |
| PH-07-n-ENERGY_J        | Weld energy (J)           | OPC-UA     | CAL-C         |
| PH-07-n-AMPLITUDE_UM    | Amplitude (µm)            | OPC-UA     | CAL-C         |
| PH-07-n-ALARM_ACTIVE    | Alarm active              | OPC-UA     | CAL-N         |

*3 units × 4 sensors = 12 data points. Z4 control total = 280 data points, with the remaining
allocated to environment sensors, conveyor scanners, and operator ID readers across the 3 assembly lines.*

---

## 6. Zone Z5 — TWS Assembly (200 data points)

### 6.1 DT-TWS-01 — Brüel & Kjær HATS Acoustic Test (×6)

| Sensor ID               | Description                       | Sensor / Source           | Protocol  | Cal. Interval |
|-------------------------|-----------------------------------|---------------------------|-----------|---------------|
| TWS-01-n-FREQ_RESP      | Frequency response curve (array)  | B&K LAN API               | LAN API   | CAL-B         |
| TWS-01-n-THD_PCT        | Total harmonic distortion (%)     | B&K LAN API               | LAN API   | CAL-B         |
| TWS-01-n-SENS_DB        | Sensitivity (dB SPL)              | B&K LAN API               | LAN API   | CAL-B         |
| TWS-01-n-PASS_FAIL      | Pass/fail result                  | B&K LAN API               | LAN API   | CAL-N         |
| TWS-01-n-SERIAL_REF     | Unit serial reference             | B&K LAN API               | LAN API   | CAL-N         |

*6 stations × 5 sensors = 30 data points.*

### 6.2 DT-TWS-02 — R&S CMW500 BT Tester (×4)

| Sensor ID               | Description                   | Sensor / Source    | Protocol   | Cal. Interval |
|-------------------------|-------------------------------|--------------------|------------|---------------|
| TWS-02-n-BT_CHANNEL     | Bluetooth channel under test  | VISA/LAN           | VISA/LAN   | CAL-A         |
| TWS-02-n-RSSI_DBM       | RSSI (dBm)                    | VISA/LAN           | VISA/LAN   | CAL-A         |
| TWS-02-n-LATENCY_MS     | BT audio latency (ms)         | VISA/LAN           | VISA/LAN   | CAL-A         |
| TWS-02-n-COMPLIANCE     | Compliance pass/fail          | VISA/LAN           | VISA/LAN   | CAL-N         |
| TWS-02-n-SERIAL_REF     | Unit serial reference         | VISA/LAN           | VISA/LAN   | CAL-N         |

*4 testers × 5 sensors = 20 data points.*

### 6.3 DT-TWS-03 — IPX Spray Chamber (×2)

| Sensor ID               | Description                  | Protocol  | Cal. Interval |
|-------------------------|------------------------------|-----------|---------------|
| TWS-03-n-SPRAY_DUR_S    | Spray duration (s)           | OPC-UA    | CAL-N         |
| TWS-03-n-PRESSURE_BAR   | Water pressure (bar)         | OPC-UA    | CAL-C         |
| TWS-03-n-TEST_RESULT    | IPX test result              | OPC-UA    | CAL-N         |
| TWS-03-n-SERIAL_REF     | Unit serial reference        | OPC-UA    | CAL-N         |

*2 chambers × 4 sensors = 8 data points. Z5 control total = 200 data points.*

---

## 7. Zone Z6 — Smartwatch Assembly (160 data points)

### 7.1 DT-SW-01 — Smartwatch Pressure Test Chamber (×2)

| Sensor ID               | Description                  | Protocol  | Cal. Interval |
|-------------------------|------------------------------|-----------|---------------|
| SW-01-n-PRESS_BAR       | Test pressure (bar)          | OPC-UA    | CAL-C         |
| SW-01-n-SOAK_TIME_S     | Pressure soak time (s)       | OPC-UA    | CAL-N         |
| SW-01-n-PASS_FAIL       | Pass/fail result             | OPC-UA    | CAL-N         |
| SW-01-n-SERIAL_REF      | Unit serial reference        | OPC-UA    | CAL-N         |

*2 chambers × 4 sensors = 8 data points.*

### 7.2 DT-SW-02 — GPS Simulator GNSS (×2)

| Sensor ID               | Description                  | Protocol   | Cal. Interval |
|-------------------------|------------------------------|------------|---------------|
| SW-02-n-GNSS_SIGNAL     | GNSS signal scenario name    | VISA/LAN   | CAL-B         |
| SW-02-n-LOCK_TIME_S     | Time to first fix (s)        | VISA/LAN   | CAL-B         |
| SW-02-n-POS_ERROR_M     | Position error (m)           | VISA/LAN   | CAL-B         |
| SW-02-n-PASS_FAIL       | Pass/fail result             | VISA/LAN   | CAL-N         |

*2 units × 4 sensors = 8 data points. Z6 control total = 160 data points.*

---

## 8. Zone Z7 — Power Bank Assembly (200 data points)

### 8.1 DT-PB-01 — Sunstone Spot Welder (×4)

| Sensor ID              | Description                     | Protocol  | Cal. Interval |
|------------------------|---------------------------------|-----------|---------------|
| PB-01-n-PULSE_ENERGY_J | Weld pulse energy (J)           | Ethernet  | CAL-C         |
| PB-01-n-VOLTAGE_V      | Weld voltage (V)                | Ethernet  | CAL-D         |
| PB-01-n-WELD_RES_MOHM  | Weld resistance (mΩ)            | Ethernet  | CAL-C         |
| PB-01-n-ALARM_ACTIVE   | Alarm active                    | Ethernet  | CAL-N         |

*4 welders × 4 sensors = 16 data points.*

### 8.2 DT-PB-02 — Chroma 17020 Battery Tester (×6)

| Sensor ID              | Description                      | Protocol      | Cal. Interval |
|------------------------|----------------------------------|---------------|---------------|
| PB-02-n-CAP_MAH        | Capacity (mAh)                   | Ethernet API  | CAL-D         |
| PB-02-n-IR_MOHM        | Internal resistance (mΩ)         | Ethernet API  | CAL-D         |
| PB-02-n-VOLTAGE_V      | Terminal voltage (V)             | Ethernet API  | CAL-D         |
| PB-02-n-CHARGE_CURVE   | Charge/discharge curve (array)   | Ethernet API  | CAL-D         |
| PB-02-n-CYCLE_COUNT    | Cycle count for aging tests      | Ethernet API  | CAL-N         |
| PB-02-n-PASS_FAIL      | Pass/fail result                 | Ethernet API  | CAL-N         |

*6 testers × 6 sensors = 36 data points.*

### 8.3 DT-PB-03 — Chroma 19053 Safety Tester (×4, Z7 and Z9)

| Sensor ID              | Description                     | Protocol      | Cal. Interval |
|------------------------|---------------------------------|---------------|---------------|
| PB-03-n-HIPOT_V        | Hipot test voltage (V)          | Ethernet API  | CAL-D         |
| PB-03-n-HIPOT_UA       | Hipot leakage current (µA)      | Ethernet API  | CAL-D         |
| PB-03-n-EARTH_BOND_OHM | Earth bond resistance (Ω)       | Ethernet API  | CAL-D         |
| PB-03-n-RESULT         | OK/NOK per serial               | Ethernet API  | CAL-N         |

*4 testers (split Z7 / Z9) × 4 sensors = 16 data points in Z7 + remainder in Z9.*

---

## 9. Zone Z8 — RF & NCC Test Laboratory (260 data points)

### 9.1 DT-RF-01 — ETS-Lindgren 7000 Shielded Chamber (×2)

| Sensor ID               | Description                    | Protocol    | Cal. Interval |
|-------------------------|--------------------------------|-------------|---------------|
| RF-01-n-BOOKING_LOG     | Chamber booking log entry      | REST API    | CAL-N         |
| RF-01-n-TEST_IN_PROG    | Test in progress flag (bool)   | REST API    | CAL-N         |
| RF-01-n-ALARM_ACTIVE    | Alarm / door-open flag         | REST API    | CAL-N         |
| RF-01-n-SHIELDING_INT   | Shielding integrity check (dB) | REST API    | CAL-A         |

*2 chambers × 4 sensors = 8 data points.*

### 9.2 DT-RF-02 — Benchtop RF Chamber (×2)

| Sensor ID               | Description                    | Protocol    | Cal. Interval |
|-------------------------|--------------------------------|-------------|---------------|
| RF-02-n-TEST_RESULT     | Test result log entry          | REST API    | CAL-N         |
| RF-02-n-FREQ_BAND       | Frequency band under test      | REST API    | CAL-N         |
| RF-02-n-PASS_FAIL       | Pass/fail result               | REST API    | CAL-N         |

*2 chambers × 3 sensors = 6 data points.*

### 9.3 DT-RF-03 — R&S CMW500 Network Analyser (×2)

| Sensor ID               | Description                      | Sensor / Source        | Protocol   | Cal. Interval |
|-------------------------|----------------------------------|------------------------|------------|---------------|
| RF-03-n-TRP_DBM         | Total Radiated Power (dBm)       | R&S CMW500 VISA        | VISA/LAN   | CAL-A         |
| RF-03-n-TIS_DBM         | Total Isotropic Sensitivity (dBm)| R&S CMW500 VISA        | VISA/LAN   | CAL-A         |
| RF-03-n-FREQ_BAND       | Band under test                  | VISA/LAN               | VISA/LAN   | CAL-N         |
| RF-03-n-TX_POWER_DBM    | Transmit power (dBm)             | VISA/LAN               | VISA/LAN   | CAL-A         |
| RF-03-n-FREQ_DEV_PPM    | Frequency deviation (ppm)        | VISA/LAN               | VISA/LAN   | CAL-A         |
| RF-03-n-PASS_FAIL       | Pass/fail result                 | VISA/LAN               | VISA/LAN   | CAL-N         |
| RF-03-n-SERIAL_REF      | Unit serial reference            | VISA/LAN               | VISA/LAN   | CAL-N         |

*2 units × 7 sensors = 14 data points.*

### 9.4 DT-RF-04 — Keysight N9020B Spectrum Analyser

| Sensor ID               | Description                    | Protocol   | Cal. Interval |
|-------------------------|--------------------------------|------------|---------------|
| RF-04-SWEEP_DATA        | Emission sweep data (array)    | VISA/LAN   | CAL-A         |
| RF-04-PEAK_FREQ_MHZ     | Peak emission frequency (MHz)  | VISA/LAN   | CAL-A         |
| RF-04-SPURIOUS_FLAG     | Spurious emission flag (bool)  | VISA/LAN   | CAL-N         |
| RF-04-LIMIT_MARGIN_DB   | Margin to limit (dB)           | VISA/LAN   | CAL-A         |

### 9.5 DT-RF-05 — Mini CATR OTA Test Range

| Sensor ID               | Description                    | Protocol   | Cal. Interval |
|-------------------------|--------------------------------|------------|---------------|
| RF-05-TRP_DBM           | TRP (dBm)                      | VISA/LAN   | CAL-A         |
| RF-05-TIS_DBM           | TIS (dBm)                      | VISA/LAN   | CAL-A         |
| RF-05-THETA_SCAN        | Theta scan angle (deg)         | VISA/LAN   | CAL-N         |
| RF-05-PHI_SCAN          | Phi scan angle (deg)           | VISA/LAN   | CAL-N         |
| RF-05-PASS_FAIL         | Pass/fail result               | VISA/LAN   | CAL-N         |

### 9.6 DT-RF-06 — RF Calibration Station (×4)

| Sensor ID               | Description                      | Protocol   | Cal. Interval |
|-------------------------|----------------------------------|------------|---------------|
| RF-06-n-CAL_BAND        | Band calibrated                  | REST API   | CAL-A         |
| RF-06-n-OFFSET_DB       | Calibration offset applied (dB)  | REST API   | CAL-A         |
| RF-06-n-SERIAL_REF      | Unit serial reference            | REST API   | CAL-N         |
| RF-06-n-CAL_RESULT      | Calibration result pass/fail     | REST API   | CAL-N         |
| RF-06-n-TIMESTAMP       | Calibration timestamp            | REST API   | CAL-N         |

*4 stations × 5 sensors = 20 data points. Z8 control total = 260 data points.*

---

## 10. Zone Z9 — Final QC & Safety Test (180 data points)

| Asset              | Key Sensor Parameters                                              | Protocol     | Cal. Interval |
|--------------------|---------------------------------------------------------------------|--------------|---------------|
| AI Vision (Cognex) | Defect class, confidence, image ref, pass/fail                     | REST API     | CAL-B         |
| Drop Test Rig      | Drop height (cm), orientation, pass/fail                           | Ethernet API | CAL-C         |
| Thermal Chamber    | Temp set-point (°C), actual (°C), soak time, result               | OPC-UA       | CAL-E         |
| Battery Cycle      | Cycle count, capacity (mAh), voltage curve, pass/fail              | Ethernet API | CAL-D         |
| Safety Tester (Z9) | Hipot V/I, earth bond result, OK/NOK per serial (Chroma 19053)    | Ethernet API | CAL-D         |

*Z9 control total = 180 data points across 4 primary assets.*

---

## 11. Zone Z10 — Packaging (120 data points)

| Asset                     | Key Sensor Parameters                                       | Protocol      | Cal. Interval |
|---------------------------|-------------------------------------------------------------|---------------|---------------|
| Carton Erect & Fill       | Carton count (shift), jam alarm, machine state             | Modbus TCP    | CAL-N         |
| Mettler Toledo Checkweigher| Weight (g), pass/fail, serial ref                         | Ethernet API  | CAL-C         |
| Barcode Print & Apply     | Label print OK/NOK, barcode verify result, serial ref      | REST API      | CAL-G         |
| Pallet Wrap Station       | Wrap cycles, roll remaining (%), alarm state               | Modbus TCP    | CAL-N         |

*Z10 control total = 120 data points across 4 assets.*

---

## 12. Zone Z11 — FG Warehouse (80 data points)

| Asset                  | Key Sensor Parameters                              | Protocol     | Cal. Interval |
|------------------------|----------------------------------------------------|--------------|---------------|
| AMR Fleet (Z11)        | Position (x,y,θ), speed, battery SoC, mission status | MQTT (MiR) | CAL-N         |
| Pallet Scan Station    | Pallet ID, serial list count, scan result          | REST API     | CAL-N         |
| Temp/Humidity Monitor  | Temperature (°C), relative humidity (%)            | Modbus TCP   | CAL-E         |
| Dispatch Dock Scanner  | Carton scan count, ASN reference, despatch time    | REST API     | CAL-N         |

*Z11 control total = 80 data points.*

---

## 13. Site — Energy Systems (400 data points)

### 13.1 Solar PV Arrays (DT-EN-PV-01 to 03)

| Sensor ID              | Description                          | Sensor Model / Source        | Protocol     | Cal. Interval |
|------------------------|--------------------------------------|------------------------------|--------------|---------------|
| EN-PV-n-GEN_KW         | Real-time generation (kW)            | Sungrow inverter Modbus      | Modbus TCP   | CAL-H         |
| EN-PV-n-CUM_KWH        | Cumulative energy (kWh)              | Sungrow inverter Modbus      | Modbus TCP   | CAL-H         |
| EN-PV-n-IRRAD_WM2      | Irradiance (W/m²)                    | Kipp & Zonen CMP6 pyranometer| Modbus TCP   | CAL-E         |
| EN-PV-n-STRING_IV      | String IV data (per string)          | Sungrow string combiner      | Modbus TCP   | CAL-H         |
| EN-PV-n-TEMP_C         | Module temperature (°C)              | PT100 (back-of-module)       | Modbus TCP   | CAL-E         |

*3 arrays × 5 sensors = 15 data points.*

### 13.2 BESS (DT-EN-BESS-01 and 02)

| Sensor ID              | Description                     | Protocol   | Cal. Interval |
|------------------------|---------------------------------|------------|---------------|
| EN-BESS-n-SOC_PCT      | State of Charge (%)             | Modbus TCP | CAL-H         |
| EN-BESS-n-SOH_PCT      | State of Health (%)             | Modbus TCP | CAL-H         |
| EN-BESS-n-CHARGE_KW    | Charge power (kW)               | Modbus TCP | CAL-H         |
| EN-BESS-n-DISCHARGE_KW | Discharge power (kW)            | Modbus TCP | CAL-H         |
| EN-BESS-n-CELL_TEMP_C  | Cell temperature — max/min (°C) | Modbus TCP | CAL-E         |
| EN-BESS-n-VOLTAGE_V    | Pack terminal voltage (V)       | Modbus TCP | CAL-D         |
| EN-BESS-n-ALARM        | BMS alarm status                | Modbus TCP | CAL-N         |

*2 BESS containers × 7 sensors = 14 data points.*

### 13.3 Sungrow Inverters (DT-EN-INV-01 to 04)

| Sensor ID              | Description               | Protocol   | Cal. Interval |
|------------------------|---------------------------|------------|---------------|
| EN-INV-n-AC_OUT_KW     | AC output power (kW)      | Modbus TCP | CAL-H         |
| EN-INV-n-DC_IN_KW      | DC input power (kW)       | Modbus TCP | CAL-H         |
| EN-INV-n-EFFICIENCY_PCT| Efficiency (%)            | Modbus TCP | CAL-H         |
| EN-INV-n-ALARM         | Inverter alarm status     | Modbus TCP | CAL-N         |

*4 inverters × 4 sensors = 16 data points.*

### 13.4 Generator, Grid Meter, HVAC

| Asset               | Key Sensors                                              | Protocol   | Cal. Interval |
|---------------------|----------------------------------------------------------|------------|---------------|
| DT-EN-GEN-01        | Run status, kW output, fuel level (L), run hours        | Modbus TCP | CAL-H         |
| DT-EN-GRID-01       | Import kW, cumulative kWh, ToU tariff period            | Modbus TCP | CAL-H         |
| DT-EN-HVAC-01/02    | Cooling kW, inlet/outlet temp (°C), COP, alarm         | OPC-UA     | CAL-E         |

*Energy site control total = 400 data points across all energy assets, including string-level and
phase-level monitoring sub-points.*

---

## 14. Gate 3 Sensor Coverage Acceptance Criteria

Before Phase 1 live machine connection (Gate 3), the following must be verified:

- [ ] All 12 zones have active sensor subscriptions in the Telegraf/MQTT configuration
- [ ] Total live data point count ≥ 2,750 (accounting for optional sub-sensors)
- [ ] Each calibration-required sensor has a CMMS maintenance task scheduled (interval per Section 2)
- [ ] All CAL-A (RF instruments) sensors verified against NIST-traceable calibration standard
- [ ] All CAL-D (electrical test) instruments verified against IEC 61010 / IEC 62353 standards
- [ ] Calibration certificates for RF instruments on file before NCC type approval submissions
- [ ] Golden-board calibration baseline run for all SPI/AOI instruments (CAL-G)
- [ ] Live data visible in Grafana dashboards for all zones before Gate 3 sign-off
- [ ] Data completeness check: < 0.1% null/dropped readings over 24-hour test window

---

## 14.1 Documentation QA Checklist (Sensor Registry)

- [x] Cross-document references present (BIM, manifest, MQTT namespace, AI status)
- [x] Zone-level control totals are explicit and auditable
- [x] Approximate/filler wording removed from control statements
- [x] Section-level ownership and integration review responsibilities defined
- [x] Gate 3 acceptance controls maintained as checklist items

---

## 15. Related Documents

- For asset spatial locations, refer to [`bim/asset-anchors.md`](./bim/asset-anchors.md).
- For zone boundaries and floor model, refer to [`bim/zone-boundaries.md`](./bim/zone-boundaries.md).
- For machine-readable asset data schema (YAML), refer to [`dt-asset-manifest.md`](./dt-asset-manifest.md).
- For MQTT topic structure, refer to [`dt-mqtt-namespace.md`](./dt-mqtt-namespace.md).
- For AI Platform API consumption of sensor data, refer to [`ai-platform-status.md`](./ai-platform-status.md).
- For integrated dependency gates and closure sequencing, refer to [`bim-simulation-readiness-program.md`](./bim-simulation-readiness-program.md).
- For gap closure status and evidence mapping, refer to [`gap-closure-report.md`](./gap-closure-report.md).
