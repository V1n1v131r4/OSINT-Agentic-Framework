# 10 — Correlation & Anomalies (Leaks)

## Objective
Consolidate the technical audit and impact analysis to identify the probable origin of the leak, the real extent of the exposure, and the correlated risks.

---

## Mandatory Inputs
- outputs from leak-impact-analysis and leak-data-audit.

---

## Tasks
1. **Correlate Data and Origin**: Link the structure of the leaked data to systems or probable attack vectors.
2. **Identify Exposure Patterns**: List data categories that repeat or indicate a specific target (e.g., only HR data).
3. **Detect Veracity Anomalies**: Identify false data (honeypots) or mixtures of old leaks.
4. **Map Attribution Risks**: Correlate the "modus operandi" of the publication with known groups.

---

## Mandatory Output
```json
{
  "leak_origin_correlation": [],
  "exposure_patterns": [],
  "veracity_anomalies": [],
  "attribution_signals": [],
  "known_gaps": [],
  "confidence": "low | medium | high"
}
```
