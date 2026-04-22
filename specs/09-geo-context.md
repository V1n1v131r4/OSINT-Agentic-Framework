# 09 — Geo Context

## Objetivo
Construir contexto geográfico comercial ou institucional sem entrar em rastreamento pessoal.

## Entradas obrigatórias
- named_entities
- supporting_signals
- target_summary

## Instruções ao agente
Use somente contexto geográfico empresarial, comercial ou institucional. Não faça inferência de rotina individual.

## Tarefas
1. Identificar ancoragens geográficas explícitas.
2. Distinguir sede, área de atuação e contexto de mercado.
3. Classificar confiança das referências geográficas.
4. Indicar como validar a geografia em fontes abertas empresariais.
5. Explicar o valor analítico do contexto geográfico para o caso.

## Saída obrigatória
```json
{
  "explicit_geographic_markers": [],
  "institutional_geography_assessment": "",
  "market_context_hypotheses": [],
  "safe_geo_validation_steps": [],
  "confidence": "low|medium|high"
}
```

## Critérios de qualidade
- sem rastreamento individual
- contexto geográfico deve servir ao objetivo do caso
