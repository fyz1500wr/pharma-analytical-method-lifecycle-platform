# Regulatory Source Priority Matrix

## Purpose

This matrix defines how regulatory, scientific, vendor, and AI-generated information should be prioritized when producing analytical method lifecycle outputs.

## Source Priority

| Tier | Source Type | Examples | Use |
|---|---|---|---|
| Tier 1 | Official regulatory guidance | ICH, FDA, EMA, TFDA | Primary basis for regulatory and validation expectations |
| Tier 2 | Official compendial / authority metadata | USP metadata, Ph. Eur. metadata, EDQM, WHO, PMDA | Supporting context, where legally accessible and applicable |
| Tier 3 | Curated scientific literature | PubMed, Europe PMC, Crossref metadata, peer-reviewed reviews | Technical context and emerging technology understanding |
| Tier 4 | Vendor / lab-provided information | CRO / CMO method descriptions, kit manuals, technical notes | Background and method-specific explanation, not regulatory authority |
| Tier 5 | Internal historical cases | Prior reviews, prior gaps, prior SME decisions | Internal learning and risk reminders |
| Tier 6 | AI-inferred suggestions | Claude / Codex generated rationale | Exploratory only; must be labeled and reviewed |

## Rules

1. Official regulatory sources override literature and vendor claims.
2. Literature may explain method principles but should not be treated as direct regulatory requirement.
3. Vendor information may explain implementation details but should not be used as standalone regulatory justification.
4. AI inference must never be presented as regulatory fact.
5. Outputs should state evidence level and confidence whenever practical.
6. Human review is mandatory before GxP, vendor-facing, or regulatory use.
