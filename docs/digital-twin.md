# Personal Electronics Factory — Digital Twin Architecture

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1
> **Document Version:** 1.0 | **Owner:** Digital Manufacturing & AI Team

---

## 1. Digital Twin Overview

The Coo-Cah Personal Electronics Factory Digital Twin is a live, synchronised virtual model of the factory's physical production environment. It ingests real-time data from machines, AMRs, energy systems, and quality test stations via the Coo-Cah MES and AI Platform. The digital twin enables simulation, root-cause analysis, and predictive optimisation without disrupting live production.

| Parameter                        | Value                                                        |
|----------------------------------|--------------------------------------------------------------|
| Digital Twin Platform            | Coo-Cah AI Platform — Digital Twin Module                   |
| Data Synchronisation Latency     | ≤ 1 second (real-time streaming via MQTT)                   |
| Asset Count (Phase 1)            | 142 registered physical assets                              |
| Sensor Integration Points        | ~2,800 data points (energy, temperature, motion, QC, AMR)  |
| Simulation Framework             | Discrete-event simulation (DES) + process physics models    |
| 3D Spatial Model                 | BIM-linked 3D model of 18,000 m² floor                     |
| Cloud Platform                   | Coo-Cah Platform (Lagos DC) + on-site edge nodes            |
| Phase 2 Expansion                | Cobot kinematics models; AI vision inference twin           |

---

## 2. Asset Registry

### 2.1 SMT & PCB Processing Assets

| Asset ID          | Asset Name                      | Location  | Sensors / Data Points                               | DT Status  |
|-------------------|---------------------------------|-----------|-----------------------------------------------------|------------|
| DT-SMT-L1-01      | DEK Horizon Printer (L1)        | Z2 SMT L1 | Print recipe, paste volume, stencil life, alarm     | Phase 1    |
| DT-SMT-L1-02      | Koh Young SPI KY8030-3 (L1)    | Z2 SMT L1 | 3D paste volume, CPK, defect count, board ID       | Phase 1    |
| DT-SMT-L1-03      | JUKI FX-3R Pick-and-Place (L1) | Z2 SMT L1 | CPH, feeder errors, nozzle state, placement count   | Phase 1    |
| DT-SMT-L1-04      | JUKI RX-7 Pick-and-Place (L1)  | Z2 SMT L1 | CPH, feeder errors, placement accuracy trend        | Phase 1    |
| DT-SMT-L1-05      | Heller 1964 MK5 Reflow (L1)    | Z2 SMT L1 | Zone temps ×8, conveyor speed, N₂ level, alarms    | Phase 1    |
| DT-SMT-L1-06      | Koh Young Zenith AOI (L1)      | Z2 SMT L1 | Defect codes, images, FPY per board, alarm          | Phase 1    |
| DT-SMT-L1-07      | Unicomp AX8200 X-Ray (L1)      | Z2 SMT L1 | BGA void analysis per board, image, pass/fail       | Phase 1    |
| DT-SMT-L1-08      | Ersa Versaflow Selective Solder (L1) | Z2   | Flux level, solder level, nozzle temp, recipe       | Phase 1    |
| DT-SMT-L1-09      | Keysight I1000D ICT (L1)       | Z2 SMT L1 | Net test pass/fail, shorts/opens count, fixture ID  | Phase 1    |
| DT-SMT-L1-10      | PCB Depanelling Router (L1)    | Z2 SMT L1 | Cycle count, spindle speed, alarm state             | Phase 1    |
| DT-SMT-L2-01 to 10| SMT Line 2 (identical set)     | Z3 SMT L2 | Same data points as L1 equivalents                 | Phase 1    |

### 2.2 Phone Assembly Assets

