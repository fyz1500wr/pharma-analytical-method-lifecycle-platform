# Validation Scope Logic

## 1. Purpose

This file defines first-pass rules for selecting and documenting analytical method validation scope.

The scope decision must be reviewed by the responsible analytical lead, QA, RA, and/or method owner before any GxP, vendor-facing, or regulatory use.

---

## 2. Scope Types

| Scope | Definition | Typical Use |
|---|---|---|
| Full validation | Complete validation package for intended use | New method, new intended use, release/stability method, major method change |
| Partial validation | Targeted validation of affected characteristics | Method change, matrix change, range change, site change, reagent change, instrument change |
| Method transfer | Demonstrate receiving lab can perform method suitably | Transfer from development lab to QC lab, external lab, CMO/CRO |
| Co-validation | Multi-site or multi-lab validation approach | Parallel validation across sites or laboratories |
| Verification | Confirm suitability of an existing method under defined local conditions | Compendial or previously validated method used in new context |
| Other | Case-specific scope | Exploratory, characterization, feasibility, bridging, or non-routine use |

---

## 3. Full Validation Triggers

Consider full validation when one or more apply:

1. method is new;
2. method is intended for release or stability decision-making;
3. method supports regulatory filing;
4. method has not been validated for this product, matrix, or intended purpose;
5. reportable result is used for specification;
6. method type or platform is substantially changed;
7. method output is used to justify shelf-life, comparability, or major CMC decision;
8. prior validation is unavailable, incomplete, or not applicable.

---

## 4. Partial Validation Triggers

Consider partial validation when one or more apply:

1. sample matrix changes;
2. dosage form or formulation changes;
3. sample preparation changes;
4. analytical range changes;
5. reportable unit changes;
6. critical reagent, column, instrument, software, or cell bank changes;
7. method parameter changes may affect performance;
8. site or analyst conditions change but prior validation remains mostly applicable;
9. intended use changes only in a limited way.

Partial validation should identify exactly which characteristics are affected and why other characteristics do not need repeat evaluation.

---

## 5. Method Transfer Triggers

Consider method transfer when:

1. a method is moved to a new lab;
2. an external lab, CRO, CMO, or QC site will perform the method;
3. analyst, instrument, site, or system differences may affect performance;
4. generated results will be used for release, stability, or regulated CMC decision-making.

A transfer protocol should define:

- sending unit and receiving unit responsibilities;
- transfer samples;
- number of runs;
- comparative criteria;
- system suitability;
- deviation handling;
- acceptance criteria;
- data review responsibilities;
- human review requirement.

---

## 6. Co-validation Triggers

Consider co-validation when:

1. multiple labs participate in the validation;
2. development and QC labs jointly generate validation data;
3. external lab data are intended to support the validation package;
4. cross-site comparability is part of the strategy.

Co-validation plans should define how data from each site will be pooled, compared, or separately evaluated.

---

## 7. Verification Triggers

Consider verification when:

1. an established or compendial method is used;
2. prior validation exists and is applicable;
3. local suitability must be confirmed;
4. product matrix may require suitability checks;
5. method is not substantially modified.

Verification should not be used to avoid validation when intended use, matrix, or method design materially differs from prior evidence.

---

## 8. Scope Decision Output Fields

A generated protocol draft should include:

| Field | Required |
|---|---:|
| selected scope | Yes |
| scope rationale | Yes |
| prior validation evidence | Conditional |
| changed elements | Conditional |
| affected validation characteristics | Conditional |
| excluded characteristics rationale | Conditional |
| transfer or receiving lab information | Conditional |
| missing information | Yes if incomplete |
| human review required | Yes |

---

## 9. Human Review Requirement

The generator may recommend a validation scope, but final validation scope must be confirmed by qualified human reviewers.
