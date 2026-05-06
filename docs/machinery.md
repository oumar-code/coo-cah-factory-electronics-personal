# Personal Electronics Factory — Machinery & Equipment Register

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1
> **Document Version:** 1.0 | **Owner:** Factory Engineering Team

---

## 1. Introduction

This document provides the complete equipment register for the Coo-Cah Personal Electronics Factory. The factory operates two full SMT (Surface Mount Technology) production lines, four product assembly lines (phones, TWS earbuds, smartwatches, and power banks), a dedicated RF and NCC type test laboratory, and a comprehensive QC suite. All FA/AI-level equipment integrates with the Coo-Cah MES via OPC-UA or MQTT.

**Automation Level Legend:**

| Code | Level              | Description                                                    |
|------|--------------------|----------------------------------------------------------------|
| M    | Manual             | Operated entirely by human; no automation                      |
| SA   | Semi-Automated     | Machine performs primary action; human loads/unloads or monitors |
| A    | Automated          | Machine operates autonomously within its cycle; minimal human supervision |
| FA   | Fully Automated    | End-to-end autonomous operation; integrated with MES; self-alarming |
| AI   | AI-Augmented       | Machine data processed by Coo-Cah AI Platform for optimisation or prediction |

---

## 2. SMT Line 1 — Smartphone & Feature Phone PCBs

SMT Line 1 is the primary PCB assembly line producing all main boards for smartphones, feature phones, and power bank control boards. It operates on a 2-shift basis and is fully integrated into the Coo-Cah MES.

| # | Equipment                           | Qty | Spec / Model                                  | Purpose                                                         | Auto Level |
|---|-------------------------------------|-----|-----------------------------------------------|-----------------------------------------------------------------|------------|
| 1 | Solder Paste Screen Printer         | 1   | DEK Horizon 02i (or MPM Momentum II)          | Deposits solder paste on PCB pads via laser-cut stencil         | FA         |
| 2 | SPI — Solder Paste Inspection       | 1   | Koh Young KY8030-3                            | 3D post-print paste volume and alignment inspection             | FA/AI      |
| 3 | Pick-and-Place (High Speed)         | 1   | JUKI FX-3R (45,000 CPH)                      | High-speed placement of 0402+ passives and ICs on phone boards  | FA/AI      |
| 4 | Pick-and-Place (Flexible / Odd-Form)| 1   | JUKI RX-7 (or Fuji NXT III M3)               | Connectors, camera modules, SIM connectors, shielding cans      | FA         |
| 5 | Reflow Oven                         | 1   | Heller 1964 MK5 (8-zone nitrogen-capable)     | Lead-free reflow soldering (SAC305 profile); smartphone BGA/QFN | FA/AI      |
| 6 | AOI — Automated Optical Inspection  | 1   | Koh Young Zenith (3D AOI)                    | Post-reflow defect detection: bridges, tombstones, missing parts | FA/AI      |
| 7 | Selective Soldering Machine         | 1   | Ersa Versaflow 4/55                          | Through-hole connectors, USB ports, antenna connectors on PCBs  | A          |
| 8 | In-Circuit Test (ICT) System        | 1   | Keysight I1000D                              | PCB net electrical test; shorts, opens, component values        | SA/AI      |
| 9 | Flying Probe Tester                 | 1   | Spea 4040 (or Takaya APT-1400F)              | NPI and low-volume board test — no dedicated fixture needed      | A          |
| 10| PCB Depanelling Router              | 1   | LPKF ProtoLaser S4 or Jyy JV-3E              | Separates individual phone mainboards from production panels     | A          |
| 11| SMT Conveyor (ESD-safe)             | 1   | SMEMA-compatible, ESD belt, variable speed    | Links all SMT Line 1 stations in production flow                | FA         |
| 12| PCB Magazine Loader/Unloader        | 2   | SMEMA auto loader (OEM compatible)           | Auto-feeds bare PCB panels and offloads populated boards         | FA         |
| 13| Rework Station                      | 2   | JBC HDE-9B (BGA hot-air, IR pre-heat)        | Manual rework for SMT defects; BGA reballing for smartphones     | M          |
| 14| Stencil Cleaner                     | 1   | DEK ProCleaner Plus                          | Automated SMT stencil cleaning between production runs           | A          |
| 15| X-Ray Inspection System             | 1   | Unicomp AX8200 (or Yxlon FF20 CT)           | BGA solder joint inspection — hidden joints on phone SoC/RAM     | A/AI       |

