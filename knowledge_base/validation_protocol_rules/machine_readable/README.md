# Machine-Readable Validation Protocol Rules

## Purpose

This directory stores machine-readable rule files used by the first validation protocol generation engine.

These files are derived from the human-readable rule files in `knowledge_base/validation_protocol_rules/` and are intended to help the code avoid hard-coding one product, method, or validation strategy.

## Files

| File | Purpose |
|---|---|
| `validation_characteristic_selection_rules.json` | Selects draft validation characteristics by method type and intended purpose |
| `validation_scope_rules.json` | Defines scope descriptions and required planning fields |
| `protocol_generation_defaults.json` | Defines default human review statement, evidence label, and draft-only warning |

## Governance

- These rules support draft generation only.
- The output must include a human review statement.
- The output must not claim approval, validation completion, or regulatory readiness.
- Final use requires review by the responsible analytical lead, QA, RA, and/or method owner.
