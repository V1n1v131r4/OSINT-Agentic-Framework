---

# 09 — `specs/09-geo-context.md`

```md
# 09 — Geo Context

## Objective

Identify the target's geographic context based on observable signals.

---

## Mandatory inputs

- addresses
- domains
- entities

---

## Instructions to the agent

- It is ALLOWED to use:
  - basic geolocation
  - public data
- Do NOT infer location without basis

---

## Tasks

### 1. Identify location

- city
- state
- country

---

### 2. Correlate geographic signals

- institutional address
- domain TLD
- regional presence

---

## Mandatory output

```json
{
  "locations": [],
  "geo_signals": [],
  "confidence": "low | medium | high"
}
```
