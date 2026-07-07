# textmasks

The persona registry for the [Paperworlds](https://github.com/Paperworlds) stack.

> *persona* (n.) — from Latin, the **mask** an actor wore to play a role. A mask
> is not the actor; it is the part they take on. That's what lives here.

`textmasks` is a curated library of **personas**: each one a YAML file declaring
a Claude subagent — a system prompt, a scoped `allowed_tools` / `disallowed_tools`
set, an optional model, and a typed `inputs:` schema. A persona is a reusable,
named **role** you can put on without hand-rolling the prompt and tool list every
time.

## Registry, not runner

textmasks owns **what a persona is** — definition, schema, validation,
resolution, rendering. It does **not** own **who spawns the process**. That
separation is the whole point: personas are a shared vocabulary that must
outlive any single tool that invokes them.

```
                      ┌── textprompts   → resolve → spawn `claude -p`   (today)
 textmasks ───────────┼── textsessions  → launch / resume a session as a mask (next)
  defs · schema        └── textserve     → surface a mask as context (maybe)
  · resolve · render
```

Invocation verbs (`run`, `use`, `launch`) belong to the consumer. textmasks just
hands back a resolved spec: `system_prompt` + tool flags + typed inputs.

## Where it sits

A persona is a **role**. It composes with the other halves of an agent session:

| Concern | Owned by | Answers |
|---|---|---|
| **Identity** | [textaccounts](https://github.com/Paperworlds/textaccounts) | *who* you are — git identity, base dir, `~/.claude` profile |
| **Role** | **textmasks** | *what* you're doing — prompt + tool scope + inputs |
| **Session** | [textsessions](https://github.com/Paperworlds/textsessions) | the live session that binds a profile + a mask to a repo |

> **a session = repo + profile (who you are) + mask (what role you play)**

## Anatomy of a mask

```yaml
# SPEC: <name> v<major.minor.patch>
description: "one line — what this role does"
mode: task            # task (finishes on its own) | interactive (adopted by a host session)
model: sonnet         # optional model hint
inputs:
  - name: target
    type: string
    required: true
    description: "what to act on"
allowed_tools:        # least-privilege grant
  - Read
  - Bash(git diff:*)
disallowed_tools:     # explicit denials win
  - Edit
  - Bash(git push:*)
system_prompt: |
  You are the <name> persona for Paperworlds.
  ...
```

Every mask is **least-privilege by construction** — it declares exactly the
tools its role needs and explicitly denies the rest. See
[`docs/SCHEMA.md`](docs/SCHEMA.md) for the full field reference and conventions.

## The cast

Sixteen personas, grouped by what they do:

**Review & quality**
- `agent-reviewer` — review agent-generated code/config/skills before they land
- `pr-reviewer` — review a pull request
- `test-author` — write fast, convention-following regression tests
- `yaml-validator` — validate YAML against the stack's schemas

**Architecture & authoring**
- `chief-architect` — high-level design and trade-off calls
- `prompt-architect` — turn structured intent into numbered prompt files
- `spec-author` — author textforums-held specs for a component
- `repo-boot` — bootstrap a repo into Paperworlds shape

**Knowledge & memory**
- `memory-steward` — curate memory; runs the weekly introspection pass
- `textmap-inbox-reviewer` — gate proposed nodes into the textmap graph
- `idea-expander` — turn `docs/IDEAS.yaml` entries into implementation proposals

**The outward loop** *(pairs with introspection)*
- `outro-spection` — scan open-source for skills/agents that fill known gaps
- `tool-vetter` — deep-vet one external tool before adoption

**Fleet & release**
- `mcp-bundle-smith` — scaffold + smoke-test a new textserve MCP bundle (dark)
- `release-warden` — audit `text*` repos for CI, version, and changelog hygiene
- `echo-shell` — minimal echo persona for wiring and smoke tests

## Status

`0.1.0` — the persona **definitions + schema**, plus schema-validation CI. This
is a data-first registry with **no CLI, by design** — textmasks never runs
personas; a consumer does. Schema conformance is enforced in CI
(`scripts/validate_personas.py`).

**Done**
- `textprompts` retired; its embedded persona copy removed. textmasks is the
  single source of truth.

**Roadmap**
- `textsessions` integration: launch or resume a session *as* a mask. This is
  where invocation belongs — textmasks stays a registry, never a runner.

## License

[Elastic License 2.0](LICENSE) — © 2026 Paperworlds.
