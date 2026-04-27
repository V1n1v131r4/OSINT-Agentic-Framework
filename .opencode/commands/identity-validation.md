---
description: Valida a identidade de indivíduos e sugere o próximo passo
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/05-identity-validation.md.

Instruções operacionais:
1. Localize o arquivo `04-individual-collection-gpt.json` e o `04-entity-graph-gpt.json` no diretório `runs` do caso atual.
2. Valide a consistência da identidade e vínculos.
3. Salve o resultado em `cases/<case-id>/runs/05-identity-validation-gpt.json`.

Objetivo:
- Confirmar identidade e reduzir ruído de homônimos.
- **Sugerir o próximo comando**: `/individual-footprint`.

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/05-identity-validation-gpt.json",
  "next_command": "/individual-footprint"
}
```
