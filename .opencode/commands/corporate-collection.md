---
description: Executes module 04 with advanced web collection and corporate correlations
agent: collector-gpt
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/04-corporate-collection.md.

Use the following files as mandatory inputs:
@cases/{{case_id}}/runs/01-case-intake.json
@cases/{{case_id}}/runs/02-framing-gpt.json

Objective of this execution:
- consolidate public corporate data of the target
- primarily identify CNPJ, corporate name, trade name, and registration status
- necessarily identify the Board of Partners and Administrators (QSA)
- identify related companies, similar domains, social networks, contacts, and WhatsApp
- perform Google Dorks to find hidden documents and mentions
- prepare a collection artifact with maximum coverage and correlations for the next modules

Mandatory operational instructions:
- Read @cases/{{case_id}}/runs/01-case-intake.json
- Read @cases/{{case_id}}/runs/02-framing-gpt.json
- Use websearch to discover public sources before concluding data absence
- Use webfetch to open specific URLs found by websearch
- Prioritize finding CNPJ and corporate name before expanding to other signals
- DO NOT end collection without completing the full spec strategy
- DO NOT accept absence of CNPJ while there is a plausible unmatched entry in any corporate directory or aggregator
- If there is a promising corporate directory result, compulsorily webfetch before concluding absence
- If a source yields a plausible but not definitive match, record it as `candidate`
- If there is coherent convergence in at least 2 plausible and independent public sources, record as `confirmed`
- Reuse each partial finding as pivot for new search

Mandatory search flow:
1. Official website
   - home
   - contact, about, footer, policies, FAQ, terms, press pages
   - extract: corporate name, CNPJ, address, phone, email, WhatsApp, domains, social networks
2. Search by brand and domain
   - trade name
   - legal name
   - domain
   - domain without TLD
   - site:<domain> CNPJ
   - site:<domain> corporate name
3. Mandatory corporate directories (Focus on QSA)
   - site:casadosdados.com.br (Priority on QSA)
   - site:transparencia.cc (Priority on QSA)
   - site:cnpj.biz
   - site:econodata.com.br
   - site:empresas.serasaexperian.com.br
   - Commercial Board / Federal Revenue
   - DO NOT accept "login required" without opening at least 2 of these directories via webfetch first.
4. Search for similar and related companies
   - trade name variations
   - corporate name variations
   - abbreviated spellings
   - name + city/state
   - name + activity
   - list all plausible CNPJs found
5. Mandatory candidate correlation
   - partners / administrators
   - address
   - phone
   - email
   - domain
   - CNAE / economic activity
   - social networks
   - WhatsApp
6. Similar domains
   - generate and search:
     - close spellings
     - variations without accents
     - hyphens and numbers
     - different extensions (.com, .com.br, .net, .org)
   - try correlating domains with the target company and related companies
7. Social networks and public presence
   - LinkedIn
   - Instagram
   - Facebook
   - YouTube
   - other relevant platforms
   - extract handles, URLs, description, location, and contacts
8. Contacts and WhatsApp
   - capture phone numbers found in:
     - official website
     - social networks
     - directories
     - public maps and listings
   - identify numbers with WhatsApp indication when explicitly shown in source
9. Google Dorks (Recovery of QSA, Public Documents, and Repositories)
   - **For Partners and Legal Documents:**
     - `filetype:pdf "company name" (partner OR administrator OR "board of partners")`
     - `filetype:pdf "company name" ("articles of incorporation" OR "contract amendment")`
     - `filetype:pdf "company name" "minutes of meeting"`
     - `site:linkedin.com/in "company name" (partner OR owner OR "founder at")`
     - `site:facebook.com "company name" (owner OR proprietor)`
     - `site:instagram.com "company name" (owner OR proprietor)`
     - `"company name" "board of partners" site:jusbrasil.com.br`
   - **For General Public Documents:**
     - `filetype:pdf OR filetype:docx OR filetype:xlsx "company name" (report OR manual OR policy OR "financial statement")`
     - `"company name" intitle:index.of (manual OR docs OR backup)`
     - `"company name" inurl:admin OR inurl:login`
   - **For Code Repositories (GitHub/GitLab):**
     - `site:github.com "company name"`
     - `site:gitlab.com "company name"`
     - `site:github.com "company name" (api_key OR password OR secret)` (to identify leaks)
   - If QSA was not found in directories, these searches are MANDATORY. Extract personal names for `partners` and document/repository URLs for `public_documents` and `code_repositories`.
10. Employee listing (LinkedIn and other directories)
   - `site:linkedin.com/company/"company name"/people` (to list employees)
   - `site:linkedin.com/in "employee name" "company name"` (for specific profiles)
   - `"company name" "employee list"` (for other directories)
   - Collect employee names, roles, and LinkedIn/other social media handles, correlating them with the company for the `employees` field.
11. Re-search by pivots
   - legal name, if found
   - candidate CNPJ, if found
   - corporate address, phone, or email, if found
   - domain and trade name combination
   - trade name + corporate name
   - trade name + CNPJ
   - domain + CNPJ

Minimum mandatory searches before concluding `unresolved` on CNPJ:
- at least 1 search by domain
- at least 1 search by trade name or brand
- at least 1 search in corporate directory
- at least 1 webfetch on plausible directory result, if any
- at least 1 attempt to search similar companies
- at least 1 attempt to search similar domains
- at least 3 distinct pivots in total

Minimum validation criteria for `confirmed`:
- at least 2 plausible and independent public sources
- coherent convergence on at least 2 of the following points, if available:
  - CNPJ
  - corporate name
  - trade name
  - address
  - phone
  - email
  - domain
  - CNAE / activity
  - social networks

Generate ONLY valid JSON compatible with spec 04.
Save the result in @cases/{{case_id}}/runs/04-corporate-collection-gpt.json.
If the folder @cases/{{case_id}}/runs does not exist, create it.

After saving, respond only with a short status JSON in this format:

{
  "status": "ok",
  "output_file": "cases/{{case_id}}/runs/04-corporate-collection-gpt.json"
}

Mandatory rules:
- Do not generate text outside JSON
- All list fields must be valid JSON arrays
- Do not use markdown
- Do not add extra fields
- If input is missing, return structured error in JSON