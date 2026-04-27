---
description: Analyzes social media presence and suggests the next step of the pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/07-brand-social-analysis.md.

Operational Instructions:
1. Locate the `04-entity-graph-gpt.json` and `04-corporate-collection-gpt.json` files in the `runs` directory of the current case.
2. Identify official channels and related partner profiles.
3. Save the result in `cases/<case-id>/runs/07-brand-social-analysis-gpt.json`.

Objective:
- Map digital presence and actor profiles.
- **Suggest the next command** based on the `operation_type`:
  - `disinformation_campaign`: `/correlation` (skips generic extraction if the focus is the network)
  - `narrative_analysis`: `/correlation`
  - Others: `/unstructured-extraction`

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/07-brand-social-analysis-gpt.json",
  "next_command": "/<suggested-command>"
}
```
