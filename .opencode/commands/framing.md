---
description: Transforma o intake em framing analítico e sugere o próximo passo da pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/02-case-framing.md.

Instruções operacionais:
1. Localize o arquivo `01-case-intake.json` no diretório `runs` do caso atual.
2. Gere o framing analítico baseado no intake.
3. Salve o resultado em `cases/<case-id>/runs/02-framing-gpt.json`.

Objetivo:
- Definir hipóteses e vetores de investigação.
- **Sugerir o próximo comando** baseado no `operation_type` do intake.

Regras de Saída:
- O campo `next_command` deve ser `/corporate-collection` para a pipeline de instituições.
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/02-framing-gpt.json",
  "next_command": "/corporate-collection"
}
```
