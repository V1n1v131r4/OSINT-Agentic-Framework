---
description: Expands the public surface and suggests the next step of the pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/03-surface-expansion.md.

Operational Instructions:
1. Locate the `02-framing-gpt.json` file and the corresponding collection file (`04-corporate-collection-gpt.json`, `04-individual-collection-gpt.json`, `04-disinfo-collection-gpt.json`, etc.) in the `runs` directory of the current case.
2. Execute surface expansion based on the collected data.
3. Save the result in `cases/<case-id>/runs/03-surface-expansion-gpt.json`.

Objective:
- Identify assets and channels.
- **Suggest the next command** based on the `operation_type`:
  - `institutions`: `/entity-graph`
  - `individuals`: `/entity-graph` (followed by identity-validation)
  - `disinformation_campaign`: `/content-analysis`
  - `narrative_analysis`: `/content-analysis`
  - `data_leak`: `/leak-impact-analysis`

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/03-surface-expansion-gpt.json",
  "next_command": "/<suggested-command>"
}
```
