# Personal Electronics Factory — Automation Roadmap

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1
> **Document Version:** 1.0 | **Owner:** Automation & Digital Manufacturing Team

---

## 1. Automation Strategy Overview

The Coo-Cah Personal Electronics Factory follows a staged automation programme across three phases spanning 2025–2030. The strategy prioritises production continuity and operator safety, ensuring no automation-driven redundancy occurs without concurrent redeployment or upskilling plans. Each phase builds on the capability established in the previous phase and is gated by defined technical and financial milestones.

| Phase | Period      | Theme                                    | Investment (₦B) | Target OEE | Jobs Created / Transitioned |
|-------|-------------|------------------------------------------|-----------------|------------|------------------------------|
| 1     | 2025–2026   | Foundation: MES + AMRs + SMT Integration | 1.6             | 72–75%     | +450 direct                  |
| 2     | 2027–2028   | Intelligence: Robot Assembly + AI Vision | 2.8             | 80–83%     | +60 advanced; 40 redeployed  |
| 3     | 2029–2030   | Autonomy: Lights-Out SMT + Adaptive WIP  | 2.2             | 88–90%     | +25 tech; 30 redeployed      |

---

## 2. Phase 1: Foundation Automation (2025–2026)

### 2.1 Phase 1 Description

Phase 1 establishes the core digital and physical automation layer: full MES deployment, AMR fleet (16 units), integrated SMT Lines 1 & 2 with MES feedback loops, and semi-automated phone assembly with MES-guided torque and flash stations. Operators are trained on MES interaction and basic ESD/SMT practices.

### 2.2 Phase 1 Milestone Table

| Milestone | Target Date | Description                                                     | Status         | KPI / Metric                     | Success Criteria                              |
|-----------|-------------|------------------------------------------------------------------|----------------|----------------------------------|-----------------------------------------------|
| M1.1      | Q1 2025     | Factory civil works and services commissioned                   | Planned        | Certificate of Occupancy         | CO issued; ESD flooring complete               |
| M1.2      | Q2 2025     | SMT Lines 1 & 2 installed, qualified, running production        | Planned        | First Article Inspection Pass    | First 100 boards defect-free (0-PPM FAI)      |
| M1.3      | Q2 2025     | AMR fleet (16 units) deployed and operational                   | Planned        | AMR mission success rate         | ≥ 97% mission success rate from week 1        |
| M1.4      | Q3 2025     | MES Phase 1 live: production order, WIP tracking, traceability  | Planned        | MES coverage (% stations)       | ≥ 90% production stations MES-connected       |
| M1.5      | Q3 2025     | Phone assembly lines PH-1, PH-2, PH-3 at target capacity       | Planned        | Units/day vs. target             | 2,000 phones/day all 3 lines combined          |
| M1.6      | Q3 2025     | NCC Type Approval secured for CCE-FP-3G, CCE-SP-LITE           | Planned        | NCC TA certificate issued        | Certificates issued for first 2 products       |
| M1.7      | Q4 2025     | RF production calibration automated (MES-linked)               | Planned        | Calibration cycle time           | RF calibration < 45 sec/unit                  |
| M1.8      | Q4 2025     | TWS + Smartwatch lines at capacity; NCC TA for BT products      | Planned        | Units/day vs. target             | 5,000 TWS pairs/day; NCC TA for CCE-TWS-01    |
| M1.9      | Q1 2026     | BESS + Solar 850 kWp fully commissioned                         | Planned        | Solar self-sufficiency ratio     | ≥ 75% in first 3 months post-commissioning    |
| M1.10     | Q2 2026     | Phase 1 OEE target achieved on SMT lines                        | Planned        | OEE (Availability × Performance × Quality) | SMT OEE ≥ 72%                   |

### 2.3 Phase 1 Automation Technologies

| Technology                        | Zone Applied        | Description                                                   | Integration   |
|-----------------------------------|---------------------|---------------------------------------------------------------|---------------|
| SMT Full-Line Integration         | Z2, Z3              | All SMT equipment linked in sequence via SMEMA; pass/fail gates | MES / SMEMA   |
| SPI + AOI AI Baseline Models      | Z2, Z3              | Koh Young AI engine baseline trained on Coo-Cah solder profiles | MES / AI     |
| 16× AMR Fleet (MiR Fleet)         | All zones           | LiDAR SLAM autonomous navigation; dynamic route planning       | MES WMS       |
| MES-Linked Torque Stations        | Z4, Z5              | Atlas Copco QMX4 torque results logged directly to MES job card | OPC-UA        |
| IMEI/Serial Flash Automation      | Z4                  | Automated IMEI burning; MES confirms uniqueness before writing | MES API       |
| Software Flash Automation         | Z4                  | 6-up Android flash fixtures; MES triggers OTA + validation    | MES REST API  |
| Battery Charge QC Automation      | Z7                  | Chroma 17020 fully automated cycle; pass/fail gate in MES     | Ethernet/MES  |
| Power Failure Resilience (ATS)    | Factory-wide        | ATS (20ms) switches to BESS/generator on grid failure         | EMS           |
| EMS — Energy Management System    | Factory-wide        | Sungrow iSolarCloud + Coo-Cah EMS for energy optimisation     | MES / SCADA   |