---

## 3. SMT Line 2 — TWS, Smartwatch & Accessory PCBs

SMT Line 2 is a second full SMT line with an identical equipment profile to Line 1, dedicated to the smaller and denser PCBs used in TWS earbuds, smartwatches, and USB-C hub controllers. It is configured for smaller panel sizes and fine-pitch components.

| # | Equipment                           | Qty | Spec / Model                                  | Purpose                                                         | Auto Level |
|---|-------------------------------------|-----|-----------------------------------------------|-----------------------------------------------------------------|------------|
| 1 | Solder Paste Screen Printer         | 1   | DEK Horizon 02i (fine-pitch stencil)          | Solder paste for TWS/watch boards; 0.3mm pitch BGA              | FA         |
| 2 | SPI — Solder Paste Inspection       | 1   | Koh Young KY8030-3                            | 3D paste inspection for fine-pitch TWS chip pads                | FA/AI      |
| 3 | Pick-and-Place (High Speed)         | 1   | JUKI FX-3R (45,000 CPH)                      | Tiny passives (01005), BT SoC, MEMS microphones on TWS boards   | FA/AI      |
| 4 | Pick-and-Place (Flexible)           | 1   | JUKI RX-7                                    | Larger ICs, connectors, sensors, battery management chips       | FA         |
| 5 | Reflow Oven                         | 1   | Heller 1964 MK5 (8-zone)                     | Lead-free reflow for watch and TWS boards; tighter profiles      | FA/AI      |
| 6 | AOI — Automated Optical Inspection  | 1   | Koh Young Zenith (3D AOI)                    | Post-reflow QC for TWS / watch boards                           | FA/AI      |
| 7 | Micro-Selective Soldering           | 1   | Ersa Versaflow 3/45 (small nozzle set)        | Through-hole antenna + speaker connectors on watch PCBs         | A          |
| 8 | Flying Probe Tester                 | 1   | Takaya APT-1400F                             | Flexible PCB testing for TWS flex circuits                      | A          |
| 9 | PCB Depanelling Router              | 1   | LPKF Contour Router S                        | Separates small TWS/watch PCB panels                            | A          |
| 10| SMT Conveyor (ESD-safe, narrow)     | 1   | SMEMA-compatible, narrow belt (50mm to 400mm) | Handles small-format TWS and watch PCB panels                   | FA         |
| 11| Rework Station (fine-pitch)         | 2   | JBC HDE-9B + micro hot-air nozzle set        | Rework of 01005 / 0.3mm pitch defects on wearable boards        | M          |
| 12| UV Curing Oven                      | 1   | Dymax BlueWave 75 (conveyor UV)              | Cures UV-adhesive underfill on shock-sensitive wearable chips    | A          |

---

## 4. Phone Assembly Lines

Three parallel phone assembly lines: Line PH-1 (Feature Phones), Line PH-2 (Budget Smartphone), Line PH-3 (Mid Smartphone). Lines PH-2 and PH-3 share tooling where model variants allow.

