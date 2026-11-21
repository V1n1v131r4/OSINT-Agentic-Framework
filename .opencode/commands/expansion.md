---
description: Expande a superfície pública e sugere o próximo passo da pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/03-surface-expansion.md.

Instruções operacionais:
1. Identifique o diretório do caso atual e execute, a partir da raiz do projeto, `python3 scripts/validate-expansion-inputs.py -- "cases/<case-id>"` com o caminho real do caso. Execute o script antes de analisar os artefatos. Prossiga somente se sair com código zero e `status: ok`. Use os arquivos listados em `inputs`.
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
- Se a validação falhar, devolva o JSON de erro do script. Se não puder executá-lo, devolva `{"status":"error","message":"Não foi possível executar o validador da expansão."}`. Em ambos os casos, interrompa a etapa sem gerar artefato ou sugerir próximo comando.

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/03-surface-expansion-gpt.json",
  "next_command": "/<comando-sugerido>"
}
```
