---
description: Executa o módulo 09 e salva o contexto geográfico em runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/09-geo-context.md.

Use como insumos obrigatórios os arquivos:
@cases/test-01/runs/08-unstructured-extraction-gpt.json
@cases/test-01/runs/04-entity-graph-gpt.json

Objetivo desta execução:
- consolidar sinais geográficos observáveis do alvo
- estruturar localizações e sinais regionais sem inferência indevida
- preparar contexto geográfico para correlação final

Instruções operacionais obrigatórias:
- Leia @cases/test-01/runs/08-unstructured-extraction-gpt.json
- Leia @cases/test-01/runs/04-entity-graph-gpt.json
- Gere APENAS JSON válido compatível com a spec 09
- Salve o resultado em @cases/test-01/runs/09-geo-context-gpt.json
- Se a pasta @cases/test-01/runs não existir, crie-a
- Após salvar, responda apenas com um JSON curto de status neste formato:

{
  "status": "ok",
  "output_file": "cases/test-01/runs/09-geo-context-gpt.json"
}

Regras obrigatórias:
- Não gerar texto fora do JSON
- Todos os campos de lista devem ser arrays JSON válidos
- Não usar markdown
- Não adicionar campos extras
- Se faltar input, retornar erro estruturado em JSON
