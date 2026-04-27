---
description: Orquestrador dinâmico que segue as sugestões de cada comando da pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Execute esta rotina de forma estritamente sequencial, seguindo as sugestões dinâmicas de cada comando.

Objetivo:
- Validar a pipeline completa conforme o `operation_type`.
- Seguir o campo `next_command` retornado por cada etapa.

Regras obrigatórias:
1. Comece executando `/case-intake`.
2. Após cada comando, leia o JSON de status retornado.
3. Se o status for "ok", execute o comando indicado no campo `next_command`.
4. Continue até que o comando sugerido seja `/postmortem` ou não haja mais sugestões.
5. Se qualquer etapa falhar, interrompa e reporte o erro.

Ordem de Execução Inicial:
1. `/case-intake`
2. Siga a sugestão dinâmica de `next_command`.

Ao final, responda com o JSON de conclusão:

```json
{
  "status": "ok",
  "message": "dynamic_pipeline_complete",
  "final_report": "cases/<case-id>/runs/11-report-gpt.json"
}
```
