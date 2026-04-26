# 02 — Case Framing

## Objective

Transform the intake into an initial analytical framework, defining:

- initial hypotheses
- investigation vectors
- critical gaps

This module defines HOW the investigation will be conducted.

---

## Mandatory Inputs

- target
- analysis_goal
- scope_definition

---

## Optional Inputs

- known_data
- constraints
- priority_questions

If mandatory inputs are missing, DO NOT proceed.

---

## Instructions to the Agent

- Do not perform extensive collection
- Work only with:
  - provided data
  - general knowledge
- Avoid categorical statements

---

## Tasks

### 1. Define Initial Hypotheses

- Formulate 2 to 5 plausible hypotheses
- Each hypothesis must:
  - be testable
  - align with the objective
  - avoid excessive speculation

---

### 2. Define Investigation Vectors

For each hypothesis, indicate:

- where to look for evidence
- what type of data can confirm or refute it

---

### 3. Identify Critical Gaps

List:

- essential information still unknown
- points that prevent validation of the hypotheses

---

## Expected Output

```json
{
  "hypotheses": [
    {
      "description": "",
      "rationale": "",
      "validation_vectors": []
    }
  ],
  "investigation_vectors": [],
  "known_gaps": []
}
```