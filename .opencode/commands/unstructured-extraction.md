---
description: Extrai dados não estruturados e sugere o próximo passo da pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/08-unstructured-extraction.md.

Instruções operacionais:
1. Localize os arquivos de análise anteriores (`03-surface-expansion-gpt.json` e o módulo de análise social correspondente: `07-brand-social-analysis-gpt.json`, `07-individual-social-analysis-gpt.json`, `07-disinfo-actor-mapping-gpt.json`, `07-narrative-ecosystem-map-gpt.json` ou `07-leak-data-audit-gpt.json`) no diretório `runs` do caso atual.
2. Extraia informações de fontes não estruturadas conforme a spec.
3. Salve o resultado em `cases/<case-id>/runs/08-unstructured-extraction-gpt.json`.

Objetivo:
- Capturar sinais qualitativos.
- **Sugerir o próximo comando** baseado no `operation_type`:
  - `institutions`: `/geo-context`
  - `individuals`: `/geo-context`
  - `data_leak`: `/correlation` (pula geo-context se não houver sinais físicos)
  - Outros: `/correlation`

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/08-unstructured-extraction-gpt.json",
  "next_command": "/<comando-sugerido>"
}
```

