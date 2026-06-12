# Protocol-to-Report Gap Feedback Workflow

## Purpose

This workflow defines how validation protocol planning rules feed into later protocol or report review.

It supports the platform feedback loop:

```text
Validation protocol planning
→ expected design elements
→ protocol/report review
→ gap assessment
→ reviewer questions
→ knowledge base update
```

---

## Inputs

Typical inputs include:

- generated validation protocol draft JSON;
- validation protocol draft Markdown;
- vendor or laboratory protocol/report summary;
- method profile;
- product profile;
- validation scope;
- method type;
- intended purpose;
- protocol-to-gap mapping rules.

---

## Review Steps

### Step 1. Identify Planning Rule Area

Map the reviewed content to a planning rule area, such as:

- intended purpose;
- validation scope;
- validation characteristics;
- acceptance criteria;
- system suitability;
- deviation handling;
- reference standard;
- sample matrix;
- human review gate.

### Step 2. Check Expected Design Element

For each rule area, check whether the expected design element is present and adequately justified.

### Step 3. Generate Gap When Needed

If the expected element is missing, unclear, or unsupported, create a review gap using:

- gap ID;
- severity;
- why it matters;
- suggested reviewer question;
- evidence level;
- human review requirement.

### Step 4. Route to Feedback Target

Each mapped gap should identify where the learning should be fed back:

- validation protocol rules;
- validation gap rules;
- reviewer question bank;
- method principle cards;
- templates;
- project instructions.

### Step 5. Preserve Human Review Gate

The workflow must not approve a protocol, report, method, validation conclusion, or regulatory strategy.

It should only help reviewers identify issues and ask better questions.

---

## Recommended Output Fields

| Field | Description |
|---|---|
| gap_id | Mapping rule ID, for example PTG-001 |
| rule_area | Planning rule area |
| severity | Critical, major, minor, or clarification |
| gap_description | What is missing, unclear, or unsupported |
| why_it_matters | Technical or review impact |
| reviewer_question | Suggested question for lab, vendor, author, or internal owner |
| evidence_level | Source category for the rule |
| feedback_target | Knowledge base area to update |
| human_review_required | Always true for real use |

---

## Example Output

| gap_id | severity | gap_description | reviewer_question | feedback_target |
|---|---|---|---|---|
| PTG-005 | Major | SST is listed but not linked to critical method performance | Please explain how each SST monitors critical method performance. | validation_gap_rules / reviewer_question_bank |
| PTG-004 | Major | Acceptance criteria are listed without rationale | Please provide the basis for each acceptance criterion. | validation_protocol_rules / validation_gap_rules |

---

## Governance

- Advisory only.
- Human review required.
- No automatic approval.
- No final regulatory conclusion without qualified review.
- AI-inferred findings must be labeled as such.

## Human Review Statement

本流程由 AI 輔助建立，用於審閱與知識庫回饋輔助。於 GxP、供應商溝通或法規用途使用前，必須由負責之 analytical lead、QA、RA 及 / 或 method owner 審閱確認。
