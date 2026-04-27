---
description: Deep data collection on individuals
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/04-individual-collection.md.

Operational Instructions:
1. Read the `01-case-intake.json` and `02-framing-gpt.json` of the current case.
2. Execute the collection focused on natural persons using websearch and webfetch.
3. Save in `cases/<case-id>/runs/04-individual-collection-gpt.json`.

Output Rules:
- Suggest the next command: `/expansion`.

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/04-individual-collection-gpt.json",
  "next_command": "/expansion"
}
```
