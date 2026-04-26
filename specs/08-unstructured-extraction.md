---

# 08 — `specs/08-unstructured-extraction.md`

```md
# 08 — Unstructured Extraction

## Objective

Extract relevant data from unstructured content.

---

## Mandatory inputs

- public pages
- previously collected content

---

## Agent instructions

- Work only with available content
- DO NOT search for new sources (already collected)
- DO NOT interpret beyond the text

---

## Tasks

### 1. Extract relevant data

- emails
- phone numbers
- addresses
- institutional names

---

### 2. Normalize data

- remove duplicates
- standardize format

---

## Mandatory output

```json
{
  "emails": [],
  "phones": [],
  "addresses": [],
  "names": [],
  "confidence": "low | medium | high"
}
```
