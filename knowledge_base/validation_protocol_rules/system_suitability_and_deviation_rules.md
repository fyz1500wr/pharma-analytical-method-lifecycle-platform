# System Suitability and Deviation Rules

## 1. Purpose

This file defines first-pass rules for system suitability planning and deviation handling in analytical method validation protocol drafts.

These rules are advisory and require human review before GxP, vendor-facing, or regulatory use.

---

## 2. System Suitability Purpose

System suitability tests should demonstrate that the analytical system and method are performing adequately for the intended analysis.

System suitability should monitor critical method performance, not merely generic instrument readiness.

---

## 3. System Suitability Design Rules

A generated protocol should define system suitability tests that are linked to:

1. method type;
2. intended purpose;
3. reportable result;
4. critical method parameters;
5. critical analytical response;
6. expected failure modes;
7. sample matrix risks;
8. reference standard or control strategy.

---

## 4. Example System Suitability Considerations by Method Type

| Method Type | SST Considerations |
|---|---|
| HPLC / UPLC | Retention time, resolution, tailing, theoretical plates, replicate injection precision, standard response, blank interference |
| SEC-HPLC | Resolution between aggregate/main/fragment regions, standard precision, system drift, column performance |
| CE-SDS / electrophoresis | Marker performance, migration time, resolution, control profile, integration consistency |
| LC-MS | Mass accuracy, system sensitivity, reference peptide or marker response, carryover, blank control |
| ELISA | Standard curve fit, blank response, positive/negative controls, QC samples, reagent lot controls |
| Cell-based bioassay | Reference standard curve, control response, cell performance, assay window, curve fit, replicate variability |
| Reporter gene assay | Reference curve, assay window, control response, background signal, curve fit, cell condition |
| qPCR / ddPCR | Standard curve or copy control, amplification efficiency, inhibition control, no-template control, extraction control |
| Microbial method | Growth promotion, negative control, recovery, inhibition suitability |
| Endotoxin | Positive product control, inhibition/enhancement, standard curve, negative control |

---

## 5. SST Rationale Fields

Each SST should include:

| Field | Required |
|---|---:|
| SST name | Yes |
| What it monitors | Yes |
| Why it matters | Yes |
| Proposed criterion | Yes, or state data required |
| Method performance link | Yes |
| Evidence level | Yes |
| Human review required | Yes |

---

## 6. Deviation Handling Principles

A validation protocol draft should define how deviations, failed runs, repeats, and invalid assays will be handled.

Deviation handling should include:

1. documentation requirement;
2. impact assessment requirement;
3. pre-defined invalidation criteria where possible;
4. repeat rule or retest decision logic;
5. data exclusion rule;
6. QA / analytical lead review requirement;
7. final report documentation requirement.

---

## 7. Repeat / Retest Rule Drafting

The protocol draft should avoid vague language such as:

```text
Repeat as needed.
```

Preferred draft language should define:

- what constitutes an invalid run;
- who reviews invalidation;
- whether original data are retained;
- when repeat is allowed;
- how repeat data are reported;
- how deviations affect validation conclusion.

---

## 8. Deviation Severity Classification

Suggested classification for draft planning:

| Severity | Meaning |
|---|---|
| Critical | May invalidate validation conclusion or intended use |
| Major | May affect one or more validation characteristics or acceptance criteria |
| Minor | Documented issue with limited expected impact |
| Clarification | Missing explanation or documentation requiring follow-up |

---

## 9. Required Human Review

Any deviation handling, failed run invalidation, repeat testing, or data exclusion rule intended for real use requires analytical lead and QA review.

---

## 10. Standard Human Review Statement

```text
本文件由 AI 輔助產生，於 GxP、供應商溝通或法規用途使用前，必須由負責之 analytical lead、QA、RA 及 / 或 method owner 審閱確認。
```
