# Method Selection Output Fields

## Purpose

This file defines the standard output fields for the Phase 1 product-to-method selection workflow.

The goal is to ensure that method recommendations are structured, reviewable, and traceable.

## Required Output Fields

| Field | Description | Required |
|---|---|---:|
| product_context | Short description of product type, sample type, dosage form, lifecycle stage, and analytical purpose | Yes |
| analytical_category | Identity, assay, potency, purity, degradation, microbiological quality, etc. | Yes |
| recommendation | Required / Conditional / Optional / Not assessable | Yes |
| candidate_methods | Candidate analytical technologies or method families | Yes |
| intended_use | Release, stability, characterization, comparability, method transfer, etc. | Yes |
| rationale | Why this analytical category is relevant | Yes |
| dependency_notes | Product, dosage form, route, matrix, lifecycle, or regulatory dependencies | Yes |
| missing_information | Information needed before finalizing method recommendation | Yes |
| risk_flags | Technical, regulatory, method development, or documentation risks | Yes |
| evidence_level | Official regulatory source / internal rule table / literature / vendor / AI-inferred / human review required | Yes |
| confidence | High / Medium / Low / Not assessed | Yes |
| human_review_required | Whether analytical lead, QA, RA, or method owner review is required | Yes |

## Recommendation Values

```text
Required
Conditional
Optional / Supportive
Not assessable
```

## Evidence Level Values

```text
Official regulatory source
Internal rule table
Curated scientific literature
Vendor / laboratory-provided information
Historical internal case
AI-inferred suggestion
Human review required
```

## Standard Human Review Statement

本文件由 AI 輔助產生，於 GxP、供應商溝通或法規用途使用前，必須由負責之 analytical lead、QA、RA 及 / 或 method owner 審閱確認。

## Notes

The output should not provide a final approval decision. It should produce a structured recommendation that can be reviewed, challenged, and refined by SMEs, QA, RA, and method owners.
