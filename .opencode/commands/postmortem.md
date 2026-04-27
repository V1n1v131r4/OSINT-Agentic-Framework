---
description: Executes the methodological review and saves lessons learned
agent: reviewer
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/13-postmortem-learning.md.

Operational Instructions:
1. Locate the pipeline output files in the `runs` directory of the current case.
2. Review the methodological quality and identify lessons learned.
3. Save the result in `cases/<case-id>/memory/13-postmortem.json`.

Objective:
- Continuous improvement of the framework and the operator.

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/memory/13-postmortem.json",
  "message": "Operation finalized. Lessons learned registered in the case memory."
}
```
