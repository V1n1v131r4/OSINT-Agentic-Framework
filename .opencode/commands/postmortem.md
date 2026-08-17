---
description: Executes the methodological review and saves lessons learned
agent: reviewer
model: openai/gpt-5-mini
---

Strictly follow the spec in @specs/13-postmortem-learning.md.

Operational Instructions:
1. Locate the pipeline output files in the `runs` directory of the current case.
2. Review the methodological quality and identify lessons learned.
3. Save the result in `cases/<case-id>/memory/13-postmortem.json`.
4. **Consolidate the learning into the global memory** (automatic learning loop):
   - Read the case `operation_type` from `cases/<case-id>/runs/01-case-intake.json`.
   - Read (or create) `memory/global/playbooks.json`.
   - Merge this case's `reusable_patterns`/`memory_objects` into the global memory strictly
     following the "Consolidation rules" in @specs/13-postmortem-learning.md: segment by
     `operation_type`, deduplicate by `(id, operation_type)`, **reinforce** (increment
     `reinforcement_count` only if the `case_id` is not yet in `source_cases` — idempotency),
     recompute `confidence_tier`.
   - Save it back to `memory/global/playbooks.json`.

Objective:
- Continuous improvement of the framework and the operator.
- Close the loop: the more cases you run, the more specialized the framework becomes (via pivot reinforcement).

Output Rules:
- Return ONLY the status JSON:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/memory/13-postmortem.json",
  "global_memory_file": "memory/global/playbooks.json",
  "message": "Operation finalized. Lessons learned registered and consolidated into the global memory."
}
```
