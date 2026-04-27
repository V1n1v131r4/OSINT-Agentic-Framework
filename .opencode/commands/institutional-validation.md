---
description: Valida sinais institucionais e sugere o próximo passo da pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/05-institutional-validation.md.

Instruções operacionais:
1. Localize o arquivo `04-entity-graph-gpt.json` no diretório `runs` do caso atual.
2. Valide as entidades institucionais em fontes públicas.
3. Salve o resultado em `cases/<case-id>/runs/05-institutional-validation-gpt.json`.

Objetivo:
- Confirmar existência e consistência institucional.
- **Sugerir o próximo comando** (geralmente `/technical-surface`).

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/05-institutional-validation-gpt.json",
  "next_command": "/technical-surface"
}
```
