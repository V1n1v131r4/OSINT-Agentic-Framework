---
description: Executa pipeline completa OSINT (GPT + Claude + comparação)
agent: collector-gpt
model: openai/gpt-5-mini
---

Etapas:

1. Framing GPT
@.opencode/commands/framing.md

2. Framing Claude
@.opencode/commands/framing-claude.md

3. Expansion GPT
@.opencode/commands/expansion.md

4. Expansion Claude
@.opencode/commands/expansion-claude.md

5. Technical Surface
@.opencode/commands/technical-surface.md

6. Correlation GPT
@.opencode/commands/correlation.md

7. Report GPT
@.opencode/commands/report.md

8. Compare
@.opencode/commands/compare.md

9. Postmortem
@.opencode/commands/postmortem.md

Regras:
- Executar sequencialmente
- Não pular etapas
- Manter consistência de outputs
