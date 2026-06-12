# SME Review Package: Validation Protocol Rules

## Purpose

This package prepares the first validation protocol rule set for review by an analytical SME, QA reviewer, RA reviewer, and/or method owner.

This package does not complete the SME review. It organizes the materials, review scope, checklist, and expected reviewer decisions so that the human review can be performed consistently.

---

## Review Objective

The reviewer should determine whether the current validation protocol rule set is suitable as internal draft guidance for AI-assisted validation protocol generation.

The reviewer should specifically check whether:

1. the rules are scientifically reasonable;
2. the rules avoid unsupported product-specific assumptions;
3. the rules remain extensible beyond the recombinant protein MVP;
4. the rules clearly separate AI-inferred suggestions from evidence-backed guidance;
5. the rules preserve mandatory human review before any real use.

---

## Files to Review

### Core protocol rule files

- `knowledge_base/validation_protocol_rules/validation_protocol_generation_rules.md`
- `knowledge_base/validation_protocol_rules/validation_characteristic_selection_matrix.md`
- `knowledge_base/validation_protocol_rules/validation_scope_logic.md`
- `knowledge_base/validation_protocol_rules/acceptance_criteria_rationale_fields.md`
- `knowledge_base/validation_protocol_rules/system_suitability_and_deviation_rules.md`
- `knowledge_base/validation_protocol_rules/rule_index.md`

### Machine-readable rule files

- `knowledge_base/validation_protocol_rules/machine_readable/validation_characteristic_selection_rules.json`
- `knowledge_base/validation_protocol_rules/machine_readable/validation_scope_rules.json`
- `knowledge_base/validation_protocol_rules/machine_readable/protocol_generation_defaults.json`

### Related generator and examples

- `src/validation_protocol_generator/generate_validation_protocol.py`
- `src/validation_protocol_generator/render_markdown.py`
- `src/validation_protocol_generator/render_validation_protocol_markdown.py`
- `examples/schema_samples/validation_protocol.synthetic.json`
- `examples/generated/validation_protocol.synthetic.generated.json`
- `examples/generated/validation_protocol.synthetic.generated.md`

### Related review loop

- `knowledge_base/validation_gap_rules/protocol_to_report_gap_mapping.md`
- `knowledge_base/validation_gap_rules/machine_readable/protocol_to_report_gap_mapping.json`
- `workflows/protocol_to_report_gap_feedback_workflow.md`

---

## Suggested Review Roles

| Role | Review Focus |
|---|---|
| Analytical SME | Technical correctness, method-type logic, validation characteristic selection |
| QA reviewer | Human review gate, deviation handling, document control suitability |
| RA reviewer | Regulatory positioning, unsupported claims, filing-risk wording |
| Method owner | Method-specific feasibility, acceptance criteria logic, operational practicality |
| PM / platform owner | Whether comments should become backlog items or knowledge base updates |

---

## Review Outcome Options

The reviewer should select one outcome.

| Outcome | Meaning |
|---|---|
| Accept for internal draft use | Rules may support internal draft generation after documented review |
| Accept with minor comments | Rules may be used after minor edits are tracked |
| Revise before use | Rules need material revision before use |
| Not suitable | Rules should not be used until substantially redesigned |
| Out of reviewer scope | Reviewer cannot assess some or all sections |

---

## Required Reviewer Comments

Reviewer comments should identify:

1. file path;
2. rule section or line reference if available;
3. issue type;
4. severity;
5. reviewer comment;
6. recommended action;
7. whether the rule can remain draft-only or must be revised before use.

Suggested issue types:

- scientific concern;
- validation design concern;
- QA/document control concern;
- RA/regulatory wording concern;
- product-specific assumption;
- missing human review gate;
- unclear evidence level;
- unclear acceptance criteria logic;
- unclear method type mapping;
- unclear implementation logic.

---

## Review Completion Criteria

Issue #9 should only be closed after a human reviewer has performed the review and the result is documented.

Minimum completion evidence:

1. reviewer name or role;
2. review date;
3. files reviewed;
4. review outcome;
5. major comments or confirmation that none were identified;
6. disposition plan for comments;
7. confirmation that human review statement remains mandatory.

---

## Human Review Statement

本文件由 AI 輔助產生，用於準備 SME / QA / RA / method owner 審閱。此文件本身不代表規則已完成審閱或已可用於 GxP、供應商溝通或法規用途。