---

## 3. Phase 2: Intelligence Automation (2027–2028)

### 3.1 Phase 2 Description

Phase 2 introduces collaborative robots (cobots) to high-repetition assembly tasks in phone assembly, deploys AI vision QC at 100% of outgoing units, and extends AI-driven predictive maintenance across all SMT equipment. The goal is to reduce phone assembly cycle time by 30% and achieve > 80% OEE factory-wide.

### 3.2 Phase 2 Milestone Table

| Milestone | Target Date | Description                                                       | Status    | KPI / Metric                      | Success Criteria                              |
|-----------|-------------|-------------------------------------------------------------------|-----------|-----------------------------------|-----------------------------------------------|
| M2.1      | Q1 2027     | Cobot (UR20) deployment at screen bonding stations (Z4)           | Planned   | Cycle time vs. manual baseline    | Screen bond cycle ≤ 28 sec; defect rate ≤ 0.5% |
| M2.2      | Q2 2027     | Cobot deployment at rear case assembly + ultrasonic stations (Z4) | Planned   | OEE Phone Lines PH-2, PH-3        | OEE ≥ 78% on both lines                       |
| M2.3      | Q2 2027     | AI Vision 100% cosmetic QC deployed (all 3 phone lines)           | Planned   | Cosmetic escape rate              | Cosmetic defect escape ≤ 200 PPM              |
| M2.4      | Q3 2027     | Predictive maintenance AI live (SMT oven, P&P feeder health)      | Planned   | Unplanned SMT downtime            | Unplanned SMT downtime < 2%                   |
| M2.5      | Q3 2027     | NCC Type Approval Phase 2: CCE-SP-MID, CCE-SW-PRO, CCE-TWS-PRO   | Planned   | NCC TA certificates               | All 3 Phase 2 products type-approved          |
| M2.6      | Q4 2027     | SCARA robots deployed for TWS driver insertion (Z5)               | Planned   | TWS yield rate                    | TWS 1st-pass yield ≥ 97%                      |
| M2.7      | Q1 2028     | AI-powered MES scheduling (dynamic OEE-based order sequencing)    | Planned   | Schedule adherence                | On-time completion ≥ 94%                      |
| M2.8      | Q2 2028     | Phase 2 OEE target achieved factory-wide                          | Planned   | Blended factory OEE               | ≥ 80% blended; SMT OEE ≥ 84%                  |
| M2.9      | Q2 2028     | Digital twin Phase 2 synchronised (all cobots + AI vision data)   | Planned   | DT data lag vs. physical          | Digital twin data lag ≤ 500 ms                |

### 3.3 Phase 2 Automation Technologies

| Technology                         | Zone Applied | Description                                                   | Integration     |
|------------------------------------|--------------|---------------------------------------------------------------|-----------------|
| Collaborative Robots (UR20)        | Z4           | ISO/TS 15066 cobot; screen bond, case press, screw stations   | MES / OPC-UA    |
| SCARA Robots (Epson G-Series)      | Z5, Z6       | TWS driver insertion; watch sensor placement                  | MES / OPC-UA    |
| AI Visual Inspection (Cognex IS9000)| Z4, Z9      | 100% cosmetic inspection; learning model updated monthly      | MES / MQTT      |
| Predictive Maintenance AI          | Z2, Z3       | Vibration/temperature monitoring on JUKI P&P feeders + ovens  | AI Platform     |
| Dynamic MES Scheduling AI          | Factory-wide | AI engine optimises production sequence based on real-time OEE | MES            |
| Digital Twin — Phase 2 Expansion   | Factory-wide | Cobot + vision data feeds digital twin simulation layer        | Digital Twin    |

---

## 4. Phase 3: Autonomy (Lights-Out SMT) (2029–2030)

### 4.1 Phase 3 Description

Phase 3 targets near-lights-out operation of the two SMT lines during overnight shifts (22:00–06:00) and full adaptive WIP management via AI. Human operators supervise via remote monitoring. SMT line changeover will be reduced to < 15 minutes via automated feeder systems and recipe-driven stencil management. Assembly lines continue to require operator-present staffing.

