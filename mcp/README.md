# MCP Design

## Purpose

This directory will contain MCP-related design and implementation files.

MCP should serve as the access layer that allows Claude, Codex, or other AI clients to query curated repository knowledge, evidence packs, regulatory source metadata, method rules, and templates.

## Preferred Pattern

```text
GitHub Actions retrieves and normalizes official sources / literature metadata
→ evidence packs are stored in this repo
→ MCP server exposes curated evidence packs and rules
→ Claude / Codex query MCP
→ outputs include evidence level and human review labels
```

## Initial MCP Servers Planned

1. `regulatory_source_server`
   - Query official guidance metadata and curated guidance summaries.
2. `literature_context_server`
   - Query curated literature metadata for analytical technology context.
3. `repository_knowledge_server`
   - Query product-method matrix, validation gap rules, reviewer question bank, templates, and method principle cards.

## Safety / Governance Rules

- MCP should not act as an uncontrolled live web search layer.
- MCP responses must preserve source metadata.
- AI-generated summaries must be labeled as AI-assisted unless reviewed.
- Outputs intended for GxP, vendor-facing, or regulatory use require human review.
