# 04 — Corporate Collection

## Objective

Collect and consolidate public corporate identifiers and verifiable institutional signals of the target, focusing on light corporate due diligence and expanded business correlation.

---

## Mandatory Inputs

- normalized_target
- analysis_goal_normalized
- scope_modules
- investigation_vectors
- minimum_required_data
- known_gaps
- restrictions

## Optional Inputs

- corporate_identifiers

If any mandatory input is missing or invalid, DO NOT proceed.

---

## Agent Instructions

- Collect only corporate and public data
- Before concluding data absence, use websearch and webfetch
- Prioritize Brazilian corporate sources and directories present in the repository https://github.com/osintbrazuca/osint-brazuca as a base for discovery during collection
- Prioritize public sources showing:
  - CNPJ
  - legal name
  - trade name
  - registration status
  - business directories
  - signs of public company proceedings
- If a plausible but not definitive match is found, register as `candidate`, do not discard
- If there is coherent convergence in at least 2 plausible and independent public sources, promote to `confirmed`
- Clearly separate:
  - confirmed data
  - candidate data
  - remaining gap

---

## Critical Rule

This stage can only conclude `unresolved` for CNPJ after:

- consulting the official website
- consulting at least 2 different search classes
- consulting at least 1 corporate directory
- opening via webfetch at least 1 plausible directory result, if any
- trying at least 3 different pivots of name, brand, or domain
- attempting to identify similar business names
- attempting to identify similar domains

If there is plausible result in a corporate directory not opened, collection CANNOT be closed.

---

## Confirmation Rule

Corporate data can be promoted to `confirmed` when there is:

- at least 2 plausible and independent public sources
- coherent convergence among these sources

Convergence can use, when available:
- CNPJ
- legal name
- trade name
- address
- phone
- e-mail
- domain
- CNAE / economic activity
- social media
- other consistent institutional signals

If there is only one plausible source or insufficient partial convergence, register as `candidate`.

---

## Mandatory Search Strategy

Collection must follow a progressive flow based on source classes.

The agent CANNOT close collection without performing all layers below:

### 1. Primary source
- official website
- internal website pages:
  - contact
  - about
  - footer
  - policies
  - footer
  - FAQ
  - terms
  - press

Extract, when available:
- legal name
- CNPJ
- address
- phone
- e-mail
- WhatsApp
- domains
- social media

### 2. General search
- entity name + CNPJ
- domain + CNPJ
- entity name + legal name
- domain + legal name
- site:<domain> CNPJ
- site:<domain> "legal name"

### 3. Expanded search
- entity name + business registration
- entity name + legal name
- domain without TLD + CNPJ
- domain without TLD + legal name
- entity name + city/state, if available
- domain + city/state, if available
- entity name + economic activity

### 4. Corporate directories and aggregators (Focus on QSA)
The agent CANNOT claim login requirement without first exhausting these sources that provide the Board of Partners and Administrators (QSA) publicly:
- `casadosdados.com.br` (Highly recommended for detailed QSA)
- `transparencia.cc` (Excellent for ownership links)
- `cnpj.biz`
- `econodata.com.br`
- `empresas.serasaexperian.com.br`
- Transparency portals and Official Gazettes

Mandatory extraction of the Board of Partners and Administrators (QSA). If not found in one source, MUST try others.

### 5. Similar and related companies
Search for:
- trade name variations
- legal name variations
- abbreviations
- alternative spellings
- similar names in the same sector or city
- multiple potentially related CNPJs

For each candidate, try to correlate by:
- partners / administrators
- address
- phone
- e-mail
- CNAE / activity
- domains
- social media

### 6. Similar domains
Search for:
- close spellings
- domains without accents
- hyphens
- numbers
- alternative TLDs
- combinations with brand, city or activity

Correlate found domains with:
- main company
- related companies
- contacts
- social media

### 7. Social media and public presence
Search for:
- LinkedIn
- Instagram
- Facebook
- YouTube
- other relevant platforms

Extract, when available:
- handle
- URL
- description
- location
- e-mail
- phone
- associated domain

### 8. Contacts and WhatsApp
Search and consolidate:
- phones
- e-mails
- public forms
- WhatsApp links
- buttons or explicit WhatsApp mentions

Only register WhatsApp when association is explicit in the source.

### 9. Google Dorks (Recovery of QSA, Public Documents, and Repositories)
If QSA is not found in directories, use of Google Dorks is MANDATORY to locate partners in indexed documents. Also, Google Dorks should be used to find other public documents and code repositories:

