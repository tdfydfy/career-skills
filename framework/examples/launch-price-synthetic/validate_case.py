#!/usr/bin/env python3
"""Validate cross-file closure for the synthetic launch price report."""

from __future__ import annotations

from collections import Counter
import csv
import json
import math
from pathlib import Path
import re

import yaml


ROOT = Path(__file__).resolve().parent
ALLOWED_RATINGS = {"A", "B+", "B", "B-", "C+", "C", "C-", "D"}


def read_csv(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def main() -> int:
    errors: list[str] = []
    source = yaml.safe_load((ROOT / "source-data.yaml").read_text(encoding="utf-8"))
    generated = json.loads((ROOT / "generated-summary.json").read_text(encoding="utf-8"))
    launch_calc = json.loads((ROOT / "launch-calculation-output.json").read_text(encoding="utf-8"))
    full_calc = json.loads((ROOT / "full-project-calculation-output.json").read_text(encoding="utf-8"))
    units = read_csv("unit-price-schedule.csv")
    customers = read_csv("customer-ledger.csv")
    unconverted = read_csv("frozen-unconverted-ledger.csv")
    report = (ROOT / "report.md").read_text(encoding="utf-8")

    if len(units) != 156 or len({row["unit_id"] for row in units}) != 156:
        errors.append("unit schedule must contain 156 unique launch units")
    launch_area = sum(float(row["area_sqm"]) for row in units)
    launch_value = sum(float(row["total_price_yuan"]) for row in units)
    if launch_area != generated["launch"]["area"]:
        errors.append("launch area does not close")
    if launch_value != generated["launch"]["value"]:
        errors.append("launch value does not close")
    for row in units:
        net = float(row["requested_net_price_per_sqm"])
        floor = float(row["floor_price_per_sqm"])
        list_price = float(row["list_price_per_sqm"])
        if net < floor:
            errors.append(f"{row['unit_id']}: net price below floor")
        if abs(net / list_price - 0.97) > 0.0001:
            errors.append(f"{row['unit_id']}: list/net discount is not 3%")
    target_units = [row for row in units if row["target_sale"] == "yes"]
    target_value = sum(float(row["total_price_yuan"]) for row in target_units)
    if len(target_units) != source["launch_target"]["units"]:
        errors.append("target sale unit count does not close")
    if target_value != source["launch_target"]["contract_amount_yuan"]:
        errors.append("target sale value does not close to selected units")
    conversion = source["launch_target"]["conversion_assumption"]
    theoretical_subscription_target = math.ceil(source["launch_target"]["units"] / conversion)
    if launch_calc["subscription"]["subscription_target"] != theoretical_subscription_target:
        errors.append("theoretical subscription target does not match the conversion assumption")
    execution_subscription_target = 0
    for building, target in source["launch_target"]["by_building"].items():
        rows = [row for row in target_units if row["building"] == building]
        if len(rows) != target["target_units"]:
            errors.append(f"{building}: target sale units do not close")
        if sum(float(row["total_price_yuan"]) for row in rows) != target["target_contract_amount_yuan"]:
            errors.append(f"{building}: target sale value does not close")
        building_subscription_target = math.ceil(target["target_units"] / conversion)
        if target["target_subscription"] != building_subscription_target:
            errors.append(f"{building}: subscription target does not match 60% conversion")
        execution_subscription_target += target["target_subscription"]
    if execution_subscription_target != 182:
        errors.append("building-level execution subscription target must equal 182")

    if len(customers) != 184 or len({row["customer_code"] for row in customers}) != 184:
        errors.append("customer ledger must contain 184 unique customers")
    ratings = Counter(row["rating"] for row in customers)
    if set(ratings) - ALLOWED_RATINGS:
        errors.append("customer ledger contains invalid ratings")
    if dict(ratings) != source["customer_summary"]["ratings"]:
        errors.append("customer rating totals do not match source summary")
    products = Counter(row["first_choice_product"] for row in customers)
    if dict(products) != source["customer_summary"]["first_choice"]:
        errors.append("customer first-choice totals do not match source summary")
    if len(unconverted) != source["customer_summary"]["unconverted_frozen"]:
        errors.append("unconverted frozen customer count does not close")

    if launch_calc["inventory"]["total_units"] != source["project"]["residential_units"] - 292:
        errors.append("launch unit count does not match source")
    if full_calc["inventory"]["total_units"] != source["project"]["residential_units"]:
        errors.append("full project unit count does not close")
    if full_calc["inventory"]["total_area"] != source["project"]["residential_saleable_area_sqm"]:
        errors.append("full project area does not close")
    parking = source["parking"]
    if sum(item["planned"] for item in parking["categories"].values()) != parking["total"]:
        errors.append("parking planned quantities do not close")
    if sum(item["expected_sales"] for item in parking["categories"].values()) != parking["expected_sales"]:
        errors.append("parking expected sales do not close")
    parking_value = sum(
        item["expected_sales"] * item["average_price_yuan"]
        for item in parking["categories"].values()
    )
    if parking_value != parking["expected_value_yuan"]:
        errors.append("parking expected value does not close")

    slide_numbers = [int(value) for value in re.findall(r"^## 幻灯片 (\d+)", report, flags=re.MULTILINE)]
    if slide_numbers != list(range(1, 26)):
        errors.append("report must contain slides 1 through 25 exactly once")
    required_strings = ["23,658", "22,994", "33,748.75", "15,100", "11.3%", "184组"]
    for value in required_strings:
        if value not in report:
            errors.append(f"report is missing decision value {value}")

    if errors:
        print("synthetic case validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("synthetic case validation passed")
    print(f"launch units/area/value: {len(units)}/{launch_area:.0f}/{launch_value:.0f}")
    print(f"customers/ratings: {len(customers)}/{dict(ratings)}")
    print(f"subscription target theoretical/execution: {theoretical_subscription_target}/{execution_subscription_target}")
    print(f"full project units/area: {full_calc['inventory']['total_units']:.0f}/{full_calc['inventory']['total_area']:.0f}")
    print(f"slides: {len(slide_numbers)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
