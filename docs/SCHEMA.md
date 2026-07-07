# Persona schema

A persona ("mask") is a single YAML file in `personas/<name>.yaml`. The filename
stem is the persona's canonical name.

## Fields

| Field | Required | Notes |
|---|---|---|
| *(top comment)* | recommended | `# SPEC: <name> v<semver>` + a one-paragraph summary of the role and what seeded it. |
| `description` | ✅ | One line. Shown in `list`. |
| `mode` | recommended | `task` — runs to completion on its own (report/thread/artifact). `interactive` / `role` — emitted for a host session to adopt as its role. Minimal smoke personas may omit it. |
| `model` | optional | Model hint, e.g. `haiku`, `sonnet`. Omit to let the consumer decide. |
| `inputs` | optional | List of typed inputs (see below). Omit or `[]` when the persona takes none. |
| `allowed_tools` | recommended | Least-privilege grant. Tool names, optionally scoped: `Bash(git diff:*)`. |
| `disallowed_tools` | recommended | Explicit denials. A denial wins over an allow. |
| `system_prompt` | ✅ | The role's instructions. Block scalar (`|`). |

### `inputs` entry

```yaml
- name: target          # identifier used as -i target=…
  type: string          # string (today's only type)
  required: true        # true | false
  default: all          # optional; only meaningful when required: false
  description: "…"       # what it is and how it's resolved
```

## Conventions

- **Least privilege.** Grant only the tools the role needs; deny the rest
  explicitly. A reviewer that must not mutate lists `Edit`, `Write`,
  `Bash(git commit:*)`, `Bash(git push:*)` under `disallowed_tools`.
- **Version in the SPEC comment.** Bump the `# SPEC:` version on any behavioural
  change; personas are contracts other tools depend on.
- **Report, then act.** Personas that could do damage default to reporting a
  recommendation and only act behind an explicit `apply` input. Irreversible or
  destructive steps stay with the human.
- **Stack-native, not generic.** A Paperworlds persona references the real tools
  it works with (`textserve`, `textmap`, `textforums`, `textread`), not
  hypothetical ones. This is what distinguishes these from a generic prompt dump.
- **Two invocation modes, by design.** `task` personas finish on their own;
  `interactive` personas hand their prompt to a live host session to adopt.
  textmasks resolves both to a spec — the consumer chooses how to run it.

## Validation

Until the `masks` CLI lands, validate with any YAML parser plus these invariants:
`description`, `mode`, `inputs`, and `system_prompt` present; `mode ∈ {task,
interactive}`; every `inputs` entry has `name`, `type`, `required`.