| # | Equipment                                 | Qty | Spec / Model                                 | Purpose                                                         | Auto Level |
|---|-------------------------------------------|-----|----------------------------------------------|-----------------------------------------------------------------|------------|
| 1 | Screen Bonding Machine                    | 2   | Goman GM-90A (vacuum OCA bonding)            | Bonds display glass to touch panel with optical clear adhesive  | SA/A       |
| 2 | Autoclave (OCA Debubble)                  | 1   | Goman GDA-A60 (80°C, 6 bar)                 | Removes micro-bubbles from OCA bond — critical for screen QC    | A          |
| 3 | Camera Module Press & Lock Station        | 3   | Pneumatic press jig (custom)                 | Presses camera module into chassis; locks with torque screw     | SA         |
| 4 | Battery Installation Station              | 4   | Assembly bench, ESD protection, torque driver | Installs Li-Po battery; connects FPC connector; torque 0.3 Nm   | M          |
| 5 | PCB + Mainboard Installation              | 4   | ESD bench, ESD wrist strap, torque driver     | Installs populated mainboard; connects all FPC/ZIF connectors   | M          |
| 6 | Rear Case Assembly + Ultrasonic Weld      | 3   | Branson 2000X series ultrasonic welder       | Ultrasonically welds or clips rear case halves together          | SA         |
| 7 | Screw Fastening Station (multi-spindle)   | 4   | Atlas Copco QMX4 or Bosch Rexroth           | Tightens all internal screws to spec torque; logs every torque   | SA/AI      |
| 8 | IMEI / Serial Number Programming Station  | 4   | Custom MES-linked programming jig            | Burns IMEI, serial number, and software baseline onto phone      | A/AI       |
| 9 | Phone Software Flash Station              | 6   | MES-integrated flash fixture (USB-C tethered) | Flashes Android firmware + Coo-Cah UI; installs bootloader      | A/AI       |
| 10| Phone Boot & Basic Function Test          | 6   | Automated test fixture (touchscreen, camera, mic) | Tests boot, touch, cameras, audio, vibration, charging port  | SA/A       |
| 11| Display Visual Inspection Station         | 4   | Light booth + automated screen analyser (AI)  | Checks screen for dead pixels, uniformity, touch sensitivity     | SA/AI      |
| 12| Cosmetic Final Inspection Station         | 4   | Inspection bench, LED ring light, UV lamp    | 360° cosmetic inspection; checks fit, gaps, surface scratches    | M          |

---

## 5. TWS Earbuds Assembly Line

A dedicated assembly line for both CCE-TWS-01 and CCE-TWS-PRO models, with quick changeover tooling (< 20 min changeover between models).

| # | Equipment                                 | Qty | Spec / Model                                 | Purpose                                                         | Auto Level |
|---|-------------------------------------------|-----|----------------------------------------------|-----------------------------------------------------------------|------------|
| 1 | TWS PCB + Driver Assembly Station         | 4   | ESD bench, micro-tweezers, torque pen         | Inserts PCB into earbud shell; connects micro-speaker driver     | M          |
| 2 | Acoustic Seal + Speaker Gasket Press      | 4   | Pneumatic micro-press + silicone gasket jig  | Seals speaker driver with acoustic gasket for consistent bass    | SA         |
| 3 | Earbud Casing Ultrasonic Weld             | 2   | Branson 900 series (micro application)       | Welds TWS earbud halves together after PCB + driver insertion    | SA         |
| 4 | Charging Pin & Contact Assembly           | 4   | Assembly bench, soldering iron (fine-tip)    | Solders pogo pin contacts for case-to-earbud wireless charging   | M          |
| 5 | TWS Charging Case Assembly                | 4   | Assembly bench, press jig                    | Assembles charging case: battery, PCB, LED, USB-C port, hinges   | M          |
| 6 | TWS Acoustic Function Test                | 6   | Brüel & Kjær HATS (or GRAS Head/Torso)       | Measures frequency response, THD, sensitivity per IEC 60268-7   | SA/AI      |
| 7 | Bluetooth Range & Connectivity Test       | 4   | NCC-configured BT test fixture (Rohde & Schwarz CMW500) | Tests BT pairing, range, audio latency, NCC compliance   | SA/AI      |
| 8 | Charging Case Wireless Charge Cycle Test  | 4   | Automated charge cycle rig (custom)          | Full charge cycle test; confirms case-to-earbud charging at spec  | SA         |
| 9 | IPX Waterproof Test (Earbuds)             | 2   | IPX4/IPX5 spray test chamber                 | Confirms water resistance rating per IEC 60529                   | SA         |
| 10| TWS Cosmetic + Fit Inspection             | 4   | Inspection bench + fit gauge jig             | Checks earbud surface, hinge operation, ear tip fit              | M          |

---

## 6. Smartwatch Assembly Line

