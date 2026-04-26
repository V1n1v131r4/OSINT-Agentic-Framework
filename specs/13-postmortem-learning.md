# 13 — Postmortem Learning

## Objective
Convert the case into reusable operational memory.

## Mandatory Inputs
- final_report
- adjudication_recommendation
- analyst_feedback
- module_outputs

## Instructions to the Agent
Extract useful patterns, errors, and method adjustments. Do not rewrite the case; produce operational learning.

## Tasks
1. Log errors detected in the process.
2. Log reusable useful patterns.
3. Log distinct behavior of each model.
4. Suggest adjustments to specs or schemas.
5. Produce clear and concise memory objects.

## Mandatory Output
```json
{
  "errors_detected": [],
  "reusable_patterns": [],
  "model_behavior_notes": {
    "gpt": [],
    "claude": []
  },
  "spec_adjustments": [],
  "memory_objects": []
}
```

## Quality Criteria
- prioritize truly reusable patterns
- avoid vague lessons