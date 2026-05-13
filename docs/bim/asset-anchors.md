# BIM Asset Anchor Points — Personal Electronics Factory

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1
> **Document Version:** 1.0 | **Owner:** Civil & Industrial Engineering Lead + Digital Manufacturing Team
> **Status:** Controlled Draft — required for DT platform 3D floor model load (Phase 0 Gate deliverable)

This document defines the spatial anchor point (insertion origin) for each of the 142 registered
physical assets. The DT platform uses these anchor points to place asset icons and bind sensor streams
to their physical location in the 3D floor model. Each anchor point is expressed in the building-local
coordinate system defined in [`zone-boundaries.md`](./zone-boundaries.md).

> **Update protocol:** Any equipment relocation triggers a mandatory BIM anchor update within
> 5 business days. Change requests must be raised via the digital twin change-control process and
> applied simultaneously to this document, the IFC model, and the DT platform asset configuration.

---

## 1. Anchor Point Schema

Each anchor point defines:

| Field          | Description                                                                |
|----------------|----------------------------------------------------------------------------|
| `Asset ID`     | Unique DT asset identifier — matches `digital-twin.md` and `dt-asset-manifest.md` |
| `Asset Name`   | Human-readable asset name                                                  |
| `Zone`         | Zone ID (Z1–Z12)                                                           |
| `X (m)`        | Local easting from SW building corner                                      |
| `Y (m)`        | Local northing from SW building corner                                     |
| `Z (m)`        | Height above FFL (finished floor level); 0.000 = floor level              |
| `Rotation (°)` | Asset heading relative to building X-axis (East); clockwise positive       |
| `IFC GUID`     | IFC GlobalId status tag; pending values are controlled and tracked to closure owner/date |

All coordinates refer to the **insertion origin** of the asset — typically the geometric centre of
the machine footprint at floor level. For overhead equipment (e.g. vision cameras), Z is the mounting
height.

---

## 1.1 IFC GUID Status Control

To avoid unmanaged placeholder text, all non-final IFC values in this document are treated as
**controlled pending status tags** under the convention `{GUID-<ASSET>-REPLACE}` with:

- **Owner:** Civil & Industrial Engineering Lead
- **Integration Reviewer:** Documentation Integration Reviewer
- **Target closure date:** 2026-06-30 (or at delivered IFC handover, whichever is earlier)

Any pending tag must be replaced with the contractor-issued IFC GlobalId during Phase 0 spatial closure.

---

## 1.2 ID Harmonization Register (DT Manifest ↔ BIM Anchors)

The BIM anchor file and the DT manifest use a small set of alternate operational IDs for grouped assets.
This crosswalk is the authoritative mapping used for consistency checks:

| DT Manifest ID | BIM Anchor ID(s) | Mapping Type |
|---|---|---|
| `DT-Z1-VLM-01` | `DT-STR-01` to `DT-STR-04` | 1-to-many (group to physical units) |
| `DT-Z9-DROP-01` | `DT-QC-02` | 1-to-1 alias |
| `DT-Z9-THERM-01` | `DT-QC-03` | 1-to-1 alias |
| `DT-Z9-BATT-CYCLE-01` | `DT-Z9-BATT-CYCLE-01` | direct |
| `DT-Z10-CHECKWEIGH-01` | `DT-PKG-02` | 1-to-1 alias |
| `DT-Z10-BARCODE-01` | `DT-PKG-03` | 1-to-1 alias |
| `DT-Z10-LABEL-01` | `DT-Z10-LABEL-01` | direct |
| `DT-Z11-TEMP-01` | `DT-WH-04` | 1-to-1 alias |
| `DT-Z11-PALLET-SCAN-01` | `DT-Z11-PALLET-SCAN-01` | direct |

---

## 2. SMT & PCB Processing Assets — Zone Z2 (SMT Line 1)

SMT Line 1 runs along a single in-line sequence from west (PCB load) to east (unload), centred at
Y = 10.000 m within Z2. Equipment spacing is nominally 4 m between machine centres.

