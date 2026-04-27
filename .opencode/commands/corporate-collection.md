---
description: Coleta dados corporativos avançados e sugere o próximo passo da pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/04-corporate-collection.md.

Instruções operacionais:
1. Localize os arquivos `01-case-intake.json` e `02-framing-gpt.json` no diretório `runs` do caso atual.
2. Execute a coleta corporativa profunda conforme o fluxo obrigatório da spec.
3. Salve o resultado em `cases/<case-id>/runs/04-corporate-collection-gpt.json`.

Objetivo:
- Consolidar CNPJ, QSA, contatos e documentos.
- **Sugerir o próximo comando** (obrigatoriamente `/expansion`).

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/04-corporate-collection-gpt.json",
  "next_command": "/expansion"
}
```
