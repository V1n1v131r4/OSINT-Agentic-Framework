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
- **Reinject the global playbook memory** (learning loop).
- **Suggest the next command** based on the `operation_type`.

Reinjection instructions (learning loop):
1. Read `memory/global/playbooks.json` (if it does not exist, proceed without playbooks).
2. Filter the playbooks by this case's `operation_type` + those with `operation_type: "all"`.
3. Sort by `reinforcement_count` (desc), take the top 5, and include them in `applicable_playbooks`
   in the saved file `cases/<case-id>/runs/01-case-intake.json`, as per spec @specs/01-case-intake.md.

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
  "applicable_playbooks_count": 0,
  "next_command": "<suggestion>"
}
```