| # | Equipment                                 | Qty | Spec / Model                                 | Purpose                                                         | Auto Level |
|---|-------------------------------------------|-----|----------------------------------------------|-----------------------------------------------------------------|------------|
| 1 | Watch PCB + Sensor Assembly Station       | 3   | ESD bench, micro-soldering (JBC T245)        | Installs heart rate / SpO₂ / accelerometer sensors to watch PCB | M          |
| 2 | Display + Touch Assembly Station          | 3   | Vacuum laminator (OCA for AMOLED Pro model) | Bonds display to chassis; applies protective lens overlay        | SA         |
| 3 | Watch Case Back Sealing                   | 3   | Ultrasonic welder (Branson) + crown seal     | Seals watch case back; installs crown seal to 5 ATM spec (Pro)  | SA         |
| 4 | Strap Assembly Station                    | 3   | Assembly bench + lug press                  | Attaches silicone/leather strap; tests lug spring bar release    | M          |
| 5 | Watch Software Flash + Function Test      | 4   | Custom MES flash jig (USB magnetic connector) | Flashes firmware; activates sensors; tests display, vibration    | SA/A       |
| 6 | Heart Rate & SpO₂ Accuracy Test           | 4   | Finger phantom simulator (optical calibration) | Validates HR and SpO₂ sensor accuracy to ±3 bpm / ±2% SpO₂    | SA/AI      |
| 7 | GPS Function Test (Pro model)             | 2   | GPS simulator (GNSS signal replay)            | Validates GPS lock time, position accuracy — CCE-SW-PRO only    | SA         |
| 8 | Water Resistance Test (5 ATM)             | 2   | Pressure test chamber (0–5 bar)              | Water resistance validation per ISO 22810 — Pro model only       | SA         |
| 9 | Watch Final Visual Inspection             | 3   | Inspection bench, LED lighting               | Cosmetic inspection: dial alignment, crystal, case finish         | M          |

---

## 7. Power Bank & Accessories Assembly Line

| # | Equipment                                 | Qty | Spec / Model                                 | Purpose                                                         | Auto Level |
|---|-------------------------------------------|-----|----------------------------------------------|-----------------------------------------------------------------|------------|
| 1 | Battery Cell Welding Station (Spot Weld)  | 4   | Sunstone Pulse Arc welder (nickel strip)     | Spot-welds nickel strip to Li-ion / LiFePO₄ cells to form pack  | SA         |
| 2 | Battery Management IC Assembly Station    | 4   | ESD bench, torque driver                     | Solders/installs BMS PCB; connects protection circuit to cells   | M          |
| 3 | Power Bank Housing Assembly               | 4   | Assembly bench, ultrasonic welder            | Inserts battery pack + PCB into housing; clips/welds shell        | SA         |
| 4 | USB-C Hub Assembly Station                | 2   | ESD bench, fine-pitch soldering              | Assembles USB-C hub PCB (from SMT) into aluminium/plastic shell  | M          |
| 5 | Power Bank Charge/Discharge Test          | 6   | Chroma 17020 battery tester (charge + discharge) | Full cycle capacity verification; confirms rated mAh ±5%    | SA/AI      |
| 6 | Power Bank Safety Test (IEC 62133)        | 4   | Hipot tester + short-circuit protection test  | Validates overcharge, over-discharge, short circuit protection    | SA/A       |
| 7 | Power Bank Output Voltage / Fast Charge Test | 4 | Programmable DC load + USB power meter      | Tests USB-A/USB-C output voltage, PD fast charge (18W/20K model) | SA/A       |

---

## 8. RF & NCC Type Approval Test Laboratory

The NCC Type Approval Test Lab is a dedicated zone that handles all regulatory RF and wireless testing required for Nigerian Communications Commission type approval across every wireless product manufactured.

| # | Equipment                                 | Qty | Spec / Model                                 | Purpose                                                         | Auto Level |
|---|-------------------------------------------|-----|----------------------------------------------|-----------------------------------------------------------------|------------|
| 1 | RF Shielded Test Chamber (Large)          | 2   | ETS-Lindgren 7000 series (or Holland Shielding) | Full RF isolation for NCC type test, OTA measurements      | SA/AI      |
| 2 | RF Shielded Test Chamber (Small)          | 2   | Comtest CLTX-02 (benchtop)                   | BT/Wi-Fi channel tests, TWS and smartwatch certification tests   | SA         |
| 3 | Network Analyser / RF Signal Generator    | 2   | Rohde & Schwarz CMW500 (wideband tester)     | Tests 3G/4G/5G, Wi-Fi, BT — NCC type approval compliance tests  | SA/AI      |
| 4 | Spectrum Analyser                         | 1   | Keysight N9020B MXA                          | RF emission characterisation; spurious emission measurements     | SA         |
| 5 | OTA (Over-the-Air) Test Range             | 1   | Mini CATR (compact antenna test range)       | Total Radiated Power (TRP) and Total Isotropic Sensitivity (TIS) | SA/AI      |
| 6 | EMC Pre-Compliance Test Equipment         | 1   | Rohde & Schwarz ESU26 + near-field probes    | Pre-compliance EMC scan before submission to accredited lab      | SA         |
| 7 | Production RF Calibration Station         | 4   | MES-linked calibration fixture (per SKU)     | Line-end RF calibration for every wireless unit — adjusts antenna | A/AI      |

