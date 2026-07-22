#!/usr/bin/env python3
"""Validate the synthetic launch marketing strategy case."""

from pathlib import Path
import re

import yaml


ROOT = Path(__file__).resolve().parent


def load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    source = load_yaml(ROOT / "source-data.yaml")
    base = load_yaml((ROOT / source["case"]["base_case"]).resolve())
    report = (ROOT / "report.md").read_text(encoding="utf-8")
    strategy = source["strategy_choice"]

    funnel = source["funnel_plan"]
    channels = source["channel_plan"]
    field_map = {
        "leads": "leads",
        "visits": "visits",
        "effective": "effective_customers",
        "subscriptions": "subscriptions_execution",
        "deals": "deals",
    }
    for channel_field, funnel_field in field_map.items():
        total = sum(row[channel_field] for row in channels)
        require(total == funnel[funnel_field], f"{channel_field} total mismatch: {total}")

    channel_budget = sum(row["budget_yuan"] for row in channels)
    require(channel_budget == 7_800_000, "channel budget must equal CNY 7.8m")
    require(
        source["budget"]["launch_stage_budget_yuan"] - channel_budget == 2_324_625,
        "common launch-stage cost must equal CNY 2.324625m",
    )

    annual_budget = sum(source["budget"]["categories"].values())
    require(annual_budget == source["budget"]["annual_budget_yuan"], "annual budget mismatch")
    annual_rate = annual_budget / source["budget"]["annual_contract_target_yuan"]
    require(abs(annual_rate - source["budget"]["annual_marketing_rate"]) < 1e-9, "annual rate mismatch")
    launch_rate = source["budget"]["launch_stage_budget_yuan"] / strategy["target_contract_yuan"]
    require(abs(launch_rate - source["budget"]["launch_stage_marketing_rate"]) < 1e-9, "launch rate mismatch")
    require(
        source["budget"]["launch_stage_budget_yuan"] + source["budget"]["post_launch_annual_budget_yuan"]
        == annual_budget,
        "launch and post-launch budgets must close to the annual budget",
    )
    post_launch_rate = (
        source["budget"]["post_launch_annual_budget_yuan"]
        / source["budget"]["post_launch_annual_contract_target_yuan"]
    )
    require(
        abs(post_launch_rate - source["budget"]["post_launch_annual_marketing_rate"]) < 0.00005,
        "post-launch annual rate mismatch",
    )
    full_project_rate = source["budget"]["full_project_budget_yuan"] / source["budget"]["full_project_contract_value_yuan"]
    require(abs(full_project_rate - source["budget"]["full_project_marketing_rate"]) < 1e-9, "full project rate mismatch")

    base_target = base["launch_target"]
    require(strategy["target_units"] == base_target["units"], "target units differ from price case")
    require(
        strategy["target_contract_yuan"] == base_target["contract_amount_yuan"],
        "target contract value differs from price case",
    )
    require(strategy["target_units"] == funnel["deals"], "strategy target and funnel deals differ")
    require(abs(funnel["subscriptions_execution"] / funnel["visits"] - 0.15) < 1e-9, "launch visit-to-subscription rate must be 15%")
    require(abs(funnel["deals"] / funnel["subscriptions_execution"] - 0.60) < 1e-9, "launch subscription-to-deal rate must be 60%")

    slide_numbers = [int(value) for value in re.findall(r"^## 幻灯片(\d+)：", report, re.MULTILINE)]
    require(slide_numbers == list(range(1, 25)), "report must contain slides 1 through 24 once and in order")
    require("3.3749亿元" in report, "report is missing the approved contract target")
    require("G1/Y1走量、Y3立标" in report, "report is missing the strategy proposition")

    print("validation passed")
    print(f"funnel: {funnel['leads']} -> {funnel['visits']} -> {funnel['effective_customers']} -> "
          f"{funnel['subscriptions_execution']} -> {funnel['deals']}")
    print(f"annual marketing rate: {annual_rate:.2%}")
    print(f"launch/full-project marketing rate: {launch_rate:.2%}/{full_project_rate:.2%}")
    print(f"slides: {len(slide_numbers)}")


if __name__ == "__main__":
    main()
