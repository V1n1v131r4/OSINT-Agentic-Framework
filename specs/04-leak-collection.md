# 04 — Leak Collection

## Objective

Collect evidence and samples of data leaks, focusing on validating the authenticity and extent of the exposure.

---

## Mandatory Inputs

- target_entity
- framing_output

---

## Tasks

1. **Search in Leak Repositories**: Search for mentions in specialized forums, pastebins, and Telegram channels.
2. **Sample Validation**: Analyze public samples to confirm if the data belongs to the target.
3. **Metadata Mapping**: Identify exposure dates and possible exfiltration vectors.
4. **Attribution Identification**: Collect signals about who published or is selling the data.
5. **Google Dorks for Leaks**:
   - `site:github.com "target_name" (password OR secret OR key)`
   - `site:pastebin.com "target_name"`
   - `"target_name" (database leak OR sql dump)`

---

## Mandatory Output

```json
{
  "leak_sources": [],
  "data_samples_metadata": [],
  "exposure_timeline": [],
  "attribution_signals": [],
  "technical_indicators": [],
  "confidence": "low | medium | high"
}
```