---

## 9. Final QC & Safety Test Equipment

| # | Equipment                                 | Qty | Spec / Model                                  | Purpose                                                          | Auto Level |
|---|-------------------------------------------|-----|-----------------------------------------------|------------------------------------------------------------------|------------|
| 1 | Electrical Safety Tester (IEC 62368-1)    | 4   | Chroma 19053 Safety Analyser                  | Dielectric withstand (hipot) + earth bond for all power products  | SA/A       |
| 2 | Drop Test Rig                             | 2   | Lansmont TEAM (1.5m drop, 6-face)             | Drop test per IEC 60068-2-31 — sample basis, 100% NPI             | SA         |
| 3 | Thermal / Humidity Chamber                | 2   | Espec TEMP-HH (−40 to +180°C, 20–98% RH)    | Accelerated reliability testing; thermal cycling; humidity soak   | SA/A       |
| 4 | Battery Cycle Life Test Rack              | 2   | Chroma 17200 (32-channel battery tester)      | Long-cycle life testing for power bank and phone battery packs    | A/AI       |
| 5 | 3D AOI (Final Board Inspection)           | 1   | Koh Young Zenith II                           | Final PCB visual inspection before assembly integration           | FA/AI      |
| 6 | Digital Microscope                        | 3   | Keyence VHX-7000                              | SMT solder joint examination; magnification to 6,000×             | SA/AI      |
| 7 | Final Test Fixture — Phones (multi-DUT)   | 4   | Custom MES-linked 4-up test fixture           | 4 phones simultaneously tested: audio, camera, touch, RF pass    | FA/AI      |
| 8 | Final Cosmetic AI Vision System           | 2   | Cognex In-Sight 9000 + custom lighting        | AI-based cosmetic defect detection on finished phone exterior      | FA/AI      |

---

## 10. Material Handling Equipment

### 10.1 Autonomous Mobile Robots (AMRs)

| # | Equipment              | Qty | Model / Type              | Purpose                                                      | Auto Level |
|---|------------------------|-----|---------------------------|--------------------------------------------------------------|------------|
| 1 | AMR — Transport        | 8   | MiR250 — 250 kg payload   | Main WIP transport between all production zones              | AI/FA      |
| 2 | AMR — Goods-to-Person  | 4   | MiR100 — 100 kg payload   | Component kits from stores to assembly line stations         | AI/FA      |
| 3 | AMR — Finished Goods   | 4   | MiR250 — 250 kg payload   | Packed product from packaging to FG warehouse                | AI/FA      |
| 4 | AMR Charging Docks     | 18  | MiR ChargePad (auto-dock) | Autonomous charging; opportunity charging during idle periods | FA         |

**AMR Fleet Specifications:**
- **Navigation:** LiDAR + camera SLAM — no floor magnets or rails required
- **Fleet Management:** MiR Fleet software integrated with Coo-Cah MES
- **Payload:** 100–250 kg per unit; ESD-safe carrying trays for PCB transport
- **Battery:** LFP, 2.4 kWh per unit; 10h+ operational time per charge
- **Communication:** Wi-Fi 6 (802.11ax); 5G-ready
- **Safety:** ISO 3691-4 compliant; emergency stop; laser person detection ≤ 3m

### 10.2 Conveyor Systems

| # | Equipment                      | Qty | Spec                                | Purpose                                    | Auto Level |
|---|--------------------------------|-----|-------------------------------------|--------------------------------------------|------------|
| 1 | Belt Conveyor — Phone Assembly | 3   | Width: 200mm; speed: variable       | Paces phone assembly stations              | A          |
| 2 | ESD-Safe Belt Conveyor — SMT   | 2   | ESD-rated belt, SMEMA-compatible    | Links SMT inline process equipment         | FA         |
| 3 | Roller Conveyor — Stores       | 4   | Length: 4m, manual gravity          | Pallet staging in inbound stores           | M          |
| 4 | Overhead Conveyor (TWS)        | 1   | Motorised; 2 kg/carrier             | Moves TWS assembly trays between stations  | SA         |

