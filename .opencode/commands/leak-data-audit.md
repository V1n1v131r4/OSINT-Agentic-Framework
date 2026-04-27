---
description: Performs technical audit of leaked data
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/07-leak-data-audit.md.

Operational Instructions:
1. Locate the `06-leak-impact-analysis-gpt.json` and `04-leak-collection-gpt.json` files in the `runs` directory of the current case.
2. Perform the technical audit of the samples and data structure.
3. Save the result in `cases/<case-id>/runs/07-leak-data-audit-gpt.json`.

Objective:
- Identify the technical depth and origin of the leak.
- **Suggest the next command**: `/unstructured-extraction`.

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/07-leak-data-audit-gpt.json",
  "next_command": "/unstructured-extraction"
}
```
