# Personal Electronics Factory — Energy Profile & Power Systems Design

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1
> **Document Version:** 1.0 | **Owner:** Energy & Infrastructure Team

---

## 1. Factory Power Demand Analysis

| # | Equipment / System                          | Rated Power (kW) | Duty Cycle (%) | Avg Load (kW) | Notes                                          |
|---|---------------------------------------------|------------------|----------------|---------------|------------------------------------------------|
| 1 | SMT Reflow Oven, Line 1 (Heller 1964 MK5)  | 80               | 85%            | 68            | High thermal mass; dominant process heat load  |
| 2 | SMT Reflow Oven, Line 2 (Heller 1964 MK5)  | 80               | 85%            | 68            | Both ovens peak simultaneously during normal ops |
| 3 | Pick-and-Place Machines ×4 (JUKI)           | 40               | 85%            | 34            | 10 kW each; 4 machines across 2 lines          |
| 4 | Wave / Selective Soldering ×2               | 30               | 60%            | 18            | Intermittent; selective solder for connectors  |
| 5 | Screen Bonding Machines ×2                  | 30               | 70%            | 21            | OCA vacuum bonding; autoclave (pressure heat)  |
| 6 | Phone Assembly Lines ×3 (conveyors/tools)   | 40               | 80%            | 32            | Motors, pneumatic drivers, conveyors           |
| 7 | TWS + Smartwatch Assembly Lines             | 20               | 75%            | 15            | Low-load precision assembly benches            |
| 8 | Power Bank Assembly + Test Rigs             | 25               | 75%            | 18.75         | Chroma battery cyclers; spot welders           |
| 9 | RF & NCC Type Test Chambers ×4              | 30               | 65%            | 19.5          | RF shielded rooms; signal generators; OTA      |
| 10| Battery QC & Cycle Test Rack                | 35               | 80%            | 28            | Chroma 17200 (32-ch); continuous charge cycle  |
| 11| IEC 62368-1 Safety Test Equipment           | 10               | 50%            | 5             | Hipot, drop test, thermal chamber intermittent |
| 12| Compressed Air (×2 Atlas Copco GA37)        | 74               | 60%            | 44.4          | 37 kW × 2; ring-main 8 bar throughout          |
| 13| HVAC (18,000 m² — 2 × Carrier chillers)    | 130              | 90%            | 117           | Largest sustained load; critical for SMT ESD zones |
| 14| Lighting — Production (LED, zoned)          | 50               | 100%           | 50            | 18,000 m² at 30W/m² occupancy-zoned LED       |
| 15| Lighting — Offices / Amenities              | 12               | 80%            | 9.6           | Motion sensor LED; office + amenities block    |
| 16| IT / MES / Edge Servers                     | 20               | 100%           | 20            | 24/7 load; MES servers + edge compute nodes   |
| 17| AMR Fleet Charging ×16 (MiR250/100)         | 30               | 40%            | 12            | Staggered opportunity charging; overnight bulk |
| 18| Packaging Lines ×2                          | 25               | 70%            | 17.5          | Carton erector, sealer, labeller, wrap         |
| 19| General Miscellaneous                       | 25               | 60%            | 15            | Hand tools, rework stations, ESD equipment     |

## 2. Power Summary

| Parameter                              | Value               |
|----------------------------------------|---------------------|
| Total Installed (Rated) Power          | 786 kW              |
| **Estimated Peak Simultaneous Load**   | **~550 kW**         |
| Average Operational Load (16h/day)     | ~380 kW             |
| Overnight Base Load (IT/HVAC/security) | ~60 kW              |
| **Daily Energy Consumption**           | **~3,800 kWh/day**  |
| **Annual Energy Consumption**          | **~1,140 MWh/year** |
| Power Factor (target)                  | ≥ 0.95              |

> **Demand Factor Basis:** Peak simultaneous load (550 kW) reflects a demand factor of 0.70 applied to total installed capacity of 786 kW. Peak occurs during the mid-morning production period when both reflow ovens, all 4 pick-and-place machines, HVAC, and battery test racks all operate concurrently.

---

## 3. Solar Site Assessment

### 3.1 Location Irradiance Data