| Asset ID          | Asset Name                          | Location | Sensors / Data Points                               | DT Status  |
|-------------------|-------------------------------------|----------|-----------------------------------------------------|------------|
| DT-PH-01          | Screen Bonding Machine (Z4) ×2      | Z4       | Vacuum level, OCA press force, cycle time, alarm    | Phase 1    |
| DT-PH-02          | Autoclave / Debubble (Z4)           | Z4       | Pressure, temperature, cycle timer, alarm           | Phase 1    |
| DT-PH-03          | Atlas Copco Torque Station ×4       | Z4       | Torque value per channel, angle, OK/NOK, sequence   | Phase 1    |
| DT-PH-04          | Phone Flash Station ×6              | Z4       | Serial number, firmware version, flash result, time | Phase 1    |
| DT-PH-05          | Phone Function Test Fixture ×6      | Z4       | Per-test result (camera, audio, touch, NFC, charge) | Phase 1    |
| DT-PH-06          | Cognex In-Sight 9000 Vision ×2      | Z4/Z9    | Defect class, confidence score, image ref, pass/fail| Phase 1    |
| DT-PH-07          | Ultrasonic Welder (Branson 2000X) ×3| Z4       | Weld time, energy, amplitude, alarm state           | Phase 1    |

### 2.3 TWS, Watch & Power Bank Assets

| Asset ID       | Asset Name                          | Location | Sensors / Data Points                               | DT Status  |
|----------------|-------------------------------------|----------|-----------------------------------------------------|------------|
| DT-TWS-01      | Brüel & Kjær HATS Acoustic Test ×6  | Z5       | Freq response, THD, sensitivity dB, pass/fail      | Phase 1    |
| DT-TWS-02      | R&S CMW500 BT Test ×4              | Z5/Z8    | BT channel, RSSI, latency, compliance pass/fail     | Phase 1    |
| DT-TWS-03      | IPX Spray Chamber ×2                | Z5       | Spray duration, pressure, test result              | Phase 1    |
| DT-SW-01       | Smartwatch Pressure Test Chamber ×2 | Z6       | Pressure bar, soak time, pass/fail                  | Phase 1    |
| DT-SW-02       | GPS Simulator (GNSS) ×2             | Z6/Z8    | GNSS signal replay, lock time, position error       | Phase 1    |
| DT-PB-01       | Sunstone Spot Welder ×4             | Z7       | Pulse energy, voltage, weld resistance, alarm       | Phase 1    |
| DT-PB-02       | Chroma 17020 Battery Tester ×6      | Z7       | Capacity mAh, IR mΩ, voltage curve, cycle count     | Phase 1    |
| DT-PB-03       | Chroma 19053 Safety Tester ×4       | Z7/Z9    | Hipot V/I, earth bond result, OK/NOK per serial     | Phase 1    |

### 2.4 RF & NCC Test Lab Assets

| Asset ID       | Asset Name                            | Location | Sensors / Data Points                               | DT Status  |
|----------------|---------------------------------------|----------|-----------------------------------------------------|------------|
| DT-RF-01       | ETS-Lindgren 7000 Chamber ×2          | Z8       | Chamber booking log, test in progress flag, alarm   | Phase 1    |
| DT-RF-02       | Benchtop RF Chamber ×2                | Z8       | Test result log, frequency band, pass/fail          | Phase 1    |
| DT-RF-03       | R&S CMW500 Network Analyser ×2        | Z8       | RF test parameters, TRP, TIS, band, result         | Phase 1    |
| DT-RF-04       | Keysight N9020B Spectrum Analyser     | Z8       | Emission sweep data, peak frequency, flag           | Phase 1    |
| DT-RF-05       | Mini CATR OTA Test Range              | Z8       | TRP dBm, TIS dBm, theta/phi scan, pass/fail         | Phase 1    |
| DT-RF-06       | RF Calibration Station ×4             | Z4/Z5/Z6 | Cal result per band, offset applied, serial, time  | Phase 1    |

### 2.5 AMR Fleet Assets

| Asset ID           | Asset Name                  | Fleet Role        | Sensors / Data Points                               | DT Status |
|--------------------|-----------------------------|-------------------|-----------------------------------------------------|-----------|
| DT-AMR-MIR250-01 to 12 | MiR250 Transport AMR ×12 | Main transport  | Position (x,y,θ), speed, payload weight, battery SoC, mission status | Phase 1 |
| DT-AMR-MIR100-01 to 04 | MiR100 Goods-to-Person ×4| Component kitting| Position, speed, battery SoC, mission status        | Phase 1   |
| DT-AMR-DOCK-01 to 18  | AMR Charging Docks ×18    | Charging         | Dock occupied (T/F), AMR ID, charge current, SoC    | Phase 1   |

