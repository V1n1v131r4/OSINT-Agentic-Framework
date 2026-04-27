# 11 — Reporting

## Objective

Transform the already correlated findings into a short, executive, and traceable report.

This module focuses on FINAL COMMUNICATION, not new analysis.

---

## Mandatory Inputs

- case intake
- output from module 10
- other previous outputs only if necessary for summary coherence

If the correlation output is not available, DO NOT proceed.

---

## Instructions to the Agent

- Work only with the provided inputs
- DO NOT search for new sources
- DO NOT expand scope
- DO NOT reinterpret the case beyond what has already been consolidated
- The report should reflect only:
  - observed relationships
  - identified patterns
  - registered anomalies
  - already known gaps

---

## Execution Rules

- Generate ONLY valid JSON
- Do not add fields outside the mandatory output
- All list fields must be valid JSON arrays
- The executive summary should be short, clear, and coherent with the original analytical objective
- Do not turn a hypothesis into a fact
- Do not omit limitations
- Do not use inflated or generic language

---

## Expected Structure

### 1. Executive Summary

Short synthesis of the case, highlighting:

- what was possible to observe
- the overall confidence level
- the main limitation of the analysis

### 2. Key Findings

List the most relevant and traceable points.

### 3. Hypotheses and Interpretations

List only hypotheses still supported by the previous data.

### 4. Gaps

List what still needs validation.

### 5. Risks and Implications

List practical implications of the findings, without exaggeration.

### 6. Next Steps

List useful complementary validations and collections.

---

## Mandatory Output

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
