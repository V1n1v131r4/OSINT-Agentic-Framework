---
description: Mapeia o ecossistema de influência e narrativas
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/07-narrative-ecosystem-map.md.

Instruções operacionais:
1. Localize o arquivo `06-content-analysis-gpt.json` e o `04-narrative-collection-gpt.json` no diretório `runs` do caso atual.
2. Mapeie os nós de influência e o fluxo de informação.
3. Salve o resultado em `cases/<case-id>/runs/07-narrative-ecosystem-map-gpt.json`.

Objetivo:
- Visualizar a estrutura de influência e alcance da narrativa.
- **Sugerir o próximo comando**: `/correlation`.

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/07-narrative-ecosystem-map-gpt.json",
  "next_command": "/correlation"
}
```
