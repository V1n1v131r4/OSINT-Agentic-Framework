---
description: Analytical framing for data leaks
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/02-framing-leak.md.

Operational Instructions:
1. Read the `01-case-intake.json` of the current case.
2. Generate the framing focused on impact and origin of the leak.
3. Save in `cases/<case-id>/runs/02-framing-gpt.json`.

Output Rules:
- Suggest the next command: `/leak-collection`.

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/02-framing-gpt.json",
  "next_command": "/leak-collection"
}
```
