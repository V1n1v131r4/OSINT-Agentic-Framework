# 10 — Correlation & Anomalies

## Objective

Consolidate the data collected in previous stages, identifying:

- observable relationships between entities and assets
- recurring patterns
- inconsistencies or conflicting signals
- points that still require validation

This module focuses on STRUCTURED CORRELATION, not on final investigative narrative.

---

## Required inputs

- relevant outputs from previous stages
- identified entities
- technical or institutional assets and signals already collected

If there is insufficient data to correlate, DO NOT proceed.

---

## Agent instructions

- Work only with data already collected
- DO NOT seek new sources
- DO NOT expand scope
- DO NOT turn correlation into a definitive conclusion
- Clearly separate:
  - observed relationship
  - pattern
  - anomaly
  - gap

---

## Execution rules

- Generate ONLY valid JSON
- All list fields must be valid JSON arrays
- Do not add fields outside the required output
- If there is insufficient evidence for a relationship, DO NOT include it
- Each relationship must reflect only observable connection or weak inference explicitly classified
- Do not create long narratives inside fields
- Do not assume causality
- Do not use speculative language without classifying the uncertainty

---

## Tasks

### 1. Identify relationships

Map connections between:

- company
- domain
- subdomains
- emails
- technical assets
- institutional profiles
- partners' and employees' profiles
- corporate identifiers
- public documents
- code repositories

Classify each relationship as:

- `direct` = clearly observable link
- `indirect` = plausible link but not directly confirmed

---

### 2. Identify patterns

List observable recurrences, such as:

- reuse of identifiers
- consistency among sources
- infrastructure concentration
- repetition of institutional contact
- alignment between institutional presence and technical assets

---

### 3. Identify anomalies

List signals such as:

- inconsistencies among sources
- assets or data that do not fit
- divergence in contact, naming, or infrastructure
- relevant lack of confirmation

---

### 4. Register gaps

List what still prevents stronger validation of relationships or hypotheses.

---

## Required output

```json
{
  "relationships": [
    {
      "entity_a": "",
      "relation": "",
      "entity_b": "",
      "type": "direct | indirect",
      "confidence": "low | medium | high"
    }
  ],
  "patterns": [],
  "anomalies": [],
  "known_gaps": [],
  "correlated_documents": [
    {
      "document_url": "string",
      "entity_id": "string",
      "correlation_type": "string (e.g., mention, authorship)",
      "evidence_level": "confirmed|candidate"
    }
  ],
  "correlated_repositories": [
    {
      "repository_url": "string",
      "entity_id": "string",
      "correlation_type": "string (e.g., owner, contributor)",
      "evidence_level": "confirmed|candidate"
    }
  ],
  "correlated_employees": [
    {
      "employee_id": "string",
      "entity_id": "string",
      "correlation_type": "string (e.g., current_employee, past_employee)",
      "evidence_level": "confirmed|candidate"
    }
  ],
  "confidence": "low | medium | high"
}
```