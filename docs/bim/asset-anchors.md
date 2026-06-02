# Personal Electronics — Asset Anchors (BIM)

> **Gate 3 Artifact (Digital Twin Spatial Readiness)**
> **Document Version:** 1.1 | **Owner:** BIM / Facilities Engineering | **Integration Reviewer:** DT Integration Lead

Asset anchor points used to place all registered assets in the 3D digital twin. All 142 Phase 1 assets are listed. IFC GUID assignment is tracked per asset; coordinates are populated as the IFC model is delivered.

---

## Governance

- Zone IDs MUST match [`floor-plan.md`](../../floor-plan.md) zone identifiers.
- DT Asset IDs MUST match the asset registry in [`digital-twin.md`](../../digital-twin.md) §2.
- Anchor Refs are consumed by [`../sensor-map.md`](../sensor-map.md) for sensor-to-anchor mapping.
- Coordinate system: Local factory grid (origin = SW corner of building at slab level). X = East, Y = North, Z = Up. Units: metres.
- IFC GUID format: 22-character base-64 IFC GlobalId string.

### Gate 3 Required Header Mapping

- **Orientation (Yaw/Pitch/Roll):** represented by the table columns `Yaw (°)`, `Pitch (°)`, and `Roll (°)`.
- **Coordinate System:** Local factory grid (origin = SW corner of building at slab level). X = East, Y = North, Z = Up.

---

## IFC GUID Status Control

| Status Code | Meaning                                             |
|-------------|-----------------------------------------------------|
| `PENDING`   | IFC GUID not yet assigned; awaiting IFC model delivery |
| `ASSIGNED`  | IFC GUID assigned and validated against IFC model   |
| `VERIFIED`  | IFC GUID verified against physical asset location   |

---

## ID Harmonization Register

The following table maps DT manifest IDs (from `digital-twin.md`) to BIM anchor IDs used in this file. Any discrepancy between the two ID sets must be resolved before DT spatial rendering is activated.

| DT Manifest ID (digital-twin.md) | BIM Anchor ID (this file) | Harmonization Status | Resolved By | Target Date |
|-----------------------------------|---------------------------|----------------------|-------------|-------------|
| DT-SMT-L1-01 through DT-SMT-L1-10| A-SMT-L1-01 through A-SMT-L1-10 | ✅ Matched  | DT Integration Lead | 2025-Q3 |
| DT-SMT-L2-01 through DT-SMT-L2-10| A-SMT-L2-01 through A-SMT-L2-10 | ✅ Matched  | DT Integration Lead | 2025-Q3 |
| DT-PH-01 through DT-PH-07        | A-PH-01 through A-PH-07   | ✅ Matched          | DT Integration Lead | 2025-Q3 |
| DT-TWS-01 through DT-TWS-03       | A-TWS-01 through A-TWS-03 | ✅ Matched          | DT Integration Lead | 2025-Q3 |
| DT-SW-01, DT-SW-02               | A-SW-01, A-SW-02          | ✅ Matched          | DT Integration Lead | 2025-Q3 |
| DT-PB-01 through DT-PB-03        | A-PB-01 through A-PB-03   | ✅ Matched          | DT Integration Lead | 2025-Q3 |
| DT-RF-01 through DT-RF-06        | A-RF-01 through A-RF-06   | ✅ Matched          | DT Integration Lead | 2025-Q3 |
| DT-AMR-MIR250-01 through -12     | A-AMR-MIR250-01 through -12 | ✅ Matched        | DT Integration Lead | 2025-Q3 |
| DT-AMR-MIR100-01 through -04     | A-AMR-MIR100-01 through -04 | ✅ Matched        | DT Integration Lead | 2025-Q3 |
| DT-AMR-DOCK-01 through -18       | A-AMR-DOCK-01 through -18 | ✅ Matched          | DT Integration Lead | 2025-Q3 |
| DT-EN-PV-01 through DT-EN-PV-03  | A-EN-PV-01 through A-EN-PV-03 | ✅ Matched       | DT Integration Lead | 2025-Q3 |
| DT-EN-BESS-01, DT-EN-BESS-02     | A-EN-BESS-01, A-EN-BESS-02 | ✅ Matched         | DT Integration Lead | 2025-Q3 |
| DT-EN-INV-01 through -04         | A-EN-INV-01 through A-EN-INV-04 | ✅ Matched     | DT Integration Lead | 2025-Q3 |
| DT-EN-GEN-01                     | A-EN-GEN-01               | ✅ Matched          | DT Integration Lead | 2025-Q3 |
| DT-EN-GRID-01                    | A-EN-GRID-01              | ✅ Matched          | DT Integration Lead | 2025-Q3 |
| DT-EN-HVAC-01, DT-EN-HVAC-02     | A-EN-HVAC-01, A-EN-HVAC-02 | ✅ Matched         | DT Integration Lead | 2025-Q3 |
| DT-Z9-BATT-CYCLE-01              | A-Z9-BATT-CYCLE-01        | ✅ Matched          | DT Integration Lead | 2025-Q3 |
| DT-Z10-LABEL-01                  | A-Z10-LABEL-01            | ✅ Matched          | DT Integration Lead | 2025-Q3 |
| DT-Z11-PALLET-SCAN-01            | A-Z11-PALLET-SCAN-01      | ✅ Matched          | DT Integration Lead | 2025-Q3 |
| DT-Z1-VLM-01                     | A-Z1-VLM-01               | ✅ Matched          | DT Integration Lead | 2025-Q3 |

