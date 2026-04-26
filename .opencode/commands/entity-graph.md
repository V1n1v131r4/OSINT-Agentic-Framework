---
description: Executes module 04 and saves the basic entity graph in runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/04-entity-graph.md.

Use the following files as mandatory input:
@cases/{{case_id}}/runs/03-surface-expansion-gpt.json
@cases/{{case_id}}/runs/04-corporate-collection-gpt.json

Objective of this execution:
- identify relevant institutional entities
- structure observable entities for validation and correlation
- prepare reusable output for subsequent modules

Mandatory operational instructions:
- Read @cases/{{case_id}}/runs/03-surface-expansion-gpt.json
- Read @cases/{{case_id}}/runs/04-corporate-collection-gpt.json
- Identify entities of type 'person' from the 'partners' and 'employees' fields in the corporate-collection output.
- Identify entities of type 'document' from the 'public_documents' field in the corporate-collection output.
- Identify entities of type 'code_repository' from the 'code_repositories' field in the corporate-collection output.
- Generate ONLY valid JSON compatible with spec 04
- Save the result to @cases/{{case_id}}/runs/04-entity-graph-gpt.json
- If the folder @cases/{{case_id}}/runs does not exist, create it
- After saving, respond only with a short status JSON in this format:

{
  "status": "ok",
  "output_file": "cases/{{case_id}}/runs/04-entity-graph-gpt.json"
}

Mandatory rules:
- Do not generate text outside of the JSON
- All list fields must be valid JSON arrays
- Do not use markdown
- Do not add extra fields
- If input is missing, return a structured error in JSON