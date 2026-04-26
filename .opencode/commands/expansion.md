---
description: Runs module 03 and automatically saves the output in runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/03-surface-expansion.md.

Use the following files as mandatory inputs:
@cases/test-01/runs/02-framing-gpt.json
@cases/test-01/runs/04-corporate-collection-gpt.json

Objective of this execution:
- expand the target’s institutional public surface
- identify assets, channels, and possible useful digital residues
- leverage already collected corporate signals to prioritize the most reliable assets

Mandatory operational instructions:
- Read @cases/test-01/runs/02-framing-gpt.json
- Read @cases/test-01/runs/04-corporate-collection-gpt.json
- Generate ONLY valid JSON compatible with spec 03
- Save the result to @cases/test-01/runs/03-surface-expansion-gpt.json
- If the folder @cases/test-01/runs does not exist, create it
- After saving, respond only with a short status JSON in this format:

{
  "status": "ok",
  "output_file": "cases/test-01/runs/03-surface-expansion-gpt.json"
}

Mandatory rules:
- Do not generate text outside the JSON
- All list fields must be valid JSON arrays
- Do not use markdown
- Do not add extra fields
- If input is missing, return a structured error in JSON