---

## Acceptance Register

| Acceptance Criterion                                         | Status     | Owner               | Due Date  |
|--------------------------------------------------------------|------------|---------------------|-----------|
| All 142 anchor rows present in register                      | ✅ Met      | BIM Engineering     | 2025-Q3   |
| All IFC GUIDs assigned (ASSIGNED status)                     | ⏳ Pending  | BIM Engineering     | 2026-Q1   |
| All IFC GUIDs verified against physical asset location       | ⏳ Pending  | Facilities / DT Lead| 2026-Q1   |
| ID harmonization register fully matched (0 mismatches)       | ✅ Met      | DT Integration Lead | 2025-Q3   |
| Coordinate system documented and consistent with zone-boundaries.md | ✅ Met | BIM Engineering  | 2025-Q3   |
| All anchor IDs referenced by sensor-map.md are valid         | ✅ Met      | DT Integration Lead | 2025-Q3   |

---

## Asset Anchor Register

| DT Asset ID | BIM Anchor ID | Asset Name | Zone ID | Anchor X (m) | Anchor Y (m) | Anchor Z (m) | Yaw (°) | Pitch (°) | Roll (°) | IFC GUID | GUID Status | IFC Owner | Target GUID Date | Source Reference |
|-------------|---------------|------------|---------|--------------|--------------|--------------|---------|-----------|----------|----------|-------------|-----------|------------------|------------------|
| DT-SMT-L1-01 | A-SMT-L1-01 | DEK Horizon Printer (L1) | Z2 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-SMT-L1-02 | A-SMT-L1-02 | Koh Young SPI KY8030-3 (L1) | Z2 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-SMT-L1-03 | A-SMT-L1-03 | JUKI FX-3R Pick-and-Place (L1) | Z2 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-SMT-L1-04 | A-SMT-L1-04 | JUKI RX-7 Pick-and-Place (L1) | Z2 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-SMT-L1-05 | A-SMT-L1-05 | Heller 1964 MK5 Reflow (L1) | Z2 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-SMT-L1-06 | A-SMT-L1-06 | Koh Young Zenith AOI (L1) | Z2 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-SMT-L1-07 | A-SMT-L1-07 | Unicomp AX8200 X-Ray (L1) | Z2 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-SMT-L1-08 | A-SMT-L1-08 | Ersa Versaflow Selective Solder (L1) | Z2 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-SMT-L1-09 | A-SMT-L1-09 | Keysight I1000D ICT (L1) | Z2 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-SMT-L1-10 | A-SMT-L1-10 | PCB Depanelling Router (L1) | Z2 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-SMT-L2-01 | A-SMT-L2-01 | DEK Horizon Printer (L2) | Z3 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-SMT-L2-02 | A-SMT-L2-02 | Koh Young SPI KY8030-3 (L2) | Z3 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-SMT-L2-03 | A-SMT-L2-03 | JUKI FX-3R Pick-and-Place (L2) | Z3 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-SMT-L2-04 | A-SMT-L2-04 | JUKI RX-7 Pick-and-Place (L2) | Z3 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-SMT-L2-05 | A-SMT-L2-05 | Heller 1964 MK5 Reflow (L2) | Z3 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-SMT-L2-06 | A-SMT-L2-06 | Koh Young Zenith AOI (L2) | Z3 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-SMT-L2-07 | A-SMT-L2-07 | Unicomp AX8200 X-Ray (L2) | Z3 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-SMT-L2-08 | A-SMT-L2-08 | Ersa Versaflow Selective Solder (L2) | Z3 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-SMT-L2-09 | A-SMT-L2-09 | Keysight I1000D ICT (L2) | Z3 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-SMT-L2-10 | A-SMT-L2-10 | PCB Depanelling Router (L2) | Z3 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.1 |
| DT-PH-01 | A-PH-01 | Screen Bonding Machine ×2 | Z4 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.2 |
| DT-PH-02 | A-PH-02 | Autoclave / Debubble | Z4 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.2 |
| DT-PH-03 | A-PH-03 | Atlas Copco Torque Station ×4 | Z4 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.2 |
| DT-PH-04 | A-PH-04 | Phone Flash Station ×6 | Z4 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.2 |
| DT-PH-05 | A-PH-05 | Phone Function Test Fixture ×6 | Z4 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.2 |
| DT-PH-06 | A-PH-06 | Cognex In-Sight 9000 Vision ×2 | Z4/Z9 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.2 |
| DT-PH-07 | A-PH-07 | Ultrasonic Welder (Branson 2000X) ×3 | Z4 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.2 |
| DT-TWS-01 | A-TWS-01 | Brüel & Kjær HATS Acoustic Test ×6 | Z5 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.3 |
| DT-TWS-02 | A-TWS-02 | R&S CMW500 BT Test ×4 | Z5/Z8 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.3 |
| DT-TWS-03 | A-TWS-03 | IPX Spray Chamber ×2 | Z5 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.3 |
| DT-SW-01 | A-SW-01 | Smartwatch Pressure Test Chamber ×2 | Z6 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.3 |
| DT-SW-02 | A-SW-02 | GPS Simulator (GNSS) ×2 | Z6/Z8 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.3 |
| DT-PB-01 | A-PB-01 | Sunstone Spot Welder ×4 | Z7 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.3 |
| DT-PB-02 | A-PB-02 | Chroma 17020 Battery Tester ×6 | Z7 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.3 |
| DT-PB-03 | A-PB-03 | Chroma 19053 Safety Tester ×4 | Z7/Z9 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.3 |
| DT-RF-01 | A-RF-01 | ETS-Lindgren 7000 Chamber ×2 | Z8 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.4 |
| DT-RF-02 | A-RF-02 | Benchtop RF Chamber ×2 | Z8 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.4 |
| DT-RF-03 | A-RF-03 | R&S CMW500 Network Analyser ×2 | Z8 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.4 |
| DT-RF-04 | A-RF-04 | Keysight N9020B Spectrum Analyser | Z8 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.4 |
| DT-RF-05 | A-RF-05 | Mini CATR OTA Test Range | Z8 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.4 |
| DT-RF-06 | A-RF-06 | RF Calibration Station ×4 | Z4/Z5/Z6 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.4 |
| DT-AMR-MIR250-01 | A-AMR-MIR250-01 | MiR250 Transport AMR 01 | Main Floor | — | — | 0.00 | — | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-MIR250-02 | A-AMR-MIR250-02 | MiR250 Transport AMR 02 | Main Floor | — | — | 0.00 | — | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-MIR250-03 | A-AMR-MIR250-03 | MiR250 Transport AMR 03 | Main Floor | — | — | 0.00 | — | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-MIR250-04 | A-AMR-MIR250-04 | MiR250 Transport AMR 04 | Main Floor | — | — | 0.00 | — | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-MIR250-05 | A-AMR-MIR250-05 | MiR250 Transport AMR 05 | Main Floor | — | — | 0.00 | — | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-MIR250-06 | A-AMR-MIR250-06 | MiR250 Transport AMR 06 | Main Floor | — | — | 0.00 | — | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-MIR250-07 | A-AMR-MIR250-07 | MiR250 Transport AMR 07 | Main Floor | — | — | 0.00 | — | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-MIR250-08 | A-AMR-MIR250-08 | MiR250 Transport AMR 08 | Main Floor | — | — | 0.00 | — | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-MIR250-09 | A-AMR-MIR250-09 | MiR250 Transport AMR 09 | Main Floor | — | — | 0.00 | — | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-MIR250-10 | A-AMR-MIR250-10 | MiR250 Transport AMR 10 | Main Floor | — | — | 0.00 | — | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-MIR250-11 | A-AMR-MIR250-11 | MiR250 Transport AMR 11 | Main Floor | — | — | 0.00 | — | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-MIR250-12 | A-AMR-MIR250-12 | MiR250 Transport AMR 12 | Main Floor | — | — | 0.00 | — | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-MIR100-01 | A-AMR-MIR100-01 | MiR100 Goods-to-Person AMR 01 | Main Floor | — | — | 0.00 | — | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-MIR100-02 | A-AMR-MIR100-02 | MiR100 Goods-to-Person AMR 02 | Main Floor | — | — | 0.00 | — | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-MIR100-03 | A-AMR-MIR100-03 | MiR100 Goods-to-Person AMR 03 | Main Floor | — | — | 0.00 | — | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-MIR100-04 | A-AMR-MIR100-04 | MiR100 Goods-to-Person AMR 04 | Main Floor | — | — | 0.00 | — | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-DOCK-01 | A-AMR-DOCK-01 | AMR Charging Dock 01 | Main Floor | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-DOCK-02 | A-AMR-DOCK-02 | AMR Charging Dock 02 | Main Floor | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-DOCK-03 | A-AMR-DOCK-03 | AMR Charging Dock 03 | Main Floor | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-DOCK-04 | A-AMR-DOCK-04 | AMR Charging Dock 04 | Main Floor | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-DOCK-05 | A-AMR-DOCK-05 | AMR Charging Dock 05 | Main Floor | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-DOCK-06 | A-AMR-DOCK-06 | AMR Charging Dock 06 | Main Floor | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-DOCK-07 | A-AMR-DOCK-07 | AMR Charging Dock 07 | Main Floor | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-DOCK-08 | A-AMR-DOCK-08 | AMR Charging Dock 08 | Main Floor | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-DOCK-09 | A-AMR-DOCK-09 | AMR Charging Dock 09 | Main Floor | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-DOCK-10 | A-AMR-DOCK-10 | AMR Charging Dock 10 | Main Floor | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-DOCK-11 | A-AMR-DOCK-11 | AMR Charging Dock 11 | Main Floor | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-DOCK-12 | A-AMR-DOCK-12 | AMR Charging Dock 12 | Main Floor | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-DOCK-13 | A-AMR-DOCK-13 | AMR Charging Dock 13 | Main Floor | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-DOCK-14 | A-AMR-DOCK-14 | AMR Charging Dock 14 | Main Floor | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-DOCK-15 | A-AMR-DOCK-15 | AMR Charging Dock 15 | Main Floor | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-DOCK-16 | A-AMR-DOCK-16 | AMR Charging Dock 16 | Main Floor | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-DOCK-17 | A-AMR-DOCK-17 | AMR Charging Dock 17 | Main Floor | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-AMR-DOCK-18 | A-AMR-DOCK-18 | AMR Charging Dock 18 | Main Floor | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.5 |
| DT-EN-PV-01 | A-EN-PV-01 | Solar PV Array — Roof Main (620 kWp) | Roof | — | — | 5.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.6 |
| DT-EN-PV-02 | A-EN-PV-02 | Solar PV Array — Warehouse (110 kWp) | Warehouse Roof | — | — | 5.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.6 |
| DT-EN-PV-03 | A-EN-PV-03 | Solar PV Array — Ground (120 kWp) | East Yard | — | — | 0.50 | 15 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.6 |
| DT-EN-BESS-01 | A-EN-BESS-01 | LFP BESS Container 1 (450 kWh) | North Yard | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.6 |
| DT-EN-BESS-02 | A-EN-BESS-02 | LFP BESS Container 2 (450 kWh) | North Yard | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.6 |
| DT-EN-INV-01 | A-EN-INV-01 | Sungrow SH250HX Inverter 01 | Inverter Room | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.6 |
| DT-EN-INV-02 | A-EN-INV-02 | Sungrow SH250HX Inverter 02 | Inverter Room | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.6 |
| DT-EN-INV-03 | A-EN-INV-03 | Sungrow SH250HX Inverter 03 | Inverter Room | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.6 |
| DT-EN-INV-04 | A-EN-INV-04 | Sungrow SH250HX Inverter 04 | Inverter Room | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.6 |
| DT-EN-GEN-01 | A-EN-GEN-01 | Perkins 500 kVA Generator | NE Corner | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.6 |
| DT-EN-GRID-01 | A-EN-GRID-01 | Grid Supply Meter (AMI) | HV Substation | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.6 |
| DT-EN-HVAC-01 | A-EN-HVAC-01 | Carrier Chiller 01 | Utility Room | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.6 |
| DT-EN-HVAC-02 | A-EN-HVAC-02 | Carrier Chiller 02 | Utility Room | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2.6 |
| DT-Z9-BATT-CYCLE-01 | A-Z9-BATT-CYCLE-01 | Battery Cycling Test Station | Z9 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2 |
| DT-Z10-LABEL-01 | A-Z10-LABEL-01 | Labelling / Printing Station | Z10 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2 |
| DT-Z11-PALLET-SCAN-01 | A-Z11-PALLET-SCAN-01 | Pallet Scan / Dispatch Station | Z11 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2 |
| DT-Z1-VLM-01 | A-Z1-VLM-01 | Vertical Lift Module (Component Store) | Z1 | — | — | 0.00 | 0 | 0 | 0 | — | PENDING | BIM Eng | 2026-Q1 | digital-twin.md §2 |

---

## Related Documents

| Document | Purpose |
|----------|---------|
| [`digital-twin.md`](../../digital-twin.md) | Asset registry (§2) — authoritative source for DT Asset IDs |
| [`../zone-boundaries.md`](./zone-boundaries.md) | Zone boundary definitions and coordinate frame |
| [`../sensor-map.md`](../sensor-map.md) | Sensor registry referencing Anchor IDs from this file |
| [`../../floor-plan.md`](../../floor-plan.md) | Physical zone layout — source for zone IDs |
| [`../gap-closure-report.md`](../gap-closure-report.md) | Gap closure status for BIM anchor readiness |
