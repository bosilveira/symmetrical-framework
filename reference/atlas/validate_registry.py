#!/usr/bin/env python3
"""Structural and impact checks for the Symmetrical Framework object atlas.

Run from any directory:
    python reference/atlas/validate_registry.py
    python reference/atlas/validate_registry.py --impact SF-P-010
    python reference/atlas/validate_registry.py --impact SF-O-010 --json

No files are changed; all results are review queues, not proof certifications.
"""
from __future__ import annotations

import argparse
from collections import defaultdict, deque
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
REG = HERE / "registry.json"
CONTRACTS = HERE / "contracts.json"
REQUIRED_CONTRACT = {
    "map_id", "source", "target", "coordinate_map", "dependent_map",
    "parameter_rules", "invertibility", "differential_rule",
    "assumptions", "verification"
}
REQUIRED_PARAMETER = {
    "id", "name", "symbol", "scope", "domain", "meaning", "parameter_kind"
}


def load() -> tuple[dict, dict]:
    return json.loads(REG.read_text(encoding="utf-8")), json.loads(
        CONTRACTS.read_text(encoding="utf-8")
    )


def check_unique(items: list[dict], label: str, errors: list[str]) -> dict:
    result: dict = {}
    for item in items:
        identifier = item.get("id", item.get("map_id"))
        if not isinstance(identifier, str) or not identifier:
            errors.append(f"{label}: blank ID")
            continue
        if identifier in result:
            errors.append(f"{label}: duplicate ID {identifier}")
        result[identifier] = item
    return result


def validate(reg: dict, contract_data: dict) -> list[str]:
    errors: list[str] = []
    params = check_unique(reg.get("parameters", []), "parameter", errors)
    objects = check_unique(reg.get("objects", []), "object", errors)
    maps = check_unique(reg.get("maps", []), "map", errors)
    contracts = check_unique(contract_data.get("contracts", []), "contract", errors)

    for pid, p in params.items():
        missing = REQUIRED_PARAMETER - set(p)
        if missing:
            errors.append(f"{pid}: missing fields {sorted(missing)}")
        if not pid.startswith("SF-P-"):
            errors.append(f"{pid}: expected SF-P- prefix")

    printed_scope: dict[tuple[str, str], str] = {}
    for pid, p in params.items():
        key = (str(p.get("symbol")), str(p.get("scope")))
        if key in printed_scope:
            errors.append(
                f"ambiguous parameter scope {key}: {printed_scope[key]} and {pid}"
            )
        printed_scope[key] = pid

    for oid, obj in objects.items():
        if not oid.startswith("SF-O-"):
            errors.append(f"{oid}: expected SF-O- prefix")
        for pid in obj.get("parameters", []):
            if pid not in params:
                errors.append(f"{oid}: unknown parameter {pid}")
        for dep in obj.get("depends_on", []):
            if dep not in objects:
                errors.append(f"{oid}: unknown dependency {dep}")
            if dep == oid:
                errors.append(f"{oid}: self dependency")
        for path in obj.get("reference_paths", []):
            if not (REPO / path).is_file():
                errors.append(f"{oid}: missing reference path {path}")

    color: dict[str, int] = {}
    def visit(oid: str, stack: list[str]) -> None:
        if color.get(oid) == 2:
            return
        if color.get(oid) == 1:
            errors.append(f"derivation graph cycle: {' -> '.join(stack + [oid])}")
            return
        color[oid] = 1
        for dep in objects[oid].get("depends_on", []):
            if dep in objects:
                visit(dep, stack + [oid])
        color[oid] = 2

    for oid in objects:
        visit(oid, [])

    if set(maps) != set(contracts):
        errors.append(
            "map/contract ID mismatch: "
            f"registry-only={sorted(set(maps) - set(contracts))}; "
            f"contract-only={sorted(set(contracts) - set(maps))}"
        )
    for mid, item in maps.items():
        if not mid.startswith("SF-M-"):
            errors.append(f"{mid}: expected SF-M- prefix")
        for key in ("source_id", "target_id"):
            if item.get(key) not in objects:
                errors.append(f"{mid}: missing {key} {item.get(key)}")

    for mid, contract in contracts.items():
        missing = REQUIRED_CONTRACT - set(contract)
        if missing:
            errors.append(f"{mid}: missing contract fields {sorted(missing)}")
        if mid not in maps:
            continue
        for key, source_key in (("source", "source_id"), ("target", "target_id")):
            side = contract.get(key)
            if not isinstance(side, dict):
                errors.append(f"{mid}: {key} must be a typed object")
                continue
            if side.get("object_id") != maps[mid].get(source_key):
                errors.append(f"{mid}: {key} object disagrees with registry")
            for k in ("independent_variables", "dependent_variables"):
                if not isinstance(side.get(k), list):
                    errors.append(f"{mid}: {key}.{k} must be a list")
        if not isinstance(contract.get("coordinate_map"), list):
            errors.append(f"{mid}: coordinate_map must be a list")
        else:
            for c in contract["coordinate_map"]:
                if not isinstance(c, dict) or not all(
                    isinstance(c.get(k), str) and c[k].strip()
                    for k in ("from", "to", "forward", "inverse", "jacobian")
                ):
                    errors.append(f"{mid}: incomplete coordinate or Jacobian rule")
        if not isinstance(contract.get("dependent_map"), dict) or not all(
            isinstance(contract.get("dependent_map", {}).get(k), str)
            and contract["dependent_map"][k].strip()
            for k in ("forward", "inverse")
        ):
            errors.append(f"{mid}: missing dependent-field map or inverse")
        for rule in contract.get("parameter_rules", []):
            if not isinstance(rule, dict):
                errors.append(f"{mid}: invalid parameter rule type")
                continue
            for field in ("from", "to"):
                ids = rule.get(field, [])
                if not isinstance(ids, list):
                    errors.append(f"{mid}: parameter {field} must be list")
                    continue
                for pid in ids:
                    if pid not in params:
                        errors.append(f"{mid}: unknown {field} parameter {pid}")
            if not isinstance(rule.get("formula"), str) or not rule["formula"]:
                errors.append(f"{mid}: parameter rule missing formula")
        for k in ("invertibility", "differential_rule", "assumptions", "verification"):
            if not contract.get(k):
                errors.append(f"{mid}: missing {k} data")
        if isinstance(contract.get("invertibility"), dict):
            for k in ("functions", "equations", "lost"):
                if not contract["invertibility"].get(k):
                    errors.append(f"{mid}: invertibility.{k} not specified")

    if contract_data.get("source_registry") != "registry.json":
        errors.append("contracts.json must declare source_registry=registry.json")

    return errors


