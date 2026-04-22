---
description: Executa o módulo 04 e salva o grafo básico de entidades em runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/04-entity-graph.md.

Use como insumo obrigatório o arquivo:
@cases/test-01/runs/03-surface-expansion-gpt.json

Objetivo desta execução:
- identificar entidades institucionais relevantes
- estruturar entidades observáveis para validação e correlação
- preparar saída reutilizável para os módulos seguintes

Instruções operacionais obrigatórias:
- Leia @cases/test-01/runs/03-surface-expansion-gpt.json
- Gere APENAS JSON válido compatível com a spec 04
- Salve o resultado em @cases/test-01/runs/04-entity-graph-gpt.json
- Se a pasta @cases/test-01/runs não existir, crie-a
- Após salvar, responda apenas com um JSON curto de status neste formato:

{
  "status": "ok",
  "output_file": "cases/test-01/runs/04-entity-graph-gpt.json"
}

Regras obrigatórias:
- Não gerar texto fora do JSON
- Todos os campos de lista devem ser arrays JSON válidos
- Não usar markdown
- Não adicionar campos extras
- Se faltar input, retornar erro estruturado em JSON