### 10.3 Lifting & Storage Equipment

| # | Equipment                  | Qty | Spec                         | Purpose                                    | Auto Level |
|---|----------------------------|-----|------------------------------|--------------------------------------------|------------|
| 1 | Electric Forklift          | 3   | 2.5 tonne, 4.8m lift height | Loading/unloading containers at dock       | M/SA       |
| 2 | Pallet Jack (Electric)     | 6   | 2,000 kg capacity            | Internal pallet movement                   | M          |
| 3 | Vertical Lift Module (VLM) | 4   | Modula Lift — 8m height      | High-density SMT component storage         | A/AI       |
| 4 | Selective Pallet Racking   | 200 bays | 3 × 1.2m pallet positions | Bulk raw material and FG storage           | M          |
| 5 | ESD-Safe Storage Cabinets  | 40  | Static-dissipative, humidity-controlled | PCB and IC component storage        | M          |

---

## 11. Packaging Equipment

| # | Equipment                     | Qty | Spec / Model                          | Purpose                                                | Auto Level |
|---|-------------------------------|-----|---------------------------------------|--------------------------------------------------------|------------|
| 1 | Automatic Carton Erector      | 2   | Endoline 701 or Wexxar WF30           | Forms and bottom-folds retail cartons at up to 25/min  | A          |
| 2 | Product Insert / Fill Station | 4   | Semi-auto with MES serial scan        | Places device, accessories, manual, warranty card into carton | SA   |
| 3 | Automatic Carton Sealer       | 2   | Endoline 222 (top + bottom tape)      | Hot-melt seals retail cartons                          | A          |
| 4 | Shrink Wrap Machine           | 2   | Minipack Torre PRATIKA 56MVS          | Overwraps multi-packs for pallet shipping              | SA         |
| 5 | Pallet Wrapper                | 1   | Robopac Ecoplat PLUS                  | Stretch-wraps pallets for outbound dispatch            | A          |
| 6 | Label Printer & Applicator    | 4   | Zebra ZT610 + Herma 132M applicator   | Prints and applies product, carton, pallet labels      | A/AI       |
| 7 | Checkweigher                  | 2   | Mettler Toledo C33 (±0.5g accuracy)   | Verifies packed weight; auto-rejects underweight units | FA/AI      |
| 8 | Inline Barcode / QR Scanner   | 4   | Cognex DataMan 475                    | Scans serial + carton barcodes for MES traceability    | FA         |

---

## 12. Energy & Utilities Equipment

| # | Equipment                          | Qty | Spec / Model                    | Purpose                                         | Auto Level |
|---|-------------------------------------|-----|---------------------------------|-------------------------------------------------|------------|
| 1 | Solar PV Array                      | —   | 850 kWp, Monocrystalline PERC   | Primary renewable energy generation             | AI/FA      |
| 2 | LFP Battery Energy Storage (BESS)   | —   | 900 kWh, 614V DC Bus            | Energy storage and overnight/backup power       | AI/FA      |
| 3 | Hybrid Inverter / PCS               | 4   | Sungrow SH250HX (250 kW each)   | DC-AC inversion, grid management                | FA         |
| 4 | Automatic Transfer Switch (ATS)     | 2   | Socomec ATYS 3s 630A            | Seamless grid/solar/BESS switching              | FA         |
| 5 | Diesel Generator (Backup)           | 1   | Perkins 500 kVA standby         | Emergency backup — grid and solar failure       | SA         |
| 6 | Air Compressor                      | 2   | Atlas Copco GA37 (37 kW each)   | 8 bar ring-main; pneumatic tools throughout     | A          |
| 7 | HVAC Central Chiller + AHUs         | 2   | Carrier 30XA (200 kW cooling)   | Factory climate control across 18,000 m²        | A/AI       |
| 8 | Cleanroom HEPA Filtration (SMT ESD) | 2   | Camfil 99.97% HEPA AHU         | Particle control in SMT zones to ISO Class 8    | A          |

---

## 13. MES / IT Equipment

