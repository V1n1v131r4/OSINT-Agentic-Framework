---
description: Executa o módulo 13 e salva automaticamente as lições aprendidas
agent: reviewer
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/13-postmortem-learning.md.

Use como insumos obrigatórios os arquivos:
@cases/test-01/runs/01-case-intake.json
@cases/test-01/runs/02-framing-gpt.json
@cases/test-01/runs/03-surface-expansion-gpt.json
@cases/test-01/runs/10-correlation-gpt.json
@cases/test-01/runs/11-report-gpt.json

Objetivo desta execução:
- revisar a qualidade metodológica do caso
- identificar falhas de spec, inconsistências e gargalos operacionais
- produzir lições aprendidas reutilizáveis

Instruções operacionais obrigatórias:
- Leia os arquivos listados acima
- Gere APENAS JSON válido compatível com a spec 13
- Salve o resultado em @cases/test-01/memory/13-postmortem.json
- Se a pasta @cases/test-01/memory não existir, crie-a
- Após salvar, responda apenas com um JSON curto de status neste formato:

{
  "status": "ok",
  "output_file": "cases/test-01/memory/13-postmortem.json"
}

Regras obrigatórias:
- Não gerar texto fora do JSON
- Todos os campos de lista devem ser arrays JSON válidos
- Não usar markdown
- Não adicionar campos extras
- Se faltar input, retornar erro estruturado em JSON
