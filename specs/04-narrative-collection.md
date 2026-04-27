# 04 — Narrative Collection

## Objective

Collect data about the ecosystem of a narrative, focusing on key actors, volume of mentions, and influence channels.

---

## Mandatory Inputs

- target_topic
- framing_output

---

## Tasks

1. **Actor Identification**: Map influencers, media outlets, and institutional profiles that set the agenda on the topic.
2. **Mention Collection**: Extract samples of posts, articles, and comments.
3. **Channel Mapping**: Identify where the narrative is strongest (social networks, forums, blogs).
4. **Engagement Analysis**: Collect volume signals (likes, shares, views) to measure impact.
5. **Google Dorks for Narratives**:
   - `"specific topic" (opinion OR analysis OR editorial)`
   - `"specific topic" site:youtube.com`
   - `"specific topic" site:medium.com OR site:substack.com`

---

## Mandatory Output

```json
{
  "key_actors": [],
  "content_ecosystem": [],
  "engagement_signals": [],
  "platform_distribution": [],
  "narrative_variants": [],
  "confidence": "low | medium | high"
}
```
