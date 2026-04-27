---
description: Collects advanced corporate data and suggests the next step of the pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/04-corporate-collection.md.

Operational Instructions:
1. Locate the `01-case-intake.json` and `02-framing-gpt.json` files in the `runs` directory of the current case.
2. Execute deep corporate collection according to the mandatory flow of the spec.
3. Save the result in `cases/<case-id>/runs/04-corporate-collection-gpt.json`.

Objective:
- Consolidate CNPJ, QSA, contacts, and documents.
- **Suggest the next command** (must be `/expansion`).

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/04-corporate-collection-gpt.json",
  "next_command": "/expansion"
}
```
