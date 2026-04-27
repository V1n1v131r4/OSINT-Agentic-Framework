# 04 — Individual Collection

## Objective

Perform deep collection of public data about an individual, focusing on identity, digital footprint, and professional/personal links.

---

## Mandatory Inputs

- target_name
- framing_output (hypotheses and vectors)

---

## Tasks

1. **Identity Validation**: Search for namesakes and confirm unique identifiers (if publicly available).
2. **Social Media Footprint**: Map profiles on LinkedIn, Instagram, Twitter, Facebook, etc.
3. **Professional History**: Collect data on roles, past companies, and professional boards.
4. **Public Records**: Search for mentions in Official Gazettes, public lawsuits, and property records.
5. **Google Dorks for Individuals**:
   - `"full name" filetype:pdf`
   - `"full name" site:jusbrasil.com.br`
   - `"full name" (email OR phone OR contact)`

---

## Mandatory Output

```json
{
  "confirmed_identity": {},
  "social_profiles": [],
  "professional_history": [],
  "public_records": [],
  "exposure_signals": [],
  "confidence": "low | medium | high"
}
```
