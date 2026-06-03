# DT Phase 1 Software Infrastructure & Synthetic Proving Kit

This folder implements the **Phase 1 without machines** execution baseline:

- foundation freeze and controlled contracts
- DEV-first DT platform proving
- synthetic telemetry for offline commissioning
- design-spec offline simulation baseline
- contract/coverage validation before pilot acceptance

## Contents

- `docker-compose.yml` — local dev proving stack (Mosquitto, InfluxDB, Grafana, Telegraf, FastAPI)
- `contracts/synthetic-profile.yaml` — canonical telemetry profile and zone/asset coverage
- `services/synthetic_publisher.py` — synthetic MQTT publisher with operating-state scenarios
- `services/offline_simulation.py` — design-spec baseline simulation runner
- `services/coverage_validator.py` — topic-pattern and coverage acceptance validator

## Quickstart

```bash
cd dt-phase1
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python services/coverage_validator.py --profile contracts/synthetic-profile.yaml
```

Start the stack:

```bash
docker compose up -d
```

Run synthetic telemetry:

```bash
python services/synthetic_publisher.py \
  --profile contracts/synthetic-profile.yaml \
  --scenario normal \
  --duration 180 \
  --mqtt-host localhost \
  --mqtt-port 1883
```

Run operating-state drills:

```bash
python services/synthetic_publisher.py --profile contracts/synthetic-profile.yaml --scenario warning --duration 120 --mqtt-host localhost
python services/synthetic_publisher.py --profile contracts/synthetic-profile.yaml --scenario alarm --duration 120 --mqtt-host localhost
python services/synthetic_publisher.py --profile contracts/synthetic-profile.yaml --scenario missing --duration 120 --mqtt-host localhost
python services/synthetic_publisher.py --profile contracts/synthetic-profile.yaml --scenario delayed --duration 120 --mqtt-host localhost
python services/synthetic_publisher.py --profile contracts/synthetic-profile.yaml --scenario burst --duration 120 --mqtt-host localhost
python services/synthetic_publisher.py --profile contracts/synthetic-profile.yaml --scenario wan_outage_recovery --duration 120 --mqtt-host localhost
```

Run offline design-spec simulation:

```bash
python services/offline_simulation.py --hours 24 --phone-mix 0.5 --earbud-mix 0.35 --watch-mix 0.15 --seed 42 --out simulation-baseline.json
```

## Promotion Path

- **DEV**: local/cloud synthetic proving (this kit)
- **STAGING**: edge-node pre-commissioning synthetic proving
- **PROD**: live OT read-only ingestion during phased commissioning

## Acceptance Gate (before machine arrival)

- Contract validation passes (`coverage_validator.py`)
- All scenario drills executed and archived
- Dashboard and alert sign-off recorded
- Edge fallback and broker buffering tested
- Runbook and change-control evidence complete

## Important

Simulation outputs in this phase are **design-spec baselines** and must be recalibrated with real production data after commissioning.
