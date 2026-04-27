# 10 — Correlation & Anomalies (Individuals)

## Objective
Consolidate the data collected about the individual, identifying relationships between digital identities, personal assets, social connections, and possible anomalies or information gaps.

---

## Mandatory Inputs
- outputs from identity-validation, individual-footprint, and individual-social-analysis.

---

## Tasks
1. **Map Identity Relationships**: Connect e-mails, handles, social profiles, and professional records to the individual.
2. **Identify Behavior Patterns**: List recurrences in activity times, language style, or platform use.
3. **Detect Anomalies**: Identify conflicting profiles, namesakes causing noise, or inconsistent biographical data.
4. **Register Gaps**: List critical information not found (e.g., unconfirmed phone, unlocated address).

---

## Mandatory Output
```json
{
  "identity_map": [],
  "social_connections": [],
  "behavioral_patterns": [],
  "anomalies_detected": [],
  "known_gaps": [],
  "confidence": "low | medium | high"
}
```
