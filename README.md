# Pharmaceutical Analytical Method Lifecycle Intelligence Platform

藥品分析方法生命週期智慧平台

## 1. Project Mission

This repository is the primary system of record for building an AI-assisted, evidence-aware, and extensible **Pharmaceutical Analytical Method Lifecycle Intelligence Platform**.

本專案目標是建立一個可支援藥品分析方法完整生命週期的平台，而不是單純的分析方法報告產生器、確效 protocol 產生器、實驗室報告審閱工具或法規新聞追蹤器。

The platform supports the following lifecycle:

```text
Product classification
→ CQA / analytical intent mapping
→ analytical method selection
→ analytical method development strategy
→ method optimization support
→ validation protocol generation
→ validation report generation
→ internal / external laboratory document review
→ technical and regulatory gap assessment
→ knowledge feedback loop
```

中文生命週期：

```text
產品分類
→ CQA / 分析目的對應
→ 分析項目與方法選擇
→ 分析方法開發策略
→ 方法條件優化
→ 確效 protocol 建立
→ 確效報告撰寫
→ 內部 / 外部實驗室文件審閱
→ 技術與法規缺失評估
→ 審閱結果回饋知識庫
```

The system is intended to help CMC, RA, QA, PM, analytical scientists, and reviewers make faster, better-structured, and more traceable decisions regarding pharmaceutical analytical methods.

---

## 2. What This Project Is

This project is:

- an analytical method lifecycle intelligence platform;
- a structured knowledge base for product-method mapping;
- a workflow repository for method development, validation, and review;
- a source-traceable evidence and rule management space;
- a foundation for Claude / Codex / GitHub Actions / MCP-assisted execution;
- a future dashboard and integration source for CMC, RA, QA, vendor management, and Notion workflows.

---

## 3. What This Project Is Not

This project is not:

- a generic chatbot;
- a simple validation report template repository;
- a regulatory news scraper without method-level impact analysis;
- a single-product IFN-only knowledge base;
- a Notion-only dashboard;
- an automated approval system;
- a replacement for analytical SME, QA, RA, or method owner judgment;
- a system that treats AI inference, vendor claims, literature, and official guidance as equivalent.

All outputs intended for GxP, vendor-facing, CMC, QA, RA, laboratory, or regulatory use require human review.

---

## 4. Core Direction Documents

Before making major changes, read these files first:

| File | Purpose |
|---|---|
| `PROJECT_DIRECTION_CALIBRATION.md` | Core direction calibration source for future PRs, architecture decisions, and scope control |
| `PROJECT_INSTRUCTION.md` | Execution rules, AI/tool responsibilities, evidence labeling, and human review principles |
| `PROJECT_STATE_CONTINUATION.md` | Current project state, agreed decisions, and next work items |
| `PROJECT_ROADMAP.md` | Phase roadmap from foundation to closed-loop knowledge management |

`PROJECT_DIRECTION_CALIBRATION.md` is the primary reference for deciding whether future work is aligned with the project direction.

---

## 5. Core Platform Modules

### Module 1 — Product & Analytical Intent Classification

Classifies product type, molecule type, dosage form, sample type, development stage, target region, CQA, and analytical purpose before selecting methods.

### Module 2 — Product-Type / Analytical Method Matrix

Maps product types and analytical purposes to candidate analytical categories and method types.

Initial MVP scope:

```text
biologics / recombinant proteins / drug product release and stability
```

The architecture must remain extensible to small molecules, peptides, monoclonal antibodies, ADCs, oligonucleotides, vaccines, cell and gene therapies, and complex formulations.

### Module 3 — Analytical Method Development Support

Supports method development rationale, method risk assessment, critical method parameters, screening design, robustness planning, DoE / enhanced approach thinking, MODR logic, system suitability, and troubleshooting.

This module may suggest scientific directions, but it must not claim to determine final optimal conditions without experimental evidence.

### Module 4 — Validation Protocol Generator

