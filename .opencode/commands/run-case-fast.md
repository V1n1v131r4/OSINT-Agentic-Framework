---
description: Fast pipeline (GPT only) with minimal operational flow
agent: collector-gpt
model: openai/gpt-5-mini
---

Run this routine strictly sequentially.

Objective:
- quickly validate the minimum pipeline
- reduce cost and time
- maintain consistency among outputs

Mandatory rules:
- Execute ONE step at a time
- After each step, wait for the status JSON
- Check if the `"status"` field is `"ok"`
- Check if the `"output_file"` field was returned
- Only proceed to the next step if the previous step completed successfully
- If any step returns an error, stop and respond only with the error JSON
- Do not respond with explanatory text outside the final JSON

Execution order:

### Step 1
Execute:
@.opencode/commands/case-intake.md

### Step 2
Execute:
@.opencode/commands/framing.md

### Step 3
Execute:
@.opencode/commands/expansion.md

### Step 4
Execute:
@.opencode/commands/entity-graph.md

### Step 5
Execute:
@.opencode/commands/technical-surface.md

### Step 6
Execute:
@.opencode/commands/correlation.md

### Step 7
Execute:
@.opencode/commands/report.md

At the end, if all steps complete successfully, respond only with this JSON:

{
  "status": "ok",
  "message": "fast_pipeline_complete",
  "final_output": "cases/test-01/runs/11-report-gpt.json"
}