#!/usr/bin/env python3
"""Extract draft protocol/report review gaps from structured review content.

This prototype reads a machine-readable protocol-to-gap mapping file and a
structured JSON review content file. It flags gaps when the content says a mapped
rule area is missing, weak, unclear, or not addressed.

The output is advisory and requires human review.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MAPPING_PATH = (
    REPO_ROOT
    / "knowledge_base"
    / "validation_gap_rules"
    / "machine_readable"
    / "protocol_to_report_gap_mapping.json"
)

TRIGGER_STATUSES = {"missing", "weak", "unclear", "not_addressed", "not_provided"}

HUMAN_REVIEW_STATEMENT = (
    "This gap assessment is AI-assisted and advisory only. It does not approve "
    "a protocol, report, method, validation conclusion, or regulatory strategy. "
    "Qualified human review is required before any real use."
)


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


def normalize_status(value: Any) -> str:
    return str(value or "").strip().lower().replace(" ", "_").replace("-", "_")


def build_gap(mapping: Mapping[str, Any], finding: Mapping[str, Any]) -> Dict[str, Any]:
    return {
        "gap_id": mapping.get("id"),
        "rule_area": mapping.get("rule_area"),
        "severity": mapping.get("severity"),
        "gap_description": mapping.get("gap_if_missing"),
        "why_it_matters": finding.get("comment", "Expected element is missing, weak, or unclear."),
        "reviewer_question": mapping.get("reviewer_question"),
        "expected_element": mapping.get("expected_element"),
        "observed_status": finding.get("status"),
        "evidence_level": mapping.get("evidence_level"),
        "feedback_targets": mapping.get("feedback_targets", []),
        "human_review_required": True,
    }


def extract_gaps(review_content: Mapping[str, Any], mapping_payload: Mapping[str, Any]) -> Dict[str, Any]:
    findings_raw = review_content.get("review_findings", [])
    if not isinstance(findings_raw, list):
        raise ValueError("review_findings must be a list")

    findings_by_area: Dict[str, Mapping[str, Any]] = {}
    for finding in findings_raw:
        if isinstance(finding, dict):
            area = str(finding.get("rule_area", "")).strip()
            if area:
                findings_by_area[area] = finding

    gaps: List[Dict[str, Any]] = []
    for mapping in mapping_payload.get("mappings", []):
        if not isinstance(mapping, dict):
            continue
        area = str(mapping.get("rule_area", ""))
        finding = findings_by_area.get(area)
        if not finding:
            continue
        status = normalize_status(finding.get("status"))
        if status in TRIGGER_STATUSES:
            gaps.append(build_gap(mapping, finding))

    return {
        "assessment_type": "protocol_report_gap_assessment_draft",
        "source_document_id": review_content.get("source_document_id", "not_specified"),
        "source_document_type": review_content.get("source_document_type", "not_specified"),
        "mapping_name": mapping_payload.get("mapping_name"),
        "mapping_version": mapping_payload.get("version"),
        "gap_count": len(gaps),
        "gaps": gaps,
        "human_review_required": True,
        "human_review_statement": HUMAN_REVIEW_STATEMENT,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract draft gaps from structured protocol/report review content.")
    parser.add_argument("--review-content", required=True, type=Path, help="Structured review content JSON")
    parser.add_argument("--output-json", required=True, type=Path, help="Output gap assessment JSON")
    parser.add_argument("--mapping", default=DEFAULT_MAPPING_PATH, type=Path, help="Protocol-to-gap mapping JSON")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    review_content = read_json(args.review_content)
    mapping_payload = read_json(args.mapping)
    assessment = extract_gaps(review_content, mapping_payload)
    write_json(args.output_json, assessment)


if __name__ == "__main__":
    main()
