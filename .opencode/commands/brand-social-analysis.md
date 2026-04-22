---
description: Executa o módulo 07 e salva a presença pública institucional em runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/07-brand-social-analysis.md.

Use como insumo obrigatório o arquivo:
@cases/test-01/runs/04-entity-graph-gpt.json

Objetivo desta execução:
- identificar canais públicos e perfis institucionais
- separar canais oficiais de candidatos não confirmados
- preparar sinais de presença pública para correlação

Instruções operacionais obrigatórias:
- Leia @cases/test-01/runs/04-entity-graph-gpt.json
- Gere APENAS JSON válido compatível com a spec 07
- Salve o resultado em @cases/test-01/runs/07-brand-social-analysis-gpt.json
- Se a pasta @cases/test-01/runs não existir, crie-a
- Após salvar, responda apenas com um JSON curto de status neste formato:

{
  "status": "ok",
  "output_file": "cases/test-01/runs/07-brand-social-analysis-gpt.json"
}

Regras obrigatórias:
- Não gerar texto fora do JSON
- Todos os campos de lista devem ser arrays JSON válidos
- Não usar markdown
- Não adicionar campos extras
- Se faltar input, retornar erro estruturado em JSON
