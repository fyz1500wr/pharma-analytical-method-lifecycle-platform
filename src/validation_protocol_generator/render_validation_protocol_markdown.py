#!/usr/bin/env python3
"""Render a validation protocol draft JSON file to Markdown."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict

from src.validation_protocol_generator.render_markdown import render_validation_protocol_markdown

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULTS_PATH = (
    REPO_ROOT
    / "knowledge_base"
    / "validation_protocol_rules"
    / "machine_readable"
    / "protocol_generation_defaults.json"
)
TEMPLATE_PATH = REPO_ROOT / "templates" / "validation_protocol_template.md"


def read_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Expected JSON object: {path}")
    return data


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def render_file(input_json: Path, output_md: Path) -> None:
    protocol = read_json(input_json)
    defaults = read_json(DEFAULTS_PATH)
    missing_information = protocol.get("missing_information", [])
    if not isinstance(missing_information, list):
        missing_information = [str(missing_information)]

    markdown = render_validation_protocol_markdown(
        protocol=protocol,
        missing_information=missing_information,
        defaults=defaults,
        template_path=TEMPLATE_PATH,
    )
    write_text(output_md, markdown)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render validation protocol JSON to Markdown.")
    parser.add_argument("--input-json", required=True, type=Path)
    parser.add_argument("--output-md", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    render_file(input_json=args.input_json, output_md=args.output_md)


if __name__ == "__main__":
    main()
