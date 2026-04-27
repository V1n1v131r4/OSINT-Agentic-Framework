---
description: Generates the final report and suggests the next step of the pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/11-reporting.md.

Operational Instructions:
1. Locate the `01-case-intake.json` and `10-correlation-gpt.json` files in the `runs` directory of the current case.
2. Generate the executive report based on the findings and correlations, adapting the tone and focus to the `operation_type`.
3. Save the result in `cases/<case-id>/runs/11-report-gpt.json`.

Objective:
- Produce a traceable executive synthesis specific to the operation purpose.
- **Suggest the next command**: `/postmortem`.

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/11-report-gpt.json",
  "next_command": "/postmortem"
}
```
