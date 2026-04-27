---
description: Analisa a superfície técnica e sugere o próximo passo da pipeline
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/06-technical-surface.md.

Instruções operacionais:
1. Localize o arquivo `03-surface-expansion-gpt.json` no diretório `runs` do caso atual.
2. Analise ativos técnicos (DNS, IPs, subdomínios).
3. Salve o resultado em `cases/<case-id>/runs/06-technical-surface-gpt.json`.

Objetivo:
- Mapear infraestrutura digital.
- **Sugerir o próximo comando** baseado no `operation_type`:
  - `data_leak`: `/unstructured-extraction` (foco em conteúdo vazado)
  - Outros: `/brand-social-analysis`

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/runs/06-technical-surface-gpt.json",
  "next_command": "/<comando-sugerido>"
}
```
