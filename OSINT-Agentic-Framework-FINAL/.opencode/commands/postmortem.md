---
description: Executa a revisão metodológica e salva lições aprendidas
agent: reviewer
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/13-postmortem-learning.md.

Instruções operacionais:
1. Localize os arquivos de output da pipeline no diretório `runs` do caso atual.
2. Revise a qualidade metodológica e identifique lições aprendidas.
3. Salve o resultado em `cases/<case-id>/memory/13-postmortem.json`.

Objetivo:
- Melhoria contínua do framework e do operador.

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/memory/13-postmortem.json",
  "message": "Operação finalizada. Lições aprendidas registradas na memória do caso."
}
```
