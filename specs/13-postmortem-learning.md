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
