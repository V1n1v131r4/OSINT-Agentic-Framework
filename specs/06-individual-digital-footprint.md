# 06 — Individual Digital Footprint

## Objective
Map the technical digital footprint of an individual, focusing on exposed identifiers, e-mails, personal domains, and presence in service databases.

---

## Mandatory Inputs
- identity_validation_output
- individual_collection_output

---

## Tasks
1. **Identifier Mapping**: Consolidate e-mails (personal and professional), user handles, and possible phone numbers.
2. **Personal Asset Enumeration**: Identify domains registered in the individual's name or personal blogs/sites.
3. **Service Exposure Verification**: Check presence on platforms (e.g., Gravatar, Keybase, GitHub) that reveal technical metadata.
4. **Document Metadata Analysis**: If documents have been collected, extract metadata that reveals software used or directory paths.

---

## Mandatory Output
```json
{
  "technical_identifiers": {
    "emails": [],
    "handles": [],
    "phones": []
  },
  "personal_assets": [],
  "service_exposure": [],
  "metadata_findings": [],
  "confidence": "low | medium | high"
}
```
