# Validation Protocol Generation Rules

## 1. Purpose

This file defines the first structured rule set for generating analytical method validation protocol drafts.

The goal is to ensure that generated protocols are:

- aligned with analytical intended purpose;
- traceable to structured rules and evidence labels;
- suitable for review by analytical lead, QA, RA, and/or method owner;
- clearly identified as draft-only;
- not positioned as automatic approval documents.

---

## 2. Required Inputs

A protocol draft generator should collect the following inputs before drafting.

| Input | Required | Notes |
|---|---:|---|
| Product profile | Yes | Use `schemas/product_profile.schema.json` where possible |
| Analytical method profile | Yes | Use `schemas/analytical_method.schema.json` where possible |
| Intended purpose | Yes | Release, stability, identity, assay, potency, purity, impurity, characterization, comparability, transfer, etc. |
| Method type | Yes | HPLC, LC-MS, ELISA, bioassay, qPCR, microbial, etc. |
| Sample matrix | Yes | DS, DP, placebo, formulation matrix, biological matrix, buffer, etc. |
| Validation scope | Yes | Full, partial, method transfer, co-validation, verification, other |
| Reportable result | Yes | Content, potency, purity %, impurity level, qualitative identity, etc. |
| Target use | Yes | Internal development, release, stability, transfer, filing support, vendor discussion, etc. |
| Existing development data | Conditional | Required when proposing acceptance criteria |
| Reference standard / controls | Conditional | Required for assay, potency, immunoassay, bioassay, and quantitative methods |
| Regulatory or internal evidence sources | Conditional | Should be linked when available |

If key information is missing, the generator should produce a missing information list rather than inventing assumptions.

---

## 3. Protocol Draft Output Sections

Generated validation protocol drafts should include these sections.

1. Protocol title
2. Method information
3. Intended purpose and validation scope
4. Background and rationale
5. Reference documents and evidence sources
6. Validation characteristic matrix
7. Experimental design
8. Standards, controls, and sample strategy
9. System suitability strategy
10. Data analysis plan
11. Acceptance criteria and rationale
12. Deviation handling
13. Missing information and assumptions
14. Evidence level and confidence labels
15. Human review statement

---

## 4. Draft-Only Rule

All generated protocols must remain draft-only until reviewed.

The generator must not state:

- protocol approved;
- method validated;
- acceptance criteria finalized;
- ready for GxP use;
- ready for regulatory submission;
- QA approved;
- RA approved.

Allowed wording:

- draft protocol;
- proposed validation design;
- suggested acceptance criteria rationale;
- requires analytical lead / QA / RA / method owner review;
- insufficient information to finalize.

---

## 5. Evidence Label Rule

Each major recommendation should be labeled using one or more of the following evidence levels.

```text
Evidence Level:
- Official regulatory source
- Internal rule table
- Curated scientific literature
- Vendor / laboratory-provided information
- Historical internal case
- AI-inferred suggestion
- Human review required
```

When official evidence is not linked yet, use:

```text
Evidence Level: Internal rule table / AI-inferred suggestion / Human review required
```

---

## 6. Missing Information Rule

If any of the following is unclear, the protocol draft should include a missing information section.

- final intended purpose;
- sample matrix;
- reportable result;
- reference standard strategy;
- specification or expected range;
- method development data;
- system suitability rationale;
- validation scope;
- target regulatory region;
- product-specific CQA relevance;
- transfer site or external laboratory context.

The generator should not silently fill these gaps with unsupported assumptions.

---

## 7. Output Quality Rule

A generated validation protocol draft is acceptable as an internal draft only if it includes:

- clear intended purpose;
- clear validation scope;
- selected validation characteristics;
- rationale for included and excluded characteristics;
- draft acceptance criteria or a placeholder stating criteria require data;
- system suitability strategy;
- deviation handling rule;
- human review statement.

If these are missing, the output should be marked as incomplete.

---

## 8. Human Review Statement

Every generated validation protocol draft must include:

```text
本文件由 AI 輔助產生，於 GxP、供應商溝通或法規用途使用前，必須由負責之 analytical lead、QA、RA 及 / 或 method owner 審閱確認。
```
