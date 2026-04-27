# 04 — Entity Graph

## Objective

Identify and organize relevant entities related to the target.

This module focuses on entity ENUMERATION, not deep correlation.

---

## Mandatory Inputs

- primary_assets
- residual_or_legacy_assets

---

## Instructions to the Agent

- It IS PERMITTED to enrich data using public sources
- DO NOT expand to natural persons outside the scope
- DO NOT create complex relationships
- Only identify observable entities

---

## Tasks

### 1. Identify entities

- company
- domains
- institutional e-mails
- associated brands
- institutional profiles

---

### 2. Classify entities

Classify as:

- `organization`
- `person` (partners, administrators, and identified employees)
- `document` (public documents found)
- `code_repository` (code repositories found)
- `domain`
- `email`
- `brand`
- `profile`
- `other`

---

## Mandatory Output

```json
{
  "entities": [
    {
      "name": "",
      "type": "organization | person | domain | email | brand | profile | document | code_repository | other"
    }
  ],
  "confidence": "low | medium | high"
}
```
