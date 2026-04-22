---
description: Executa o módulo 08 e salva extrações estruturadas de conteúdo textual em runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/08-unstructured-extraction.md.

Use como insumos obrigatórios os arquivos:
@cases/test-01/runs/03-surface-expansion-gpt.json
@cases/test-01/runs/07-brand-social-analysis-gpt.json

Objetivo desta execução:
- extrair dados relevantes de conteúdo não estruturado já coletado
- normalizar e deduplicar e-mails, telefones, endereços e nomes
- preparar dados estruturados para contexto geográfico e correlação

Instruções operacionais obrigatórias:
- Leia @cases/test-01/runs/03-surface-expansion-gpt.json
- Leia @cases/test-01/runs/07-brand-social-analysis-gpt.json
- Gere APENAS JSON válido compatível com a spec 08
- Salve o resultado em @cases/test-01/runs/08-unstructured-extraction-gpt.json
- Se a pasta @cases/test-01/runs não existir, crie-a
- Após salvar, responda apenas com um JSON curto de status neste formato:

{
  "status": "ok",
  "output_file": "cases/test-01/runs/08-unstructured-extraction-gpt.json"
}

Regras obrigatórias:
- Não gerar texto fora do JSON
- Todos os campos de lista devem ser arrays JSON válidos
- Não usar markdown
- Não adicionar campos extras
- Se faltar input, retornar erro estruturado em JSON
