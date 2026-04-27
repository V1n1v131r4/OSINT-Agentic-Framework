# 06 — Content & Narrative Analysis

## Objective

Analyze the collected content to identify language patterns, sentiments, narrative variants, and signals of coordination or inauthenticity.

---

## Mandatory Inputs

- collection_output (disinfo or narrative)
- expansion_output

---

## Tasks

1. **Narrative Identification**: Categorize the different versions of the main message.
2. **Sentiment Analysis**: Assess the emotional load and tone of the posts/articles.
3. **Pattern Detection**: Identify repetition of phrases, coordinated hashtags, or use of identical media across different channels.
4. **Coordination Assessment**: Check if posts occur at suspicious time intervals or if there is massive cross-sharing.
5. **Influence Mapping**: Identify which actors have the greatest agenda-setting power within the ecosystem.

---

## Mandatory Output

```json
{
  "narrative_variants": [],
  "sentiment_profile": {},
  "coordination_signals": [],
  "key_influencers": [],
  "content_patterns": [],
  "confidence": "low | medium | high"
}
```
