#!/usr/bin/env python3
"""Render a draft protocol/report gap assessment JSON file to Markdown."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Mapping

DEFAULT_HUMAN_REVIEW_STATEMENT = (
    "This review report is AI-assisted and advisory only. It does not approve "
    "a protocol, report, method, validation conclusion, or regulatory strategy. "
    "Qualified human review is required before any real use."
)


def read_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Expected JSON object at {path}")
    return data


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def as_list(value: Any) -> List[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def render_gap_assessment_markdown(assessment: Mapping[str, Any]) -> str:
    gaps = assessment.get("gaps", [])
    if not isinstance(gaps, list):
        gaps = []

    human_review_statement = str(
        assessment.get("human_review_statement", DEFAULT_HUMAN_REVIEW_STATEMENT)
    )

    lines: List[str] = []
    lines.append("# Draft Protocol / Report Gap Assessment")
    lines.append("")
    lines.append("> AI-assisted advisory output. Human review is required before any real use.")
    lines.append("")
    lines.append("## Assessment Summary")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append(f"| Assessment type | {assessment.get('assessment_type', 'not specified')} |")
    lines.append(f"| Source document ID | {assessment.get('source_document_id', 'not specified')} |")
    lines.append(f"| Source document type | {assessment.get('source_document_type', 'not specified')} |")
    lines.append(f"| Mapping | {assessment.get('mapping_name', 'not specified')} |")
    lines.append(f"| Mapping version | {assessment.get('mapping_version', 'not specified')} |")
    lines.append(f"| Gap count | {assessment.get('gap_count', len(gaps))} |")
    lines.append(f"| Human review required | {assessment.get('human_review_required', True)} |")
    lines.append("")

    lines.append("## Gap Table")
    lines.append("")
    if gaps:
        lines.append("| Gap ID | Rule Area | Severity | Observed Status | Reviewer Question | Feedback Targets |")
        lines.append("|---|---|---|---|---|---|")
        for gap in gaps:
            if not isinstance(gap, dict):
                continue
            targets = ", ".join(as_list(gap.get("feedback_targets")))
            lines.append(
                "| "
                f"{gap.get('gap_id', '')} | "
                f"{gap.get('rule_area', '')} | "
                f"{gap.get('severity', '')} | "
                f"{gap.get('observed_status', '')} | "
                f"{gap.get('reviewer_question', '')} | "
                f"{targets} |"
            )
    else:
        lines.append("No gaps were identified by this prototype. Human review is still required.")
    lines.append("")

    lines.append("## Detailed Gaps")
    lines.append("")
    if gaps:
        for gap in gaps:
            if not isinstance(gap, dict):
                continue
            lines.append(f"### {gap.get('gap_id', 'Gap')} — {gap.get('rule_area', 'not specified')}")
            lines.append("")
            lines.append(f"- Severity: {gap.get('severity', 'not specified')}")
            lines.append(f"- Gap description: {gap.get('gap_description', 'not specified')}")
            lines.append(f"- Expected element: {gap.get('expected_element', 'not specified')}")
            lines.append(f"- Observed status: {gap.get('observed_status', 'not specified')}")
            lines.append(f"- Why it matters: {gap.get('why_it_matters', 'not specified')}")
            lines.append(f"- Reviewer question: {gap.get('reviewer_question', 'not specified')}")
            lines.append(f"- Evidence level: {gap.get('evidence_level', 'not specified')}")
            lines.append(f"- Feedback targets: {', '.join(as_list(gap.get('feedback_targets')))}")
            lines.append(f"- Human review required: {gap.get('human_review_required', True)}")
            lines.append("")
    else:
        lines.append("No detailed gaps to display.")
        lines.append("")

    lines.append("## Human Review Statement")
    lines.append("")
    lines.append(human_review_statement)
    lines.append("")
    return "\n".join(lines)


def render_file(input_json: Path, output_md: Path) -> None:
    assessment = read_json(input_json)
    markdown = render_gap_assessment_markdown(assessment)
    write_text(output_md, markdown)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render draft gap assessment JSON to Markdown.")
    parser.add_argument("--input-json", required=True, type=Path)
    parser.add_argument("--output-md", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    render_file(args.input_json, args.output_md)


if __name__ == "__main__":
    main()
