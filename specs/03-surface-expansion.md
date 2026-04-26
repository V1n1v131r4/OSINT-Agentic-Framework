# 03 — Surface Expansion

## Objective
Expand the institutional public surface of the target from the initial seed, maintaining relevance, coherence, and analytical utility.

---

## Mandatory Inputs
- target_summary
- investigation_vectors
- known_gaps

If any input is missing or invalid, DO NOT proceed.

## Optional Inputs
- corporate_identity
- official_channels
- corporate_registry_signals
- public_litigation_signals

---

## Agent Instructions

- When there is a corporate collection artifact, use it to prioritize confirmed assets and channels
- Expand only institutional and public assets
- Do not investigate individuals
- Do not infer unobservable data
- Do not enrich with unsupported external knowledge
- Prioritize quality and relevance, not volume
- Clearly differentiate:
  - observed asset
  - inferred asset
  - suspected asset

---

## Tasks

1. Identify institutional assets directly related to the target
2. Identify official public channels (social networks, directories, etc.)
3. Classify assets into:
   - primary (central to the operation)
   - secondary (support)
   - residual/legacy (not maintained or inconsistent)
4. Identify possible inconsistencies or signs of weak digital governance
5. Suggest useful business pivots for deepening

---

## Mandatory Output

Return **ONLY valid JSON**, without additional text.

```json
{
  "primary_assets": [],
  "secondary_assets": [],
  "public_channels": [],
  "residual_or_legacy_assets": [],
  "business_pivots": [],
  "expansion_notes": ""
}
```