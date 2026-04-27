# 07 — Individual Social Analysis

## Objective
Analyze the presence and behavior of an individual on social networks, focusing on connections, lifestyle, circle of influence, and exposure of sensitive information.

---

## Mandatory Inputs
- individual_footprint_output
- identity_validation_output

---

## Tasks
1. **Profile Analysis**: Assess biographies, photos, and posts to extract location signals, habits, and interests.
2. **Connection Mapping**: Identify family members, close friends, and frequent coworkers.
3. **Activity Analysis**: Check posting times and frequency to infer routines or time zones.
4. **OPSEC Risk Identification**: Note if the individual exposes sensitive data (photos of badges, passports, real-time geolocation).

---

## Mandatory Output
```json
{
  "social_behavior_summary": "",
  "key_connections": [],
  "lifestyle_signals": [],
  "opsec_vulnerabilities": [],
  "activity_patterns": {},
  "confidence": "low | medium | high"
}
```
