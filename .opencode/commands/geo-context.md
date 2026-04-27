---
description: Analyzes the geographical context and suggests the next step of the pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/09-geo-context.md.

Operational Instructions:
1. Locate the previous analysis files (`07-individual-social-analysis-gpt.json`, `08-unstructured-extraction-gpt.json`, or `04-entity-graph-gpt.json`) in the `runs` directory of the current case.
2. Identify and correlate geographical signals.
3. Save the result in `cases/<case-id>/runs/09-geo-context-gpt.json`.

Objective:
- Map physical and regional location.
- **Suggest the next command** (usually `/correlation`).

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/09-geo-context-gpt.json",
  "next_command": "/correlation"
}
```
