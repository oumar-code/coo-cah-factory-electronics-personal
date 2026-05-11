#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

import yaml

TOPIC_RE = re.compile(r"^[a-z0-9-]+/[a-z0-9-]+/[a-z0-9-]+/[a-z0-9-]+(?:/[0-9]{2})?/[a-z0-9_]+$")


def canonical_topic(factory, site, zone, asset_id, metric, instance=None):
    if instance:
        return f"{factory}/{site}/{zone}/{asset_id}/{instance}/{metric}"
    return f"{factory}/{site}/{zone}/{asset_id}/{metric}"


def main():
    parser = argparse.ArgumentParser(description="Validate synthetic profile coverage and topic contract")
    parser.add_argument("--profile", required=True)
    args = parser.parse_args()

    profile = yaml.safe_load(Path(args.profile).read_text())
    zones = set(profile["zones"])
    factory = profile["factory"]
    site = profile["site"]

    seen_topics = set()
    problems = []
    covered_zones = set()

    for asset in profile["assets"]:
        zone = asset["zone"]
        covered_zones.add(zone)
        if zone not in zones:
            problems.append(f"zone_not_declared:{zone}")
        for metric in asset["metrics"]:
            if not re.match(r"^[a-z0-9_]+$", metric):
                problems.append(f"metric_invalid:{asset['asset_id']}:{metric}")
            instances = asset.get("instances") or [None]
            for instance in instances:
                topic = canonical_topic(factory, site, zone, asset["asset_id"], metric, instance)
                if topic in seen_topics:
                    problems.append(f"duplicate_topic:{topic}")
                seen_topics.add(topic)
                if not TOPIC_RE.match(topic):
                    problems.append(f"topic_pattern_invalid:{topic}")

    gate = {
        "zones_declared": len(zones),
        "zones_covered": len(covered_zones),
        "topic_count": len(seen_topics),
        "has_contract_errors": len(problems) > 0,
        "acceptance_gate_pass": len(problems) == 0 and covered_zones == zones,
    }

    print(json.dumps({"gate": gate, "problems": problems}, indent=2))
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
