---
description: Estrutura o grafo de entidades e sugere o próximo passo da pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/04-entity-graph.md.

Instruções operacionais:
1. Localize o arquivo `03-surface-expansion-gpt.json` e o arquivo de coleta correspondente (`04-corporate-collection-gpt.json` ou `04-individual-collection-gpt.json`) no diretório `runs` do caso atual.
2. Identifique e normalize entidades (pessoas, documentos, repositórios, empresas).
3. Salve o resultado em `cases/<case-id>/runs/04-entity-graph-gpt.json`.

Objetivo:
- Estruturar o grafo de relações.
- **Sugerir o próximo comando** baseado no `operation_type`:
  - `institutions`: `/institutional-validation`
  - `individuals`: `/identity-validation`
  - Outros: `/technical-surface` ou `/brand-social-analysis` (conforme relevância)

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/04-entity-graph-gpt.json",
  "next_command": "/<comando-sugerido>"
}
```
