---

## `specs/11-reporting.md`

```md
# 11 — Reporting

## Objective

Transform the already correlated findings into a short, executive, and traceable report.

This module focuses on FINAL COMMUNICATION, not on new analysis.

---

## Mandatory inputs

- case intake
- output from module 10
- other previous outputs only if necessary for summary coherence

If the correlation output is not available, DO NOT proceed.

---

## Instructions to the agent

- Work only with the provided inputs
- DO NOT seek new sources
- DO NOT expand the scope
- DO NOT reinterpret the case beyond what has already been consolidated
- The report should reflect only:
  - observed relationships
  - identified patterns
  - recorded anomalies
  - already known gaps

---

## Execution rules

- Generate ONLY valid JSON
- Do not add fields outside the mandatory output
- All list fields must be valid JSON arrays
- The executive summary must be short, clear, and consistent with the original analytical objective
- Do not transform hypotheses into facts
- Do not omit limitations
- Do not use inflated or generic language

---

## Expected structure

### 1. Executive summary

Short synthesis of the case, highlighting:

- what was possible to observe
- the overall confidence level
- the main limitation of the analysis

### 2. Key findings

List the most relevant and traceable points.

### 3. Hypotheses and interpretations

List only hypotheses still supported by the previous data.

### 4. Gaps

List what still needs validation.

### 5. Risks and implications

List practical implications of the findings, without exaggeration.

### 6. Next steps

List useful complementary validations and collections.

---

## Mandatory output

```json
{
  "executive_summary": "",
  "key_findings": [],
  "hypotheses": [],
  "gaps": [],
  "risks": [],
  "next_steps": [],
  "confidence": "low | medium | high"
}
```
