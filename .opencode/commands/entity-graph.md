---
description: Structures the entity graph and suggests the next step of the pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/04-entity-graph.md.

Operational Instructions:
1. Locate the `03-surface-expansion-gpt.json` file and the corresponding collection file (`04-corporate-collection-gpt.json` or `04-individual-collection-gpt.json`) in the `runs` directory of the current case.
2. Identify and normalize entities (people, documents, repositories, companies).
3. Save the result in `cases/<case-id>/runs/04-entity-graph-gpt.json`.

Objective:
- Structure the relationship graph.
- **Suggest the next command** based on the `operation_type`:
  - `institutions`: `/institutional-validation`
  - `individuals`: `/identity-validation`
  - Others: `/technical-surface` or `/brand-social-analysis` (as relevant)

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/04-entity-graph-gpt.json",
  "next_command": "/<suggested-command>"
}
```
