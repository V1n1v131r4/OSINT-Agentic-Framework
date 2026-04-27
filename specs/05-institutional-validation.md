# 05 — Institutional Validation

## Objective

Validate institutional signals of the target in reliable public sources.

---

## Mandatory Inputs

- entities

---

## Instructions to the Agent

- It IS PERMITTED to consult:
  - public records
  - business aggregators
  - institutional bases
- DO NOT validate natural persons outside the scope
- DO NOT assume validity without evidence

---

## Tasks

### 1. Validate institutional existence

- CNPJ (if applicable)
- legal name
- address
- activity

---

### 2. Identify consistency

- company name
- domain
- institutional contacts

---

## Mandatory Output

```json
{
  "validated_entities": [],
  "inconsistencies": [],
  "unverified_entities": [],
  "confidence": "low | medium | high"
}
```
