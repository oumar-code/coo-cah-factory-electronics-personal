# BIM Zone Boundaries — Personal Electronics Factory

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1
> **Document Version:** 1.0 | **Owner:** Civil & Industrial Engineering Lead + Digital Manufacturing Team
> **Status:** Controlled Draft — required for DT platform 3D floor model load (Phase 0 Gate deliverable)

This document is the authoritative reference for zone boundary definitions used by the Coo-Cah Digital
Twin platform to load and render the 3D floor model. All zone IDs, coordinate extents, and IFC object
names in this document must match exactly the asset manifest ([`dt-asset-manifest.md`](../dt-asset-manifest.md)),
the MQTT topic namespace ([`dt-mqtt-namespace.md`](../dt-mqtt-namespace.md)), and the IFC file delivered
by the civil contractor.

---

## 1. Coordinate Reference System

| Parameter                | Value                                                                 |
|--------------------------|-----------------------------------------------------------------------|
| Local CRS Origin         | SW corner of main building — finished floor level (FFL)              |
| X-axis (positive)        | East                                                                  |
| Y-axis (positive)        | North                                                                 |
| Z-axis (positive)        | Up (metres above FFL = 0.000)                                        |
| Horizontal unit          | Metres                                                                |
| Vertical datum           | FFL = 0.000 m; site grade level ≈ +0.600 m above external datum      |
| Geographic reference     | WGS 84 UTM Zone 31N (EPSG:32631)                                     |
| Approx. site easting     | 450 820 m E                                                           |
| Approx. site northing    | 757 340 m N                                                          |
| True north rotation      | +3.5° from local grid north (clockwise)                              |
| IFC schema               | IFC 4.0 (IFC4)                                                       |
| IFC site/building entity | `IfcBuilding` → `IfcBuildingStorey` (Ground Floor, Z = 0.000)        |

> **Note:** The IFC file origin must be set to this building SW-corner origin before import into the
> DT platform. The civil contractor must deliver the IFC with this origin applied; the DT team must
> confirm origin alignment before final import acceptance.

---

## 2. Building Footprint

| Corner     | Local X (m) | Local Y (m) | Description            |
|------------|-------------|-------------|------------------------|
| SW         | 0.000       | 0.000       | Origin / Inbound dock side |
| SE         | 180.000     | 0.000       | Outbound dock side     |
| NE         | 180.000     | 100.000     | FG Warehouse corner    |
| NW         | 0.000       | 100.000     | North-west corner      |

Total enclosed area: **18,000 m²** (180 m × 100 m)
Column grid: 12 m × 12 m (15 bays E-W × 8 bays N-S; bays numbered 1–16 E-W, A–I N-S)

---

## 3. Zone Boundary Definitions

Each zone is defined as a rectangular `IfcZone` entity bounding box at ground-floor level.
All coordinates are local to the building origin (Section 2).

### 3.1 Production Zones

| Zone ID | Zone Name                       | SW Corner (X, Y) | NE Corner (X, Y) | Area (m²) | Clear Height (m) | IFC Zone Name                     |
|---------|---------------------------------|------------------|------------------|-----------|------------------|-----------------------------------|
| Z1      | Inbound Goods / Component Stores| (0.000, 0.000)   | (36.000, 50.000) | 1,800     | 8.0              | `CCE-SAG-Z1-STORES`               |
| Z2      | SMT Line 1                      | (36.000, 0.000)  | (76.000, 20.000) | 800       | 6.0              | `CCE-SAG-Z2-SMT-L1`               |
| Z3      | SMT Line 2                      | (36.000, 20.000) | (76.000, 40.000) | 800       | 6.0              | `CCE-SAG-Z3-SMT-L2`               |
| Z4      | Phone Assembly Lines            | (76.000, 0.000)  | (141.000, 34.000)| 2,210     | 8.0              | `CCE-SAG-Z4-PHONE-ASSEMBLY`       |
| Z5      | TWS Earbuds Assembly            | (36.000, 40.000) | (76.000, 60.000) | 800       | 6.0              | `CCE-SAG-Z5-TWS-ASSEMBLY`         |
| Z6      | Smartwatch Assembly             | (36.000, 60.000) | (71.000, 80.000) | 700       | 6.0              | `CCE-SAG-Z6-WATCH-ASSEMBLY`       |
| Z7      | Power Bank & Accessories        | (36.000, 80.000) | (66.000, 100.000)| 600       | 6.0              | `CCE-SAG-Z7-POWERBANK-ASSEMBLY`   |
| Z8      | RF & NCC Type Test Laboratory   | (141.000, 0.000) | (180.000, 18.000)| 702       | 6.0              | `CCE-SAG-Z8-RF-NCC-LAB`           |
| Z9      | Final QC & Safety Test          | (141.000, 18.000)| (165.000, 43.000)| 600       | 6.0              | `CCE-SAG-Z9-FINAL-QC`             |
| Z10     | Packaging Lines                 | (66.000, 80.000) | (106.000, 100.000)| 800      | 6.0              | `CCE-SAG-Z10-PACKAGING`           |
| Z11     | Finished Goods Warehouse        | (106.000, 50.000)| (180.000, 100.000)| 3,700    | 10.0             | `CCE-SAG-Z11-FG-WAREHOUSE`        |