| Parameter                              | Value              | Source                       |
|----------------------------------------|--------------------|------------------------------|
| Factory Location                       | Sagamu, Ogun State | —                            |
| Latitude / Longitude                   | 6.84° N, 3.65° E   | —                            |
| Peak Sun Hours (PSH) — Annual Average  | 4.7 hours/day      | NASA POWER / SolarGIS        |
| Peak Sun Hours — Worst Month           | 4.1 hrs/day        | July (cloudy season)         |
| Peak Sun Hours — Best Month            | 6.0 hrs/day        | January (harmattan, clear)   |
| Average GHI                            | 4.8 kWh/m²/day     | SolarGIS                     |
| Temperature Correction Factor          | 0.92               | Based on avg 30°C ambient    |

### 3.2 Rooftop / Ground Mount Area Assessment

| Zone                           | Available Area (m²) | Usable for Solar (m²) | Tilt Angle | Orientation | Estimated Yield     |
|--------------------------------|---------------------|-----------------------|------------|-------------|---------------------|
| Factory Roof — Main Building   | 9,500 m²            | 6,500 m²              | 10°        | South-facing | 1,160 kWh/kWp/year |
| Factory Roof — Warehouse Block | 3,200 m²            | 2,200 m²              | 10°        | South-facing | 1,160 kWh/kWp/year |
| Ground Mount — East Yard       | 2,000 m²            | 1,800 m²              | 10°        | South-facing | 1,180 kWh/kWp/year |
| **Total Available**            | **14,700 m²**       | **10,500 m²**         |            |             |                     |

---

## 4. Recommended Energy System

### 4.1 Solar PV — 850 kWp

**Calculation:**

```
Daily Demand:          3,800 kWh/day
Target Solar Supply:   80% = 3,040 kWh/day
Peak Sun Hours:        4.5 hrs/day (worst month basis — conservative sizing)
System Efficiency:     0.89

Required PV Capacity = 3,040 ÷ 4.5 ÷ 0.89
                     = 759 kWp

Rounded to: 850 kWp (12% design margin for soiling, degradation, cable losses)
```

**Recommended Solar PV System:**

| Parameter               | Specification                                         |
|-------------------------|-------------------------------------------------------|
| Installed Capacity      | 850 kWp                                               |
| Panel Technology        | Monocrystalline PERC, ≥ 21% efficiency               |
| Panel Wattage           | 580W per panel (Longi LR5-72HBD or equiv.)           |
| Number of Panels        | 1,465 panels                                          |
| Inverter Type           | Hybrid string inverter (solar + BESS integrated)      |
| Inverter Capacity       | 4 × Sungrow SH250HX (250 kW each)                   |
| Mounting System         | Roof ballast (main + warehouse), ground-mount (east)  |
| Estimated Annual Yield  | ~1,020 MWh/year (4.7 avg PSH)                        |

### 4.2 Battery Energy Storage System (BESS) — 900 kWh LFP

**Calculation:**

```
Overnight Base Load:     60 kW × 10 hrs         = 600 kWh
Morning Ramp (pre-solar): 220 kW × 1.5 hrs      = 330 kWh
Emergency Reserve (30 min peak):  100 kW × 0.5  =  50 kWh
Gross Required:          980 kWh
Adjusted for DoD (80%): 980 ÷ 0.80              = 1,225 kWh gross
Select commercial standard: 900 kWh usable (2 × 450 kWh rack systems)
(Note: grid available as top-up; full DoD capacity not required every cycle)
```

**Recommended BESS System:**

| Parameter               | Specification                                         |
|-------------------------|-------------------------------------------------------|
| Usable Capacity         | 900 kWh                                               |
| Chemistry               | LFP (Lithium Iron Phosphate)                          |
| Cycle Life              | ≥ 3,500 cycles @ 80% DoD                             |
| DC Voltage Bus          | 614V DC                                               |
| Form Factor             | 2 × containerised 20ft rack systems (450 kWh each)   |
| BMS                     | Active cell balancing, thermal management, fire detection |
| Preferred Suppliers     | CATL / BYD / Pylontech EnerS                          |
| Fire Suppression        | Built-in Novec 1230 gaseous suppression per container |
| Warranty                | ≥ 10 years / ≥ 3,500 cycles                           |

### 4.3 Grid Connection

