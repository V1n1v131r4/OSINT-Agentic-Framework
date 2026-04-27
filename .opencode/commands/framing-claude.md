---
description: Framing analítico com Claude (suporta múltiplos propósitos)
agent: collector-claude
model: anthropic/claude-sonnet-4-5
---

Siga a spec de framing correspondente ao `operation_type` definido no intake.

Instruções operacionais:
1. Localize o arquivo `01-case-intake.json` no diretório `runs` do caso atual.
2. Gere o framing analítico baseado no intake e no propósito da operação.
3. Salve o resultado em `cases/<case-id>/runs/02-framing-claude.json`.

Objetivo:
- Definir hipóteses e vetores de investigação específicos.
- **Sugerir o próximo comando** baseado no `operation_type`:
  - `institutions` -> `/corporate-collection`
  - `individuals` -> `/individual-collection`
  - `disinformation_campaign` -> `/disinfo-collection`
  - `narrative_analysis` -> `/narrative-collection`
  - `data_leak` -> `/leak-collection`

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/02-framing-claude.json",
  "next_command": "<sugestão>"
}
```
