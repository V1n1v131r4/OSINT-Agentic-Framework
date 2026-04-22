---
description: Pipeline rápida (somente GPT) com fluxo mínimo operacional
agent: collector-gpt
model: openai/gpt-5-mini
---

Execute esta rotina de forma estritamente sequencial.

Objetivo:
- validar rapidamente a pipeline mínima
- reduzir custo e tempo
- manter coerência entre outputs

Regras obrigatórias:
- Execute UMA etapa por vez
- Após cada etapa, aguarde o JSON de status
- Verifique se o campo `"status"` é `"ok"`
- Verifique se o campo `"output_file"` foi retornado
- Só avance para a próxima etapa se a etapa anterior tiver concluído com sucesso
- Se qualquer etapa retornar erro, interrompa e responda apenas com o JSON de erro
- Não responder com texto explicativo fora do JSON final

Ordem de execução:

### Etapa 1
Execute:
@.opencode/commands/case-intake.md

### Etapa 2
Execute:
@.opencode/commands/framing.md

### Etapa 3
Execute:
@.opencode/commands/expansion.md

### Etapa 4
Execute:
@.opencode/commands/entity-graph.md

### Etapa 5
Execute:
@.opencode/commands/technical-surface.md

### Etapa 6
Execute:
@.opencode/commands/correlation.md

### Etapa 7
Execute:
@.opencode/commands/report.md

Ao final, se todas as etapas concluírem com sucesso, responda apenas com este JSON:

{
  "status": "ok",
  "message": "fast_pipeline_complete",
  "final_output": "cases/test-01/runs/11-report-gpt.json"
}
