# 06 — Leak Impact Analysis

## Objective

Analyze the extent and real impact of a data leak, focusing on the sensitivity of the information and the risks to the affected entity and individuals.

---

## Mandatory Inputs

- leak_collection_output
- expansion_output

---

## Tasks

1. **Data Classification**: Categorize the types of PII (names, e-mails, passwords, documents, financial data).
2. **Volume Assessment**: Estimate the number of unique records exposed.
3. **Recency Analysis**: Check if the data is current or from old leaks (rehash).
4. **Risk Identification**: List immediate risks (phishing, impersonation, financial fraud).
5. **Attribution Correlation**: Try to link the leak to known threat groups or attack vectors.

---

## Mandatory Output

```json
{
  "data_sensitivity_score": "low | medium | high | critical",
  "exposed_data_categories": [],
  "estimated_record_count": 0,
  "risk_assessment": [],
  "attribution_hypotheses": [],
  "confidence": "low | medium | high"
}
```
