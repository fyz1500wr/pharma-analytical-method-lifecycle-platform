# GitHub Project Manual Operating Notes

## Purpose

This note defines how to operate this repository during the early build stage.

## Current Practice

- Use GitHub issues for Phase 0 / Phase 1 work tracking.
- Use PRs for non-trivial changes once the repository foundation is stable.
- Keep `PROJECT_DIRECTION_CALIBRATION.md` as the direction calibration source.
- Keep `PROJECT_STATE_CONTINUATION.md` updated after major decisions or milestones.
- Do not merge changes that convert the project into a generic chatbot, a single-product knowledge base, or a regulatory news scraper without method-level impact analysis.

## Suggested Issue Labels

Labels may be created manually later:

- `phase-0-foundation`
- `phase-1-mvp`
- `schema`
- `workflow`
- `knowledge-base`
- `technical-review`
- `regulatory-intelligence`
- `mcp`
- `dashboard`
- `human-review-required`

## Merge Decision Rule

Before merging future PRs, check against the direction calibration questions in `PROJECT_DIRECTION_CALIBRATION.md`.
