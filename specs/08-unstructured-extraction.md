# 08 — Unstructured Extraction

## Objective

Extract relevant data from unstructured content.

---

## Mandatory Inputs

- public pages
- previously collected content

---

## Instructions to the Agent

- Work only with available content
- DO NOT search for new sources (already collected)
- DO NOT interpret beyond the text

---

## Tasks

### 1. Extract relevant data

- e-mails
- phones
- addresses
- institutional names

---

### 2. Normalize data

- remove duplicates
- standardize format

---

## Mandatory Output

```json
{
  "emails": [],
  "phones": [],
  "addresses": [],
  "names": [],
  "confidence": "low | medium | high"
}
```