| Asset ID        | Asset Name                        | X (m)  | Y (m)  | Z (m)  | Rot (°) | IFC GUID / Status Tag           |
|-----------------|-----------------------------------|--------|--------|--------|---------|---------------------------------|
| DT-SMT-L1-01    | DEK Horizon Screen Printer (L1)   | 40.000 | 10.000 | 0.000  | 90      | `{GUID-SMT-L1-01-REPLACE}`      |
| DT-SMT-L1-02    | Koh Young KY8030-3 SPI (L1)       | 44.000 | 10.000 | 0.000  | 90      | `{GUID-SMT-L1-02-REPLACE}`      |
| DT-SMT-L1-03    | JUKI FX-3R Pick-and-Place (L1)    | 49.000 | 10.000 | 0.000  | 90      | `{GUID-SMT-L1-03-REPLACE}`      |
| DT-SMT-L1-04    | JUKI RX-7 Pick-and-Place (L1)     | 54.500 | 10.000 | 0.000  | 90      | `{GUID-SMT-L1-04-REPLACE}`      |
| DT-SMT-L1-05    | Heller 1964 MK5 Reflow Oven (L1)  | 61.000 | 10.000 | 0.000  | 90      | `{GUID-SMT-L1-05-REPLACE}`      |
| DT-SMT-L1-06    | Koh Young Zenith AOI (L1)         | 67.000 | 10.000 | 0.000  | 90      | `{GUID-SMT-L1-06-REPLACE}`      |
| DT-SMT-L1-07    | Unicomp AX8200 X-Ray (L1)         | 70.500 | 10.000 | 0.000  | 90      | `{GUID-SMT-L1-07-REPLACE}`      |
| DT-SMT-L1-08    | Ersa Versaflow Selective Solder (L1)| 74.000| 10.000 | 0.000  | 90     | `{GUID-SMT-L1-08-REPLACE}`      |
| DT-SMT-L1-09    | Keysight I1000D ICT (L1)          | 44.000 | 15.000 | 0.000  | 0       | `{GUID-SMT-L1-09-REPLACE}`      |
| DT-SMT-L1-10    | PCB Depanelling Router (L1)       | 74.500 | 15.000 | 0.000  | 0       | `{GUID-SMT-L1-10-REPLACE}`      |

---

## 3. SMT & PCB Processing Assets — Zone Z3 (SMT Line 2)

SMT Line 2 mirrors Line 1, centred at Y = 30.000 m within Z3.

| Asset ID        | Asset Name                        | X (m)  | Y (m)  | Z (m)  | Rot (°) | IFC GUID / Status Tag           |
|-----------------|-----------------------------------|--------|--------|--------|---------|---------------------------------|
| DT-SMT-L2-01    | DEK Horizon Screen Printer (L2)   | 40.000 | 30.000 | 0.000  | 90      | `{GUID-SMT-L2-01-REPLACE}`      |
| DT-SMT-L2-02    | Koh Young KY8030-3 SPI (L2)       | 44.000 | 30.000 | 0.000  | 90      | `{GUID-SMT-L2-02-REPLACE}`      |
| DT-SMT-L2-03    | JUKI FX-3R Pick-and-Place (L2)    | 49.000 | 30.000 | 0.000  | 90      | `{GUID-SMT-L2-03-REPLACE}`      |
| DT-SMT-L2-04    | JUKI RX-7 Pick-and-Place (L2)     | 54.500 | 30.000 | 0.000  | 90      | `{GUID-SMT-L2-04-REPLACE}`      |
| DT-SMT-L2-05    | Heller 1964 MK5 Reflow Oven (L2)  | 61.000 | 30.000 | 0.000  | 90      | `{GUID-SMT-L2-05-REPLACE}`      |
| DT-SMT-L2-06    | Koh Young Zenith AOI (L2)         | 67.000 | 30.000 | 0.000  | 90      | `{GUID-SMT-L2-06-REPLACE}`      |
| DT-SMT-L2-07    | Unicomp AX8200 X-Ray (L2)         | 70.500 | 30.000 | 0.000  | 90      | `{GUID-SMT-L2-07-REPLACE}`      |
| DT-SMT-L2-08    | Ersa Versaflow Selective Solder (L2)| 74.000| 30.000 | 0.000  | 90     | `{GUID-SMT-L2-08-REPLACE}`      |
| DT-SMT-L2-09    | Keysight I1000D ICT (L2)          | 44.000 | 35.000 | 0.000  | 0       | `{GUID-SMT-L2-09-REPLACE}`      |
| DT-SMT-L2-10    | PCB Depanelling Router (L2)       | 74.500 | 35.000 | 0.000  | 0       | `{GUID-SMT-L2-10-REPLACE}`      |

---

## 4. Phone Assembly Assets — Zone Z4

