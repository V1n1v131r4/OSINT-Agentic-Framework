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
4. **Consolide o aprendizado na memória global** (loop de aprendizado automático):
   - Leia o `operation_type` do caso em `cases/<case-id>/runs/01-case-intake.json`.
   - Leia (ou crie) `memory/global/playbooks.json`.
   - Funda os `reusable_patterns`/`memory_objects` deste caso na memória global seguindo
     estritamente as "Regras de consolidação" da spec @specs/13-postmortem-learning.md:
     segmentar por `operation_type`, deduplicar por `(id, operation_type)`, **reforçar**
     (incrementar `reinforcement_count` apenas se o `case_id` ainda não estiver em
     `source_cases` — idempotência), recalcular `confidence_tier`.
   - Salve de volta em `memory/global/playbooks.json`.

Objetivo:
- Melhoria contínua do framework e do operador.
- Fechar o loop: quanto mais casos, mais especialista o framework fica (via reforço de pivôs).

Regras de Saída:
- Retorne APENAS o JSON de status:

```json
{
  "status": "ok",
  "output_file": "cases/<case-id>/memory/13-postmortem.json",
  "global_memory_file": "memory/global/playbooks.json",
  "message": "Operação finalizada. Lições aprendidas registradas e consolidadas na memória global."
}
```
