# 10 — Correlation & Anomalies

## Objective

Consolidate the data collected in the previous stages, identifying:

- observable relationships between entities and assets
- recurring patterns
- inconsistencies or conflicting signals
- points that still require validation

This module focuses on STRUCTURED CORRELATION, not a final investigative narrative.

---

## Mandatory Inputs

- relevant outputs from previous stages
- identified entities
- technical or institutional assets and signals already collected

If there is not enough data to correlate, DO NOT proceed.

---

## Instructions to the Agent

- Work only with data already collected
- DO NOT search for new sources
- DO NOT expand scope
- DO NOT turn correlation into a definitive conclusion
- Clearly separate:
  - observed relationship
  - pattern
  - anomaly
  - gap

---

## Execution Rules

- Generate ONLY valid JSON
- All list fields must be valid JSON arrays
- Do not add fields outside the mandatory output
- If there is not enough evidence for a relationship, DO NOT include it
- Each relationship should reflect only an observable connection or an explicitly classified weak inference
- Do not create a long narrative within the fields
- Do not assume causality
- Do not use speculative language without classifying uncertainty

---

## Tasks

### 1. Identify relationships

Map connections between:

- company
- domain
- subdomains
- e-mails
- technical assets
- institutional profiles
- partner and employee profiles
- corporate identifiers
- public documents
- code repositories

Classify each relationship as:

- `direct` = clearly observable link
- `indirect` = plausible link, but not directly confirmed

---

### 2. Identify patterns

List observable recurrences, such as:

- reuse of identifiers
- consistency across sources
- infrastructure concentration
- repetition of institutional contact
- alignment between institutional presence and technical assets

---

### 3. Identify anomalies

List signals such as:

- inconsistencies across sources
- assets or data that do not fit
- divergence in contact, naming, or infrastructure
- relevant absence of confirmation

---

### 4. Register gaps

List what still prevents stronger validation of relationships or hypotheses.

---

## Mandatory Output

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
