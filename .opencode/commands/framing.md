---
description: Runs module 02 and automatically saves the output in runs  
agent: collector-gpt  
model: openai/gpt-5-mini  
---

Strictly follow the spec in @specs/02-case-framing.md.

Use the input file:  
@cases/test-01/runs/01-case-intake.json

Objective of this execution:  
- transform the normalized case intake into initial analytical framing

Mandatory operational instructions:  
- Read @cases/test-01/runs/01-case-intake.json  
- Generate ONLY valid JSON compatible with spec 02  
- Save the result in @cases/test-01/runs/02-framing-gpt.json  
- After saving, respond only with a short status JSON in this format:

```json
{
  "status": "ok",
  "output_file": "cases/test-01/runs/02-framing-gpt.json"
}
```

Mandatory rules:  
- Do not generate text outside the JSON  
- All list fields must be valid JSON arrays  
- Do not use markdown  
- If input is missing, return a structured error in JSON