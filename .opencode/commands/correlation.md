---
description: Consolida correlações e sugere o próximo passo da pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Instruções operacionais:
1. Localize os arquivos de output anteriores no diretório `runs` do caso atual.
2. Selecione a spec de correlação baseada no `operation_type`:
   - `institutions`: `@specs/10-correlation-anomalies.md`
   - `individuals`: `@specs/10-correlation-indiv.md`
   - `disinformation_campaign` ou `narrative_analysis`: `@specs/10-correlation-narrative.md`
   - `data_leak`: `@specs/10-correlation-leak.md`
3. Consolide relações, padrões e anomalias conforme a spec selecionada.
4. Salve o resultado em `cases/<case-id>/runs/10-correlation-gpt.json`.

Objetivo:
- Gerar base rastreável e específica para o relatório.
- **Sugerir o próximo comando**: `/report`.

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/10-correlation-gpt.json",
  "next_command": "/report"
}
```
