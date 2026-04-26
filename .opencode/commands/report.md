---
description: Executes module 11 and saves the final report in runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/11-reporting.md.

Use as mandatory inputs the files:
@cases/test-01/runs/01-case-intake.json
@cases/test-01/runs/10-correlation-gpt.json

Objective of this execution:
- transform the correlation into a short, executive, and traceable report
- maintain coherence with the original analytical objective
- prepare the final output for review

Mandatory operational instructions:
- Read @cases/test-01/runs/01-case-intake.json
- Read @cases/test-01/runs/10-correlation-gpt.json
- Generate ONLY valid JSON compatible with spec 11
- Save the result in @cases/test-01/runs/11-report-gpt.json
- If the folder @cases/test-01/runs does not exist, create it
- After saving, respond only with a short status JSON in this format:

{
  "status": "ok",
  "output_file": "cases/test-01/runs/11-report-gpt.json"
}

Mandatory rules:
- Do not generate text outside the JSON
- All list fields must be valid JSON arrays
- Do not use markdown
- Do not add extra fields
- If input is missing, return a structured error in JSON