Phone Assembly contains three parallel assembly lines (PH-1, PH-2, PH-3) plus shared test and vision stations.

| Asset ID    | Asset Name                          | X (m)   | Y (m)  | Z (m)  | Rot (°) | IFC GUID / Status Tag        |
|-------------|-------------------------------------|---------|--------|--------|---------|------------------------------|
| DT-PH-01    | Screen Bonding Machine (×2)         | 84.000  | 8.000  | 0.000  | 0       | `{GUID-PH-01-REPLACE}`       |
| DT-PH-02    | Autoclave / Debubble                | 92.000  | 8.000  | 0.000  | 0       | `{GUID-PH-02-REPLACE}`       |
| DT-PH-03    | Atlas Copco Torque Station (×4)     | 100.000 | 10.000 | 0.000  | 0       | `{GUID-PH-03-REPLACE}`       |
| DT-PH-04    | Phone Flash Station (×6)            | 115.000 | 10.000 | 0.000  | 0       | `{GUID-PH-04-REPLACE}`       |
| DT-PH-05    | Phone Function Test Fixture (×6)    | 125.000 | 10.000 | 0.000  | 0       | `{GUID-PH-05-REPLACE}`       |
| DT-PH-06    | Cognex In-Sight 9000 Vision (×2)    | 132.000 | 10.000 | 3.000  | 270     | `{GUID-PH-06-REPLACE}`       |
| DT-PH-07    | Ultrasonic Welder Branson 2000X (×3)| 108.000 | 28.000 | 0.000  | 0       | `{GUID-PH-07-REPLACE}`       |

---

## 5. TWS Earbuds Assembly Assets — Zone Z5

| Asset ID    | Asset Name                         | X (m)  | Y (m)  | Z (m)  | Rot (°) | IFC GUID / Status Tag        |
|-------------|------------------------------------|--------|--------|--------|---------|------------------------------|
| DT-TWS-01   | Brüel & Kjær HATS Acoustic Test (×6)| 40.000| 45.000 | 0.000  | 0       | `{GUID-TWS-01-REPLACE}`      |
| DT-TWS-02   | R&S CMW500 BT Tester (×4)          | 55.000 | 45.000 | 0.000  | 0       | `{GUID-TWS-02-REPLACE}`      |
| DT-TWS-03   | IPX Spray Chamber (×2)             | 70.000 | 45.000 | 0.000  | 0       | `{GUID-TWS-03-REPLACE}`      |

---

## 6. Smartwatch Assembly Assets — Zone Z6

| Asset ID    | Asset Name                          | X (m)  | Y (m)  | Z (m)  | Rot (°) | IFC GUID / Status Tag        |
|-------------|-------------------------------------|--------|--------|--------|---------|------------------------------|
| DT-SW-01    | Smartwatch Pressure Test Chamber (×2)| 40.000| 65.000 | 0.000  | 0       | `{GUID-SW-01-REPLACE}`       |
| DT-SW-02    | GPS Simulator GNSS (×2)             | 55.000 | 65.000 | 0.000  | 0       | `{GUID-SW-02-REPLACE}`       |

---

## 7. Power Bank Assembly Assets — Zone Z7

| Asset ID    | Asset Name                     | X (m)  | Y (m)  | Z (m)  | Rot (°) | IFC GUID / Status Tag        |
|-------------|--------------------------------|--------|--------|--------|---------|------------------------------|
| DT-PB-01    | Sunstone Spot Welder (×4)      | 40.000 | 85.000 | 0.000  | 0       | `{GUID-PB-01-REPLACE}`       |
| DT-PB-02    | Chroma 17020 Battery Tester (×6)| 50.000| 85.000 | 0.000  | 0       | `{GUID-PB-02-REPLACE}`       |
| DT-PB-03    | Chroma 19053 Safety Tester (×4) | 60.000| 85.000 | 0.000  | 0       | `{GUID-PB-03-REPLACE}`       |

---

## 8. RF & NCC Test Laboratory Assets — Zone Z8

RF Lab is in the NE corner (X=141–180, Y=0–18). Equipment is positioned within the primary shielded
chamber enclosure and adjacent benching.

