---
description: Analytical framing for disinformation campaigns
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/02-framing-disinfo.md.

Operational Instructions:
1. Read the `01-case-intake.json` of the current case.
2. Generate the framing focused on narratives and coordination.
3. Save in `cases/<case-id>/runs/02-framing-gpt.json`.

Output Rules:
- Suggest the next command: `/disinfo-collection`.

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/02-framing-gpt.json",
  "next_command": "/disinfo-collection"
}
```
