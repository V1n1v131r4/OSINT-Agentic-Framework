---
description: Analisa a presença e comportamento social de indivíduos
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/07-individual-social-analysis.md.

Instruções operacionais:
1. Localize o arquivo `06-individual-footprint-gpt.json` e o `05-identity-validation-gpt.json` no diretório `runs` do caso atual.
2. Analise perfis, conexões e comportamento social.
3. Salve o resultado em `cases/<case-id>/runs/07-individual-social-analysis-gpt.json`.

Objetivo:
- Mapear o ecossistema social e vulnerabilidades do indivíduo.
- **Sugerir o próximo comando**: `/geo-context`.

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/07-individual-social-analysis-gpt.json",
  "next_command": "/geo-context"
}
```
