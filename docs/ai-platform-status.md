# Coo-Cah AI Platform — Deployment Status & Endpoint Registry

> **Project Coo-Cah | AI-Powered Manufacturing Ecosystem**
> **Factory:** Coo-Cah Personal Electronics Factory | **Location:** Sagamu Industrial Estate, Ogun State | **Phase:** Phase 1
> **Document Version:** 1.0 | **Owner:** AI Platform Team + MES / Digital Manufacturing Team
> **Status:** Phase 1 Baseline — Stub/Mock endpoints live; production model deployment in progress

This document records the deployment status of the Coo-Cah AI Platform and confirms which API
endpoints are live, which are running as validated stubs, and which are pending production model
deployment. It is the companion confirmation document to the API contract specifications in
[`mes-integration.md`](./mes-integration.md) §6.

> **Relationship to MES integration:** The MES consumes the AI Platform endpoints for real-time
> quality and operational decisions. This document must be updated at each deployment milestone
> and kept in sync with the API contracts in `mes-integration.md`.

---

## 1. Platform Deployment Summary

| Parameter                     | Value                                                              |
|-------------------------------|--------------------------------------------------------------------|
| AI Platform Host (Production) | `ai-platform.cce-sag.internal` (factory intranet)                |
| AI Platform Host (Cloud)      | `ai-platform.coo-cah.cloud` (Rwanda hub, HTTPS/TLS 1.3)           |
| Platform Framework            | FastAPI (Python 3.11) + Celery workers + Redis queue               |
| Model Serving                 | MLflow Model Registry + FastAPI prediction routes                  |
| Auth Method                   | JWT Bearer token (scoped per calling service)                      |
| MES → AI Platform auth        | Service account `svc-mes-aip` with API key (rotated 90 days)      |
| Base API URL (internal)       | `https://ai-platform.cce-sag.internal/api/v1/`                    |
| Base API URL (cloud fallback) | `https://ai-platform.coo-cah.cloud/api/v1/`                       |
| Infrastructure deployment     | Docker Compose stack on factory edge node VM + Rwanda cloud VM     |
| Status dashboard              | Grafana panel `AI-Platform-Health` on factory operations dashboard |
| Last deployment date          | 2026-04-15 (stub stack); production models: see Section 3          |

---

## 2. Endpoint Status Key

| Status Badge      | Meaning                                                                         |
|-------------------|---------------------------------------------------------------------------------|
| 🟢 **LIVE-PROD**  | Production model deployed; endpoint accepting real factory data                 |
| 🟡 **STUB**       | Endpoint is live and callable; returns schema-valid stub responses; production model pending |
| 🔴 **PENDING**    | Endpoint not yet deployed; integration tests blocked                            |
| 🔵 **PHASE-2**    | Planned for Phase 2; not required for Phase 1 go-live                           |

---

## 3. Endpoint Registry

### 3.1 SMT Defect Prediction API

**Contract:** `mes-integration.md` §6.1
**Endpoint:** `POST /api/v1/ai/smt-defect-predict`
**Status:** 🟡 **STUB**

| Attribute                 | Value                                                                      |
|---------------------------|----------------------------------------------------------------------------|
| Stub response             | Returns `defect_risk_score: 0.05`, `risk_level: "LOW"`, `recommended_action: "PROCEED"` |
| Stub validation           | Schema validation passes MES integration test suite (all required fields present, correct types) |
| Production model          | `smt-predict-v2.3` — training complete; pending factory FAT data ingestion for final calibration |
| Expected LIVE-PROD date   | Phase 1 SMT commissioning + 4 weeks of live data (~Q3 2026)               |
| Latency SLA               | ≤ 300 ms (p99) — stub currently returns in < 20 ms                        |
| MES integration test      | ✅ Passed (2026-04-22) — stub responses drive correct MES hold/proceed logic|
| Fallback behaviour        | If endpoint unreachable: MES defaults to `PROCEED` with alert raised to engineer |

**Stub deployment evidence:**

```
GET https://ai-platform.cce-sag.internal/api/v1/health
Response: {"status": "ok", "version": "1.0.0-stub", "models": {"smt-predict": "stub"}}
Last verified: 2026-04-22T14:30:00Z by MES Team Lead
```

---

### 3.2 RF Calibration & NCC Compliance AI API

**Contract:** `mes-integration.md` §6.2
**Endpoint:** `POST /api/v1/ai/rf-calibration`
**Status:** 🟡 **STUB**

| Attribute                 | Value                                                                        |
|---------------------------|------------------------------------------------------------------------------|
| Stub response             | Returns `rf_calibration_status: "PASS"`, `ncc_compliance: "COMPLIANT"`, `dispatch_cleared: true` |
| Stub validation           | Schema validation passes; NCC TA number pass-through logic confirmed correct |
| Production model          | `rf-cal-ncc-v1.0` — model spec complete; training data from NCC pre-compliance test runs needed |
| Expected LIVE-PROD date   | Phase 1 RF lab commissioning + NCC pre-compliance test runs (~Q4 2026)      |
| Latency SLA               | ≤ 500 ms (p99) — stub currently < 30 ms                                     |
| MES integration test      | ✅ Passed (2026-04-22) — stub responses drive correct dispatch-gate logic    |
| Fallback behaviour        | If endpoint unreachable: MES blocks dispatch; requires manual Regulatory Affairs override |

---

### 3.3 Production OEE & Scheduling API

**Contract:** `mes-integration.md` §6.3
**Endpoint:** `GET /api/v1/mes/oee/realtime`
**Status:** 🟡 **STUB**

