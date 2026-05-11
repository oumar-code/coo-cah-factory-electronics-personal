#!/usr/bin/env python3
import argparse
import json
import random
import time
from collections import deque
from pathlib import Path

import yaml

try:
    import paho.mqtt.client as mqtt
except Exception:
    mqtt = None


def metric_value(metric: str, scenario: str):
    base = {
        "zone1_temp_c": random.uniform(190, 230),
        "zone7_temp_c": random.uniform(238, 248),
        "conveyor_speed_mm_min": random.uniform(700, 1000),
        "torque_nm": random.uniform(0.2, 0.5),
        "sensitivity_db": random.uniform(86, 100),
        "thd_pct": random.uniform(0.1, 2.5),
        "pressure_bar": random.uniform(1.0, 5.0),
        "capacity_mah": random.uniform(4800, 21000),
        "ir_mohm": random.uniform(20, 90),
        "trp_dbm": random.uniform(18, 26),
        "tis_dbm": random.uniform(-104, -90),
        "pos_x_m": random.uniform(0, 120),
        "pos_y_m": random.uniform(0, 90),
        "pos_theta_deg": random.uniform(0, 360),
        "battery_soc_pct": random.uniform(35, 95),
        "amr_soc_pct": random.uniform(35, 95),
        "charge_current_a": random.uniform(0, 18),
        "generation_kw": random.uniform(120, 620),
        "irradiance_w_m2": random.uniform(300, 1100),
        "soc_pct": random.uniform(25, 95),
        "soh_pct": random.uniform(95, 100),
        "charge_discharge_kw": random.uniform(-180, 180),
        "machine_state": random.choice(["RUN", "IDLE", "SETUP"]),
        "alarm_active": False,
        "result_ok_nok": random.choice(["OK", "OK", "OK", "NOK"]),
        "flash_result": random.choice(["PASS", "PASS", "FAIL"]),
        "firmware_version": random.choice(["1.0.3", "1.0.4", "1.1.0"]),
        "pass_fail": random.choice(["PASS", "PASS", "FAIL"]),
        "overall_result": random.choice(["PASS", "PASS", "FAIL"]),
        "dock_occupied": random.choice([True, False]),
        "mission_status": random.choice(["IDLE", "EXECUTING", "CHARGING"]),
    }.get(metric, random.uniform(0, 100))

    if scenario == "warning" and isinstance(base, (int, float)):
        return base * 1.1
    if scenario == "alarm":
        if metric in {"alarm_active"}:
            return True
        if metric in {"machine_state"}:
            return "ALARM"
        if isinstance(base, (int, float)):
            return base * 1.35
    return base


def build_topic(factory, site, zone, asset_id, metric, instance=None):
    if instance:
        return f"{factory}/{site}/{zone}/{asset_id}/{instance}/{metric}"
    return f"{factory}/{site}/{zone}/{asset_id}/{metric}"


def main():
    parser = argparse.ArgumentParser(description="DT synthetic telemetry publisher")
    parser.add_argument("--profile", required=True)
    parser.add_argument("--scenario", default="normal", choices=["normal", "warning", "alarm", "missing", "delayed", "burst", "wan_outage_recovery"])
    parser.add_argument("--duration", type=int, default=300)
    parser.add_argument("--mqtt-host", default="")
    parser.add_argument("--mqtt-port", type=int, default=1883)
    args = parser.parse_args()

    profile = yaml.safe_load(Path(args.profile).read_text())
    factory = profile["factory"]
    site = profile["site"]

    client = None
    if args.mqtt_host and mqtt:
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        client.connect(args.mqtt_host, args.mqtt_port, 60)
        client.loop_start()

    start = time.time()
    buffer = deque()
    tick = 0
    next_emit = {}
    assets = profile["assets"]

    while time.time() - start < args.duration:
        tick += 1
        now = time.time()
        for idx, asset in enumerate(assets):
            freq = float(asset.get("update_frequency_s", 1))
            freq = max(0.1, freq)
            if now < next_emit.get(idx, 0.0):
                continue
            next_emit[idx] = now + freq

            instances = asset.get("instances") or [None]
            for instance in instances:
                for metric in asset["metrics"]:
                    if args.scenario == "missing" and random.random() < 0.25:
                        continue

                    topic = build_topic(factory, site, asset["zone"], asset["asset_id"], metric, instance)
                    payload = {
                        "ts": int(time.time() * 1000),
                        "value": metric_value(metric, args.scenario),
                        "scenario": args.scenario,
                    }

                    if args.scenario == "wan_outage_recovery" and tick < 25:
                        buffer.append((topic, payload))
                        continue

                    if client:
                        if args.scenario == "burst" and random.random() < 0.4:
                            client.publish(topic, json.dumps(payload), qos=0)
                        client.publish(topic, json.dumps(payload), qos=1)
                    else:
                        print(json.dumps({"topic": topic, "payload": payload}))

        if args.scenario == "wan_outage_recovery" and tick == 25:
            while buffer:
                topic, payload = buffer.popleft()
                if client:
                    client.publish(topic, json.dumps(payload), qos=1)
                else:
                    print(json.dumps({"topic": topic, "payload": payload, "replayed": True}))

        if args.scenario == "delayed":
            time.sleep(1.6)
        elif args.scenario == "burst":
            time.sleep(0.2)
        else:
            time.sleep(1.0)

    if client:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