| Asset ID    | Asset Name                          | X (m)   | Y (m)  | Z (m)  | Rot (°) | IFC GUID / Status Tag        |
|-------------|-------------------------------------|---------|--------|--------|---------|------------------------------|
| DT-RF-01    | ETS-Lindgren 7000 Chamber (×2)      | 148.000 | 8.000  | 0.000  | 0       | `{GUID-RF-01-REPLACE}`       |
| DT-RF-02    | Benchtop RF Chamber (×2)            | 162.000 | 5.000  | 0.000  | 0       | `{GUID-RF-02-REPLACE}`       |
| DT-RF-03    | R&S CMW500 Network Analyser (×2)    | 170.000 | 12.000 | 0.000  | 0       | `{GUID-RF-03-REPLACE}`       |
| DT-RF-04    | Keysight N9020B Spectrum Analyser   | 174.000 | 12.000 | 1.200  | 0       | `{GUID-RF-04-REPLACE}`       |
| DT-RF-05    | Mini CATR OTA Test Range            | 155.000 | 14.000 | 0.000  | 0       | `{GUID-RF-05-REPLACE}`       |
| DT-RF-06    | RF Calibration Station (×4)         | 145.000 | 5.000  | 1.000  | 0       | `{GUID-RF-06-REPLACE}`       |

---

## 9. Final QC & Safety Test Assets — Zone Z9

| Asset ID    | Asset Name                              | X (m)   | Y (m)  | Z (m)  | Rot (°) | IFC GUID / Status Tag        |
|-------------|------------------------------------------|---------|--------|--------|---------|------------------------------|
| DT-QC-01    | Cognex In-Sight 9000 Vision Station — Z9 | 145.000 | 25.000 | 3.000  | 270     | `{GUID-QC-01-REPLACE}`       |
| DT-QC-02    | Drop Test Rig                            | 152.000 | 28.000 | 0.000  | 0       | `{GUID-QC-02-REPLACE}`       |
| DT-QC-03    | Thermal Cycling Chamber                  | 158.000 | 28.000 | 0.000  | 0       | `{GUID-QC-03-REPLACE}`       |
| DT-QC-04    | Chroma 19053 Safety Tester — Z9          | 162.000 | 35.000 | 0.000  | 0       | `{GUID-QC-04-REPLACE}`       |
| DT-Z9-BATT-CYCLE-01 | Battery Cycle Test Station        | 160.000 | 31.000 | 0.000  | 0       | `{GUID-Z9-BATT-CYCLE-01-REPLACE}` |

---

## 10. Packaging Line Assets — Zone Z10

| Asset ID    | Asset Name                          | X (m)  | Y (m)  | Z (m)  | Rot (°) | IFC GUID / Status Tag        |
|-------------|-------------------------------------|--------|--------|--------|---------|------------------------------|
| DT-PKG-01   | Carton Erect & Fill Station         | 70.000 | 86.000 | 0.000  | 90      | `{GUID-PKG-01-REPLACE}`      |
| DT-PKG-02   | Mettler Toledo Checkweigher         | 80.000 | 86.000 | 0.000  | 90      | `{GUID-PKG-02-REPLACE}`      |
| DT-PKG-03   | Barcode Print & Apply Station       | 88.000 | 86.000 | 0.000  | 90      | `{GUID-PKG-03-REPLACE}`      |
| DT-PKG-04   | Pallet Wrap / Shrink Station        | 100.000| 86.000 | 0.000  | 90      | `{GUID-PKG-04-REPLACE}`      |
| DT-Z10-LABEL-01 | Label Verification Station       | 92.000 | 86.000 | 0.000  | 90      | `{GUID-Z10-LABEL-01-REPLACE}` |

---

## 11. FG Warehouse Assets — Zone Z11

| Asset ID    | Asset Name                          | X (m)   | Y (m)  | Z (m)  | Rot (°) | IFC GUID / Status Tag        |
|-------------|-------------------------------------|---------|--------|--------|---------|------------------------------|
| DT-WH-01    | Pallet Racking Bay (selective) ×n   | 115.000 | 60.000 | 0.000  | 0       | `{GUID-WH-01-REPLACE}`       |
| DT-WH-02    | AMR Pallet Lane Marker Set          | 115.000 | 80.000 | 0.000  | 0       | `{GUID-WH-02-REPLACE}`       |
| DT-WH-03    | Dispatch Staging Dock               | 175.000 | 55.000 | 0.000  | 90      | `{GUID-WH-03-REPLACE}`       |
| DT-WH-04    | Temp/Humidity Monitor (FG Area)     | 145.000 | 75.000 | 2.500  | 0       | `{GUID-WH-04-REPLACE}`       |
| DT-Z11-PALLET-SCAN-01 | Pallet Scan Station         | 171.000 | 55.000 | 0.000  | 90      | `{GUID-Z11-PALLET-SCAN-01-REPLACE}` |

