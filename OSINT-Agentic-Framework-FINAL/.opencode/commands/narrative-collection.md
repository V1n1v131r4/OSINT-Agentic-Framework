---
description: Coleta de dados sobre ecossistemas de narrativas
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/04-narrative-collection.md.

Instruções operacionais:
1. Leia o `01-case-intake.json` e o `02-framing-gpt.json` do caso atual.
2. Execute a coleta focada em atores e influência.
3. Salve em `cases/<case-id>/runs/04-narrative-collection-gpt.json`.

Regras de Saída:
- Sugira o próximo comando: `/expansion`.

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/04-narrative-collection-gpt.json",
  "next_command": "/expansion"
}
```