Generates analytical method validation protocol drafts based on intended purpose, method type, product profile, sample matrix, validation scope, and evidence rules.

Output remains draft-only and requires analytical lead / QA / RA / method owner review.

### Module 5 — Validation Report Generator

Generates validation report drafts when structured data are available.

Without structured data, the platform may generate a narrative review or report shell, but should not generate definitive validation conclusions.

### Module 6 — Technical Context-Aware Analytical Report Review Module

A core child module of the platform.

This module helps PMs, reviewers, QA, RA, and analytical leads rapidly understand unfamiliar, complex, or emerging analytical reports.

It should produce:

- technical principle cards;
- method suitability assessments;
- technical and regulatory gap assessments;
- reviewer question lists;
- SME review flags;
- evidence-level labels.

This module does not approve reports. It helps reviewers understand, triage, and ask better questions.

### Module 7 — Regulatory / Literature / Technology Intelligence

Tracks official guidance, curated source metadata, technology context, literature metadata, and internal review knowledge.

Official regulatory sources should be prioritized over literature, vendor claims, and AI inference when making compliance-related conclusions.

---

## 6. Repository Structure

```text
pharma-analytical-method-lifecycle-platform/
├─ README.md
├─ PROJECT_DIRECTION_CALIBRATION.md
├─ PROJECT_INSTRUCTION.md
├─ PROJECT_STATE_CONTINUATION.md
├─ PROJECT_ROADMAP.md
│
├─ knowledge_base/
│  ├─ regulatory_source_priority_matrix.md
│  ├─ product_type_method_matrix/
│  ├─ analytical_technology_registry/
│  ├─ method_principle_cards/
│  ├─ common_failure_modes/
│  ├─ validation_gap_rules/
│  ├─ reviewer_question_bank/
│  └─ evidence_packs/
│
├─ schemas/
│  ├─ product_profile.schema.json
│  ├─ analytical_method.schema.json
│  ├─ evidence_source.schema.json
│  ├─ validation_protocol.schema.json
│  ├─ technical_context_card.schema.json
│  └─ analytical_report_gap_assessment.schema.json
│
├─ workflows/
│  ├─ product_classification_workflow.md
│  ├─ method_selection_workflow.md
│  ├─ validation_protocol_generation_workflow.md
│  └─ technical_context_report_review_workflow.md
│
├─ templates/
│  ├─ validation_protocol_template.md
│  ├─ technical_context_card_template.md
│  └─ lab_report_gap_assessment_template.md
│
├─ mcp/
├─ dashboard/
├─ docs/
├─ examples/
├─ src/
├─ tests/
└─ .github/workflows/
```

---

## 7. Tool Responsibilities

### Claude

Claude is preferred for:

- final technical reasoning;
- regulatory interpretation;
- analytical method development rationale;
- protocol drafting;
- report drafting;
- technical report review;
- gap assessment;
- reviewer question generation;
- PM briefing notes;
- direction calibration.

### Codex

Codex is preferred for:

- repository implementation;
- schema implementation;
- workflow implementation;
- GitHub Actions;
- tests;
- MCP server development;
- data pipelines;
- file structure maintenance;
- PR preparation.

### GitHub Actions

GitHub Actions should be used for:

- schema validation;
- source metadata refresh;
- regulatory evidence pack generation;
- literature metadata refresh;
- dashboard data refresh;
- artifact generation;
- automated checks.

### MCP

MCP should act as an access layer for curated repository knowledge, evidence packs, rules, templates, and source metadata.

Preferred pattern:

```text
GitHub Actions retrieves and normalizes sources
→ evidence packs are stored in this repo
→ MCP exposes curated evidence and rules
→ Claude / Codex query MCP
→ outputs include evidence level and human review labels
```

MCP should not be used as an uncontrolled live web search layer.

---

## 8. Evidence and Confidence Labels

Outputs should distinguish evidence type whenever practical.

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

Recommended confidence labels:

