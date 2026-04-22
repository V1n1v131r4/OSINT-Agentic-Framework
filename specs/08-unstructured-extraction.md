# 08 — Unstructured Extraction

## Objetivo
Extrair entidades, temas, pistas e contexto de conteúdo não estruturado.

## Entradas obrigatórias
- pages_or_documents_text
- target_summary

## Instruções ao agente
Converta texto promocional ou descritivo em sinais estruturados. Não reescreva a página; extraia valor analítico.

## Tarefas
1. Extrair entidades nomeadas.
2. Identificar temas recorrentes.
3. Localizar categorias de serviço, produto ou atuação.
4. Identificar pistas úteis para pivot empresarial.
5. Resumir o que o texto revela sobre o posicionamento operacional.

## Saída obrigatória
```json
{
  "named_entities": [],
  "recurring_themes": [],
  "service_or_operation_categories": [],
  "business_pivot_clues": [],
  "operational_positioning_summary": ""
}
```

## Critérios de qualidade
- extrair, não ornamentar
- limitar a 10 entidades e 10 temas
