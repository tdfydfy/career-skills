#!/usr/bin/env python3
"""Validate the synthetic sustained-sales diagnosis case."""

from pathlib import Path
import re

import yaml


ROOT = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    source = yaml.safe_load((ROOT / "source-data.yaml").read_text(encoding="utf-8"))
    report = (ROOT / "report.md").read_text(encoding="utf-8")
    project = source["project"]

    require(
        project["sold_units"] + project["launched_available_units"] == project["launched_units"],
        "sold and available units must close to launched units",
    )
    require(
        project["launched_units"] + project["unlaunched_units"] == project["residential_total_units"],
        "launched and unlaunched units must close to the full project",
    )
    require(
        sum(row["available"] for row in project["product_inventory"]) == project["launched_available_units"],
        "product inventory must close",
    )

    loss = source["customer_loss_sample"]
    require(sum(loss["reasons"].values()) == loss["sample_size"], "customer loss sample must close")
    require(
        len(source["candidate_factors"]["external"]) + len(source["candidate_factors"]["internal"]) == 15,
        "the case must preserve 15 candidate factors",
    )
    require(len(source["root_cause_chains"]) == 4, "the case must contain three root chains and one amplifier")

    parking = source["housing_parking"]
    ratio = parking["sold_parking_spaces"] / parking["residential_sold_units"]
    require(abs(ratio - parking["current_housing_parking_ratio"]) < 0.0001, "housing-parking ratio mismatch")
    require(
        parking["next_8_week_parking_target"] / parking["next_8_week_residential_target"]
        == parking["target_housing_parking_ratio"],
        "target housing-parking ratio mismatch",
    )

    finance = source["finance"]
    require(
        abs(finance["full_project_marketing_budget_yuan"] / finance["full_project_expected_contract_yuan"]
            - finance["full_project_marketing_rate"]) < 1e-9,
        "full-project marketing rate mismatch",
    )
    require(
        finance["full_project_marketing_budget_yuan"] - finance["recognized_marketing_expense_yuan"]
        == finance["remaining_project_budget_yuan"],
        "remaining project budget mismatch",
    )
    require(
        finance["recovery_plan_budget_yuan"] <= finance["remaining_project_budget_yuan"],
        "recovery plan exceeds remaining budget",
    )

    slides = [int(value) for value in re.findall(r"^## 幻灯片(\d+)：", report, re.MULTILINE)]
    require(slides == list(range(1, 19)), "report must contain slides 1 through 18 once and in order")
    for text in ("不进行全盘普降", "客户自愿", "老业主", "三条主因果链"):
        require(text in report, f"report is missing required decision boundary: {text}")

    print("validation passed")
    print(f"inventory sold/available/unlaunched: {project['sold_units']}/{project['launched_available_units']}/{project['unlaunched_units']}")
    print(f"candidate factors/root chains: 15/{len(source['root_cause_chains'])}")
    print(f"housing-parking ratio current/target: {ratio:.2f}/{parking['target_housing_parking_ratio']:.2f}")
    print(f"full-project marketing rate: {finance['full_project_marketing_rate']:.2%}")
    print(f"slides: {len(slides)}")


if __name__ == "__main__":
    main()
