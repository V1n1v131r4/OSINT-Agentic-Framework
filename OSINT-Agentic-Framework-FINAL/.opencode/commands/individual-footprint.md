---
description: Mapeia a pegada digital técnica de indivíduos
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/06-individual-digital-footprint.md.

Instruções operacionais:
1. Localize o arquivo `05-identity-validation-gpt.json` e o `04-individual-collection-gpt.json` no diretório `runs` do caso atual.
2. Mapeie e-mails, handles e ativos pessoais.
3. Salve o resultado em `cases/<case-id>/runs/06-individual-footprint-gpt.json`.

Objetivo:
- Consolidar a infraestrutura digital pessoal.
- **Sugerir o próximo comando**: `/individual-social-analysis`.

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/06-individual-footprint-gpt.json",
  "next_command": "/individual-social-analysis"
}
```
