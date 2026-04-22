---
description: Executa o módulo 02 e salva automaticamente o output em runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/02-case-framing.md.

Use como entrada o arquivo:
@cases/test-01/runs/01-case-intake.json

Objetivo desta execução:
- transformar o case intake normalizado em framing analítico inicial

Instruções operacionais obrigatórias:
- Leia @cases/test-01/runs/01-case-intake.json
- Gere APENAS JSON válido compatível com a spec 02
- Salve o resultado em @cases/test-01/runs/02-framing-gpt.json
- Após salvar, responda apenas com um JSON curto de status neste formato:

{
  "status": "ok",
  "output_file": "cases/test-01/runs/02-framing-gpt.json"
}

Regras obrigatórias:
- Não gerar texto fora do JSON
- Todos os campos de lista devem ser arrays JSON válidos
- Não usar markdown
- Se faltar input, retornar erro estruturado em JSON
