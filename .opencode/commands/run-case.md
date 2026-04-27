---
description: Automatically executes the complete OSINT pipeline in sequence
agent: collector-gpt
model: openai/gpt-5-mini
subtask: true
return:
  - /framing
  - /expansion
  - /entity-graph
  - /institutional-validation
  - /technical-surface
  - /brand-social-analysis
  - /unstructured-extraction
  - /geo-context
  - /correlation
  - /report
  - /postmortem
---

## CRITICAL RULE (EXECUTION)

You MUST NOT:

- execute modules manually
- generate JSON for subsequent modules
- interpret data for next stages
- continue the pipeline on your own

You MUST:

- execute ONLY the command for this stage
- return the result
- let the chaining occur via `return`

---

## MANDATORY BEHAVIOR

After executing the command:

- STOP immediately
- DO NOT continue reasoning about the next module
- DO NOT generate additional output
- DO NOT anticipate stages

---

## EXECUTION

Execute exclusively:

@.opencode/commands/case-intake.md

---

## FINAL RESTRICTION

If you generate any content beyond the JSON of the executed command:

→ this is considered an execution error
