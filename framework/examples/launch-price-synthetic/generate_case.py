#!/usr/bin/env python3
"""Generate deterministic ledgers for the synthetic launch-price-report case."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


BUILDING_RULES = {
    "G1": {
        "floors": 17,
        "units": [
            ("01", "105㎡小高层", 105, 20450, 100),
            ("02", "125㎡小高层", 125, 20850, 100),
            ("03", "125㎡小高层", 125, 20750, 100),
            ("04", "105㎡小高层", 105, 20350, 100),
        ],
    },
    "Y1": {
        "floors": 11,
        "units": [
            ("01", "132㎡洋房", 132, 23100, 120),
            ("02", "132㎡洋房", 132, 23000, 120),
            ("03", "132㎡洋房", 132, 23150, 120),
            ("04", "132㎡洋房", 132, 23050, 120),
        ],
    },
    "Y3": {
        "floors": 11,
        "units": [
            ("01", "168㎡洋房", 168, 25000, 140),
            ("02", "168㎡洋房", 168, 24900, 140),
            ("03", "168㎡洋房", 168, 25050, 140),
            ("04", "168㎡洋房", 168, 24950, 140),
        ],
    },
}


CUSTOMER_DISTRIBUTION = {
    "105㎡小高层": {"A": 18, "B+": 10, "B": 7, "B-": 5, "C+": 2, "C": 1, "C-": 1, "D": 1},
    "125㎡小高层": {"A": 16, "B+": 8, "B": 6, "B-": 4, "C+": 3, "C": 2, "C-": 2, "D": 1},
    "132㎡洋房": {"A": 22, "B+": 9, "B": 8, "B-": 5, "C+": 4, "C": 3, "C-": 1, "D": 1},
    "168㎡洋房": {"A": 16, "B+": 7, "B": 5, "B-": 4, "C+": 5, "C": 4, "C-": 2, "D": 1},
}


PRODUCT_BUILDING = {
    "105㎡小高层": "G1",
    "125㎡小高层": "G1",
    "132㎡洋房": "Y1",
    "168㎡洋房": "Y3",
}


PRODUCT_PRICE_RANGE = {
    "105㎡小高层": "215-235万元",
    "125㎡小高层": "265-285万元",
    "132㎡洋房": "300-325万元",
    "168㎡洋房": "420-450万元",
}


UNRESOLVED_BY_RATING = {
    "A": "仅需确认选房顺序和付款资料",
    "B+": "决策人将在开盘前到场",
    "B": "需完成月供测算或竞品复访比较",
    "B-": "需卖房或补足首付款",
    "C+": "短期观望市场价格",
    "C": "家庭意见尚未统一",
    "C-": "预算与意向房源存在明显差距",
    "D": "无明确购房计划，停止常规跟进",
}


def build_unit_schedule() -> tuple[list[dict], dict[str, dict]]:
    rows = []
    summaries: dict[str, dict] = {}
    for building, rule in BUILDING_RULES.items():
        for floor in range(1, rule["floors"] + 1):
            for unit, product, area, base, increment in rule["units"]:
                unit_price = base + floor * increment
                total_price = area * unit_price
                rows.append(
                    {
                        "unit_id": f"{building}-{floor:02d}{unit}",
                        "building": building,
                        "floor": floor,
                        "unit": unit,
                        "product": product,
                        "area_sqm": area,
                        "requested_net_price_per_sqm": unit_price,
                        "floor_price_per_sqm": unit_price - 500,
                        "list_price_per_sqm": round(unit_price / 0.97),
                        "total_price_yuan": total_price,
                        "target_sale": "no",
                    }
                )
        building_rows = [row for row in rows if row["building"] == building]
        area = sum(row["area_sqm"] for row in building_rows)
        value = sum(row["total_price_yuan"] for row in building_rows)
        summaries[building] = {
            "units": len(building_rows),
            "area": area,
            "value": value,
            "average_price": value / area,
        }
    target_units = {"G1": 50, "Y1": 32, "Y3": 26}
    for building, count in target_units.items():
        building_average = summaries[building]["average_price"]
        candidates = sorted(
            (row for row in rows if row["building"] == building),
            key=lambda row: (
                abs(row["requested_net_price_per_sqm"] - building_average),
                row["unit_id"],
            ),
        )
        for row in candidates[:count]:
            row["target_sale"] = "yes"
    return rows, summaries


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def build_customer_ledger() -> list[dict]:
    rows = []
    customer_number = 1
    for product, ratings in CUSTOMER_DISTRIBUTION.items():
        for rating, count in ratings.items():
            for _ in range(count):
                rows.append(
                    {
                        "customer_code": f"C{customer_number:03d}",
                        "rating": rating,
                        "first_choice_product": product,
                        "first_choice_building": PRODUCT_BUILDING[product],
                        "acceptable_total_price": PRODUCT_PRICE_RANGE[product],
                        "money_status": "ready" if rating in {"A", "B+"} else "partial",
                        "authority_status": "ready" if rating == "A" else "pending",
                        "need_fit_status": "matched" if rating not in {"C-", "D"} else "weak",
                        "unresolved_issue": UNRESOLVED_BY_RATING[rating],
                        "as_of_date": "2026-07-19",
                    }
                )
                customer_number += 1
    return rows


def build_unconverted_ledger() -> list[dict]:
    reasons = {
        "可继续跟进，等待家庭成员返场": 17,
        "市场观望，担心后续降价": 12,
        "家庭意见不统一": 8,
        "预算不足": 6,
        "卖房置换尚未完成": 5,
        "转向竞品": 3,
    }
    rows = []
    number = 1
    for reason, count in reasons.items():
        for _ in range(count):
            rows.append(
                {
                    "frozen_customer_code": f"F{number:03d}",
                    "reason": reason,
                    "follow_up": "yes" if reason != "转向竞品" else "no",
                    "as_of_date": "2026-07-19",
                }
            )
            number += 1
    return rows


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    units, launch_summaries = build_unit_schedule()
    write_csv(ROOT / "unit-price-schedule.csv", units)
    write_csv(ROOT / "customer-ledger.csv", build_customer_ledger())
    write_csv(ROOT / "frozen-unconverted-ledger.csv", build_unconverted_ledger())

    launch_inventory = [
        {
            "name": building,
            "area": summary["area"],
            "unit_price": summary["average_price"],
            "units": summary["units"],
        }
        for building, summary in launch_summaries.items()
    ]
    launch_value = sum(item["area"] * item["unit_price"] for item in launch_inventory)
    launch_area = sum(item["area"] for item in launch_inventory)
    launch_input = {
        "inventory": launch_inventory,
        "sales": {"launched_units": 156, "sold_units": 108},
        "subscription": {"target_sales_units": 108, "conversion_rate": 0.6, "current_subscriptions": 184},
        "comparisons": [
            {"name": "首开申请均价较启动会整盘均价", "baseline": 22500, "current": launch_value / launch_area},
            {"name": "整盘预计均价较启动会", "baseline": 22500, "current": 0},
        ],
        "prices": [row["requested_net_price_per_sqm"] for row in units],
    }

    full_inventory = [
        *launch_inventory,
        {"name": "G2", "area": 7820, "unit_price": 21350, "units": 68},
        {"name": "G3", "area": 7820, "unit_price": 21200, "units": 68},
        {"name": "G5", "area": 7820, "unit_price": 21100, "units": 68},
        {"name": "Y2", "area": 5808, "unit_price": 24200, "units": 44},
        {"name": "Y5", "area": 7392, "unit_price": 25800, "units": 44},
    ]
    full_value = sum(item["area"] * item["unit_price"] for item in full_inventory)
    full_area = sum(item["area"] for item in full_inventory)
    full_average = full_value / full_area
    launch_input["comparisons"][1]["current"] = full_average
    full_input = {
        "inventory": full_inventory,
        "comparisons": [
            {"name": "整盘住宅均价", "baseline": 22500, "current": full_average},
            {"name": "整盘住宅货值", "baseline": 1297800000, "current": full_value},
        ],
    }
    write_json(ROOT / "launch-calculation-input.json", launch_input)
    write_json(ROOT / "full-project-calculation-input.json", full_input)
    write_json(
        ROOT / "generated-summary.json",
        {
            "launch": {
                "units": sum(item["units"] for item in launch_inventory),
                "area": launch_area,
                "value": launch_value,
                "average_price": launch_value / launch_area,
                "target_sales_units": sum(row["target_sale"] == "yes" for row in units),
                "target_sales_value": sum(
                    row["total_price_yuan"] for row in units if row["target_sale"] == "yes"
                ),
                "target_sales_by_building": {
                    building: {
                        "units": sum(
                            row["target_sale"] == "yes" and row["building"] == building
                            for row in units
                        ),
                        "value": sum(
                            row["total_price_yuan"]
                            for row in units
                            if row["target_sale"] == "yes" and row["building"] == building
                        ),
                    }
                    for building in BUILDING_RULES
                },
            },
            "full_project": {
                "units": sum(item["units"] for item in full_inventory),
                "area": full_area,
                "value": full_value,
                "average_price": full_average,
            },
        },
    )


if __name__ == "__main__":
    main()
