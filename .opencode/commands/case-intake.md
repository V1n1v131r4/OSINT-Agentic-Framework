---
description: Normaliza o intake e sugere a pipeline correta baseada no propósito da operação
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/01-case-intake.md.

Instruções operacionais:
1. Localize o arquivo `intake.json` no diretório do caso (ex: `cases/<case-id>/intake.json`).
2. Se o operador não especificou o caminho, procure por arquivos `intake.json` recentes.
3. Valide o `operation_type`.

Objetivo:
- Normalizar o intake bruto.
- Atribuir/Validar o `case_id`.
- **Sugerir o próximo comando** baseado no `operation_type`.

Regras de Saída:
- Salve o resultado em `cases/<case-id>/runs/01-case-intake.json`.
- O campo `next_step_suggestion` deve seguir o mapeamento:
  - `institutions` -> `/framing`
  - `individuals` -> `/framing-indiv`
  - `disinformation_campaign` -> `/framing-disinfo`
  - `narrative_analysis` -> `/framing-narrative`
  - `data_leak` -> `/framing-leak`

Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "case_id": "<case-id>",
  "operation_type": "<type>",
  "output_file": "cases/<case-id>/runs/01-case-intake.json",
  "next_command": "<sugestão>"
}
```