> **Tolerance note:** Zone areas in this table are derived from coordinate extents and may differ from
> the planning-approved zone areas by ±2% due to structural column offsets. The IFC file from the
> civil contractor takes precedence for as-built verification.

### 3.2 Support Zones

| Zone ID  | Zone Name                        | SW Corner (X, Y) | NE Corner (X, Y)  | Area (m²) | IFC Zone Name                        |
|----------|----------------------------------|------------------|-------------------|-----------|--------------------------------------|
| Z12      | Engineering, MES & Offices       | (0.000, 50.000)  | (36.000, 75.000)  | 900       | `CCE-SAG-Z12-ENGINEERING-OFFICES`    |
| UTIL     | Utility / Energy Room            | (0.000, 75.000)  | (30.000, 95.000)  | 600       | `CCE-SAG-UTIL-ENERGY-ROOM`           |
| AMEN     | Amenities, First Aid & Lockers   | (30.000, 75.000) | (36.000, 100.000) | 150       | `CCE-SAG-AMEN-WELFARE`               |
| CIRC     | Aisles, Circulation & Walls      | (varies)         | (varies)          | 2,438     | `CCE-SAG-CIRC-AISLES`                |

> **AMR lane clearance:** All primary AMR travel lanes are 2.0 m wide. Lane centre-lines run parallel
> to the X-axis at Y = 40.000, 60.000, and 80.000, and parallel to the Y-axis at X = 36.000 and
> X = 106.000. These lanes are modelled as separate `IfcSpace` entities tagged `AMR-LANE-*` in the IFC.

---

## 4. Mezzanine Level

| Zone       | Description                             | Extent (X, Y)           | Z Range (m)    | IFC Storey          |
|------------|-----------------------------------------|--------------------------|----------------|---------------------|
| MEZZ-Z1    | Mezzanine above Z1 (office / canteen)   | (0.000, 0.000) – (36.000, 25.000) | +4.000 to +7.000 | `IfcBuildingStorey` — Mezzanine |
| MEZZ-Z12   | Engineering office mezzanine above Z12  | (0.000, 50.000) – (36.000, 75.000)| +4.000 to +7.000 | `IfcBuildingStorey` — Mezzanine |

---

## 5. Zone Attribute Metadata (IFC Property Set: `Pset_CCE_ZoneProperties`)

Each `IfcZone` must carry the following custom property set so the DT platform can resolve zone
metadata at run-time:

| Property Name       | Data Type | Example Value       | Purpose                                         |
|---------------------|-----------|---------------------|-------------------------------------------------|
| `ZoneID`            | String    | `Z2`                | Short zone identifier — matches DT asset IDs    |
| `ZoneName`          | String    | `SMT Line 1`        | Human-readable name for UI labels               |
| `ESDRequired`       | Boolean   | `true`              | Indicates ESD-safe floor and access requirements|
| `HEPAControlled`    | Boolean   | `true`              | HEPA-filtered cleanroom ventilation present     |
| `RFShielded`        | Boolean   | `false`             | RF-shielded room (true for Z8 only)             |
| `MaxOccupancy`      | Integer   | `24`                | Fire-safety max occupancy (persons)             |
| `DT_MQTTPrefix`     | String    | `cce/sag/z2/`       | MQTT topic prefix for all assets in this zone   |
| `DT_InfluxBucket`   | String    | `factory_smt`       | InfluxDB bucket for zone time-series data       |

---

## 6. Zone Boundary Acceptance Checklist

The following must be verified and signed off by the Civil & Industrial Engineering Lead and the
Digital Manufacturing Team Lead before the DT platform 3D model is accepted for Phase 0 closure:

- [ ] IFC file received from civil contractor in IFC 4.0 format with correct origin alignment
- [ ] All 11 production zones (Z1–Z11) and Z12 present as named `IfcZone` entities with matching IDs
- [ ] Column grid verified against as-built survey; deviations > 50 mm documented
- [ ] All zone extents in IFC match the coordinate table in Section 3 within ±100 mm tolerance
- [ ] Mezzanine storeys modelled as separate `IfcBuildingStorey` entities
- [ ] AMR lane `IfcSpace` entities present with correct clearance widths (≥ 2.0 m)
- [ ] `Pset_CCE_ZoneProperties` applied to all zones with values populated
- [ ] DT platform import test completed; zone names resolve correctly in the UI
- [ ] Zone boundary file and IFC version hash recorded in Phase 0 governance register

---

*For asset spatial anchor points within each zone, refer to [`asset-anchors.md`](./asset-anchors.md).*
*For the full asset registry with DT status, refer to [`digital-twin.md`](../digital-twin.md).*
*For Phase 0 governance sign-off controls, refer to [`dt-phase0-governance.md`](../dt-phase0-governance.md).*
*For DT implementation task context (Task 0.3), refer to [`dt-implementation-plan.md`](../dt-implementation-plan.md).*
