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
- **Reinject the global playbook memory** (see "Learning Loop" below).

---

## Learning Loop (Playbook Reinjection)

This is the **entry point of all 5 pipelines**. Before routing, it **reinjects the knowledge
accumulated** by the framework in previous cases — this is what makes it "the more you use it,
the more specialized it gets".

1. Read `memory/global/playbooks.json` (if it does not exist, proceed without playbooks).
2. **Filter by this case's `operation_type`** — also include those with `operation_type: "all"`
   (cross-cutting). Never bring in playbooks from other operation types.
3. Sort by `reinforcement_count` (desc) and select the **top 5**.
4. Emit them in the `applicable_playbooks` field of the output, as **method context** for the
   following steps. They are neither hypotheses nor collection — they are proven pivots to prioritize.

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
  "applicable_playbooks": [
    {
      "id": "",
      "pivot": "",
      "confidence_tier": "",
      "reinforcement_count": 0
    }
  ],
  "next_step_suggestion": "/framing"
}
```

### Next Step Mapping:
- **institutions**: `/framing`
- **individuals**: `/framing-indiv`
- **disinformation_campaign**: `/framing-disinfo`
- **narrative_analysis**: `/framing-narrative`
- **data_leak**: `/framing-leak`
