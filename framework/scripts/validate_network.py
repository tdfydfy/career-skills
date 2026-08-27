#!/usr/bin/env python3
"""Validate the marketing skill network registry and shared YAML resources."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parents[2]
FRAMEWORK = ROOT / "framework"
REGISTRY = FRAMEWORK / "skill-network.yaml"
NODE_GROUPS = (
    "existing_nodes",
    "foundation_nodes",
    "business_nodes",
    "deliverable_nodes",
)


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate mapping keys."""


def construct_unique_mapping(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_unique_mapping,
)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as stream:
        return yaml.load(stream, Loader=UniqueKeyLoader)


def duplicates(values):
    return sorted(value for value, count in Counter(values).items() if count > 1)


def dependency_cycles(nodes):
    graph = {node["id"]: node.get("depends_on", []) for node in nodes}
    state = {}
    stack = []
    cycles = []

    def visit(node_id):
        if state.get(node_id) == "done":
            return
        if state.get(node_id) == "active":
            start = stack.index(node_id)
            cycles.append(" -> ".join(stack[start:] + [node_id]))
            return
        state[node_id] = "active"
        stack.append(node_id)
        for dependency in graph.get(node_id, []):
            if dependency in graph:
                visit(dependency)
        stack.pop()
        state[node_id] = "done"

    for node_id in graph:
        visit(node_id)
    return sorted(set(cycles))


