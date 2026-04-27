---
description: Analyzes the technical surface and suggests the next step of the pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/06-technical-surface.md.

Operational Instructions:
1. Locate the `03-surface-expansion-gpt.json` file in the `runs` directory of the current case.
2. Analyze technical assets (DNS, IPs, subdomains).
3. Save the result in `cases/<case-id>/runs/06-technical-surface-gpt.json`.

Objective:
- Map digital infrastructure.
- **Suggest the next command** based on the `operation_type`:
  - `data_leak`: `/unstructured-extraction` (focus on leaked content)
  - Others: `/brand-social-analysis`

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/06-technical-surface-gpt.json",
  "next_command": "/<suggested-command>"
}
```
