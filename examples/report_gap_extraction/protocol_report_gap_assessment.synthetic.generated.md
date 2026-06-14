# Draft Protocol / Report Gap Assessment

> AI-assisted advisory output. Human review is required before any real use.

## Assessment Summary

| Field | Value |
|---|---|
| Assessment type | protocol_report_gap_assessment_draft |
| Source document ID | synthetic-protocol-review-001 |
| Source document type | validation_protocol_draft |
| Mapping | protocol_to_report_gap_mapping |
| Mapping version | 0.1.0 |
| Gap count | 4 |
| Human review required | True |

## Gap Table

| Gap ID | Rule Area | Severity | Observed Status | Reviewer Question | Feedback Targets |
|---|---|---|---|---|---|
| PTG-002 | validation_scope | major | weak | Please provide the rationale for the selected validation scope. | validation_protocol_rules, validation_gap_rules |
| PTG-004 | acceptance_criteria | major | unclear | Please provide the basis for each acceptance criterion. | validation_protocol_rules, validation_gap_rules |
| PTG-005 | system_suitability | major | weak | Please explain how each SST monitors critical method performance. | validation_gap_rules, reviewer_question_bank |
| PTG-006 | deviation_handling | major | missing | Please provide predefined deviation and repeat testing rules. | validation_protocol_rules, validation_gap_rules |

## Detailed Gaps

### PTG-002 — validation_scope

- Severity: major
- Gap description: Validation scope is not justified
- Expected element: Scope and rationale are defined
- Observed status: weak
- Why it matters: The protocol says full validation but does not explain why full validation is required.
- Reviewer question: Please provide the rationale for the selected validation scope.
- Evidence level: internal_rule_table_human_review_required
- Feedback targets: validation_protocol_rules, validation_gap_rules
- Human review required: True

### PTG-004 — acceptance_criteria

- Severity: major
- Gap description: Acceptance criteria lack rationale or source
- Expected element: Criteria are linked to purpose, method type, and data source
- Observed status: unclear
- Why it matters: Criteria are listed but no rationale or source is provided.
- Reviewer question: Please provide the basis for each acceptance criterion.
- Evidence level: internal_rule_table_human_review_required
- Feedback targets: validation_protocol_rules, validation_gap_rules
- Human review required: True

### PTG-005 — system_suitability

- Severity: major
- Gap description: SST is generic or not linked to method performance
- Expected element: SST monitors critical method performance
- Observed status: weak
- Why it matters: SST criteria are generic and not linked to critical assay performance.
- Reviewer question: Please explain how each SST monitors critical method performance.
- Evidence level: internal_rule_table_human_review_required
- Feedback targets: validation_gap_rules, reviewer_question_bank
- Human review required: True

### PTG-006 — deviation_handling

- Severity: major
- Gap description: Failed-run or repeat rule is unclear
- Expected element: Invalid run, repeat, retest, and exclusion rules are defined
- Observed status: missing
- Why it matters: No failed-run, repeat-run, or data exclusion rule is provided.
- Reviewer question: Please provide predefined deviation and repeat testing rules.
- Evidence level: internal_rule_table_human_review_required
- Feedback targets: validation_protocol_rules, validation_gap_rules
- Human review required: True

## Human Review Statement

This gap assessment is AI-assisted and advisory only. It does not approve a protocol, report, method, validation conclusion, or regulatory strategy. Qualified human review is required before any real use.
