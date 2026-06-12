#!/usr/bin/env python3
"""Generate an analytical method validation protocol draft.

This is a first prototype for Issue #6. It reads structured product and method
profiles plus machine-readable rule files, then produces:

1. a JSON draft aligned with schemas/validation_protocol.schema.json;
2. a Markdown draft summary containing missing information and review notes.

The output is draft-only and must not be used as an approved protocol.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence

REPO_ROOT = Path(__file__).resolve().parents[2]
RULE_DIR = REPO_ROOT / "knowledge_base" / "validation_protocol_rules" / "machine_readable"

CHARACTERISTIC_RULES_PATH = RULE_DIR / "validation_characteristic_selection_rules.json"
SCOPE_RULES_PATH = RULE_DIR / "validation_scope_rules.json"
DEFAULTS_PATH = RULE_DIR / "protocol_generation_defaults.json"

VALID_SCOPE_VALUES = {
    "full_validation",
    "partial_validation",
    "method_transfer",
    "co_validation",
    "verification",
    "other",
}


def read_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Expected JSON object at {path}")
    return data


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def as_list(value: Any) -> List[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def unique_in_order(items: Iterable[str]) -> List[str]:
    seen = set()
    output: List[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            output.append(item)
    return output


def resolve_method_rule(method_type: str, rule_data: Mapping[str, Any]) -> Dict[str, Any]:
    rules = rule_data.get("method_type_rules", {})
    method_rule = rules.get(method_type) or rules.get(method_type.lower())
    if not method_rule:
        return dict(rules.get("default", {}))

    if "inherits" in method_rule:
        parent_name = method_rule["inherits"]
        parent_rule = rules.get(parent_name, rules.get("default", {}))
        merged = dict(parent_rule)
        merged.update({key: value for key, value in method_rule.items() if key != "inherits"})
        return merged

    return dict(method_rule)


def select_characteristics(
    method_profile: Mapping[str, Any],
    intended_purpose: Sequence[str],
    characteristic_rules: Mapping[str, Any],
) -> List[str]:
    method_type = str(method_profile.get("method_type", "default"))
    method_rule = resolve_method_rule(method_type, characteristic_rules)

    selected = as_list(method_rule.get("usually_include"))

    purpose_modifiers = characteristic_rules.get("purpose_modifiers", {})
    for purpose in intended_purpose:
        modifier = purpose_modifiers.get(purpose)
        if modifier:
            selected.extend(as_list(modifier.get("add")))

    # If the method profile already includes intended purpose terms, use them too.
    for purpose in as_list(method_profile.get("intended_purpose")):
        modifier = purpose_modifiers.get(purpose)
        if modifier:
            selected.extend(as_list(modifier.get("add")))

    return unique_in_order(selected)


def build_acceptance_criteria(characteristics: Sequence[str], defaults: Mapping[str, Any]) -> List[str]:
    prefix = str(defaults.get("default_acceptance_criteria_prefix", "Draft criterion requires review"))
    return [f"{prefix}: {characteristic}" for characteristic in characteristics]


def collect_missing_information(
    product_profile: Mapping[str, Any],
    method_profile: Mapping[str, Any],
    scope: str,
) -> List[str]:
    missing: List[str] = []

    required_product_fields = ["product_type", "sample_type", "analytical_purpose"]
    required_method_fields = ["method_name", "method_type", "intended_purpose", "sample_matrix", "reportable_result"]

    for field in required_product_fields:
        if not product_profile.get(field):
            missing.append(f"Product profile missing field: {field}")

    for field in required_method_fields:
        if not method_profile.get(field):
            missing.append(f"Analytical method profile missing field: {field}")

    existing_missing = as_list(product_profile.get("missing_information"))
    missing.extend(existing_missing)

    if scope not in VALID_SCOPE_VALUES:
        missing.append(f"Validation scope is not recognized: {scope}")

    if not method_profile.get("reference_standard"):
        missing.append("Reference standard strategy not provided")

    if not method_profile.get("system_suitability_tests"):
        missing.append("System suitability tests not provided")

    return unique_in_order(missing)


def build_protocol_json(
    product_profile: Mapping[str, Any],
    method_profile: Mapping[str, Any],
    scope: str,
    characteristic_rules: Mapping[str, Any],
    scope_rules: Mapping[str, Any],
    defaults: Mapping[str, Any],
) -> Dict[str, Any]:
    intended_purpose = as_list(method_profile.get("intended_purpose")) or as_list(product_profile.get("analytical_purpose"))
    method_name = str(method_profile.get("method_name", "Synthetic method draft"))
    method_type = str(method_profile.get("method_type", "other"))
    sample_matrix = str(method_profile.get("sample_matrix", "not specified"))

    selected_scope = scope if scope in VALID_SCOPE_VALUES else "other"
    characteristics = select_characteristics(method_profile, intended_purpose, characteristic_rules)

    scope_info = scope_rules.get("scopes", {}).get(selected_scope, {})
    scope_description = scope_info.get("description", "Draft scope requires human review.")
    required_fields = as_list(scope_info.get("required_planning_fields"))

    missing_information = collect_missing_information(product_profile, method_profile, selected_scope)
    criteria = build_acceptance_criteria(characteristics, defaults)

    evidence_sources = list(defaults.get("default_evidence_sources", []))
    evidence_sources.extend(characteristic_rules.get("default_rule_sources", []))
    evidence_sources.extend(scope_rules.get("default_rule_sources", []))
    evidence_sources = unique_in_order(str(item) for item in evidence_sources)

    experimental_design_summary = (
        f"Draft {selected_scope} plan for {method_name}. "
        f"Scope rationale: {scope_description}. "
        f"Required planning fields: {', '.join(required_fields) if required_fields else 'not specified'}. "
        "This design requires confirmation with method development data and human review."
    )

    if missing_information:
        experimental_design_summary += " Missing information must be resolved before final use."

    protocol = {
        "protocol_title": f"Draft Validation Protocol - {method_name}",
        "method_name": method_name,
        "method_type": method_type,
        "intended_purpose": intended_purpose or ["not specified"],
        "sample_matrix": sample_matrix,
        "validation_scope": selected_scope,
        "validation_characteristics": characteristics or ["other"],
        "acceptance_criteria": criteria or ["Draft criteria require method data and human review"],
        "experimental_design_summary": experimental_design_summary,
        "deviation_handling": str(defaults.get("default_deviation_handling", "Deviation handling requires human review.")),
        "evidence_sources": evidence_sources,
        "human_review_statement": str(defaults.get("human_review_statement", "Human review required.")),
        "human_review_required": True,
    }

    return protocol


def build_markdown(
    protocol: Mapping[str, Any],
    missing_information: Sequence[str],
    defaults: Mapping[str, Any],
) -> str:
    lines: List[str] = []
    lines.append(f"# {protocol['protocol_title']}")
    lines.append("")
    lines.append("> AI-assisted draft only. This output does not approve the method, protocol, report, validation conclusion, or regulatory strategy.")
    lines.append("")
    lines.append("## 1. Method Information")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append(f"| Method name | {protocol['method_name']} |")
    lines.append(f"| Method type | {protocol['method_type']} |")
    lines.append(f"| Sample matrix | {protocol['sample_matrix']} |")
    lines.append(f"| Validation scope | {protocol['validation_scope']} |")
    lines.append(f"| Intended purpose | {', '.join(as_list(protocol['intended_purpose']))} |")
    lines.append("")
    lines.append("## 2. Selected Validation Characteristics")
    lines.append("")
    for item in as_list(protocol.get("validation_characteristics")):
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## 3. Draft Acceptance Criteria")
    lines.append("")
    for item in as_list(protocol.get("acceptance_criteria")):
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## 4. Experimental Design Summary")
    lines.append("")
    lines.append(str(protocol.get("experimental_design_summary", "")))
    lines.append("")
    lines.append("## 5. Deviation Handling")
    lines.append("")
    lines.append(str(protocol.get("deviation_handling", "")))
    lines.append("")
    lines.append("## 6. Missing Information")
    lines.append("")
    if missing_information:
        for item in missing_information:
            lines.append(f"- {item}")
    else:
        lines.append("- No missing information identified by this prototype. Human review still required.")
    lines.append("")
    lines.append("## 7. Evidence Sources")
    lines.append("")
    for item in as_list(protocol.get("evidence_sources")):
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## 8. Human Review Statement")
    lines.append("")
    lines.append(str(defaults.get("human_review_statement", protocol.get("human_review_statement", "Human review required."))))
    lines.append("")
    return "\n".join(lines)


def generate(
    product_profile_path: Path,
    method_profile_path: Path,
    scope: str,
    output_json_path: Path,
    output_md_path: Path,
) -> None:
    product_profile = read_json(product_profile_path)
    method_profile = read_json(method_profile_path)
    characteristic_rules = read_json(CHARACTERISTIC_RULES_PATH)
    scope_rules = read_json(SCOPE_RULES_PATH)
    defaults = read_json(DEFAULTS_PATH)

    selected_scope = scope if scope in VALID_SCOPE_VALUES else "other"
    protocol = build_protocol_json(
        product_profile=product_profile,
        method_profile=method_profile,
        scope=selected_scope,
        characteristic_rules=characteristic_rules,
        scope_rules=scope_rules,
        defaults=defaults,
    )
    missing = collect_missing_information(product_profile, method_profile, selected_scope)
    markdown = build_markdown(protocol, missing, defaults)

    write_json(output_json_path, protocol)
    write_text(output_md_path, markdown)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a draft validation protocol from structured inputs.")
    parser.add_argument("--product-profile", required=True, type=Path, help="Path to product profile JSON")
    parser.add_argument("--method-profile", required=True, type=Path, help="Path to analytical method JSON")
    parser.add_argument("--scope", required=True, choices=sorted(VALID_SCOPE_VALUES), help="Validation scope")
    parser.add_argument("--output-json", required=True, type=Path, help="Output JSON path")
    parser.add_argument("--output-md", required=True, type=Path, help="Output Markdown path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    generate(
        product_profile_path=args.product_profile,
        method_profile_path=args.method_profile,
        scope=args.scope,
        output_json_path=args.output_json,
        output_md_path=args.output_md,
    )


if __name__ == "__main__":
    main()
