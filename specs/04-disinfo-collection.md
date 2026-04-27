# 04 — Disinfo Collection

## Objective

Collect evidence of disinformation campaigns, focusing on original sources, propagation patterns, and content metadata.

---

## Mandatory Inputs

- target_narrative
- framing_output

---

## Tasks

1. **Source Mapping**: Identify the first profiles or sites to publish the narrative.
2. **Content Collection**: Extract texts, images, and videos associated with the campaign.
3. **Metadata Analysis**: Check creation dates of profiles, domains, and files (if available).
4. **Amplifier Identification**: List profiles with a high volume of sharing or suspicious behavior.
5. **Google Dorks for Disinformation**:
   - `"specific narrative" site:twitter.com`
   - `"specific narrative" site:t.me` (Telegram)
   - `intext:"specific narrative" -site:official_outlets.com`

---

## Mandatory Output

```json
{
  "source_nodes": [],
  "content_samples": [],
  "amplification_nodes": [],
  "timeline_signals": [],
  "technical_artifacts": [],
  "confidence": "low | medium | high"
}
```
