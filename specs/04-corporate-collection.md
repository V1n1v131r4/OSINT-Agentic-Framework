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

## Instructions to the Agent

- Collect only corporate and public data
- Before concluding data absence, use websearch and webfetch
- Prioritize Brazilian corporate sources and directories present in the repository https://github.com/osintbrazuca/osint-brazuca as a discovery base during collection
- Prioritize public sources that display:
  - CNPJ (Tax ID)
  - Legal name
  - Trade name
  - Registration status
  - Business directories
  - Signals of public lawsuits involving the company
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
- consulting at least 1 business directory
- opening via webfetch at least 1 plausible directory result, if any
- trying at least 3 distinct pivots of name, brand, or domain
- trying to identify similar business names
- trying to identify similar domains

If there is a plausible result in a business directory not opened, the collection CANNOT be closed.

---

## Confirmation Rule

A corporate data point can be promoted to `confirmed` when there is:

- at least 2 plausible and independent public sources
- coherent convergence between these sources

Convergence can use, when available:
- CNPJ
- Legal name
- Trade name
- Address
- Phone
- E-mail
- Domain
- CNAE / economic activity
- Social networks
- Other consistent institutional signals

If there is only one plausible source, or insufficient partial convergence, register as `candidate`.

---

## Mandatory Search Strategy

The collection must follow a progressive flow based on source classes.

The agent CANNOT close the collection without executing all layers below:

### 1. Primary Source
- official website
- internal pages of the site:
  - contact
  - about
  - footer
  - policies
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
- social networks

### 2. General Search
- entity name + CNPJ
- domain + CNPJ
- entity name + legal name
- domain + legal name
- site:<domain> CNPJ
- site:<domain> "legal name"

### 3. Expanded Search
- entity name + business registration
- entity name + legal name
- domain without TLD + CNPJ
- domain without TLD + legal name
- entity name + city/state, if available
- domain + city/state, if available
- entity name + economic activity

### 4. Business Directories and Aggregators (Focus on QSA/Partners)
The agent CANNOT claim login necessity without first exhausting these sources that provide the Board of Partners and Administrators (QSA) publicly:
- `casadosdados.com.br` (Highly recommended for detailed QSA)
- `transparencia.cc` (Excellent for corporate links)
- `cnpj.biz`
- `econodata.com.br`
- `empresas.serasaexperian.com.br`
- Transparency portals and Official Gazettes

Mandatorily extract the Board of Partners and Administrators (QSA). If not found in one source, MUST try the others.

### 5. Similar and Related Companies
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
- social networks

### 6. Similar Domains
Search for:
- close spellings
- domains without accents
- hyphens
- numbers
- alternative TLDs
- combinations with brand, city, or activity

Correlate the domains found with:
- main company
- related companies
- contacts
- social networks

### 7. Social Networks and Public Presence
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
- buttons or explicit mentions of WhatsApp

Only register WhatsApp when the association is explicit in the source.

### 9. Google Dorks (QSA Recovery, Public Documents, and Repositories)
If the QSA is not found in the directories, the use of Google Dorks is MANDATORY to locate partners in indexed documents. Additionally, Google Dorks should be used to find other public documents and code repositories:

**For Partners and Legal Documents:**
- `filetype:pdf "company name" (partner OR administrator OR "shareholding structure")`
- `filetype:pdf "company name" ("articles of incorporation" OR "contract amendment")`
- `filetype:pdf "company name" "minutes of the meeting"`
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

The agent must extract names of natural persons from these documents to feed the `partners` field and URLs of documents/repositories for the `public_documents` and `code_repositories` fields.

### 10. Employee Listing (LinkedIn and Other Directories)
- `site:linkedin.com/company/"company name"/people` (to list employees)
- `site:linkedin.com/in "employee name" "company name"` (for specific profiles)
- `"company name" "employee list"` (for other directories)

The agent must collect employee names, roles, and LinkedIn/other social media handles, correlating them with the company.

### 11. Revalidation
Any partial result must be reused as a pivot, including cross-referencing.

Execute a new search using:
- legal name, if found
- candidate CNPJ, if found
- address, phone, or corporate e-mail, if found
- domain and trade name in combination
- trade name + legal name
- trade name + CNPJ
- domain + CNPJ

The agent must:
- advance to the next layer if no result is found
- NOT stop after layer 1
- NOT consider data absence without executing layer 4
- use layers 5, 6, 7, and 8 to expand coverage and confirm candidates
- register in `search_trace` which source classes were used
- also register queries and most relevant open URLs

---

## Tasks

1. Try to identify as a priority:
   - CNPJ
   - legal name
   - trade name
   - registration status

2. Try to identify public signals of:
   - board of partners at the corporate level
   - official company channels
   - public lawsuits involving the company

3. Try to identify:
   - related or similar companies
   - multiple plausible CNPJs
   - similar domains
   - social media handles
   - public contacts, including WhatsApp when explicit

4. If a partial result appears, reuse it as a pivot for a second search

5. Consolidate the best available match, without inventing

6. Register what remained missing

7. Produce a short collection summary for the next modules

---

## Mandatory Output

Return ONLY valid JSON, without additional text.

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
