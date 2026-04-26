---
description: Executes module 05 and saves the institutional validation in runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/05-institutional-validation.md.

Use the following file as mandatory input:
@cases/test-01/runs/04-entity-graph-gpt.json

Objective of this execution:
- validate institutional signals in public sources
- separate confirmed, inconsistent, and unverifiable entities
- prepare institutional base for later correlation

Mandatory operational instructions:
- Read @cases/test-01/runs/04-entity-graph-gpt.json
- Generate ONLY valid JSON compatible with spec 05
- Save the result in @cases/test-01/runs/05-institutional-validation-gpt.json
- If the folder @cases/test-01/runs does not exist, create it
- After saving, respond only with a short status JSON in this format:

{
  "status": "ok",
  "output_file": "cases/test-01/runs/05-institutional-validation-gpt.json"
}

Mandatory rules:
- Do not generate text outside the JSON
- All list fields must be valid JSON arrays
- Do not use markdown
- Do not add extra fields
- If input is missing, return a structured error in JSON