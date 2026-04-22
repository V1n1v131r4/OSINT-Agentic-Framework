---
description: Executa o módulo 01 e salva automaticamente o output em runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/01-case-intake.md.

Use como entrada o arquivo:
@cases/test-01/intake.json

Objetivo desta execução:
- normalizar o intake bruto
- preparar o payload para o módulo 02

Instruções operacionais obrigatórias:
- Leia @cases/test-01/intake.json
- Gere APENAS JSON válido compatível com a spec 01
- Salve o resultado em @cases/test-01/runs/01-case-intake.json
- Se a pasta @cases/test-01/runs não existir, crie-a
- Após salvar, responda apenas com um JSON curto de status neste formato:

{
  "status": "ok",
  "output_file": "cases/test-01/runs/01-case-intake.json"
}

Regras obrigatórias:
- Não gerar texto fora do JSON
- Todos os campos de lista devem ser arrays JSON válidos
- Não usar markdown
- Se faltar input, retornar erro estruturado em JSON
