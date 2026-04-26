---
description: Executes module 08 and saves structured extractions of textual content in runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/08-unstructured-extraction.md.

Use the following files as mandatory inputs:
@cases/test-01/runs/03-surface-expansion-gpt.json
@cases/test-01/runs/07-brand-social-analysis-gpt.json

Objective of this run:
- extract relevant data from already collected unstructured content
- normalize and deduplicate emails, phone numbers, addresses, and names
- prepare structured data for geographic context and correlation

Mandatory operational instructions:
- Read @cases/test-01/runs/03-surface-expansion-gpt.json
- Read @cases/test-01/runs/07-brand-social-analysis-gpt.json
- Generate ONLY valid JSON compatible with spec 08
- Save the result in @cases/test-01/runs/08-unstructured-extraction-gpt.json
- If the folder @cases/test-01/runs does not exist, create it
- After saving, respond only with a short JSON status in this format:

{
  "status": "ok",
  "output_file": "cases/test-01/runs/08-unstructured-extraction-gpt.json"
}

Mandatory rules:
- Do not generate text outside JSON
- All list fields must be valid JSON arrays
- Do not use markdown
- Do not add extra fields
- If input is missing, return a structured error in JSON