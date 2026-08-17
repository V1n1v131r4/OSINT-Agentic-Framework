# 13 — Postmortem Learning

## Objetivo
Converter o caso em memória operacional reutilizável.

## Entradas obrigatórias
- final_report
- adjudication_recommendation
- analyst_feedback
- module_outputs

## Instruções ao agente
Extraia padrões úteis, erros e ajustes de método. Não reescreva o caso; produza aprendizado operacional.

## Tarefas
1. Registrar erros detectados no processo.
2. Registrar padrões úteis reaproveitáveis.
3. Registrar comportamentos distintos de cada modelo.
4. Sugerir ajustes em specs ou schemas.
5. Produzir objetos de memória claros e curtos.
6. **Consolidar o aprendizado na memória global** (ver seção "Loop de Aprendizado" abaixo).

## Saída obrigatória
```json
{
  "errors_detected": [],
  "reusable_patterns": [],
  "model_behavior_notes": {
    "gpt": [],
    "claude": []
  },
  "spec_adjustments": [],
  "memory_objects": []
}
```

## Critérios de qualidade
- priorizar padrões realmente reutilizáveis
- evitar lições vagas

---

## Loop de Aprendizado (Consolidação Automática)

Esta etapa é a **última de todas as 5 pipelines**. Além de salvar o postmortem do caso, ela
**fecha o loop de aprendizado do framework** consolidando os padrões reutilizáveis em uma
**memória global** que será reinjetada em casos futuros pelo `case-intake` (spec 01).

Nenhum comando adicional é executado pelo operador — esta consolidação ocorre **na mesma
execução** do postmortem, automaticamente.

### Fonte
- Os `reusable_patterns` e `memory_objects` que você acabou de produzir para este caso.
- O `operation_type` do caso (leia de `cases/<case-id>/runs/01-case-intake.json`).

### Alvo
- Arquivo: `memory/global/playbooks.json` (schema: `schemas/playbook-memory.schema.json`).
- Se o arquivo não existir, crie-o com `{ "version": 1, "playbooks": [] }`.

### Regras de consolidação
1. **Segmentação por operation_type.** Cada playbook é carimbado com o `operation_type` do caso.
   Pivôs genuinamente transversais (ex.: checklist de pivôs passivos) podem usar
   `operation_type: "all"`. Nunca misture aprendizado de tipos diferentes no mesmo balde.
2. **Deduplicação por (id, operation_type).** Gere um `id` slug (kebab-case) estável a partir da
   essência do pivô. Se já existir um playbook com o mesmo `id` **e** o mesmo `operation_type`,
   trate como o mesmo pivô — **não crie um duplicado**.
3. **Reforço (é o que torna o agente mais especialista).** Ao encontrar um pivô já existente:
   - Se o `case_id` atual **ainda não** estiver em `source_cases`: adicione-o, incremente
     `reinforcement_count` em 1 e atualize `last_seen_case`.
   - Se o `case_id` **já** estiver em `source_cases`: não altere a contagem (garante
     **idempotência** — rodar o postmortem do mesmo caso duas vezes não infla o número).
4. **Novos pivôs.** Se o pivô não existir no balde, adicione com `reinforcement_count: 1`,
   `first_seen_case` e `last_seen_case` iguais ao `case_id`, e `source_cases: [case_id]`.
5. **confidence_tier** derivado de `reinforcement_count`: `1` → `baixa`; `2-3` → `media`;
   `4+` → `alta`.
6. Atualize `updated_by_case` com o `case_id` atual.

### Critérios
- Só promova a playbook aquilo que é **realmente reutilizável** em casos futuros do mesmo tipo.
- Prefira poucos pivôs de alto valor a muitos genéricos.

### Próximo passo
- O loop está fechado. `next_command` do postmortem é vazio (fim do caso).
