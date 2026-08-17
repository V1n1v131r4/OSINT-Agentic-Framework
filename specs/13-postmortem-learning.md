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
1. Register errors detected in the process.
2. Register reusable useful patterns.
3. Register distinct behaviors of each model.
4. Suggest adjustments to specs or schemas.
5. Produce clear and short memory objects.
6. **Consolidate the learning into the global memory** (see "Learning Loop" section below).

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

---

## Learning Loop (Automatic Consolidation)

This step is the **last one in all 5 pipelines**. Besides saving the case postmortem, it
**closes the framework's learning loop** by consolidating the reusable patterns into a **global
memory** that will be reinjected into future cases by `case-intake` (spec 01).

No additional command is run by the operator — this consolidation happens **in the same
execution** as the postmortem, automatically.

### Source
- The `reusable_patterns` and `memory_objects` you just produced for this case.
- The case `operation_type` (read it from `cases/<case-id>/runs/01-case-intake.json`).

### Target
- File: `memory/global/playbooks.json` (schema: `schemas/playbook-memory.schema.json`).
- If the file does not exist, create it as `{ "version": 1, "playbooks": [] }`.

### Consolidation rules
1. **Segmentation by operation_type.** Each playbook is stamped with the case `operation_type`.
   Genuinely cross-cutting pivots (e.g. the passive-pivots checklist) may use
   `operation_type: "all"`. Never mix learning from different types in the same bucket.
2. **Deduplication by (id, operation_type).** Generate a stable `id` slug (kebab-case) from the
   essence of the pivot. If a playbook already exists with the same `id` **and** the same
   `operation_type`, treat it as the same pivot — **do not create a duplicate**.
3. **Reinforcement (this is what makes the agent more specialized).** When you find an existing
   pivot:
   - If the current `case_id` is **not yet** in `source_cases`: add it, increment
     `reinforcement_count` by 1, and update `last_seen_case`.
   - If the `case_id` is **already** in `source_cases`: do not change the count (guarantees
     **idempotency** — running the same case's postmortem twice does not inflate the number).
4. **New pivots.** If the pivot does not exist in the bucket, add it with
   `reinforcement_count: 1`, `first_seen_case` and `last_seen_case` equal to the `case_id`, and
   `source_cases: [case_id]`.
5. **confidence_tier** derived from `reinforcement_count`: `1` → `low`; `2-3` → `medium`;
   `4+` → `high`.
6. Update `updated_by_case` with the current `case_id`.

### Criteria
- Only promote to a playbook what is **truly reusable** in future cases of the same type.
- Prefer a few high-value pivots over many generic ones.

### Next step
- The loop is closed. The postmortem `next_command` is empty (end of case).
