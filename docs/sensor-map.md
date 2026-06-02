# Personal Electronics — Sensor Map

> **Gate 3 Artifact (Digital Twin Spatial Readiness)**
> **Document Version:** 1.1 | **Owner:** Digital Manufacturing / Sensors Team
> **Integration Reviewer:** DT Integration Lead
> **Control Total:** 142 registered DT assets; ~2,800 sensor data points expected at full population.

This standalone sensor map is the canonical source of truth for physical sensor placement and calibration governance for the **Personal Electronics** factory. All entries must be consistent with the asset registry in [`digital-twin.md`](../digital-twin.md) §2 and the anchor coordinates in [`bim/asset-anchors.md`](./bim/asset-anchors.md).

---

## 1. Sensor Registry

The table below records one row per sensor/data-point integration. Rows marked `[PENDING]` are pre-declared entries awaiting population from the MES sensor inventory data-load (target: 2026-Q1).

| Sensor ID | Sensor Model | Sensor Type | Location (Zone) | Mounted On (Asset ID) | Anchor Ref | Protocol | Calibration Interval | Last Calibration | Data Owner | Notes |
|-----------|--------------|-------------|------------------|-----------------------|------------|----------|----------------------|------------------|------------|-------|
| SEN-SMT-L1-SPI-001 | Koh Young KY8030-3 | 3D SPI | Z2 | DT-SMT-L1-02 | A-SMT-L1-02 | SECS/GEM | 6 months | [PENDING] | SMT Engineering | Paste volume CPK |
| SEN-SMT-L1-AOI-001 | Koh Young Zenith | 2D/3D AOI | Z2 | DT-SMT-L1-06 | A-SMT-L1-06 | SECS/GEM | 6 months | [PENDING] | SMT Engineering | FPY per board |
| SEN-SMT-L1-XRAY-001 | Unicomp AX8200 | X-Ray | Z2 | DT-SMT-L1-07 | A-SMT-L1-07 | REST API | 12 months | [PENDING] | SMT Engineering | BGA void analysis |
| SEN-SMT-L1-REFLOW-TEMP-001 | Heller 1964 MK5 | Zone Temperature ×8 | Z2 | DT-SMT-L1-05 | A-SMT-L1-05 | OPC-UA | 3 months | [PENDING] | SMT Engineering | Zone temps 1–8 |
| SEN-SMT-L1-ICT-001 | Keysight I1000D | In-Circuit Test | Z2 | DT-SMT-L1-09 | A-SMT-L1-09 | VISA/LAN | 12 months | [PENDING] | Quality Engineering | Net test pass/fail |
| SEN-RF-NCC-001 | R&S CMW500 | RF Network Analyser | Z8 | DT-RF-03 | A-RF-03 | VISA/LAN | 12 months | [PENDING] | RF Engineering | TRP/TIS NCC |
| SEN-RF-SPEC-001 | Keysight N9020B | Spectrum Analyser | Z8 | DT-RF-04 | A-RF-04 | VISA/LAN | 12 months | [PENDING] | RF Engineering | Spurious emission sweep |
| SEN-EN-PV-001 | Sungrow SH250HX (string monitor) | Energy / PV Generation | Factory Roof | DT-EN-PV-01 | A-EN-PV-01 | Modbus TCP | 12 months | [PENDING] | Energy Team | kW real-time |
| SEN-EN-BESS-001 | BMS (integrated) | Battery SoC/SoH | North Yard | DT-EN-BESS-01 | A-EN-BESS-01 | CAN / Modbus | 6 months | [PENDING] | Energy Team | Cell temp, voltage |
| SEN-EN-GRID-001 | AMI Grid Meter | Grid Import kW | HV Substation | DT-EN-GRID-01 | A-EN-GRID-01 | Modbus TCP | 12 months | [PENDING] | Energy Team | ToU period flag |
| SEN-AMR-001 | MiR Fleet (API) | Position / Mission | Main Floor | DT-AMR-MIR250-01 | A-AMR-MIR250-01 | REST API | N/A | N/A | OT Engineering | x, y, θ, SoC |
| [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] | Remaining ~2,789 entries to be loaded from MES sensor inventory — target 2026-Q1 |

---

## 2. Naming and Mapping Rules

- `Location (Zone)` values MUST match zone IDs defined in [`floor-plan.md`](../floor-plan.md).
- `Mounted On (Asset ID)` values MUST match asset IDs in [`digital-twin.md`](../digital-twin.md) §2.
- `Anchor Ref` values MUST match `BIM Anchor ID` entries in [`bim/asset-anchors.md`](./bim/asset-anchors.md).
- `Sensor ID` format: `SEN-<ZONE_PREFIX>-<ASSET_PREFIX>-<SEQ>` (zero-padded 3 digits).
- `Calibration Interval` is mandatory for all measurement sensors; enter `N/A` only for positional/status sensors with no calibration requirement.

---

## 3. Integration Reviewer Responsibilities

The **DT Integration Lead** is responsible for:

1. Reviewing all new entries before merge to confirm Asset ID and Anchor Ref cross-document consistency.
2. Signing off the control total (target: 2,800 data points) at full population.
3. Approving any sensor retirement or re-categorisation that affects anchor mapping.
4. Confirming calibration interval compliance during Gate 4 readiness review.

---

## 4. Documentation QA Checklist

Before marking this document as fully populated, the following checks must be completed:

| Check | Description | Status |
|-------|-------------|--------|
| QA-01 | All ~2,800 sensor rows are populated (no `[PENDING]` data rows remaining) | ⏳ Open — target 2026-Q1 |
| QA-02 | Every `Mounted On (Asset ID)` exists in `digital-twin.md` §2 asset registry | ⏳ Open — blocked on full population |
| QA-03 | Every `Anchor Ref` exists in `bim/asset-anchors.md` register | ⏳ Open — blocked on full population |
| QA-04 | Every `Location (Zone)` matches a zone ID in `floor-plan.md` | ⏳ Open — blocked on full population |
| QA-05 | Calibration intervals set for all measurement sensors | ⏳ Open — blocked on full population |
| QA-06 | Integration Reviewer sign-off on control total | ⏳ Open — pending QA-01 completion |
| QA-07 | `mkdocs build --strict` passes with no broken links | ✅ Closed |

---

## Related Documents

| Document | Purpose |
|----------|---------|
| [`digital-twin.md`](../digital-twin.md) | Asset registry (§2) and sensor coverage map overview (§3) |
| [`bim/asset-anchors.md`](./bim/asset-anchors.md) | BIM anchor coordinates referenced by `Anchor Ref` column |
| [`floor-plan.md`](../floor-plan.md) | Zone IDs and spatial layout |
| [`gap-closure-report.md`](./gap-closure-report.md) | Gap closure status for sensor registry completeness |