---

## 12. AMR Fleet — All Zones

AMR anchor points are dynamic (AMRs move continuously). The coordinates below represent the
**home-dock / charging-dock positions** only. Live position tracking is streamed via MQTT in real
time and overlaid on the DT floor map separately; these static anchors are used to initialise
the DT model.

### 12.1 MiR250 Transport AMRs (×12) — Home Docks

AMR charging docks for MiR250 fleet are located along the north face of Z4 (Y ≈ 34 m):

| Asset ID               | Home Dock X (m) | Home Dock Y (m) | Z (m) | IFC GUID / Status Tag           |
|------------------------|-----------------|-----------------|-------|---------------------------------|
| DT-AMR-MIR250-01       | 78.000          | 34.500          | 0.000 | `{GUID-AMR-MIR250-01-REPLACE}`  |
| DT-AMR-MIR250-02       | 81.000          | 34.500          | 0.000 | `{GUID-AMR-MIR250-02-REPLACE}`  |
| DT-AMR-MIR250-03       | 84.000          | 34.500          | 0.000 | `{GUID-AMR-MIR250-03-REPLACE}`  |
| DT-AMR-MIR250-04       | 87.000          | 34.500          | 0.000 | `{GUID-AMR-MIR250-04-REPLACE}`  |
| DT-AMR-MIR250-05       | 90.000          | 34.500          | 0.000 | `{GUID-AMR-MIR250-05-REPLACE}`  |
| DT-AMR-MIR250-06       | 93.000          | 34.500          | 0.000 | `{GUID-AMR-MIR250-06-REPLACE}`  |
| DT-AMR-MIR250-07       | 96.000          | 34.500          | 0.000 | `{GUID-AMR-MIR250-07-REPLACE}`  |
| DT-AMR-MIR250-08       | 99.000          | 34.500          | 0.000 | `{GUID-AMR-MIR250-08-REPLACE}`  |
| DT-AMR-MIR250-09       | 102.000         | 34.500          | 0.000 | `{GUID-AMR-MIR250-09-REPLACE}`  |
| DT-AMR-MIR250-10       | 105.000         | 34.500          | 0.000 | `{GUID-AMR-MIR250-10-REPLACE}`  |
| DT-AMR-MIR250-11       | 108.000         | 34.500          | 0.000 | `{GUID-AMR-MIR250-11-REPLACE}`  |
| DT-AMR-MIR250-12       | 111.000         | 34.500          | 0.000 | `{GUID-AMR-MIR250-12-REPLACE}`  |

### 12.2 MiR100 Goods-to-Person AMRs (×4) — Home Docks

MiR100 docks are in the Z1 stores area:

| Asset ID               | Home Dock X (m) | Home Dock Y (m) | Z (m) | IFC GUID / Status Tag          |
|------------------------|-----------------|-----------------|-------|--------------------------------|
| DT-AMR-MIR100-01       | 5.000           | 10.000          | 0.000 | `{GUID-AMR-MIR100-01-REPLACE}` |
| DT-AMR-MIR100-02       | 8.000           | 10.000          | 0.000 | `{GUID-AMR-MIR100-02-REPLACE}` |
| DT-AMR-MIR100-03       | 11.000          | 10.000          | 0.000 | `{GUID-AMR-MIR100-03-REPLACE}` |
| DT-AMR-MIR100-04       | 14.000          | 10.000          | 0.000 | `{GUID-AMR-MIR100-04-REPLACE}` |

### 12.3 AMR Charging Docks (×18)

18 charging-dock positions distributed across Z1, Z4, and Z11:

