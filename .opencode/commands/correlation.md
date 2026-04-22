---
description: Executa o módulo 10 e salva automaticamente o output em runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/10-correlation-anomalies.md.

Use como insumos obrigatórios os arquivos:
@cases/test-01/runs/02-framing-gpt.json
@cases/test-01/runs/03-surface-expansion-gpt.json

Objetivo desta execução:
- correlacionar os achados do framing e da expansão
- identificar convergências, anomalias e limites de evidência
- produzir uma leitura integrada para o relatório

Instruções operacionais obrigatórias:
- Leia @cases/test-01/runs/02-framing-gpt.json
- Leia @cases/test-01/runs/03-surface-expansion-gpt.json
- Gere APENAS JSON válido compatível com a spec 10
- Salve o resultado em @cases/test-01/runs/10-correlation-gpt.json
- Se a pasta @cases/test-01/runs não existir, crie-a
- Após salvar, responda apenas com um JSON curto de status neste formato:

{
  "status": "ok",
  "output_file": "cases/test-01/runs/10-correlation-gpt.json"
}

Regras obrigatórias:
- Não gerar texto fora do JSON
- Todos os campos de lista devem ser arrays JSON válidos
- Não usar markdown
- Não adicionar campos extras
- Se faltar input, retornar erro estruturado em JSON
