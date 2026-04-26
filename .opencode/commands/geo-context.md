---
description: Executes module 09 and saves the geographic context in runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/09-geo-context.md.

Use the following files as mandatory inputs:
@cases/test-01/runs/08-unstructured-extraction-gpt.json
@cases/test-01/runs/04-entity-graph-gpt.json

Objective of this execution:
- consolidate observable geographic signals from the target
- structure locations and regional signals without undue inference
- prepare geographic context for final correlation

Mandatory operational instructions:
- Read @cases/test-01/runs/08-unstructured-extraction-gpt.json
- Read @cases/test-01/runs/04-entity-graph-gpt.json
- Generate ONLY valid JSON compatible with spec 09
- Save the result in @cases/test-01/runs/09-geo-context-gpt.json
- If the folder @cases/test-01/runs does not exist, create it
- After saving, respond only with a short status JSON in this format:

{
  "status": "ok",
  "output_file": "cases/test-01/runs/09-geo-context-gpt.json"
}

Mandatory rules:
- Do not generate text outside the JSON
- All list fields must be valid JSON arrays
- Do not use markdown
- Do not add extra fields
- If input is missing, return a structured error in JSON