### 2.6 Energy System Assets

| Asset ID       | Asset Name                        | Location       | Sensors / Data Points                               | DT Status  |
|----------------|-----------------------------------|----------------|-----------------------------------------------------|------------|
| DT-EN-PV-01    | Solar PV Array — Roof Main (620 kWp) | Factory Roof | Real-time generation kW, cumulative kWh, panel string IV, irradiance | Phase 1 |
| DT-EN-PV-02    | Solar PV Array — Warehouse (110 kWp) | Warehouse Roof| Real-time generation kW, cumulative kWh, irradiance  | Phase 1   |
| DT-EN-PV-03    | Solar PV Array — Ground (120 kWp)  | East Yard      | Real-time generation kW, temp, irradiance           | Phase 1    |
| DT-EN-BESS-01  | LFP BESS Container 1 (450 kWh)    | North Yard     | SoC%, SoH%, charge/discharge kW, cell temps, voltage | Phase 1   |
| DT-EN-BESS-02  | LFP BESS Container 2 (450 kWh)    | North Yard     | SoC%, SoH%, charge/discharge kW, cell temps, voltage | Phase 1   |
| DT-EN-INV-01 to 04| Sungrow SH250HX Inverters ×4  | Inverter Room  | AC output kW, DC input kW, efficiency, alarm        | Phase 1    |
| DT-EN-GEN-01   | Perkins 500 kVA Generator         | NE Corner      | Running status, kW output, fuel level L, run hours  | Phase 1    |
| DT-EN-GRID-01  | Grid Supply Meter (AMI)           | HV Substation  | Import kW, cumulative kWh, ToU tariff period        | Phase 1    |
| DT-EN-HVAC-01/02 | Carrier Chillers ×2             | Utility Room   | Cooling kW, inlet/outlet temp, COP, alarm           | Phase 1    |

---

## 3. Sensor Coverage Map

### 3.1 Zone-Level Sensor Density

| Zone | Zone Name             | Assets Monitored | Data Points | Primary Sensor Types                              |
|------|-----------------------|-----------------|-------------|---------------------------------------------------|
| Z2   | SMT Line 1            | 10              | 420         | Temperature, pressure, SECS/GEM, OPC-UA, vision  |
| Z3   | SMT Line 2            | 10              | 420         | Temperature, pressure, SECS/GEM, OPC-UA, vision  |
| Z4   | Phone Assembly        | 8               | 280         | Torque, vision, flash/test results, barcode scan  |
| Z5   | TWS Assembly          | 6               | 200         | Acoustic, RF, ultrasonic weld, IPX test           |
| Z6   | Smartwatch Assembly   | 5               | 160         | Pressure, GPS sim, OCA laminator, flash results   |
| Z7   | Power Bank Assembly   | 6               | 200         | Spot weld energy, battery test data, safety test  |
| Z8   | RF & NCC Lab          | 6               | 260         | RF parameters (TRP/TIS), spectrum, chamber status |
| Z9   | Final QC              | 4               | 180         | AI vision, drop/thermal, battery cycle, safety    |
| Z10  | Packaging             | 4               | 120         | Weight, barcode, label print, carton count        |
| Z11  | FG Warehouse          | 4               | 80          | AMR position, pallet scan, temperature, humidity  |
| Z1   | Stores                | 4               | 80          | VLM pick count, inventory level, temperature      |
| Site | Energy Systems        | 12              | 400         | Power (kW/kWh), SoC, temp, generation, fuel       |

---

## 4. Digital Twin Simulation Use Cases

### 4.1 Production Simulation

| Use Case                                 | Description                                                             | Business Value                          |
|------------------------------------------|-------------------------------------------------------------------------|-----------------------------------------|
| Production Ramp Simulation               | Simulate ramp from 500k to 1M phones/year; identify bottleneck stations | Reduces ramp risk; faster time to volume|
| SMT Line Changeover Optimisation         | Model optimal feeder change + recipe switch sequence                    | Reduces changeover time by est. 20–30% |
| WIP Flow Balancing                       | Simulate queue build-up; identify starvation points across assembly     | Maintains takt time; reduces idle time  |
| Product Mix Scenario Planning            | Model factory OEE for different phone vs. earbud vs. watch ratios      | Supports monthly production planning    |
| New Product Introduction (NPI) Simulation | Simulate cycle time and yield before physical first article runs       | Reduces NPI cost and time               |

