---

# 07 — `specs/07-brand-social-analysis.md`

```md
# 07 — Brand & Social Analysis

## Objective

Identify the target's public presence on institutional platforms and channels.

---

## Mandatory inputs

- entities

---

## Agent instructions

- It is ALLOWED to search on:
  - social networks
  - public directories
  - institutional websites
- It is ALLOWED to investigate personal profiles of identified partners and employees for institutional correlation
- Do NOT infer affiliation without evidence

---

## Tasks

### 1. Identify official and partner channels

- institutional website
- corporate social networks
- professional platforms (company and partners’ LinkedIn)
- social profiles of partners and employees (to validate affiliation with the company)

---

### 2. Identify patterns

- name consistency
- use of institutional domain
- active vs inactive presence

---

## Mandatory output

```json
{
  "official_channels": [],
  "partner_channels": [
    {
      "partner_name": "",
      "platform": "",
      "handle": "",
      "url": "",
      "correlation_evidence": "company mention in bio | photos on-site | related posts",
      "evidence_level": "confirmed|candidate|unresolved"
    }
  ],
  "candidate_channels": [],
  "signals": [],
  "confidence": "low | medium | high"
}
```
