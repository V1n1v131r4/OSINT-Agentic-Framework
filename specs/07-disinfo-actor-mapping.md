# 07 — Disinfo Actor Mapping

## Objective
Map and categorize the actors involved in a disinformation campaign, differentiating between original sources, inauthentic amplifiers (bots/cyborgs), and influenced organic users.

---

## Mandatory Inputs
- content_analysis_output
- disinfo_collection_output

---

## Tasks
1. **Profile Categorization**: Classify profiles into:
   - `Source`: Creators of the original content.
   - `Amplifier`: Profiles that only replicate without adding content.
   - `Influencer`: Real profiles that give credibility to the narrative.
2. **Network Analysis**: Identify connections between profiles (mutual followers, frequent interactions).
3. **Inauthenticity Detection**: Look for signs of automation (close creation dates, name patterns, AI-generated profile photos).
4. **Platform Mapping**: Identify if actors operate in a coordinated manner across multiple networks (X, Telegram, Facebook).

---

## Mandatory Output
```json
{
  "actor_network": [],
  "bot_signals_detected": [],
  "key_amplifiers": [],
  "cross_platform_presence": [],
  "confidence": "low | medium | high"
}
```
