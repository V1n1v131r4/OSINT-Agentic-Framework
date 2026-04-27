# 05 — Identity Validation (Individuals)

## Objective

Validate the target's identity, cross-referencing data from multiple sources to confirm if the profiles and records found belong to the same natural person.

---

## Mandatory Inputs

- individual_collection_output
- entity_graph_output

---

## Tasks

1. **Identifier Cross-Referencing**: Check if e-mails, phones, or usernames repeat across different platforms.
2. **Biographical Consistency**: Validate if the professional and educational history is coherent across LinkedIn, resumes, and public records.
3. **Link Analysis**: Confirm relationships with companies or other people mentioned in the intake.
4. **Confidence Classification**:
   - `Confirmed`: Identity validated by multiple points of convergence.
   - `Candidate`: Probable profile, but with ambiguities (e.g., namesakes).
   - `Unverified`: Without sufficient data for confirmation.

---

## Expected Output

```json
{
  "validated_identity": {
    "full_name": "",
    "confirmed_identifiers": [],
    "status": "confirmed | candidate | unverified"
  },
  "identity_conflicts": [],
  "biographical_summary": ""
}
```
