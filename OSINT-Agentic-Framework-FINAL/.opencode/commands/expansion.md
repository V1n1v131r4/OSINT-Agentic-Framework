---
description: Expande a superfície pública e sugere o próximo passo da pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/03-surface-expansion.md.

Instruções operacionais:
1. Localize o arquivo `02-framing-gpt.json` e o arquivo de coleta correspondente (`04-corporate-collection-gpt.json`, `04-individual-collection-gpt.json`, `04-disinfo-collection-gpt.json`, etc.) no diretório `runs` do caso atual.
2. Execute a expansão de superfície baseada nos dados coletados.
3. Salve o resultado em `cases/<case-id>/runs/03-surface-expansion-gpt.json`.

Objetivo:
- Identificar ativos e canais.
- **Sugerir o próximo comando** baseado no `operation_type`:
  - `institutions`: `/entity-graph`
  - `individuals`: `/entity-graph` (seguido de identity-validation)
  - `disinformation_campaign`: `/content-analysis`
  - `narrative_analysis`: `/content-analysis`
  - `data_leak`: `/leak-impact-analysis`

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/03-surface-expansion-gpt.json",
  "next_command": "/<comando-sugerido>"
}
```
