---
description: Maps the technical digital footprint of individuals
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/06-individual-digital-footprint.md.

Operational Instructions:
1. Locate the `05-identity-validation-gpt.json` and `04-individual-collection-gpt.json` files in the `runs` directory of the current case.
2. Map e-mails, handles, and personal assets.
3. Save the result in `cases/<case-id>/runs/06-individual-footprint-gpt.json`.

Objective:
- Consolidate personal digital infrastructure.
- **Suggest the next command**: `/individual-social-analysis`.

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/06-individual-footprint-gpt.json",
  "next_command": "/individual-social-analysis"
}
```
