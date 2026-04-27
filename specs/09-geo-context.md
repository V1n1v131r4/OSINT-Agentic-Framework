# 09 — Geo Context

## Objective

Identify the target's geographical context based on observable signals.

---

## Mandatory Inputs

- addresses
- domains
- entities

---

## Instructions to the Agent

- It IS PERMITTED to use:
  - basic geolocation
  - public data
- DO NOT infer location without a basis

---

## Tasks

### 1. Identify location

- city
- state
- country

---

### 2. Correlate geographical signals

- institutional address
- domain TLD
- regional presence

---

## Mandatory Output

```json
{
  "locations": [],
  "geo_signals": [],
  "confidence": "low | medium | high"
}
```
