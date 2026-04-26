---
description: Runs module 13 and automatically saves the lessons learned
agent: reviewer
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/13-postmortem-learning.md.

Use the following files as mandatory inputs:
@cases/test-01/runs/01-case-intake.json
@cases/test-01/runs/02-framing-gpt.json
@cases/test-01/runs/03-surface-expansion-gpt.json
@cases/test-01/runs/10-correlation-gpt.json
@cases/test-01/runs/11-report-gpt.json

Objective of this execution:
- review the methodological quality of the case
- identify spec flaws, inconsistencies, and operational bottlenecks
- produce reusable lessons learned

Mandatory operational instructions:
- Read the files listed above
- Generate ONLY valid JSON compatible with spec 13
- Save the result to @cases/test-01/memory/13-postmortem.json
- If the folder @cases/test-01/memory does not exist, create it
- After saving, respond with only a short status JSON in this format:

{
  "status": "ok",
  "output_file": "cases/test-01/memory/13-postmortem.json"
}

Mandatory rules:
- Do not generate text outside the JSON
- All list fields must be valid JSON arrays
- Do not use markdown
- Do not add extra fields
- If input is missing, return a structured error in JSON