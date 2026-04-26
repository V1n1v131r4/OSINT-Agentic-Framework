---
description: Executes module 10 and saves the structured correlation in runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/10-correlation-anomalies.md.

Use the following files as mandatory inputs:
@cases/{{case_id}}/runs/04-entity-graph-gpt.json
@cases/{{case_id}}/runs/05-institutional-validation-gpt.json
@cases/{{case_id}}/runs/06-technical-surface-gpt.json
@cases/{{case_id}}/runs/07-brand-social-analysis-gpt.json
@cases/{{case_id}}/runs/08-unstructured-extraction-gpt.json
@cases/{{case_id}}/runs/09-geo-context-gpt.json

Objective of this execution:
- consolidate observable relationships between entities and assets
- highlight patterns, anomalies, and gaps
- prepare a traceable basis for the final report

Mandatory operational instructions:
- Read all the files listed above
- Pay special attention to the 'partners' and 'google_dorks_results' fields from the corporate-collection output
- Correlate the social media of partners (from the brand-social-analysis output) with the company and identified partners
- Generate ONLY valid JSON compatible with spec 10
- Save the result at @cases/{{case_id}}/runs/10-correlation-gpt.json
- If the folder @cases/{{case_id}}/runs does not exist, create it
- After saving, reply only with a brief status JSON in this format:

{
  "status": "ok",
  "output_file": "cases/{{case_id}}/runs/10-correlation-gpt.json"
}

Mandatory rules:
- Do not generate text outside the JSON
- All list fields must be valid JSON arrays
- Do not use markdown
- Do not add extra fields
- If any input is missing, return a structured error in JSON