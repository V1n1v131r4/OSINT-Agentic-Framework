---
description: Analyzes the social presence and behavior of individuals
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/07-individual-social-analysis.md.

Operational Instructions:
1. Locate the `06-individual-footprint-gpt.json` and `05-identity-validation-gpt.json` files in the `runs` directory of the current case.
2. Analyze profiles, connections, and social behavior.
3. Save the result in `cases/<case-id>/runs/07-individual-social-analysis-gpt.json`.

Objective:
- Map the individual's social ecosystem and vulnerabilities.
- **Suggest the next command**: `/geo-context`.

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/07-individual-social-analysis-gpt.json",
  "next_command": "/geo-context"
}
```
