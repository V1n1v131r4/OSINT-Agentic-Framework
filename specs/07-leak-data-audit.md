# 07 — Leak Data Audit

## Objective
Perform a detailed audit of the leaked data samples, focusing on identifying technical patterns that reveal the origin of the leak and the depth of the exposure.

---

## Mandatory Inputs
- leak_impact_analysis_output
- leak_collection_output

---

## Tasks
1. **Data Structure Analysis**: Identify if the data comes from a database dump (SQL), server logs, or API extraction.
2. **PII Audit**: List specific exposed fields (e.g., Tax ID, Password Hash, IP Address, Session Token).
3. **Authenticity Verification**: Cross-reference samples with known public data to confirm veracity.
4. **Search for Technical Secrets**: Identify if there are API keys, configuration secrets, or administrative credentials in the leak.

---

## Mandatory Output
```json
{
  "technical_audit_summary": "",
  "exposed_pii_details": [],
  "technical_secrets_found": [],
  "data_origin_hypotheses": [],
  "confidence": "low | medium | high"
}
```
