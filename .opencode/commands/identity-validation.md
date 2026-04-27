---
description: Validates the identity of individuals and suggests the next step
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/05-identity-validation.md.

Operational Instructions:
1. Locate the `04-individual-collection-gpt.json` and `04-entity-graph-gpt.json` files in the `runs` directory of the current case.
2. Validate the consistency of identity and links.
3. Save the result in `cases/<case-id>/runs/05-identity-validation-gpt.json`.

Objective:
- Confirm identity and reduce noise from namesakes.
- **Suggest the next command**: `/individual-footprint`.

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/05-identity-validation-gpt.json",
  "next_command": "/individual-footprint"
}
```
