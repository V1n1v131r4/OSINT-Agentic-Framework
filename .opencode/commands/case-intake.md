---
description: Normalizes the intake and suggests the correct pipeline based on the operation purpose
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/01-case-intake.md.

Operational Instructions:
1. Locate the `intake.json` file in the case directory (e.g., `cases/<case-id>/intake.json`).
2. If the operator did not specify the path, look for recent `intake.json` files.
3. Validate the `operation_type`.

Objective:
- Normalize the raw intake.
- Assign/Validate the `case_id`.
- **Suggest the next command** based on the `operation_type`.

Output Rules:
- Save the result in `cases/<case-id>/runs/01-case-intake.json`.
- The `next_step_suggestion` field must follow the mapping:
  - `institutions` -> `/framing`
  - `individuals` -> `/framing-indiv`
  - `disinformation_campaign` -> `/framing-disinfo`
  - `narrative_analysis` -> `/framing-narrative`
  - `data_leak` -> `/framing-leak`

Return ONLY the status JSON:

```json
{
  "status": "ok",
  "case_id": "<case-id>",
  "operation_type": "<type>",
  "output_file": "cases/<case-id>/runs/01-case-intake.json",
  "next_command": "<suggestion>"
}
```
