---
description: Executes module 07 and saves the institutional public presence in runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/07-brand-social-analysis.md.

Use as mandatory input the file:
@cases/{{case_id}}/runs/04-entity-graph-gpt.json
@cases/{{case_id}}/runs/04-corporate-collection-gpt.json

Objective of this execution:
- identify public channels and institutional profiles
- separate official channels from unconfirmed candidate channels
- prepare public presence signals for correlation

Mandatory operational instructions:
- Read @cases/{{case_id}}/runs/04-entity-graph-gpt.json
- Read @cases/{{case_id}}/runs/04-corporate-collection-gpt.json
- Identify partners' social media from the 'partners' field in corporate-collection output and correlate with the company.
- Generate ONLY valid JSON compatible with spec 07
- Save the result in @cases/{{case_id}}/runs/07-brand-social-analysis-gpt.json
- If the folder @cases/{{case_id}}/runs does not exist, create it
- After saving, respond only with a short JSON status in this format:

{
  "status": "ok",
  "output_file": "cases/{{case_id}}/runs/07-brand-social-analysis-gpt.json"
}

Mandatory rules:
- Do not generate text outside the JSON
- All list fields must be valid JSON arrays
- Do not use markdown
- Do not add extra fields
- If input is missing, return structured JSON error