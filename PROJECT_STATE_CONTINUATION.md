# PROJECT_STATE_CONTINUATION

## Current Project State

Repo: `fyz1500wr/pharma-analytical-method-lifecycle-platform`

Project status: **Foundation stage**

This project has been initiated as the main repository for the **Pharmaceutical Analytical Method Lifecycle Intelligence Platform**.

The agreed direction is documented in:

- `PROJECT_DIRECTION_CALIBRATION.md`
- `PROJECT_INSTRUCTION.md`

---

## Current Strategic Direction

The project should build a version-controlled, extensible, evidence-aware, AI-assisted platform for pharmaceutical analytical method lifecycle support.

The platform should support:

1. Product and analytical intent classification
2. Product-type to analytical-method mapping
3. Analytical method development support
4. Method optimization support
5. Validation protocol generation
6. Validation report generation
7. Technical context-aware analytical report review
8. Regulatory / literature / technology intelligence
9. Closed-loop knowledge feedback

---

## Important Architecture Decisions

1. Use **one main repo with multiple modules** at the beginning.
2. Do not split the Technical Context-Aware Analytical Report Review Module into a separate platform.
3. The Technical Context-Aware Analytical Report Review Module is a core child module of the lifecycle platform.
4. GitHub is the source of truth for rules, templates, evidence packs, and version-controlled logic.
5. Notion may be used as dashboard / task tracking, but not as the primary knowledge base.
6. Claude is preferred for final technical reasoning and document drafting.
7. Codex is preferred for repo implementation, schemas, workflows, tests, GitHub Actions, and MCP work.
8. GitHub Actions should be used to refresh and archive official regulatory source metadata.
9. MCP should expose curated evidence packs and repo knowledge to AI clients.
10. All outputs intended for GxP, vendor-facing, or regulatory use require human review.

---

## Initial MVP Direction

Initial MVP should prioritize:

```text
biologics / recombinant proteins / drug product release and stability
```

But all schemas, workflows, and knowledge base entries must remain extensible to:

- small molecules
- peptides
- monoclonal antibodies
- ADCs
- oligonucleotides
- vaccines
- cell and gene therapies
- complex formulations

---

## Next Recommended Work Items

1. Complete foundation file structure.
2. Build initial schemas.
3. Build initial product-type / method matrix.
4. Build source priority matrix.
5. Build method selection workflow.
6. Build validation protocol generation workflow.
7. Build technical context-aware report review workflow.
8. Create GitHub issues for Phase 0 and Phase 1.
9. Later: add GitHub Actions for schema validation and regulatory source refresh.
10. Later: design MCP access layer.

---

## Direction Calibration Reminder

Before future work, ask:

- Does this support the analytical method lifecycle?
- Does this preserve extensibility beyond recombinant protein MVP?
- Does this separate official evidence from AI inference?
- Does this include human review gates?
- Does this strengthen product-method mapping, method development, validation, report review, regulatory intelligence, or feedback learning?

If not, the work may be outside current project direction.
