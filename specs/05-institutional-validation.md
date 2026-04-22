# 05 — Institutional Validation

## Objetivo
Determinar se os ativos e sinais coletados parecem pertencer à mesma organização.

## Entradas obrigatórias
- main_entities
- direct_relationships
- target_summary
- public_channels
- expansion_notes

## Instruções ao agente
Valide coerência institucional. Não conclua fraude, risco ou legitimidade além do que os sinais suportam.

## Tarefas
1. Avaliar consistência entre nome, setor, posicionamento e canais.
2. Apontar inconsistências institucionais.
3. Classificar nível de confiança.
4. Dizer o que falta para confirmação mais robusta.
5. Separar problemas de identidade de problemas de maturidade digital.

## Saída obrigatória
```json
{
  "same_organization_assessment": "likely|uncertain|unlikely",
  "supporting_signals": [],
  "institutional_inconsistencies": [],
  "digital_maturity_inconsistencies": [],
  "missing_for_stronger_validation": [],
  "confidence": "low|medium|high"
}
```

## Critérios de qualidade
- não confundir site fraco com entidade falsa
- usar linguagem conservadora