**For Partners and Legal Documents:**
- `filetype:pdf "company name" (partner OR administrator OR "board of partners")`
- `filetype:pdf "company name" ("social contract" OR "contract amendment")`
- `filetype:pdf "company name" "meeting minutes"`
- `site:linkedin.com/in "company name" (partner OR owner OR "founder at")`
- `site:facebook.com "company name" (owner OR proprietor)`
- `site:instagram.com "company name" (owner OR proprietor)`
- `"company name" "board of partners" site:jusbrasil.com.br`

**For General Public Documents:**
- `filetype:pdf OR filetype:docx OR filetype:xlsx "company name" (report OR manual OR policy OR "financial statement")`
- `"company name" intitle:index.of (manual OR docs OR backup)`
- `"company name" inurl:admin OR inurl:login`

**For Code Repositories (GitHub/GitLab):**
- `site:github.com "company name"`
- `site:gitlab.com "company name"`
- `site:github.com "company name" (api_key OR password OR secret)` (to identify leaks)

The agent must extract names of natural persons from these documents to feed the `partners` field and document/repository URLs for the `public_documents` and `code_repositories` fields (to be added).

### 10. Employee listing (LinkedIn and Other Directories)
- `site:linkedin.com/company/"company name"/people` (to list employees)
- `site:linkedin.com/in "employee name" "company name"` (for specific profiles)
- `"company name" "employee list"` (for other directories)

The agent should collect employee names, roles, and LinkedIn/other social media handles, correlating them with the company.

### 11. Revalidation
Any partial result must be reused as pivot, including cross-wise.

Perform new search using:
- legal name, if found
- candidate CNPJ, if found
- corporate address, phone or e-mail, if found
- domain and trade name in combination
- trade name + legal name
- trade name + CNPJ
- domain + CNPJ

The agent must:
- advance layer if no result is found
- NOT stop after layer 1
- NOT consider data absent without executing layer 4
- use layers 5, 6, 7 and 8 to expand coverage and confirm candidates
- register in `search_trace` which source classes were used
- also register most relevant queries and opened URLs

---

## Tasks

1. Try to identify primarily:
   - CNPJ
   - legal name
   - trade name
   - registration status

2. Try to identify public signals of:
   - board at corporate level
   - official company channels
   - public proceedings involving the company

3. Try to identify:
   - related or similar companies
   - multiple plausible CNPJs
   - similar domains
   - social media handles
   - public contacts, including WhatsApp when explicit

4. If a partial result appears, reuse it as pivot for a second search

5. Consolidate the best available match, without inventing

6. Register what remains absent

7. Produce a short collection summary for the next modules

---

## Mandatory Output

Return ONLY valid JSON, no additional text.

```json
{
  "corporate_identity": {
    "cnpj": "",
    "legal_name": "",
    "trade_name": "",
    "registration_status": "",
    "partners": [
      {
        "name": "",
        "role": "",
        "social_handles": [],
        "evidence_level": "confirmed|candidate|unresolved"
      }
    ],
    "evidence_level": "confirmed|candidate|unresolved"
  },
  "related_companies": [
    {
      "cnpj": "",
      "legal_name": "",
      "trade_name": "",
      "relationship_type": "same_group|subsidiary|parent|partner|possible",
      "evidence_level": "confirmed|candidate|unresolved",
      "correlation_points": {
        "partners": [],
        "address": [],
        "phone": [],
        "email": [],
        "domain": [],
        "cnae": [],
        "social_handles": []
      }
    }
  ],
  "domains": [
    {
      "domain": "",
      "type": "official|related|similar",
      "evidence_level": "confirmed|candidate|unresolved",
      "notes": ""
    }
  ],
  "social_handles": [
    {
      "platform": "",
      "handle": "",
      "url": "",
      "evidence_level": "confirmed|candidate|unresolved"
    }
  ],
  "contacts": [
    {
      "type": "phone|email|whatsapp",
      "value": "",
      "source": "",
      "notes": ""
    }
  ],
  "official_channels": [],
  "corporate_registry_signals": [],
  "public_litigation_signals": [],
  "google_dorks_results": [
    {
      "query": "string",
      "finding": "string",
      "url": "string"
    }
  ],
  "public_documents": [
    {
      "title": "string",
      "url": "string",
      "type": "string (pdf, docx, xlsx, etc)",
      "source": "string"
    }
  ],
  "code_repositories": [
    {
      "name": "string",
      "url": "string",
      "platform": "string (github, gitlab, etc)",
      "owner": "string"
    }
  ],
  "employees": [
    {
      "name": "string",
      "role": "string",
      "social_handles": [
        {
          "platform": "string",
          "handle": "string",
          "url": "string"
        }
      ],
      "evidence_level": "confirmed|candidate"
    }
  ],
  "search_trace": [],
  "unresolved_gaps": [],
  "collection_summary": "",
  "confidence": "low|medium|high"
}
```