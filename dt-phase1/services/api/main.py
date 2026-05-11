from pathlib import Path

import yaml
from fastapi import FastAPI

app = FastAPI(title="CCE DT Phase1 API", version="0.1.0")
PROFILE = Path(__file__).resolve().parents[2] / "contracts" / "synthetic-profile.yaml"


def profile_data():
    return yaml.safe_load(PROFILE.read_text())


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/v1/assets")
def assets():
    data = profile_data()
    return {"count": len(data["assets"]), "assets": data["assets"]}


@app.get("/api/v1/contracts/zones")
def zones():
    data = profile_data()
    return {"zones": data["zones"]}
