# 01 — Case Intake

## Objective

Register the initial context of the case in a structured way, ensuring clarity about the purpose of the operation and defining the pipeline to be followed.

---

## Mandatory Inputs

- **case_id**: Unique identifier for the case.
- **operation_type**: Type of operation (institutions, individuals, disinformation_campaign, narrative_analysis, data_leak).
- **target_name**: Main target.
- **analysis_goal**: Investigation objective.
- **restrictions**: Operational limits.

---

## Optional Inputs

- target_url
- scope_type
- known_data
- analyst_notes
- source_seed

If mandatory inputs are missing or ambiguous, DO NOT proceed.

---

## Instructions to the Agent

- Validate if the `operation_type` is one of the supported types.
- Do not start collection.
- Do not generate hypotheses.
- This module is only structural and for routing.

---

## Expected Output

The agent must return the structured JSON and, in its textual response (if any), indicate the suggested next command based on the `operation_type`.

```json
{
  "case_id": "",
  "operation_type": "",
  "target_name": "",
  "analysis_goal": "",
  "scope_definition": "",
  "next_step_suggestion": "/framing"
}
```

### Next Step Mapping:
- **institutions**: `/framing`
- **individuals**: `/framing-indiv`
- **disinformation_campaign**: `/framing-disinfo`
- **narrative_analysis**: `/framing-narrative`
- **data_leak**: `/framing-leak`
