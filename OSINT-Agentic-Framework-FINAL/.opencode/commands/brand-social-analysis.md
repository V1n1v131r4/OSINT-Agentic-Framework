---
description: Analisa presença em redes sociais e sugere o próximo passo da pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/07-brand-social-analysis.md.

Instruções operacionais:
1. Localize os arquivos `04-entity-graph-gpt.json` e `04-corporate-collection-gpt.json` no diretório `runs` do caso atual.
2. Identifique canais oficiais e perfis de sócios relacionados.
3. Salve o resultado em `cases/<case-id>/runs/07-brand-social-analysis-gpt.json`.

Objetivo:
- Mapear presença digital e perfis de atores.
- **Sugerir o próximo comando** baseado no `operation_type`:
  - `disinformation_campaign`: `/correlation` (pula extração genérica se o foco for rede)
  - `narrative_analysis`: `/correlation`
  - Outros: `/unstructured-extraction`

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/07-brand-social-analysis-gpt.json",
  "next_command": "/<comando-sugerido>"
}
```