### 4.2 Phase 3 Milestone Table

| Milestone | Target Date | Description                                                         | Status    | KPI / Metric                    | Success Criteria                           |
|-----------|-------------|---------------------------------------------------------------------|-----------|----------------------------------|---------------------------------------------|
| M3.1      | Q1 2029     | Automated SMT feeder loading system installed (JUKI Auto-Loader)   | Planned   | Feeder change time               | SMT line changeover ≤ 15 min              |
| M3.2      | Q2 2029     | Lights-out SMT trial: 4h overnight unattended run (1 supervisor)    | Planned   | SMT OEE (overnight) vs daytime  | Overnight OEE ≥ 87% vs daytime baseline    |
| M3.3      | Q3 2029     | Adaptive WIP AI: real-time flow balancing across all assembly lines | Planned   | WIP inventory turns/day          | WIP turns > 8×/day; no starvation events   |
| M3.4      | Q4 2029     | Full lights-out SMT (both lines, 8h/night); 2 supervisors only     | Planned   | Unplanned stops per night        | < 1 unplanned stop per night               |
| M3.5      | Q1 2030     | AI-driven yield prediction model live (pre-empts SMT defects)       | Planned   | SMT first-pass yield              | SMT FPY ≥ 99.2%                           |
| M3.6      | Q2 2030     | Phase 3 OEE target achieved                                         | Planned   | Blended factory OEE              | ≥ 88% blended; SMT OEE ≥ 92%              |

---

## 5. Workforce Transition Plan

Automation at the Coo-Cah Personal Electronics Factory is designed to complement and upskill the workforce, not to replace jobs. All transitions are supported by the Coo-Cah Academy training programme.

| Phase | Roles Automated / Assisted           | Redeployment / Upskilling Path                         | Net Headcount Impact |
|-------|---------------------------------------|--------------------------------------------------------|----------------------|
| 1     | Manual WIP transport (replaced by AMR) | AMR Fleet Operators / MES Data Entry Officers         | +10 tech roles       |
| 2     | Screen bond manual stations (cobot)   | Cobot Cell Technicians; AI Vision Quality Engineers    | Neutral (reassigned) |
| 2     | TWS driver insertion (SCARA)          | Wearables Process Technician; Precision Assembly Lead  | Neutral (reassigned) |
| 3     | SMT overnight operators (lights-out)  | SMT Night Supervisor (remote); Automation Analyst     | -6 / +3 = -3 net     |

**Key Principle:** No operator is made redundant against their will. The Coo-Cah People Policy commits to retraining all automation-displaced staff into higher-value technical roles. Any residual surplus is managed through voluntary redeployment to other Coo-Cah factories in the ecosystem.

---

## 6. Automation KPI Dashboard

| KPI                              | Phase 1 Target | Phase 2 Target | Phase 3 Target | Measurement Method              |
|----------------------------------|----------------|----------------|----------------|---------------------------------|
| Factory OEE (blended)            | 72–75%         | 80–83%         | 88–90%         | MES OEE module                  |
| SMT First-Pass Yield             | ≥ 97.0%        | ≥ 98.5%        | ≥ 99.2%        | MES SMT quality data            |
| Phone Assembly Defect Rate       | ≤ 2,500 PPM    | ≤ 800 PPM      | ≤ 300 PPM      | MES final test failure data     |
| AMR Mission Success Rate         | ≥ 97%          | ≥ 98.5%        | ≥ 99%          | MiR Fleet Manager               |
| Mean Time Between Failure (MTBF) | ≥ 400 h        | ≥ 600 h        | ≥ 900 h        | MES maintenance module          |
| Mean Time To Repair (MTTR)       | ≤ 3 h          | ≤ 2 h          | ≤ 1.5 h        | MES maintenance module          |
| Changeover Time (SMT)            | ≤ 90 min       | ≤ 45 min       | ≤ 15 min       | MES production event timestamps |
| Energy per Unit — Phone          | ≤ 4.8 kWh      | ≤ 4.0 kWh      | ≤ 3.2 kWh      | EMS ÷ MES production            |
| On-Time Delivery to Distribution | ≥ 92%          | ≥ 95%          | ≥ 97%          | MES delivery performance        |
| NCC Type Approvals Active        | 5              | 8              | 12             | Regulatory register             |

---

*For MES integration details, refer to [`mes-integration.md`](./mes-integration.md).*
*For digital twin and simulation capabilities, refer to [`digital-twin.md`](./digital-twin.md).*
*For CapEx investment per automation phase, refer to [`capex-opex.md`](./capex-opex.md).*
