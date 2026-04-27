---
description: Expansão de superfície com Claude (suporta múltiplos propósitos)
agent: collector-claude
model: anthropic/claude-sonnet-4-5
---

Siga a spec `@specs/03-surface-expansion.md`.

Instruções operacionais:
1. Localize o arquivo `02-framing-claude.json` (ou `02-framing-gpt.json`) e o arquivo de coleta correspondente no diretório `runs` do caso atual.
2. Execute a expansão de superfície baseada nos dados coletados.
3. Salve o resultado em `cases/<case-id>/runs/03-surface-expansion-claude.json`.

Objetivo:
- Identificar ativos e canais.
- **Sugerir o próximo comando** baseado no `operation_type` (conforme lógica do comando `/expansion` padrão).

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/03-surface-expansion-claude.json",
  "next_command": "/<comando-sugerido>"
}
```