### 4.2 Predictive Maintenance Simulation

| Use Case                                 | Description                                                             | Business Value                          |
|------------------------------------------|-------------------------------------------------------------------------|-----------------------------------------|
| Reflow Oven Thermal Degradation Model    | Track heating element current draw vs. age; predict element failure    | Avoid unplanned SMT downtime            |
| JUKI P&P Feeder Vibration Model          | Monitor feeder vibration signature; flag feeder wear before miss-pick   | Maintain SMT FPY ≥ 97%                 |
| AMR Battery End-of-Life Prediction       | Monitor SoH trend; predict AMR battery replacement window              | Maintain AMR availability ≥ 98%        |
| BESS State-of-Health Modelling           | Compare BESS capacity fade to electrochemical model; project SoH at 5yr | Plan BESS replacement at optimal time  |

### 4.3 Energy Optimisation Simulation

| Use Case                                 | Description                                                             | Business Value                          |
|------------------------------------------|-------------------------------------------------------------------------|-----------------------------------------|
| BESS Dispatch Optimisation               | Simulate optimal BESS charge/discharge schedule vs. solar forecast + ToU | Minimise grid cost; maximise solar self-consumption |
| Factory Load Shift                       | Identify deferrable loads (e.g., AMR charging) to shift off-peak       | Reduce grid import; flatten demand curve|
| Solar Soiling Loss Modelling             | Compare actual vs. expected yield; flag underperforming panel strings   | Optimise cleaning schedule              |
| Generator Run Minimisation               | Simulate scenarios to reduce diesel generator run hours below 100/year  | Lower OpEx; lower emissions             |

### 4.4 Quality & Compliance Simulation

| Use Case                                 | Description                                                             | Business Value                          |
|------------------------------------------|-------------------------------------------------------------------------|-----------------------------------------|
| SMT Solder Paste CPK Drift Model         | Track CPK trend; predict process drift before excursion                | Maintain SMT SPC control                |
| NCC RF Test Sample Yield Prediction      | Model RF calibration yield per shift based on incoming component spread | Reduce NCC re-test volume               |
| Cosmetic Defect Root Cause (AI)          | Correlate AI vision defect codes with upstream assembly parameters     | Reduce cosmetic escapes to ≤ 200 PPM   |

---

## 5. Digital Twin Maturity Roadmap

| Phase | Period    | Maturity Level        | Capabilities Added                                            |
|-------|-----------|-----------------------|---------------------------------------------------------------|
| 1     | 2025–2026 | Descriptive Twin      | Real-time machine state, WIP tracking, energy monitoring, NCC log |
| 2     | 2027–2028 | Diagnostic + Predictive | Cobot kinematics model, AI vision inference twin, pred. maintenance |
| 3     | 2029–2030 | Prescriptive Twin     | Fully autonomous schedule recommendation; lights-out SMT simulation |

---

## 6. Data Governance for Digital Twin

| Requirement                     | Implementation                                                    |
|---------------------------------|-------------------------------------------------------------------|
| Data Ownership                  | All digital twin data owned by Coo-Cah Group; not shared with third parties without consent |
| Intellectual Property           | Machine learning models and simulation outputs are Coo-Cah proprietary IP |
| Data Retention                  | Real-time data: 90 days in edge cache; aggregated data: 10 years in cloud |
| Access Control                  | Role-based: Operator (read only), Engineer (simulate), Admin (configure) |
| Export / API Access             | REST API available for approved Coo-Cah cross-factory integrations only |
| Audit Trail                     | All simulation runs logged with user ID, input parameters, output summary |

---

*For MES data architecture and machine integration protocols, refer to [`mes-integration.md`](./mes-integration.md).*
*For automation milestones that expand the digital twin scope, refer to [`automation-roadmap.md`](./automation-roadmap.md).*
*For energy system monitoring details, refer to [`energy-profile.md`](./energy-profile.md).*
