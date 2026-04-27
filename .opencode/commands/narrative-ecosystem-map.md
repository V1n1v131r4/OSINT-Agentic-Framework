---
description: Maps the influence and narrative ecosystem
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/07-narrative-ecosystem-map.md.

Operational Instructions:
1. Locate the `06-content-analysis-gpt.json` and `04-narrative-collection-gpt.json` files in the `runs` directory of the current case.
2. Map the influence nodes and the information flow.
3. Save the result in `cases/<case-id>/runs/07-narrative-ecosystem-map-gpt.json`.

Objective:
- Visualize the influence structure and reach of the narrative.
- **Suggest the next command**: `/correlation`.

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/07-narrative-ecosystem-map-gpt.json",
  "next_command": "/correlation"
}
```
