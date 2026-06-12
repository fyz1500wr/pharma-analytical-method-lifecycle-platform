# Protocol Rule to Report Review Gap Mapping

## Purpose

This mapping connects validation protocol planning rules to later protocol or report review gaps.

It is used to support the closed-loop review pattern:

```text
Protocol planning rule
→ expected design element
→ missing or weak element in protocol/report
→ review gap
→ reviewer question
→ feedback into rule base
```

All mappings are advisory and require human review before use in CMC, QA, RA, laboratory, vendor-facing, GxP, or regulatory contexts.

---

## Mapping Table

| Protocol Planning Rule Area | Expected Design Element | Review Gap If Missing or Weak | Suggested Reviewer Question | Severity | Evidence Level |
|---|---|---|---|---|---|
| Intended purpose | Clear use such as release, stability, transfer, characterization, or development | Intended use is unclear or broader than supported data | Please clarify the intended use and whether the data support that use. | Major | Internal rule table / Human review required |
| Validation scope | Full, partial, transfer, co-validation, verification, or other with rationale | Validation scope is not justified | Please provide the rationale for the selected validation scope. | Major | Internal rule table / Human review required |
| Validation characteristics | Included and excluded characteristics with rationale | Expected validation characteristic is missing or excluded without rationale | Please explain why this characteristic is not included or not applicable. | Major | Internal rule table / Human review required |
| Acceptance criteria | Proposed criteria linked to purpose, method type, and data source | Acceptance criteria lack rationale or source | Please provide the basis for each acceptance criterion. | Major | Internal rule table / Human review required |
| System suitability | Tests linked to critical method performance | SST is generic or not linked to method performance | Please explain how each SST monitors critical method performance. | Major | Internal rule table / Human review required |
| Deviation handling | Defined invalid run, repeat, retest, and exclusion logic | Failed-run or repeat rule is unclear | Please provide predefined deviation and repeat testing rules. | Major | Internal rule table / Human review required |
| Reference standard | Standard identity, qualification, handling, and role | Reference standard strategy is unclear | Please clarify reference standard qualification, storage, handling, and use. | Major | Internal rule table / Human review required |
| Sample matrix | Matrix suitability or interference assessment | Matrix effect is not addressed | Please provide matrix effect or suitability assessment for the intended matrix. | Major | Internal rule table / Human review required |
| Reportable range | Range covers expected sample and decision range | Range does not cover intended reportable result | Please justify the reportable range for the intended use. | Major | Internal rule table / Human review required |
| Data analysis | Model, calculation, and decision rules are described | Data analysis model is unclear | Please describe the calculation, model, and decision rule. | Major | Internal rule table / Human review required |
| Evidence labels | Source and confidence are labeled | Recommendation lacks traceability | Please identify the source and confidence for this recommendation. | Clarification | Internal rule table / Human review required |
| Human review gate | Review requirement is clearly stated | Output appears to imply approval or final use | Please confirm that this output remains draft-only and requires qualified review. | Critical | Human review required |

---

## Reviewer Output Requirement

When a mapped gap is triggered, the review output should include:

1. gap ID or mapped rule area;
2. gap severity;
3. why it matters;
4. suggested reviewer question;
5. evidence level;
6. human review requirement;
7. recommended feedback target in the knowledge base.

---

## Feedback Target

Mapped gaps should feed into one or more of:

- `knowledge_base/validation_protocol_rules/`
- `knowledge_base/validation_gap_rules/`
- `knowledge_base/reviewer_question_bank/`
- `knowledge_base/method_principle_cards/`
- future report review examples under `examples/technical_context_review/`

---

## Human Review Statement

本對照表由 AI 輔助建立，用於審閱輔助。於 GxP、供應商溝通或法規用途使用前，必須由負責之 analytical lead、QA、RA 及 / 或 method owner 審閱確認。
