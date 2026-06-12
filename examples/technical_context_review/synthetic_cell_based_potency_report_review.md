# Synthetic Technical Context-Aware Report Review Example

## 1. Example Status

```text
Document type: Synthetic example
Use: Training / workflow demonstration only
Real product data: No
Real vendor data: No
GxP record: No
Human review required: Yes
```

This example demonstrates how the Technical Context-Aware Analytical Report Review Module should review an analytical report without claiming automatic approval.

---

## 2. Synthetic Report Scenario

A synthetic external laboratory report describes a cell-based potency assay for a recombinant protein drug product. The report states that the method is intended to support release and stability testing.

The report includes a reference standard curve, sample response curves, basic precision summary, and a final conclusion that the method is suitable for its intended purpose.

The report does not clearly describe matrix effect assessment, parallelism, reference standard qualification, or the rationale for system suitability criteria.

---

## 3. Technical Principle Card Summary

| Item | Review Summary |
|---|---|
| Method family | Cell-based potency assay |
| What it measures | A biological response used as a surrogate for product activity |
| Signal source | Cell response generated after exposure to reference standard and sample |
| Typical output | Relative potency or activity estimate |
| Suitable for | Potency support when the biological response is relevant to the product mechanism |
| Not sufficient for | Identity, purity, impurity, or content unless supported by separate methods |
| Key controls | Reference standard, positive control, negative control, matrix control, assay control, cell condition control |
| Main review risk | Variability, matrix interference, weak curve model justification, missing parallelism, unclear reference standard strategy |

Evidence level:

```text
Internal rule table / AI-assisted synthetic example / Human review required
```

Confidence:

```text
Medium for workflow demonstration; not assessed for real use
```

---

## 4. Method Suitability Assessment

| Review Question | Assessment | Comment |
|---|---|---|
| Does the method match the stated analytical purpose? | Potentially yes | A cell-based assay can support potency if the biological response is relevant to the product mechanism. |
| Does the report explain what biological response is measured? | Partial | The synthetic report describes a response but does not clearly justify its relevance to potency. |
| Is matrix effect addressed? | Gap | DP matrix impact on cell response is not clearly assessed. |
| Is parallelism addressed? | Gap | Dilution-response similarity between reference standard and sample is not clearly demonstrated. |
| Is the reference standard strategy adequate? | Clarification needed | Qualification status and suitability for relative potency calculation are not clearly described. |
| Are system suitability criteria meaningful? | Gap | Criteria are listed but not linked to critical assay performance. |
| Is the conclusion fully supported? | Not yet | The report conclusion may be reasonable, but additional rationale and data are needed. |

---

## 5. Gap Assessment

| Severity | Gap | Why It Matters | Recommended Action | Evidence Level |
|---|---|---|---|---|
| Major | Matrix effect is not clearly evaluated | Product matrix may alter cell response and bias potency estimate | Request matrix control or dilution recovery assessment | Internal rule table / Human review required |
| Major | Parallelism is not clearly demonstrated | Non-parallel sample and standard curves can make relative potency unreliable | Request dilution-response comparison and predefined decision criteria | Internal rule table / Human review required |
| Major | Reference standard qualification is unclear | Relative potency depends on a suitable and controlled reference standard | Request reference standard qualification status and handling history | Internal rule table / Human review required |
| Major | System suitability rationale is weak | SST should monitor critical assay performance, not only generic run acceptance | Request rationale linking SST to assay window, curve fit, control response, and variability | Internal rule table / Human review required |
| Clarification | Intended use is broader than demonstrated data | Release and stability use may require different evidence than development screening | Ask whether this report supports final validation, feasibility, transfer, or routine use | AI-assisted synthetic example / Human review required |

---

## 6. Reviewer Question List

1. Please clarify whether this report is intended to support method development, validation, method transfer, release testing, stability testing, or only feasibility evaluation.
2. Please provide the biological rationale linking the assay response to the intended potency attribute.
3. Please provide matrix effect assessment for the actual drug product matrix or justify why matrix effect is not applicable.
4. Please provide parallelism or dilution-response comparison between reference standard and sample.
5. Please clarify the reference standard qualification status, storage condition, handling history, and suitability for relative potency calculation.
6. Please explain the rationale for each system suitability criterion and how it monitors critical assay performance.
7. Please provide failed-run, repeat-run, or invalidation rules if any runs were excluded or repeated.
8. Please clarify whether the method range covers the expected sample concentration, specification range, and stability trend range.

---

## 7. SME Review Flag Logic

```text
SME Review Required: Yes
```

Reason:

- The method is a biological potency assay.
- Matrix effect is not clearly addressed.
- Parallelism is not clearly addressed.
- Reference standard strategy is unclear.
- The report may be used for release and stability decisions.

Recommended reviewers:

- analytical method owner;
- bioassay SME;
- QA reviewer;
- RA reviewer if the report supports filing or response to authority questions.

---

## 8. Unknown / Emerging Technology Handling Note

If the platform encounters a method or terminology that is not internally mapped, it should classify the technology status as:

```text
Known but not internally mapped
```

or:

```text
Emerging / insufficient internal knowledge
```

In that mode, the platform should not provide a final suitability conclusion. It should instead:

1. generate a technical principle card;
2. identify what the method appears to measure;
3. identify what the method cannot support without more evidence;
4. generate SME questions;
5. label conclusions as human-review-required.

---

## 9. Draft Conclusion

The synthetic report provides an initial basis for understanding the assay, but the review identifies several gaps that should be resolved before the report is used to support release, stability, vendor-facing, GxP, or regulatory decisions.

This example does not approve the method or report.

---

## 10. Human Review Statement

本文件由 AI 輔助產生，於 GxP、供應商溝通或法規用途使用前，必須由負責之 analytical lead、QA、RA 及 / 或 method owner 審閱確認。