| Attribute                 | Value                                                                  |
|---------------------------|------------------------------------------------------------------------|
| Stub response             | Returns factory-blended OEE 0.743 with static line entries (as per spec) |
| Stub validation           | Dashboard integration test passes; Grafana panel renders correctly     |
| Production feed           | Will be replaced by live InfluxDB → FastAPI aggregation once MES is live |
| Expected LIVE-PROD date   | Phase 1 MES go-live + 1 week of stable production data (~Q3 2026)     |
| Update interval           | 60-second refresh (stub); target 30-second refresh (production)        |
| MES integration test      | ✅ Passed (2026-04-22)                                                 |

---

### 3.4 AMR Fleet Mission Dispatch API

**Contract:** `mes-integration.md` §6.4
**Endpoint:** `POST /api/v1/amr/dispatch`
**Status:** 🟡 **STUB**

| Attribute                 | Value                                                                        |
|---------------------------|------------------------------------------------------------------------------|
| Stub response             | Returns `status: "DISPATCHED"`, assigns `MIR250-07` with estimated completion time |
| Stub validation           | MES mission-creation workflow test passes end-to-end with stub              |
| Production integration    | Will route to MiR Fleet Manager REST API once AMR fleet is on-site          |
| Expected LIVE-PROD date   | AMR fleet commissioning + MiR Fleet API integration testing (~Q3 2026 / M1.3) |
| Failure handling          | If endpoint unreachable: MES raises manual-move task to operator             |
| MES integration test      | ✅ Passed (2026-04-22)                                                      |

---

### 3.5 Additional Phase 2 Endpoints (Not Yet Deployed)

| Endpoint                                | Contract Location         | Status     | Phase |
|-----------------------------------------|---------------------------|------------|-------|
| `POST /api/v1/ai/predictive-maintenance`| Planned — Phase 2 spec    | 🔵 PHASE-2 | 2     |
| `GET /api/v1/ai/schedule-recommendation`| Planned — Phase 2 spec   | 🔵 PHASE-2 | 2     |
| `POST /api/v1/ai/cosmetic-qc`           | Planned — Phase 2 spec    | 🔵 PHASE-2 | 2     |
| `GET /api/v1/dt/simulation-trigger`     | Planned — Phase 2 spec    | 🔵 PHASE-2 | 2     |

---

## 4. Platform Health & Monitoring

| Monitoring Point                   | Implementation                                                      |
|------------------------------------|---------------------------------------------------------------------|
| Endpoint health check              | `GET /api/v1/health` — returns model status dict; polled every 60 s|
| Response time alerting             | Grafana alert if p99 latency > 500 ms for any endpoint             |
| Error rate alerting                | Alert if HTTP 5xx rate > 1% over 5-minute window                   |
| Model drift monitoring             | Placeholder — activated when production models deployed            |
| Auth token expiry alerting         | Alert 7 days before service account API key expiry                 |
| Uptime target (Phase 1)            | ≥ 99.5% during production hours (06:00–22:00 WAT)                  |
| Log retention                      | All API calls logged to InfluxDB `ai_platform_audit` measurement; 90-day rolling |

---

## 5. Stub-to-Production Transition Checklist

For each endpoint, the following must be completed before transitioning from STUB to LIVE-PROD:

- [ ] **smt-defect-predict:** Minimum 30 days of labelled SMT production data ingested; model re-trained and validated (AUC ≥ 0.85 on held-out validation set); shadow-mode comparison with stub complete
- [ ] **rf-calibration:** NCC pre-compliance RF test data from ≥ 3 SKUs ingested; model calibration offset prediction within ±0.5 dB of manual calibration; NCC review sign-off
- [ ] **oee/realtime:** Live InfluxDB query replaces stub; < 1% discrepancy vs. MES dashboard OEE counters over 5-day parallel run
- [ ] **amr/dispatch:** MiR Fleet Manager API integrated and tested; end-to-end mission creation latency < 2 s; AMR team sign-off
- [ ] All transitions approved by AI Platform Team Lead and MES Team Lead
- [ ] Updated endpoint status reflected in this document on transition date

---

## 6. Integration Test Evidence Summary

| Test                                | Date       | Result   | Tester                    |
|-------------------------------------|------------|----------|---------------------------|
| SMT Defect Predict stub — schema    | 2026-04-22 | ✅ PASS  | MES Integration Engineer  |
| RF Calibration stub — dispatch gate | 2026-04-22 | ✅ PASS  | MES Integration Engineer  |
| OEE endpoint — Grafana render       | 2026-04-22 | ✅ PASS  | MES Integration Engineer  |
| AMR Dispatch stub — mission create  | 2026-04-22 | ✅ PASS  | MES Integration Engineer  |
| Platform health check — endpoint up | 2026-04-22 | ✅ PASS  | DevOps / IT Lead          |
| Auth token validation               | 2026-04-22 | ✅ PASS  | DevOps / IT Lead          |

---

## 7. Related Documents

- For AI API contract specifications, refer to [`mes-integration.md`](./mes-integration.md) §6.
- For the MES phase 1 software setup and sandbox gate, refer to [`mes-phase1-software-setup.md`](./mes-phase1-software-setup.md).
- For sensor data consumed by the AI Platform, refer to [`sensor-map.md`](./sensor-map.md).
- For penetration test scope affecting API exposure and security controls, refer to [`pentest-scoping.md`](./pentest-scoping.md).
- For integrated closure gates and production-readiness sequencing, refer to [`bim-simulation-readiness-program.md`](./bim-simulation-readiness-program.md).
- For documentation gap-closure status and evidence mapping, refer to [`gap-closure-report.md`](./gap-closure-report.md).
