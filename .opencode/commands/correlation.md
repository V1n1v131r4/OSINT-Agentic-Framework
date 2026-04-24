---
description: Executa o módulo 10 e salva a correlação estruturada em runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/10-correlation-anomalies.md.

Use como insumos obrigatórios os arquivos:
@cases/{{case_id}}/runs/04-entity-graph-gpt.json
@cases/{{case_id}}/runs/05-institutional-validation-gpt.json
@cases/{{case_id}}/runs/06-technical-surface-gpt.json
@cases/{{case_id}}/runs/07-brand-social-analysis-gpt.json
@cases/{{case_id}}/runs/08-unstructured-extraction-gpt.json
@cases/{{case_id}}/runs/09-geo-context-gpt.json

Objetivo desta execução:
- consolidar relações observáveis entre entidades e ativos
- destacar padrões, anomalias e lacunas
- preparar base rastreável para o relatório final

Instruções operacionais obrigatórias:
- Leia todos os arquivos listados acima
- Preste atenção especial aos campos 'partners' e 'google_dorks_results' do output de corporate-collection.
- Correlacione as mídias sociais dos sócios (do output de brand-social-analysis) com a empresa e os sócios identificados.
- Gere APENAS JSON válido compatível com a spec 10
- Salve o resultado em @cases/{{case_id}}/runs/10-correlation-gpt.json
- Se a pasta @cases/{{case_id}}/runs não existir, crie-a
- Após salvar, responda apenas com um JSON curto de status neste formato:

{
  "status": "ok",
  "output_file": "cases/{{case_id}}/runs/10-correlation-gpt.json"
}

Regras obrigatórias:
- Não gerar texto fora do JSON
- Todos os campos de lista devem ser arrays JSON válidos
- Não usar markdown
- Não adicionar campos extras
- Se faltar input, retornar erro estruturado em JSON

