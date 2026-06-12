# Validation Protocol Rule Index

## Purpose

This index maps validation protocol rule files to the workflows, schemas, and templates they support.

## Rule File Map

| Rule File | Supports | Used By |
|---|---|---|
| `validation_protocol_generation_rules.md` | Overall generation logic | `workflows/validation_protocol_generation_workflow.md`, `templates/validation_protocol_template.md` |
| `validation_characteristic_selection_matrix.md` | Characteristic selection | `schemas/validation_protocol.schema.json`, protocol generator, review workflow |
| `validation_scope_logic.md` | Scope selection | Protocol generator, method transfer planning, partial validation planning |
| `acceptance_criteria_rationale_fields.md` | Acceptance criteria drafting | Protocol template, future report review gap rules |
| `system_suitability_and_deviation_rules.md` | SST and deviation handling | Protocol template, validation report review, lab document review |

## Required Cross-Links

Future implementation should connect these rule files to:

- `schemas/validation_protocol.schema.json`
- `workflows/validation_protocol_generation_workflow.md`
- `templates/validation_protocol_template.md`
- `knowledge_base/validation_gap_rules/`
- `knowledge_base/reviewer_question_bank/`

## Direction Control

These rules are advisory and draft-supporting. They do not approve methods, protocols, reports, validation conclusions, or regulatory strategies.
