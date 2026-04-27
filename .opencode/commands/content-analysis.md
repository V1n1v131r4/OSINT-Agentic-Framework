---
description: Analyzes content and narratives for disinformation and influence
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/06-content-analysis.md.

Operational Instructions:
1. Locate the collection files (`04-disinfo-collection-gpt.json` or `04-narrative-collection-gpt.json`) and the `03-surface-expansion-gpt.json` in the `runs` directory of the current case.
2. Analyze content patterns, sentiment, and coordination signals.
3. Save the result in `cases/<case-id>/runs/06-content-analysis-gpt.json`.

Objective:
- Decompose the narrative and identify inauthenticity.
- **Suggest the next command** based on the `operation_type`:
  - `disinformation_campaign`: `/disinfo-actor-mapping`
  - `narrative_analysis`: `/narrative-ecosystem-map`

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/06-content-analysis-gpt.json",
  "next_command": "/<suggested-command>"
}
```
