---
description: Transforms the intake into analytical framing and suggests the next step of the pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/02-case-framing.md.

Operational Instructions:
1. Locate the `01-case-intake.json` file in the `runs` directory of the current case.
2. Generate the analytical framing based on the intake.
3. Save the result in `cases/<case-id>/runs/02-framing-gpt.json`.

Objective:
- Define hypotheses and investigation vectors.
- **Suggest the next command** based on the `operation_type` from the intake.

Output Rules:
- The `next_command` field must be `/corporate-collection` for the institutions pipeline.
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/02-framing-gpt.json",
  "next_command": "/corporate-collection"
}
```