def impact(reg: dict, contracts: dict, item_id: str) -> dict:
    p = {x["id"]: x for x in reg["parameters"]}
    o = {x["id"]: x for x in reg["objects"]}
    m = {x["id"]: x for x in reg["maps"]}
    cm = {x["map_id"]: x for x in contracts["contracts"]}
    if item_id not in p and item_id not in o and item_id not in m:
        raise ValueError(f"Unknown ID {item_id}")
    reverse: dict[str, set[str]] = defaultdict(set)
    for obj in o.values():
        for dep in obj["depends_on"]:
            reverse[dep].add(obj["id"])
    direct = set()
    if item_id in p:
        direct = {obj["id"] for obj in o.values()
                  if item_id in obj.get("parameters", [])}
        for mc in cm.values():
            for rule in mc.get("parameter_rules", []):
                if item_id in rule.get("from", []) or item_id in rule.get("to", []):
                    direct.add(mc["source"]["object_id"])
                    direct.add(mc["target"]["object_id"])
    elif item_id in o:
        direct = {item_id}
    else:
        direct = {m[item_id]["source_id"], m[item_id]["target_id"]}
    seen = set(direct)
    queue = deque(sorted(direct))
    while queue:
        for next_id in sorted(reverse[queue.popleft()]):
            if next_id not in seen:
                seen.add(next_id)
                queue.append(next_id)
    touching = sorted(
        mid for mid, mc in cm.items()
        if mc["source"]["object_id"] in seen or mc["target"]["object_id"] in seen
    )
    paths = sorted({
        path for obj_id in seen for path in o[obj_id].get("reference_paths", [])
    })
    return {
        "target": item_id,
        "notice": "Read-only review queue; mathematical validity of dependents is not presumed to change.",
        "directly_affected_objects": sorted(direct),
        "all_downstream_objects": sorted(seen),
        "transformation_contracts_to_review": touching,
        "source_files_to_inspect": paths,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--impact", metavar="SF-ID",
                        help="compute downstream object/contract review queue")
    parser.add_argument("--json", action="store_true",
                        help="print JSON rather than concise console text")
    args = parser.parse_args()
    reg, contracts = load()
    errors = validate(reg, contracts)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} registry errors", file=sys.stderr)
        return 1
    if args.impact:
        try:
            result = impact(reg, contracts, args.impact)
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 2
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"Review target: {args.impact}")
            print("Direct objects: " + ", ".join(result["directly_affected_objects"]))
            print("Downstream objects: " + ", ".join(result["all_downstream_objects"]))
            print("Review contracts: " + ", ".join(result["transformation_contracts_to_review"]))
            print("Source paths:")
            for path in result["source_files_to_inspect"]:
                print("  " + path)
    else:
        print(
            "PASS: "
            f"{len(reg['objects'])} objects, "
            f"{len(reg['parameters'])} scoped parameters, "
            f"{len(reg['maps'])} map records and "
            f"{len(contracts['contracts'])} typed contracts; "
            "DAG and referenced paths valid."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
