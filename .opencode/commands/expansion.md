---
description: Executa o módulo 03 e salva automaticamente o output em runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/03-surface-expansion.md.

Use como insumos obrigatórios os arquivos:
@cases/test-01/runs/02-framing-gpt.json
@cases/test-01/runs/04-corporate-collection-gpt.json

Objetivo desta execução:
- expandir a superfície pública institucional do alvo
- identificar ativos, canais e possíveis resíduos digitais úteis
- aproveitar sinais corporativos já coletados para priorizar ativos mais confiáveis

Instruções operacionais obrigatórias:
- Leia @cases/test-01/runs/02-framing-gpt.json
- Leia @cases/test-01/runs/04-corporate-collection-gpt.json
- Gere APENAS JSON válido compatível com a spec 03
- Salve o resultado em @cases/test-01/runs/03-surface-expansion-gpt.json
- Se a pasta @cases/test-01/runs não existir, crie-a
- Após salvar, responda apenas com um JSON curto de status neste formato:

{
  "status": "ok",
  "output_file": "cases/test-01/runs/03-surface-expansion-gpt.json"
}

Regras obrigatórias:
- Não gerar texto fora do JSON
- Todos os campos de lista devem ser arrays JSON válidos
- Não usar markdown
- Não adicionar campos extras
- Se faltar input, retornar erro estruturado em JSON
