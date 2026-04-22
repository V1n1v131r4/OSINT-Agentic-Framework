# 04 — Entity Graph

## Objetivo
Organizar entidades e relações em um grafo investigativo mínimo e útil.

## Entradas obrigatórias
- primary_assets
- secondary_assets
- public_channels
- residual_or_legacy_assets

## Instruções ao agente
Monte um grafo institucional. Não invente relações. Só represente conexões suportadas ou explicitamente hipotéticas.

## Tarefas
1. Listar entidades principais.
2. Listar entidades secundárias.
3. Mapear relações diretas.
4. Mapear relações indiretas plausíveis, marcadas como hipótese.
5. Sugerir quais nós merecem validação prioritária.

## Saída obrigatória
```json
{
  "main_entities": [],
  "secondary_entities": [],
  "direct_relationships": [],
  "indirect_relationships_hypotheses": [],
  "priority_nodes_for_validation": [],
  "graph_summary": ""
}
```

## Critérios de qualidade
- diferenciar relação observada e relação inferida
- manter o grafo pequeno e operacional
