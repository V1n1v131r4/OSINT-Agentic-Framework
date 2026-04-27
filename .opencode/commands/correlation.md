---
description: Consolidates correlations and suggests the next step of the pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Operational Instructions:
1. Locate the previous output files in the `runs` directory of the current case.
2. Select the correlation spec based on the `operation_type`:
   - `institutions`: `@specs/10-correlation-anomalies.md`
   - `individuals`: `@specs/10-correlation-indiv.md`
   - `disinformation_campaign` or `narrative_analysis`: `@specs/10-correlation-narrative.md`
   - `data_leak`: `@specs/10-correlation-leak.md`
3. Consolidate relationships, patterns, and anomalies according to the selected spec.
4. Save the result in `cases/<case-id>/runs/10-correlation-gpt.json`.

Objective:
- Generate a traceable and specific base for the report.
- **Suggest the next command**: `/report`.

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/10-correlation-gpt.json",
  "next_command": "/report"
}
```
