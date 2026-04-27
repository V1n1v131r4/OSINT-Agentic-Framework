---
description: Maps actors and disinformation networks
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/07-disinfo-actor-mapping.md.

Operational Instructions:
1. Locate the `06-content-analysis-gpt.json` and `04-disinfo-collection-gpt.json` files in the `runs` directory of the current case.
2. Map the actor network and identify inauthenticity signals.
3. Save the result in `cases/<case-id>/runs/07-disinfo-actor-mapping-gpt.json`.

Objective:
- Identify the human and technical structure behind the campaign.
- **Suggest the next command**: `/correlation`.

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/07-disinfo-actor-mapping-gpt.json",
  "next_command": "/correlation"
}
```
