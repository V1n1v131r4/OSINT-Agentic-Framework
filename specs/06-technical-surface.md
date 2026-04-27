# 06 — Technical Surface

## Objective

Map the target's public technical surface, identifying externally visible digital infrastructure assets and signals.

This module focuses on technical ENUMERATION with passive enrichment.

---

## Mandatory Inputs

- primary_assets (main domain, known subdomains)
- residual_or_legacy_assets

## Optional Inputs

- supporting_signals

If no domain or technical asset is defined, DO NOT proceed.

---

## Instructions to the Agent

- Work only with public data
- It IS PERMITTED to enrich data using:
  - public DNS
  - WHOIS records
  - domain resolution
  - certificate transparency (crt.sh)
- DO NOT perform active or intrusive scanning
- DO NOT test for vulnerabilities

---

## Execution Rules

- All list fields must be valid JSON arrays
- Each item must be a simple value (string or structured object)
- DO NOT include explanatory text within the fields
- DO NOT include inferences without observable evidence
- If there is no clear evidence, DO NOT include the item
- Do not describe items — only list values

---

## Tasks

### 1. Identify domains and subdomains

- main domain
- subdomains discovered via:
  - DNS
  - certificates
  - common patterns (www, api, mail)

---

### 2. Identify DNS records

Search for:

- A / AAAA
- MX
- NS
- TXT (SPF, DKIM, DMARC)

---

### 3. Identify IPs and infrastructure

- IPs associated with the domains
- CDN or proxy (if visible)
- providers

---

### 4. Identify ASN (when possible)

- ASN
- organization

---

### 5. Identify technical services

- web (http/https)
- e-mail (MX)
- CDN
- proxy

---

### 6. Identify technical signals

- SPF present
- DMARC present
- use of CDN
- use of third parties

---

## Mandatory Output

```json
{
  "domains": [],
  "subdomains": [],
  "dns_records": {
    "a_records": [],
    "mx_records": [],
    "ns_records": [],
    "txt_records": []
  },
  "ip_addresses": [],
  "asn_info": [
    {
      "asn": "",
      "organization": ""
    }
  ],
  "providers": [],
  "exposed_services": [],
  "technical_signals": [],
  "confidence": "low | medium | high"
}
```