| Asset ID             | X (m)   | Y (m)   | Z (m) | Zone | IFC GUID / Status Tag        |
|----------------------|---------|---------|-------|------|------------------------------|
| DT-AMR-DOCK-01       | 5.000   | 10.000  | 0.000 | Z1   | `{GUID-AMR-DOCK-01-REPLACE}` |
| DT-AMR-DOCK-02       | 8.000   | 10.000  | 0.000 | Z1   | `{GUID-AMR-DOCK-02-REPLACE}` |
| DT-AMR-DOCK-03       | 11.000  | 10.000  | 0.000 | Z1   | `{GUID-AMR-DOCK-03-REPLACE}` |
| DT-AMR-DOCK-04       | 14.000  | 10.000  | 0.000 | Z1   | `{GUID-AMR-DOCK-04-REPLACE}` |
| DT-AMR-DOCK-05       | 78.000  | 34.500  | 0.000 | Z4   | `{GUID-AMR-DOCK-05-REPLACE}` |
| DT-AMR-DOCK-06       | 81.000  | 34.500  | 0.000 | Z4   | `{GUID-AMR-DOCK-06-REPLACE}` |
| DT-AMR-DOCK-07       | 84.000  | 34.500  | 0.000 | Z4   | `{GUID-AMR-DOCK-07-REPLACE}` |
| DT-AMR-DOCK-08       | 87.000  | 34.500  | 0.000 | Z4   | `{GUID-AMR-DOCK-08-REPLACE}` |
| DT-AMR-DOCK-09       | 90.000  | 34.500  | 0.000 | Z4   | `{GUID-AMR-DOCK-09-REPLACE}` |
| DT-AMR-DOCK-10       | 93.000  | 34.500  | 0.000 | Z4   | `{GUID-AMR-DOCK-10-REPLACE}` |
| DT-AMR-DOCK-11       | 96.000  | 34.500  | 0.000 | Z4   | `{GUID-AMR-DOCK-11-REPLACE}` |
| DT-AMR-DOCK-12       | 99.000  | 34.500  | 0.000 | Z4   | `{GUID-AMR-DOCK-12-REPLACE}` |
| DT-AMR-DOCK-13       | 110.000 | 55.000  | 0.000 | Z11  | `{GUID-AMR-DOCK-13-REPLACE}` |
| DT-AMR-DOCK-14       | 113.000 | 55.000  | 0.000 | Z11  | `{GUID-AMR-DOCK-14-REPLACE}` |
| DT-AMR-DOCK-15       | 116.000 | 55.000  | 0.000 | Z11  | `{GUID-AMR-DOCK-15-REPLACE}` |
| DT-AMR-DOCK-16       | 119.000 | 55.000  | 0.000 | Z11  | `{GUID-AMR-DOCK-16-REPLACE}` |
| DT-AMR-DOCK-17       | 122.000 | 55.000  | 0.000 | Z11  | `{GUID-AMR-DOCK-17-REPLACE}` |
| DT-AMR-DOCK-18       | 125.000 | 55.000  | 0.000 | Z11  | `{GUID-AMR-DOCK-18-REPLACE}` |

---

## 13. Energy System Assets — Site Level

Energy assets are distributed across multiple roof, yard, and utility areas. Coordinates are relative
to the same building origin; roof-mounted assets use Z > 0.

| Asset ID          | Asset Name                           | X (m)   | Y (m)  | Z (m)  | Zone / Location     | IFC GUID / Status Tag           |
|-------------------|--------------------------------------|---------|--------|--------|---------------------|---------------------------------|
| DT-EN-PV-01       | Solar PV Array — Main Roof (620 kWp) | 90.000  | 50.000 | 9.000  | Factory Roof        | `{GUID-EN-PV-01-REPLACE}`       |
| DT-EN-PV-02       | Solar PV Array — Warehouse (110 kWp) | 143.000 | 75.000 | 11.000 | Warehouse Roof      | `{GUID-EN-PV-02-REPLACE}`       |
| DT-EN-PV-03       | Solar PV Array — Ground (120 kWp)    | 175.000 | 115.000| 1.500  | East Yard           | `{GUID-EN-PV-03-REPLACE}`       |
| DT-EN-BESS-01     | LFP BESS Container 1 (450 kWh)       | 20.000  | 110.000| 0.000  | North Yard          | `{GUID-EN-BESS-01-REPLACE}`     |
| DT-EN-BESS-02     | LFP BESS Container 2 (450 kWh)       | 28.000  | 110.000| 0.000  | North Yard          | `{GUID-EN-BESS-02-REPLACE}`     |
| DT-EN-INV-01      | Sungrow SH250HX Inverter 1           | 8.000   | 78.000 | 0.000  | Inverter Room       | `{GUID-EN-INV-01-REPLACE}`      |
| DT-EN-INV-02      | Sungrow SH250HX Inverter 2           | 11.000  | 78.000 | 0.000  | Inverter Room       | `{GUID-EN-INV-02-REPLACE}`      |
| DT-EN-INV-03      | Sungrow SH250HX Inverter 3           | 14.000  | 78.000 | 0.000  | Inverter Room       | `{GUID-EN-INV-03-REPLACE}`      |
| DT-EN-INV-04      | Sungrow SH250HX Inverter 4           | 17.000  | 78.000 | 0.000  | Inverter Room       | `{GUID-EN-INV-04-REPLACE}`      |
| DT-EN-GEN-01      | Perkins 500 kVA Generator            | 178.000 | 5.000  | 0.000  | NE Corner Yard      | `{GUID-EN-GEN-01-REPLACE}`      |
| DT-EN-GRID-01     | Grid Supply Meter (AMI)              | 5.000   | 78.000 | 1.200  | HV Substation       | `{GUID-EN-GRID-01-REPLACE}`     |
| DT-EN-HVAC-01     | Carrier Chiller 1                    | 10.000  | 82.000 | 0.000  | Utility Room        | `{GUID-EN-HVAC-01-REPLACE}`     |
| DT-EN-HVAC-02     | Carrier Chiller 2                    | 14.000  | 82.000 | 0.000  | Utility Room        | `{GUID-EN-HVAC-02-REPLACE}`     |

