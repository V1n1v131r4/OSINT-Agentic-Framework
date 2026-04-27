---
description: Validates institutional signals and suggests the next step of the pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/05-institutional-validation.md.

Operational Instructions:
1. Locate the `04-entity-graph-gpt.json` file in the `runs` directory of the current case.
2. Validate institutional entities in public sources.
3. Save the result in `cases/<case-id>/runs/05-institutional-validation-gpt.json`.

Objective:
- Confirm institutional existence and consistency.
- **Suggest the next command** (usually `/technical-surface`).

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/05-institutional-validation-gpt.json",
  "next_command": "/technical-surface"
}
```
