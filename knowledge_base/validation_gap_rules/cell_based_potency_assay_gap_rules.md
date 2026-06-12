# Cell-Based Potency Assay Gap Rules

## Purpose

This file provides first-pass gap rules for reviewing cell-based potency assay documents.

These rules support the Technical Context-Aware Analytical Report Review Module and should be used as advisory review prompts only.

---

## Gap Rule Table

| Rule ID | Trigger | Gap Severity | Why It Matters | Suggested Reviewer Question | Evidence Level | Human Review |
|---|---|---|---|---|---|---|
| CBP-GAP-001 | Method purpose is not clearly stated | Major | Review cannot determine whether data support development, release, stability, transfer, or characterization | Please clarify the intended use of the method and report. | Internal rule table | Yes |
| CBP-GAP-002 | Biological response is not linked to potency attribute | Major | A cell response is not automatically equivalent to potency unless scientifically justified | Please explain how the measured response is linked to product biological activity. | Internal rule table | Yes |
| CBP-GAP-003 | Matrix effect not assessed | Major | Product matrix may bias response, recovery, or curve behavior | Please provide matrix effect assessment using the intended sample matrix. | Internal rule table | Yes |
| CBP-GAP-004 | Parallelism not assessed where relative potency is reported | Major | Non-parallel curves may invalidate relative potency interpretation | Please provide parallelism or dilution-response comparison between reference and sample. | Internal rule table | Yes |
| CBP-GAP-005 | Reference standard strategy unclear | Major | Potency estimates depend on suitable reference standard control | Please clarify reference standard qualification, storage, handling, and intended role. | Internal rule table | Yes |
| CBP-GAP-006 | Curve model not justified | Major | Incorrect model may bias potency estimate | Please justify the curve model, weighting, and reportable range. | Internal rule table | Yes |
| CBP-GAP-007 | SST criteria are generic | Major | SST should monitor critical assay performance, not only generic run status | Please explain how each SST criterion monitors critical assay performance. | Internal rule table | Yes |
| CBP-GAP-008 | Failed-run or repeat-run rule missing | Major | Uncontrolled repeat or exclusion rules may bias validation or report conclusions | Please provide predefined failed-run, invalidation, repeat, and data exclusion rules. | Internal rule table | Yes |
| CBP-GAP-009 | Report conclusion exceeds supporting data | Critical / Major | Data may not support release, stability, or filing use | Please clarify which conclusions are directly supported by the submitted data. | Internal rule table | Yes |
| CBP-GAP-010 | Stability use claimed but potency trend sensitivity unclear | Major | Stability use requires ability to detect meaningful activity change | Please explain how the method detects potency change during stability studies. | Internal rule table | Yes |

---

## Review Output Requirement

When one of these rules is triggered, the output should include:

- gap severity;
- gap description;
- why it matters;
- recommended action;
- reviewer question;
- evidence level;
- human review requirement.

---

## Human Review Statement

本規則表由 AI 輔助建立，用於審閱輔助。於 GxP、供應商溝通或法規用途使用前，必須由負責之 analytical lead、QA、RA 及 / 或 method owner 審閱確認。
