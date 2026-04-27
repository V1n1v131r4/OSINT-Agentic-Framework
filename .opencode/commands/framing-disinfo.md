---
description: Framing analítico para campanhas de desinformação
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/02-framing-disinfo.md.

Instruções operacionais:
1. Leia o `01-case-intake.json` do caso atual.
2. Gere o framing focado em narrativas e coordenação.
3. Salve em `cases/<case-id>/runs/02-framing-gpt.json`.

Regras de Saída:
- Sugira o próximo comando: `/disinfo-collection`.

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/02-framing-gpt.json",
  "next_command": "/disinfo-collection"
}
```
