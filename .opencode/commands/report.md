---
description: Executa o módulo 11 e salva automaticamente o relatório em runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/11-reporting.md.

Use como insumos obrigatórios os arquivos:
@cases/test-01/runs/01-case-intake.json
@cases/test-01/runs/10-correlation-gpt.json

Objetivo desta execução:
- transformar a correlação em um relatório curto, executivo e rastreável
- manter coerência com o objetivo analítico original
- preparar saída final para revisão

Instruções operacionais obrigatórias:
- Leia @cases/test-01/runs/01-case-intake.json
- Leia @cases/test-01/runs/10-correlation-gpt.json
- Gere APENAS JSON válido compatível com a spec 11
- Salve o resultado em @cases/test-01/runs/11-report-gpt.json
- Se a pasta @cases/test-01/runs não existir, crie-a
- Após salvar, responda apenas com um JSON curto de status neste formato:

{
  "status": "ok",
  "output_file": "cases/test-01/runs/11-report-gpt.json"
}

Regras obrigatórias:
- Não gerar texto fora do JSON
- Todos os campos de lista devem ser arrays JSON válidos
- Não usar markdown
- Não adicionar campos extras
- Se faltar input, retornar erro estruturado em JSON