| Parameter                         | Specification                                |
|-----------------------------------|----------------------------------------------|
| Grid Supply                       | Ogun-Osun DisCo — 11 kV intake              |
| Grid Connection Capacity          | 600 kW contracted demand                     |
| Role                              | Secondary backup + overnight top-up          |
| Smart Meter                       | AMI smart meter for ToU tariff management    |
| Import/Export Management          | Managed by hybrid inverter EMS               |
| Grid Failure Response             | ATS switches to BESS within 20 ms            |

### 4.4 Backup Generator

| Parameter              | Specification                                           |
|------------------------|---------------------------------------------------------|
| Generator Capacity     | 500 kVA (400 kW) standby                               |
| Fuel                   | Diesel                                                  |
| Auto-Start             | Yes — triggered by BESS SoC < 20% + grid failure       |
| Runtime                | ~72h at 40% load (2,000L bunded diesel tank)            |
| Emission Standard      | EU Stage IIIA equivalent (best available in Nigeria)    |
| Tank Capacity          | 2,000 L (bunded double-walled tank)                     |

---

## 5. Energy KPIs

| KPI                                   | Target            | Measurement Method          | Frequency  |
|---------------------------------------|-------------------|-----------------------------|------------|
| Solar Self-Sufficiency Ratio          | ≥ 80%             | EMS energy meter data       | Monthly    |
| BESS Cycle Utilisation                | ≥ 280 cycles/year | BMS cycle counter           | Annual     |
| Grid Import (% of total energy)       | ≤ 20%             | Smart meter data            | Monthly    |
| Energy Intensity (kWh/phone)          | ≤ 4.8 kWh/unit    | MES production ÷ EMS data   | Monthly    |
| Energy Intensity (kWh/earbud pair)    | ≤ 0.35 kWh/pair   | MES production ÷ EMS data   | Monthly    |
| Energy Intensity (kWh/smartwatch)     | ≤ 1.8 kWh/unit    | MES production ÷ EMS data   | Monthly    |
| Energy Intensity (kWh/power bank)     | ≤ 0.5 kWh/unit    | MES production ÷ EMS data   | Monthly    |
| Generator Run Hours                   | < 100 hrs/year    | Generator hour meter        | Annual     |
| Power Factor                          | ≥ 0.95            | Main MCC power analyser     | Monthly    |
| BESS State of Health (SoH) at Yr 5   | ≥ 85%             | BMS diagnostics             | Quarterly  |
| Annual CO₂ Avoidance                  | ~720 t CO₂/year   | Grid emission factor × solar| Annual     |
| Unplanned Power Downtime              | < 4 hrs/year      | EMS event log               | Annual     |

---

## 6. Grid Dependency Analysis

### 6.1 Scenario Analysis

| Scenario                           | Grid | Solar | BESS | Generator | Production Impact                   |
|------------------------------------|------|-------|------|-----------|--------------------------------------|
| Normal Day (Grid + Solar + BESS)   | ✅   | ✅    | ✅   | Off       | Full production; BESS charges        |
| Grid Failure (daytime)             | ❌   | ✅    | ✅   | Off       | Full production (solar primary)      |
| Grid Failure (night / overcast)    | ❌   | ❌    | ✅   | Standby   | Overnight base load + critical only  |
| Solar + Grid Failure (extended)    | ❌   | ❌    | ✅→❌ | ✅       | Critical production loads            |
| Total Outage (all sources)         | ❌   | ❌    | ❌   | ❌        | Emergency shutdown procedure         |

### 6.2 Critical Load Priority Tiers

| Priority         | Load Tier          | Systems Included                                              | Minimum Sustain Time |
|------------------|--------------------|---------------------------------------------------------------|----------------------|
| 1 — Critical     | Must Never Lose    | IT/MES servers, RF test equipment in mid-cycle, fire alarm    | 24 hrs (BESS)        |
| 2 — Essential    | Production Continuity | Both SMT lines, phone assembly, battery test, AMR fleet    | 8 hrs (BESS)         |
| 3 — Important    | Normal Operations  | TWS/watch assembly, packaging, warehousing, offices           | 4 hrs (BESS)         |
| 4 — Deferrable   | Comfort            | Non-production HVAC zones, EV/AMR opportunity charging        | Shed first           |

