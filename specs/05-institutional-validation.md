---

# 05 — `specs/05-institutional-validation.md`

```md
# 05 — Institutional Validation

## Objective

Validate institutional signals of the target in reliable public sources.

---

## Mandatory Inputs

- entities

---

## Agent Instructions

- It is ALLOWED to consult:
  - public records
  - business aggregators
  - institutional databases
- Do NOT validate individual persons outside the scope
- Do NOT assume validity without evidence

---

## Tasks

### 1. Validate institutional existence

- CNPJ (if applicable)
- corporate name
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
