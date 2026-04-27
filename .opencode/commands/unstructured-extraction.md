---
description: Extracts unstructured data and suggests the next step of the pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/08-unstructured-extraction.md.

Operational Instructions:
1. Locate the previous analysis files (`03-surface-expansion-gpt.json` and the corresponding social analysis module: `07-brand-social-analysis-gpt.json`, `07-individual-social-analysis-gpt.json`, `07-disinfo-actor-mapping-gpt.json`, `07-narrative-ecosystem-map-gpt.json`, or `07-leak-data-audit-gpt.json`) in the `runs` directory of the current case.
2. Extract information from unstructured sources according to the spec.
3. Save the result in `cases/<case-id>/runs/08-unstructured-extraction-gpt.json`.

Objective:
- Capture qualitative signals.
- **Suggest the next command** based on the `operation_type`:
  - `institutions`: `/geo-context`
  - `individuals`: `/geo-context`
  - `data_leak`: `/correlation` (skips geo-context if there are no physical signals)
  - Others: `/correlation`

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/08-unstructured-extraction-gpt.json",
  "next_command": "/<suggested-command>"
}
```