```text
Confidence:
- High: directly supported by official guidance or approved internal rule
- Medium: supported by related guidance, accepted practice, or curated literature
- Low: exploratory suggestion requiring SME review
```

AI inference must not be presented as regulatory fact.

---

## 9. Human Review Gate

All outputs intended for CMC, QA, RA, laboratory, vendor-facing, GxP, or regulatory use must include a human review requirement.

Standard statement:

```text
本文件由 AI 輔助產生，於 GxP、供應商溝通或法規用途使用前，必須由負責之 analytical lead、QA、RA 及 / 或 method owner 審閱確認。
```

The platform may assist with decisions, but it must not approve protocols, reports, methods, validation conclusions, or regulatory strategies by itself.

---

## 10. Development Roadmap

### Phase 0 — Foundation

Current status: in progress / partially complete.

Goals:

- establish project direction;
- establish repository architecture;
- establish schemas;
- establish workflows;
- establish templates;
- establish evidence and human review rules.

### Phase 1 — Product → Method Matrix MVP

Initial MVP scope:

```text
biologics / recombinant proteins / drug product release and stability
```

Goal: produce structured method selection output with analytical category recommendations, method type suggestions, evidence level, missing information, risk flags, and human review requirement.

### Phase 2 — Validation Protocol Generator

Goal: generate structured analytical method validation protocol drafts based on product profile, method type, intended purpose, and validation scope.

### Phase 3 — Technical Context-Aware Report Review

Goal: help reviewers rapidly understand unfamiliar or complex analytical reports and generate technical context cards, gap assessments, reviewer questions, and SME review flags.

### Phase 4 — Regulatory / Literature Intelligence

Goal: add GitHub Actions source refresh, evidence pack generation, literature metadata refresh, and MCP access layer.

### Phase 5 — Closed-Loop Knowledge Management

Goal: capture recurring gaps, update method checklists and question banks, track vendor/lab issues, and improve future protocol/report templates.

---

## 11. Current Foundation Status

Completed foundation items include:

- direction calibration document;
- project instruction document;
- continuation state document;
- roadmap;
- initial knowledge base directories;
- initial schemas;
- initial workflows;
- initial templates;
- schema validation GitHub Action;
- initial biologics / recombinant protein DP release and stability method matrix;
- seed backlog and implementation notes.

See:

```text
docs/phase0_foundation_checklist.md
```

---

## 12. Current Issues

Initial GitHub issues were created to guide the next work items:

1. Expand README into full platform overview.
2. Expand biologics / recombinant protein DP release and stability method matrix.
3. Create synthetic examples and schema validation samples.
4. Draft validation protocol generation rules.
5. Build first technical context-aware report review example.

---

## 13. Data Governance

Do not commit confidential product data, raw lab reports, vendor documents, patient data, personal data, or GxP-controlled records into this repository unless they are properly sanitized and approved for repository use.

Use synthetic examples for testing and demonstration.

See:

```text
examples/sample_data_governance.md
```

---

## 14. Direction Calibration Rule

Before adding a new module, workflow, PR, or integration, ask:

1. Does it support the analytical method lifecycle?
2. Does it preserve extensibility beyond the initial recombinant protein MVP?
3. Does it distinguish official evidence from AI inference?
4. Does it preserve human review gates?
5. Does it strengthen product-method mapping, method development, validation, report review, regulatory intelligence, or feedback learning?
6. Does it avoid duplicating rules outside the source of truth?
7. Does it help PMs, reviewers, analytical leads, QA, or RA make better decisions?

If the answer to most of these questions is no, the change is likely outside the project’s core direction.

---

## 15. Final Positioning

This repository is the foundation for a version-controlled, extensible, evidence-aware, AI-assisted pharmaceutical analytical method lifecycle platform.

It should help users understand established and emerging analytical technologies, identify technical and regulatory gaps, generate high-quality draft documents, and support fast PM / CMC / QA / RA decision-making.

The system relies on structured rules, curated regulatory evidence, technical knowledge cards, and human review gates. It does not replace expert judgment or regulatory responsibility.