---

## 14. Component Stores Assets — Zone Z1

| Asset ID    | Asset Name                          | X (m)  | Y (m)  | Z (m)  | Rot (°) | IFC GUID / Status Tag        |
|-------------|-------------------------------------|--------|--------|--------|---------|------------------------------|
| DT-STR-01   | Modula VLM Unit 1                   | 8.000  | 20.000 | 0.000  | 0       | `{GUID-STR-01-REPLACE}`      |
| DT-STR-02   | Modula VLM Unit 2                   | 12.000 | 20.000 | 0.000  | 0       | `{GUID-STR-02-REPLACE}`      |
| DT-STR-03   | Modula VLM Unit 3                   | 16.000 | 20.000 | 0.000  | 0       | `{GUID-STR-03-REPLACE}`      |
| DT-STR-04   | Modula VLM Unit 4                   | 20.000 | 20.000 | 0.000  | 0       | `{GUID-STR-04-REPLACE}`      |
| DT-Z1-VLM-01 | Modula VLM Group Anchor             | 14.000 | 20.000 | 0.000  | 0       | `{GUID-Z1-VLM-01-REPLACE}`   |

---

## 15. Asset Anchor Acceptance Register

| Control | Status | Owner | Due Date |
|---|---|---|---|
| All 142 registered assets mapped to anchors directly or through the ID harmonization register | ✅ Complete (mapping established) | Digital Manufacturing Team | 2026-05-12 |
| Pending IFC GUID status tags replaced with delivered contractor IFC GlobalIds | ⏳ In progress | Civil & Industrial Engineering Lead | 2026-06-30 |
| Coordinates verified against commissioning survey | ⏳ In progress | Civil & Industrial Engineering Lead | 2026-06-30 |
| AMR home-dock positions verified against MiR Fleet map data | ⏳ In progress | AMR / Logistics Engineering Lead | 2026-06-15 |
| Energy asset Z-values verified from structural drawings | ⏳ In progress | Civil Engineering Lead | 2026-06-15 |
| Deviations > 200 mm recorded via change request register | ⏳ In progress | PMO + Digital Manufacturing Team | 2026-06-30 |
| Anchor file version and IFC SHA-256 hash recorded in Phase 0 register | ⏳ In progress | Documentation Integration Reviewer | 2026-06-30 |
| DT platform import test renders all planned asset icons in 3D floor view | ⏳ In progress | Digital Manufacturing Team | 2026-06-30 |

---

## Related Documents

- For zone boundary coordinates and IFC CRS reference, refer to [`zone-boundaries.md`](./zone-boundaries.md).
- For the asset registry and DT status, refer to [`digital-twin.md`](../digital-twin.md).
- For sensor data schemas for each asset, refer to [`dt-asset-manifest.md`](../dt-asset-manifest.md).
- For canonical sensor coverage and calibration controls, refer to [`../sensor-map.md`](../sensor-map.md).
- For integrated dependency gates and closure sequencing, refer to [`../bim-simulation-readiness-program.md`](../bim-simulation-readiness-program.md).
- For closure tracking of document gaps, refer to [`../gap-closure-report.md`](../gap-closure-report.md).
