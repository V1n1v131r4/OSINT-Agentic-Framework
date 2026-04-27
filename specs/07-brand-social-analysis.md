# 07 — Brand & Social Analysis

## Objective

Identify the target's public presence on institutional platforms and channels.

---

## Mandatory Inputs

- entities

---

## Instructions to the Agent

- It IS PERMITTED to search in:
  - social networks
  - public directories
  - institutional sites
- It IS PERMITTED to investigate personal profiles of identified partners and employees for institutional correlation
- DO NOT infer a link without evidence

---

## Tasks

### 1. Identify official and partner channels

- institutional site
- corporate social networks
- professional platforms (LinkedIn of the company and partners)
- social profiles of partners and employees (to validate the link with the company)

---

### 2. Identify patterns

- name consistency
- use of institutional domain
- active vs. inactive presence

---

## Mandatory Output

```json
{
  "official_channels": [],
  "partner_channels": [
    {
      "partner_name": "",
      "platform": "",
      "handle": "",
      "url": "",
      "correlation_evidence": "mention of the company in bio | photos on site | related posts",
      "evidence_level": "confirmed|candidate|unresolved"
    }
  ],
  "candidate_channels": [],
  "signals": [],
  "confidence": "low | medium | high"
}
```
