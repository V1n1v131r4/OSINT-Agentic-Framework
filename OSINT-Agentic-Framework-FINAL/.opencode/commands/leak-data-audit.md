---
description: Realiza auditoria técnica de dados vazados
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/07-leak-data-audit.md.

Instruções operacionais:
1. Localize o arquivo `06-leak-impact-analysis-gpt.json` e o `04-leak-collection-gpt.json` no diretório `runs` do caso atual.
2. Realize a auditoria técnica das amostras e estrutura dos dados.
3. Salve o resultado em `cases/<case-id>/runs/07-leak-data-audit-gpt.json`.

Objetivo:
- Identificar a profundidade técnica e origem do vazamento.
- **Sugerir o próximo comando**: `/unstructured-extraction`.

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/07-leak-data-audit-gpt.json",
  "next_command": "/unstructured-extraction"
}
```
