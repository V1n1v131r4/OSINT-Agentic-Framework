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
- **Reinjetar a memória global de playbooks** (loop de aprendizado).
- **Sugerir o próximo comando** baseado no `operation_type`.

Instruções de reinjeção (loop de aprendizado):
1. Leia `memory/global/playbooks.json` (se não existir, siga sem playbooks).
2. Filtre os playbooks pelo `operation_type` deste caso + os de `operation_type: "all"`.
3. Ordene por `reinforcement_count` (desc), pegue o top-5 e inclua-os em `applicable_playbooks`
   no arquivo salvo `cases/<case-id>/runs/01-case-intake.json`, conforme a spec
   @specs/01-case-intake.md.

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
  "applicable_playbooks_count": 0,
  "next_command": "<sugestão>"
}
```
