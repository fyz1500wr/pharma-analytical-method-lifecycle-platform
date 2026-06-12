"""Markdown rendering utilities for validation protocol drafts.

The renderer converts a structured validation protocol draft JSON object into a
reviewable Markdown draft. It is intentionally conservative: every output keeps
AI-assisted draft-only wording and a human review statement.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, List, Mapping, Sequence


DEFAULT_DRAFT_ONLY_WARNING = (
    "AI-assisted draft only. This output does not approve the method, protocol, "
    "report, validation conclusion, or regulatory strategy."
)

DEFAULT_HUMAN_REVIEW_STATEMENT = (
    "本文件由 AI 輔助產生，於 GxP、供應商溝通或法規用途使用前，"
    "必須由負責之 analytical lead、QA、RA 及 / 或 method owner 審閱確認。"
)


def as_list(value: Any) -> List[str]:
    """Return value as a list of strings."""
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def load_template_reference(template_path: Path | None = None) -> str:
    """Return a template reference note.

    The current renderer does not directly substitute the full template file.
    Instead, it records which template the output is aligned with. This keeps the
    prototype simple while preserving traceability to the repository template.
    """
    if template_path is None:
        return "templates/validation_protocol_template.md"
    return str(template_path)


def render_validation_protocol_markdown(
    protocol: Mapping[str, Any],
    missing_information: Sequence[str] | None = None,
    defaults: Mapping[str, Any] | None = None,
    template_path: Path | None = None,
) -> str:
    """Render a validation protocol draft as Markdown."""
    defaults = defaults or {}
    missing_information = list(missing_information or [])

    draft_warning = str(defaults.get("draft_only_warning", DEFAULT_DRAFT_ONLY_WARNING))
    human_review_statement = str(
        defaults.get(
            "human_review_statement",
            protocol.get("human_review_statement", DEFAULT_HUMAN_REVIEW_STATEMENT),
        )
    )
    template_reference = load_template_reference(template_path)

    lines: List[str] = []
    lines.append(f"# {protocol.get('protocol_title', 'Draft Validation Protocol')}")
    lines.append("")
    lines.append(f"> {draft_warning}")
    lines.append("")
    lines.append("## Template Reference")
    lines.append("")
    lines.append(f"This draft is aligned with `{template_reference}`.")
    lines.append("")
    lines.append("## 1. Method Information")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append(f"| Method name | {protocol.get('method_name', 'not specified')} |")
    lines.append(f"| Method type | {protocol.get('method_type', 'not specified')} |")
    lines.append(f"| Sample matrix | {protocol.get('sample_matrix', 'not specified')} |")
    lines.append(f"| Validation scope | {protocol.get('validation_scope', 'not specified')} |")
    lines.append(f"| Intended purpose | {', '.join(as_list(protocol.get('intended_purpose')))} |")
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
    lines.append(human_review_statement)
    lines.append("")
    return "\n".join(lines)
