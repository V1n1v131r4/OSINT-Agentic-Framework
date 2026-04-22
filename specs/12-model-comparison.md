# 12 — Model Comparison

## Objetivo
Comparar saídas de dois modelos no mesmo módulo ou no caso inteiro.

## Entradas obrigatórias
- gpt_output
- claude_output
- module_name
- rubric_reference

## Instruções ao agente
Compare estrutura, disciplina de evidência, utilidade e extrapolação. Ignore estilo como critério principal.

## Tarefas
1. Identificar fatos consensuais.
2. Identificar divergências analíticas.
3. Marcar inferências sem suporte.
4. Apontar qual saída foi melhor em clareza, disciplina e utilidade.
5. Recomendar adjudicação ao analista.

## Saída obrigatória
```json
{
  "consensus_facts": [],
  "divergent_points": [],
  "unsupported_inferences": [],
  "best_output_by_dimension": {
    "clarity": "",
    "evidence_discipline": "",
    "operational_usefulness": ""
  },
  "adjudication_recommendation": ""
}
```

## Critérios de qualidade
- não favorecer prolixidade
- privilegiar aderência à evidência
