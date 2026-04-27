---
description: Analisa conteúdo e narrativas para desinformação e influência
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/06-content-analysis.md.

Instruções operacionais:
1. Localize os arquivos de coleta (`04-disinfo-collection-gpt.json` ou `04-narrative-collection-gpt.json`) e o `03-surface-expansion-gpt.json` no diretório `runs` do caso atual.
2. Analise padrões de conteúdo, sentimento e sinais de coordenação.
3. Salve o resultado em `cases/<case-id>/runs/06-content-analysis-gpt.json`.

Objetivo:
- Decompor a narrativa e identificar inautenticidade.
- **Sugerir o próximo comando** baseado no `operation_type`:
  - `disinformation_campaign`: `/disinfo-actor-mapping`
  - `narrative_analysis`: `/narrative-ecosystem-map`

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/06-content-analysis-gpt.json",
  "next_command": "/<comando-sugerido>"
}
```
