#!/usr/bin/env python3
"""Validate every persona in personas/ against the textmasks schema.

Invariants (see docs/SCHEMA.md):
- top level is a mapping
- required keys: description, system_prompt
- mode, if present, in {task, interactive, role} (some minimal personas omit it)
- inputs, if present, is a list; each entry has at least name + type
"""
import glob
import sys

import yaml

REQUIRED = {"description", "system_prompt"}
MODES = {"task", "interactive", "role"}


def main() -> int:
    errors: list[str] = []
    files = sorted(glob.glob("personas/*.yaml"))
    if not files:
        print("no personas found under personas/", file=sys.stderr)
        return 1

    for f in files:
        try:
            with open(f) as fh:
                doc = yaml.safe_load(fh)
        except yaml.YAMLError as exc:
            errors.append(f"{f}: YAML parse error: {exc}")
            continue

        if not isinstance(doc, dict):
            errors.append(f"{f}: top-level is not a mapping")
            continue

        missing = REQUIRED - doc.keys()
        if missing:
            errors.append(f"{f}: missing required fields: {sorted(missing)}")

        if "mode" in doc and doc["mode"] not in MODES:
            errors.append(f"{f}: mode must be one of {sorted(MODES)}, got {doc['mode']!r}")

        inputs = doc.get("inputs")
        if inputs is not None and not isinstance(inputs, list):
            errors.append(f"{f}: inputs must be a list")
        elif isinstance(inputs, list):
            for i, inp in enumerate(inputs):
                if not isinstance(inp, dict) or {"name", "type"} - inp.keys():
                    errors.append(f"{f}: inputs[{i}] must have name + type")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"\n{len(errors)} problem(s) across {len(files)} personas", file=sys.stderr)
        return 1

    print(f"OK — {len(files)} personas valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
