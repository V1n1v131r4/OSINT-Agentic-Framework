# 12 — Model Comparison

## Objective
Compare outputs from two models within the same module or the entire case.

## Required Inputs
- gpt_output
- claude_output
- module_name
- rubric_reference

## Agent Instructions
Compare structure, evidence discipline, usefulness, and extrapolation. Ignore style as a primary criterion.

## Tasks
1. Identify consensual facts.
2. Identify analytical divergences.
3. Mark unsupported inferences.
4. Point out which output was better in clarity, discipline, and usefulness.
5. Recommend adjudication to the analyst.

## Required Output
```json
{
  "consensus_facts": [],
  "divergent_points": [],
  "unsupported_inferences": [],
  "best_output_by_dimension": {
    "clarity": "",
    "evidence_discipline": "",
    "operational_usefulness": ""
  },
  "adjudication_recommendation": ""
}
```

## Quality Criteria
- do not favor verbosity
- prioritize adherence to evidence