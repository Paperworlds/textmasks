# textmasks — Claude Instructions

## Project
The persona ("mask") registry for the Paperworlds stack. Data-first: curated
persona definitions under `personas/`, plus the schema in `docs/SCHEMA.md`.
Registry, not runner — invocation lives in consumers (textprompts, textsessions).

## Working here
- Personas are contracts. Bump the `# SPEC: <name> v<semver>` comment on any
  behavioural change.
- Keep least-privilege tool grants; deny destructive tools explicitly.
- New/changed persona → validate it parses and update `CHANGELOG.md`.

## Commit rules (Paperworlds)
- GPG-sign every commit (`git commit -S`). No `Co-Authored-By` lines.
- Identity: `user.email = paolo@paradigm.co`.
- Prefix the subject with `[textmasks]`.
- Update `CHANGELOG.md` under `## [Unreleased]` for anything notable.
- Never commit secrets, `op://` paths, or credentials.

## Relationship to textprompts
textprompts currently ships an embedded copy of these personas. The canonical
home is here. The cutover (textprompts depends on textmasks; its copy removed)
is pending — do not let the two drift silently; if you edit a persona, note
which side is authoritative.
