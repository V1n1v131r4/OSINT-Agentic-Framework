# 01 — Case Intake

## Objective

To record the initial context of the case in a structured manner, ensuring clarity on:

- analysis target
- investigation objective
- permitted scope
- operational constraints

---

## Mandatory inputs

- target (company, domain, or institutional entity)
- analysis_goal
- scope_definition

---

## Optional inputs

- known_data
- constraints
- priority_questions

If mandatory inputs are missing or ambiguous, DO NOT proceed.

---

## Agent instructions

- Do not start collection
- Do not generate hypotheses
- Do not interpret data

This module is structural only.

---

## Expected output

```json
{
  "target": "",
  "analysis_goal": "",
  "scope_definition": "",
  "known_data": [],
  "constraints": [],
  "priority_questions": []
}
```