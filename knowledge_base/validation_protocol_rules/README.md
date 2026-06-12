# Validation Protocol Rules

## Purpose

This directory stores the structured rule layer for generating analytical method validation protocol drafts.

The rules in this directory support:

- validation characteristic selection;
- validation scope logic;
- acceptance criteria rationale drafting;
- system suitability planning;
- deviation handling planning;
- evidence labeling;
- human review statement enforcement.

## Important Positioning

These rules are intended to support AI-assisted draft generation only.

They must not be used to automatically approve validation protocols, validation reports, methods, specifications, or regulatory strategies.

All generated outputs intended for CMC, QA, RA, laboratory, vendor-facing, GxP, or regulatory use require review by the responsible analytical lead, QA, RA, and/or method owner.

## Rule Files

| File | Purpose |
|---|---|
| `validation_protocol_generation_rules.md` | Overall protocol generation logic and output requirements |
| `validation_characteristic_selection_matrix.md` | Rules for selecting validation characteristics by method purpose and method type |
| `validation_scope_logic.md` | Rules for full validation, partial validation, transfer, co-validation, and verification |
| `acceptance_criteria_rationale_fields.md` | Required rationale fields for acceptance criteria drafting |
| `system_suitability_and_deviation_rules.md` | Rules for system suitability and deviation handling |

## Required Output Principles

Every generated protocol draft should include:

1. intended purpose;
2. validation scope;
3. validation characteristics;
4. experimental design summary;
5. acceptance criteria with rationale;
6. system suitability strategy;
7. deviation handling rule;
8. evidence level labels;
9. missing information list;
10. human review statement.

## Standard Human Review Statement

```text
本文件由 AI 輔助產生，於 GxP、供應商溝通或法規用途使用前，必須由負責之 analytical lead、QA、RA 及 / 或 method owner 審閱確認。
```
