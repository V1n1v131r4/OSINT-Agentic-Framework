---
description: Executes module 01 and automatically saves the output in runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/01-case-intake.md.

Use the file as input:
@cases/test-01/intake.json

Objective of this execution:
- normalize the raw intake
- prepare the payload for module 02

Mandatory operational instructions:
- Read @cases/test-01/intake.json
- Generate ONLY valid JSON compatible with spec 01
- Save the result in @cases/test-01/runs/01-case-intake.json
- If the folder @cases/test-01/runs does not exist, create it
- After saving, respond only with a short JSON status in this format:

{
  "status": "ok",
  "output_file": "cases/test-01/runs/01-case-intake.json"
}

Mandatory rules:
- Do not generate text outside JSON
- All list fields must be valid JSON arrays
- Do not use markdown
- If input is missing, return a structured error in JSON