---
description: Gera o relatório final e sugere o próximo passo da pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/11-reporting.md.

Instruções operacionais:
1. Localize os arquivos `01-case-intake.json` e `10-correlation-gpt.json` no diretório `runs` do caso atual.
   - Para `narrative_analysis`, execute primeiro `python3 scripts/validate-narrative-evidence.py -- "cases/<case-id>"` com o diretório real. Prossiga somente com código zero e `status: ok`. Se falhar ou não puder ser executado, retorne um JSON com `status: error` e a mensagem ou causa e interrompa sem gerar relatório ou sugerir outro comando.
   - Para esse tipo de operação, aplique @specs/narrative-evidence.md ao preencher `key_findings` e `hypotheses`.
2. Gere o relatório executivo baseado nos achados e correlações, adaptando o tom e o foco ao `operation_type`.
3. Salve o resultado em `cases/<case-id>/runs/11-report-gpt.json`.

Objetivo:
- Produzir síntese executiva rastreável e específica para o propósito da operação.
- **Sugerir o próximo comando**: `/postmortem`.

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/11-report-gpt.json",
  "next_command": "/postmortem"
}
```
