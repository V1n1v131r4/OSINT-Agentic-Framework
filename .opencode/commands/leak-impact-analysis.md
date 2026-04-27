---
description: Analisa o impacto e sensibilidade de vazamentos de dados
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/06-leak-impact-analysis.md.

Instruções operacionais:
1. Localize o arquivo `04-leak-collection-gpt.json` e o `03-surface-expansion-gpt.json` no diretório `runs` do caso atual.
2. Avalie a sensibilidade, volume e riscos do vazamento.
3. Salve o resultado em `cases/<case-id>/runs/06-leak-impact-analysis-gpt.json`.

Objetivo:
- Dimensionar o dano e a veracidade do vazamento.
- **Sugerir o próximo comando**: `/leak-data-audit`.

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/06-leak-impact-analysis-gpt.json",
  "next_command": "/leak-data-audit"
}
```
