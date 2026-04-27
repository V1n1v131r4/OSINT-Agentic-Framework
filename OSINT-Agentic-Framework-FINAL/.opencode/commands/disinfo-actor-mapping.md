---
description: Mapeia atores e redes de desinformação
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/07-disinfo-actor-mapping.md.

Instruções operacionais:
1. Localize o arquivo `06-content-analysis-gpt.json` e o `04-disinfo-collection-gpt.json` no diretório `runs` do caso atual.
2. Mapeie a rede de atores e identifique sinais de inautenticidade.
3. Salve o resultado em `cases/<case-id>/runs/07-disinfo-actor-mapping-gpt.json`.

Objetivo:
- Identificar a estrutura humana e técnica por trás da campanha.
- **Sugerir o próximo comando**: `/correlation`.

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/07-disinfo-actor-mapping-gpt.json",
  "next_command": "/correlation"
}
```
