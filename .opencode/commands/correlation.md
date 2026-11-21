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
   - Para `narrative_analysis`, aplique também @specs/narrative-evidence.md. Antes de analisar, execute `python3 scripts/validate-narrative-evidence.py --collection-only -- "cases/<case-id>"` com o diretório real. Use `evidence_origins` para contar origens conhecidas distintas por achado.
   - Se a checagem falhar ou não puder ser executada, retorne um JSON com `status: error` e a mensagem do validador ou a causa da falha. Interrompa a etapa sem gravar o artefato ou sugerir outro comando.
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
