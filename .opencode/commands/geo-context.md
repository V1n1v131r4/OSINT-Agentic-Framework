---
description: Analisa o contexto geográfico e sugere o próximo passo da pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/09-geo-context.md.

Instruções operacionais:
1. Localize os arquivos de análise anteriores (`07-individual-social-analysis-gpt.json`, `08-unstructured-extraction-gpt.json` ou `04-entity-graph-gpt.json`) no diretório `runs` do caso atual.
2. Identifique e correlacione sinais geográficos.
3. Salve o resultado em `cases/<case-id>/runs/09-geo-context-gpt.json`.

Objetivo:
- Mapear localização física e regional.
- **Sugerir o próximo comando** (geralmente `/correlation`).

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/09-geo-context-gpt.json",
  "next_command": "/correlation"
}
```