*Ogun State grid: Sagamu Industrial Estate typically receives 8–12h grid supply per day. The 850 kWp solar + 900 kWh BESS system is designed to sustain full 16-hour production without grid dependency.*

---

## 7. Energy Cost Analysis

### 7.1 Baseline (Grid Only) vs Solar + BESS Scenario

| Parameter                               | Grid Only            | Solar + BESS System        |
|-----------------------------------------|----------------------|----------------------------|
| Annual Energy Consumption               | ~1,140 MWh/year      | ~1,140 MWh/year            |
| Grid Import (annual)                    | 1,140 MWh            | ~230 MWh/year (20%)        |
| Average Grid Tariff                     | ₦100/kWh             | ₦100/kWh                   |
| Annual Grid Energy Cost                 | ₦114,000,000         | ₦23,000,000                |
| Solar + BESS Capital Cost               | —                    | ~₦2,100,000,000            |
| Annual O&M (solar + BESS)               | —                    | ~₦24,000,000/year          |
| Annual Savings vs Grid Only             | Baseline             | ~₦91,000,000/year          |
| Simple Payback (energy cost only)       | —                    | ~12.5 years                |
| 25-Year NPV (at 18% discount rate)      | —                    | ~₦180,000,000              |

> *Primary investment case: production continuity. Every hour of production downtime (from grid failure without solar + BESS) costs an estimated ₦12–18M in lost output. With Nigeria's current grid reliability, the solar + BESS system pays back in under 3 years on combined energy savings plus downtime avoidance.*

---

## 8. Energy Infrastructure Layout

```
PERSONAL ELECTRONICS FACTORY SITE (18,000 m²)
│
├── Rooftop Solar Arrays
│     ├── Zone A: Main Production Building Roof — 620 kWp
│     │         1,069 × Longi 580W panels; 3 × Sungrow SH250HX
│     └── Zone B: Warehouse Block Roof — 110 kWp
│               190 × Longi 580W panels; 1 × Sungrow SH110RT
│
├── Ground-Mount Solar Array (East Yard — 1,800 m²)
│     └── 120 kWp — 207 × Longi 580W panels
│           10° tilt, south-facing fixed-mount aluminium structure
│
├── BESS Enclosures (standalone, fire-rated, ventilated, north yard)
│     ├── Container 1: 450 kWh LFP rack (CATL/BYD)
│     └── Container 2: 450 kWh LFP rack (CATL/BYD)
│           Novec 1230 fire suppression; remote BMS monitoring
│
├── Hybrid Inverter / PCS Room (adjacent to BESS)
│     └── 4 × Sungrow SH250HX (250 kW each)
│           Coo-Cah EMS + iSolarCloud energy management
│
├── HV/LV Intake Substation (north boundary)
│     └── 11 kV → 415 V 630 kVA transformer
│           AMI smart meter; PFC capacitor banks
│
├── Main MCC (Electrical Room — production centre)
│     └── Sub-distribution boards per production zone
│           ESD-protected circuits for all SMT + electronics areas
│           ATS (Socomec 630A ×2) for generator/BESS switching
│
└── Backup Generator Pad (external, bunded, north-east corner)
      └── Perkins 500 kVA diesel generator
            2,000 L bunded double-wall diesel tank
```

---

## 9. Environmental & Sustainability Notes

- LFP chemistry selected for safety, longevity, and cobalt-free supply chain. Operating temperature range well-suited to Nigerian climate.
- Solar panel end-of-life: SON-registered e-waste recycling partner for panel disposal after 25–30 years.
- BESS second-life: Battery modules at 70%+ remaining capacity repurposed for Coo-Cah Smart Estate community storage before final recycling through certified partner.
- Annual CO₂ avoidance (~720 tonnes) to be tracked and verified annually. To be assessed for carbon credit generation under Article 6 Paris Agreement mechanisms.
- Diesel fuel and generator emissions tracked monthly; reported in Coo-Cah annual sustainability report.
- All LED lighting throughout factory; energy consumption per unit produced tracked as a KPI and published in the annual sustainability disclosure.

---

*For machine-level power ratings, refer to [`machinery.md`](./machinery.md).*
*For digital twin energy monitoring integration, refer to [`digital-twin.md`](./digital-twin.md).*
*For energy-related CapEx and OpEx, refer to [`capex-opex.md`](./capex-opex.md).*
