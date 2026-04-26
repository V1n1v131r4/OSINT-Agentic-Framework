# 04 — Entity Graph

## Objective

Identify and organize relevant entities related to the target.

This module focuses on ENUMERATION of entities, not on deep correlation.

---

## Mandatory Inputs

- primary_assets
- residual_or_legacy_assets

---

## Agent Instructions

- It is ALLOWED to enrich data using public sources
- Do NOT expand to individuals outside the scope
- Do NOT create complex relationships
- Only identify observable entities

---

## Tasks

### 1. Identify entities

- company
- domains
- institutional emails
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