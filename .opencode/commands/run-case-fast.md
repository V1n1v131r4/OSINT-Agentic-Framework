---
description: Dynamic orchestrator that follows the suggestions of each pipeline command
agent: collector-gpt
model: openai/gpt-5-mini
---

Execute this routine in a strictly sequential manner, following the dynamic suggestions of each command.

Objective:
- Validate the complete pipeline according to the `operation_type`.
- Follow the `next_command` field returned by each stage.

Mandatory Rules:
1. Start by executing `/case-intake`.
2. After each command, read the returned status JSON.
3. If the status is "ok", execute the command indicated in the `next_command` field.
4. Continue until the suggested command is `/postmortem` or there are no more suggestions.
5. If any stage fails, stop and report the error.

Initial Execution Order:
1. `/case-intake`
2. Follow the dynamic suggestion of `next_command`.

At the end, respond with the completion JSON:

```json
{
  "status": "ok",
  "message": "dynamic_pipeline_complete",
  "final_report": "cases/<case-id>/runs/11-report-gpt.json"
}
```