def validate() -> list[str]:
    errors: list[str] = []

    for path in sorted(FRAMEWORK.rglob("*.yaml")):
        try:
            load_yaml(path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"invalid YAML {path.relative_to(ROOT)}: {exc}")

    if errors:
        return errors

    registry = load_yaml(REGISTRY)
    nodes = [node for group in NODE_GROUPS for node in registry.get(group, [])]
    node_ids = [node.get("id") for node in nodes]
    valid_statuses = set(registry["network"]["status_values"])
    valid_layers = set(registry["network"]["layers"])
    valid_kinds = set(registry["network"]["node_kinds"])

    for node_id in duplicates(node_ids):
        errors.append(f"duplicate node id: {node_id}")

    node_id_set = set(node_ids)
    expected_layers = {
        "foundation_nodes": "foundation",
        "business_nodes": "business",
        "deliverable_nodes": "deliverable",
    }
    for group, expected_layer in expected_layers.items():
        for node in registry.get(group, []):
            if node.get("layer") != expected_layer:
                errors.append(
                    f"{node.get('id')}: group {group} requires layer {expected_layer}"
                )
    for cycle in dependency_cycles(nodes):
        errors.append(f"dependency cycle: {cycle}")
    for node in nodes:
        node_id = node.get("id", "<missing-id>")
        for field in ("title", "layer", "kind", "status"):
            if not node.get(field):
                errors.append(f"{node_id}: missing {field}")
        if node.get("layer") not in valid_layers:
            errors.append(f"{node_id}: invalid layer {node.get('layer')}")
        if node.get("kind") not in valid_kinds:
            errors.append(f"{node_id}: invalid kind {node.get('kind')}")
        if node.get("status") not in valid_statuses:
            errors.append(f"{node_id}: invalid status {node.get('status')}")
        if node.get("status") == "draft" and not node.get("path"):
            errors.append(f"{node_id}: draft node has no path")
        if node.get("layer") in {"business", "deliverable"} and node.get("status") == "draft":
            if not node.get("section"):
                errors.append(f"{node_id}: draft workflow has no section")

        for dependency in node.get("depends_on", []):
            if dependency not in node_id_set:
                errors.append(f"{node_id}: missing dependency {dependency}")

        paths = []
        if node.get("path"):
            paths.append(node["path"])
        if node.get("spec_path"):
            paths.append(node["spec_path"])
        paths.extend(node.get("resources", []))
        for relative_path in paths:
            if not (ROOT / relative_path).exists():
                errors.append(f"{node_id}: missing path {relative_path}")

        if node.get("status") == "active" and node.get("kind") in {
            "executable-skill",
            "orchestrator-skill",
        }:
            skill_md = ROOT / node["path"] / "SKILL.md"
            if not skill_md.exists():
                errors.append(f"{node_id}: active skill has no SKILL.md")

        if node.get("section") and node.get("path"):
            path = ROOT / node["path"]
            heading = f"## {node['section']}"
            if path.exists() and heading not in path.read_text(encoding="utf-8"):
                errors.append(f"{node_id}: section not found: {heading}")

    for name, relative_path in registry.get("contracts", {}).items():
        if not (ROOT / relative_path).exists():
            errors.append(f"contract {name}: missing path {relative_path}")

    for name, relative_path in registry.get("governance", {}).items():
        if not (ROOT / relative_path).exists():
            errors.append(f"governance {name}: missing path {relative_path}")

    sources = registry.get("knowledge_sources", [])
    source_ids = [source.get("id") for source in sources]
    for source_id in duplicates(source_ids):
        errors.append(f"duplicate knowledge source id: {source_id}")
    source_id_set = set(source_ids)
    for source in sources:
        path = ROOT / source["path"]
        if not path.exists():
            errors.append(f"knowledge source {source['id']}: missing {source['path']}")
    for node in nodes:
        for source_id in node.get("knowledge_sources", []):
            if source_id not in source_id_set:
                errors.append(f"{node['id']}: unknown knowledge source {source_id}")

    contract_ids = {
        load_yaml(ROOT / relative_path).get("contract")
        for relative_path in registry.get("contracts", {}).values()
    }
    valid_atom_targets = node_id_set | contract_ids
    knowledge_atoms = []
    for source in sources:
        path = ROOT / source["path"]
        if path.suffix in {".yaml", ".yml"}:
            source_data = load_yaml(path)
            knowledge_atoms.extend(source_data.get("atoms", []))
    atom_ids = [atom.get("id") for atom in knowledge_atoms]
    for atom_id in duplicates(atom_ids):
        errors.append(f"duplicate knowledge atom id: {atom_id}")
    for atom in knowledge_atoms:
        if not atom.get("id"):
            errors.append("knowledge atom: missing id")
        for node_id in atom.get("target_nodes", []):
            if node_id not in valid_atom_targets:
                errors.append(f"knowledge atom {atom.get('id')}: unknown target {node_id}")

    metric_data = load_yaml(FRAMEWORK / "knowledge/metric-baseline-001.yaml")
    metrics = metric_data.get("metrics", [])
    metric_ids = [metric.get("id") for metric in metrics]
    for metric_id in duplicates(metric_ids):
        errors.append(f"duplicate metric id: {metric_id}")
    metric_required = {"id", "title", "category", "definition", "unit", "formula", "status"}
    atom_id_set = set(atom_ids)
    for metric in metrics:
        missing = metric_required - set(metric)
        if missing:
            errors.append(f"metric {metric.get('id')}: missing {sorted(missing)}")
        for atom_id in metric.get("source_atoms", []):
            if atom_id not in atom_id_set:
                errors.append(f"metric {metric.get('id')}: unknown atom {atom_id}")

    for path in sorted((FRAMEWORK / "examples").rglob("*.yaml")):
        example = load_yaml(path)
        example_contract = example.get("contract")
        if example_contract is None:
            if not example.get("case"):
                errors.append(
                    f"example {path.relative_to(ROOT)}: missing contract or case manifest"
                )
            continue
        if example_contract not in contract_ids:
            errors.append(f"example {path.relative_to(ROOT)}: unknown contract {example_contract}")
        if example_contract == "metric-snapshot":
            for value in example.get("values", []):
                if value.get("metric_id") not in set(metric_ids):
                    errors.append(
                        f"example {path.relative_to(ROOT)}: unknown metric {value.get('metric_id')}"
                    )
        if example_contract == "deliverable-request":
            for node_id in example.get("required_capabilities", []) + example.get("optional_capabilities", []):
                if node_id not in node_id_set:
                    errors.append(f"example {path.relative_to(ROOT)}: unknown capability {node_id}")
        if example_contract == "capability-result":
            node_id = example.get("capability", {}).get("id")
            if node_id not in node_id_set:
                errors.append(f"example {path.relative_to(ROOT)}: unknown capability {node_id}")

    action_data = load_yaml(FRAMEWORK / "knowledge/marketing-action-baseline-001.yaml")
    actions = action_data.get("actions", [])
    action_ids = [action.get("id") for action in actions]
    for action_id in duplicates(action_ids):
        errors.append(f"duplicate action id: {action_id}")
    action_required = {"id", "title", "category", "solves", "prerequisites", "outputs", "risks"}
    for action in actions:
        missing = action_required - set(action)
        if missing:
            errors.append(f"action {action.get('id')}: missing {sorted(missing)}")

    enterprise_data = load_yaml(FRAMEWORK / "enterprise-inputs.yaml")
    enterprise_inputs = enterprise_data.get("inputs", [])
    input_ids = [item.get("id") for item in enterprise_inputs]
    for input_id in duplicates(input_ids):
        errors.append(f"duplicate enterprise input id: {input_id}")
    for item in enterprise_inputs:
        if item.get("status") not in set(enterprise_data.get("status_values", [])):
            errors.append(f"enterprise input {item.get('id')}: invalid status {item.get('status')}")
        missing = {"id", "priority", "title", "status", "request", "affects"} - set(item)
        if missing:
            errors.append(f"enterprise input {item.get('id')}: missing {sorted(missing)}")
        for node_id in item.get("affects", []):
            if node_id not in node_id_set:
                errors.append(f"enterprise input {item.get('id')}: unknown node {node_id}")

    router = load_yaml(FRAMEWORK / "task-router.yaml")
    routes = router.get("routes", [])
    route_ids = [route.get("id") for route in routes]
    for route_id in duplicates(route_ids):
        errors.append(f"duplicate route id: {route_id}")
    for route in routes:
        missing = {"id", "intent", "triggers", "primary_node"} - set(route)
        if missing:
            errors.append(f"route {route.get('id')}: missing {sorted(missing)}")
        if route.get("primary_node") not in node_id_set:
            errors.append(f"route {route.get('id')}: unknown node {route.get('primary_node')}")
        for node_id in route.get("supporting_nodes", []):
            if node_id not in node_id_set:
                errors.append(f"route {route.get('id')}: unknown supporting node {node_id}")

    print(f"nodes: {len(nodes)}")
    for group in NODE_GROUPS:
        print(f"  {group}: {len(registry.get(group, []))}")
    print(f"knowledge sources: {len(sources)}")
    print(f"knowledge atoms: {len(atom_ids)}")
    print(f"metrics: {len(metrics)}")
    print(f"marketing actions: {len(actions)}")
    print(f"enterprise inputs: {len(enterprise_inputs)}")
    print(f"task routes: {len(routes)}")
    print(f"examples: {len(list((FRAMEWORK / 'examples').rglob('*.yaml')))}")
    print(f"node status: {dict(Counter(node.get('status') for node in nodes))}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
