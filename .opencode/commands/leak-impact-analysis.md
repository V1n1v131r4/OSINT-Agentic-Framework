---
description: Analyzes the impact and sensitivity of data leaks
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/06-leak-impact-analysis.md.

Operational Instructions:
1. Locate the `04-leak-collection-gpt.json` and `03-surface-expansion-gpt.json` files in the `runs` directory of the current case.
2. Assess the sensitivity, volume, and risks of the leak.
3. Save the result in `cases/<case-id>/runs/06-leak-impact-analysis-gpt.json`.

Objective:
- Scale the damage and veracity of the leak.
- **Suggest the next command**: `/leak-data-audit`.

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/06-leak-impact-analysis-gpt.json",
  "next_command": "/leak-data-audit"
}
```
