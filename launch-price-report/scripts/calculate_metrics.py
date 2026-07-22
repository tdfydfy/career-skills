#!/usr/bin/env python3
"""Recalculate deterministic metrics for a launch price report from JSON."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from statistics import median
from typing import Any


def require_nonnegative(value: float, field: str) -> float:
    number = float(value)
    if number < 0:
        raise ValueError(f"{field} must be nonnegative")
    return number


def safe_ratio(numerator: float, denominator: float) -> float | None:
    return numerator / denominator if denominator else None


def summarize_inventory(rows: list[dict[str, Any]]) -> dict[str, Any]:
    total_area = 0.0
    total_value = 0.0
    total_units = 0.0
    groups: list[dict[str, Any]] = []
    for index, row in enumerate(rows):
        area = require_nonnegative(row["area"], f"inventory[{index}].area")
        price = require_nonnegative(row["unit_price"], f"inventory[{index}].unit_price")
        units = require_nonnegative(row.get("units", 0), f"inventory[{index}].units")
        value = area * price
        total_area += area
        total_value += value
        total_units += units
        groups.append(
            {
                "name": row.get("name", str(index + 1)),
                "area": area,
                "units": units,
                "value": value,
            }
        )
    for group in groups:
        group["area_share"] = safe_ratio(group["area"], total_area)
        group["unit_share"] = safe_ratio(group["units"], total_units)
        group["value_share"] = safe_ratio(group["value"], total_value)
    return {
        "total_area": total_area,
        "total_units": total_units,
        "total_value": total_value,
        "weighted_average_price": safe_ratio(total_value, total_area),
        "groups": groups,
    }


def summarize_sales(data: dict[str, Any]) -> dict[str, Any]:
    launched = require_nonnegative(data["launched_units"], "sales.launched_units")
    sold = require_nonnegative(data["sold_units"], "sales.sold_units")
    if sold > launched:
        raise ValueError("sales.sold_units cannot exceed sales.launched_units")
    return {"sell_through_rate": safe_ratio(sold, launched)}


def summarize_subscription(data: dict[str, Any]) -> dict[str, Any]:
    target_sales = require_nonnegative(data["target_sales_units"], "subscription.target_sales_units")
    conversion = float(data["conversion_rate"])
    current = require_nonnegative(data["current_subscriptions"], "subscription.current_subscriptions")
    if not 0 < conversion <= 1:
        raise ValueError("subscription.conversion_rate must be in (0, 1]")
    target = math.ceil(target_sales / conversion)
    return {
        "subscription_target": target,
        "current_subscriptions": current,
        "gap": target - current,
    }


def summarize_comparisons(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    output = []
    for index, row in enumerate(rows):
        baseline = float(row["baseline"])
        current = float(row["current"])
        output.append(
            {
                "name": row.get("name", str(index + 1)),
                "baseline": baseline,
                "current": current,
                "change": current - baseline,
                "change_rate": safe_ratio(current - baseline, baseline),
            }
        )
    return output


def summarize_prices(values: list[float]) -> dict[str, Any]:
    prices = [require_nonnegative(value, "prices[]") for value in values]
    if not prices:
        return {"count": 0, "minimum": None, "maximum": None, "range": None, "median": None}
    return {
        "count": len(prices),
        "minimum": min(prices),
        "maximum": max(prices),
        "range": max(prices) - min(prices),
        "median": median(prices),
    }


def calculate(payload: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    if "inventory" in payload:
        result["inventory"] = summarize_inventory(payload["inventory"])
    if "sales" in payload:
        result["sales"] = summarize_sales(payload["sales"])
    if "subscription" in payload:
        result["subscription"] = summarize_subscription(payload["subscription"])
    if "comparisons" in payload:
        result["comparisons"] = summarize_comparisons(payload["comparisons"])
    if "prices" in payload:
        result["price_dispersion"] = summarize_prices(payload["prices"])
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="UTF-8 JSON input file")
    parser.add_argument("--output", type=Path, help="Write result JSON to this file")
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    output = json.dumps(calculate(payload), ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
