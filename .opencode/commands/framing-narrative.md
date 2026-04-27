---
description: Framing analítico para análise de narrativas
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/02-framing-narrative.md.

Instruções operacionais:
1. Leia o `01-case-intake.json` do caso atual.
2. Gere o framing focado em ecossistema e influência.
3. Salve em `cases/<case-id>/runs/02-framing-gpt.json`.

Regras de Saída:
- Sugira o próximo comando: `/narrative-collection`.

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/02-framing-gpt.json",
  "next_command": "/narrative-collection"
}
```
