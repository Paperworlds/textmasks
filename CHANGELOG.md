# Changelog

All notable changes to textmasks are documented here. Dates are ISO-8601.
Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

## [0.1.0] — 2026-07-07

Birth of textmasks — the persona registry extracted as its own repo so personas
outlive any single runner (`textprompts` today, `textsessions` next).

### Added
- The persona registry: 16 curated persona definitions under `personas/`,
  migrated from `textprompts/src/textprompts/personas/`.
  - Carried over: `agent-reviewer`, `pr-reviewer`, `yaml-validator`,
    `chief-architect`, `prompt-architect`, `repo-boot`, `memory-steward`,
    `idea-expander`, `release-warden`, `echo-shell`.
  - New in this cut: `textmap-inbox-reviewer`, `outro-spection`, `tool-vetter`,
    `spec-author`, `mcp-bundle-smith`, `test-author`.
- `docs/SCHEMA.md` — the persona field reference and authoring conventions.
- `README.md` — the registry-not-runner model and the identity/role/session triad
  (`textaccounts` · textmasks · `textsessions`).
- Elastic License 2.0, matching the rest of the stack.

### Notes
- This 0.1.0 is definitions + schema only; there is no CLI (invocation stays in
  the consumers, by design).
- `textprompts` still ships its own embedded copy of these personas. Cutting it
  over to depend on textmasks — then deleting that copy — is the next step and
  is intentionally NOT done in this release.

[0.1.0]: https://github.com/Paperworlds/textmasks/releases/tag/0.1.0