| # | Equipment                         | Qty | Spec / Model              | Purpose                                                  | Auto Level |
|---|-----------------------------------|-----|---------------------------|----------------------------------------------------------|------------|
| 1 | MES Workstation (Floor)           | 20  | Dell Latitude Rugged 5430 | Operator production entry, job tracking                  | M/AI       |
| 2 | Industrial Panel PC (Line)        | 30  | Advantech TPC-1581H (IP65)| Mounted at each station for real-time MES display        | SA/AI      |
| 3 | Shop Floor Barcode Scanners       | 40  | Zebra DS8100 (2D)         | WIP scanning, component traceability, serial number scan | SA         |
| 4 | Machine Interface Gateway (OPC-UA)| 10  | Kepware KEPServerEX       | OPC-UA/MQTT bridge between machines and MES              | FA/AI      |
| 5 | Industrial Wi-Fi Access Points    | 25  | Cisco Catalyst IW6300 (Wi-Fi 6, IP67) | AMR connectivity, mobile tablet network           | FA         |
| 6 | Network Switch — Industrial       | 8   | Cisco IE 3400 (managed)   | Factory LAN backbone (VLAN-segmented OT/IT)              | FA         |
| 7 | Edge Computing Node               | 4   | Dell XR5610 (ruggedised)  | Local AI inference, MES edge processing                  | AI/FA      |
| 8 | CCTV System                       | 45  | Axis P3245-V (4MP IP)     | Safety monitoring, QC audit, security                    | AI         |
| 9 | UPS (IT Room)                     | 2   | Eaton 9PX 20 kVA          | Power backup for MES servers and network equipment       | FA         |

---

## 14. Equipment Maintenance Schedule Summary

| Maintenance Type       | Frequency        | Responsible Team              | MES Trigger               |
|------------------------|------------------|-------------------------------|---------------------------|
| Preventive Maintenance | Per OEM schedule | Maintenance Team + MES PM     | Automated work order      |
| Predictive Maintenance | Continuous       | AI Platform vibration/temp alert | AI work order trigger  |
| Solder Paste / Stencil | Per shift        | SMT Operators                 | MES paste life counter    |
| SMT Nozzle Clean/Replace | Weekly         | SMT Technician                | PM schedule + cycle count |
| Calibration (RF lab)   | Quarterly        | QA Lab + NCC-accredited body  | Calibration register      |
| Reflow Oven Profiling  | Per product change | Process Engineer             | MES product changeover    |
| Annual Overhaul        | Yearly           | OEM-authorised service team   | Annual shutdown            |

---

## 15. Spare Parts & Consumables Register

| # | Item                         | Equipment                     | Min Stock  | Reorder Point | Supplier Type  |
|---|------------------------------|-------------------------------|------------|---------------|----------------|
| 1 | SMT Nozzles (JUKI CP nozzles)| JUKI FX-3R, RX-7              | 50 pcs     | 25 pcs        | OEM/Import     |
| 2 | Solder Paste (SAC305, 500g)  | DEK Horizon Printer           | 30 jars    | 15 jars       | Import         |
| 3 | SMT Stencils (per product)   | DEK Screen Printer            | 2 per SKU  | 1 per SKU     | Import         |
| 4 | Reflow Oven Heating Elements | Heller 1964 MK5 (both lines)  | 4 sets     | 2 sets        | OEM Import     |
| 5 | ESD Wrist Straps             | All assembly stations         | 200 pcs    | 80 pcs        | Local          |
| 6 | OCA Adhesive Sheets          | Screen Bonding Machine        | 10,000 pcs | 4,000 pcs     | Import         |
| 7 | AMR Battery Module           | MiR250 AMR Fleet              | 4 units    | 2 units       | OEM            |
| 8 | Ultrasonic Weld Horns/Boosters | Branson Welders              | 4 sets     | 2 sets        | OEM Import     |
| 9 | HEPA Filter Packs            | SMT Zone HVAC                 | 8 units    | 4 units       | Import         |
| 10| Flux Cleaner (IPA-based)     | Rework + Wave Solder stations | 20 L       | 10 L          | Local/Import   |

---

*For energy consumption data per machine, refer to [`energy-profile.md`](./energy-profile.md).*
*For digital twin asset registration, refer to [`digital-twin.md`](./digital-twin.md).*
