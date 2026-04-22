# 01 — Case Intake

## Objetivo
Normalizar o pedido bruto em um payload mínimo e consistente para os próximos módulos.

---

## Entradas obrigatórias
- case_id
- target_name
- target_url
- scope_type
- analysis_goal
- scope_modules
- restrictions

## Entradas opcionais
- corporate_identifiers.cnpj
- corporate_identifiers.legal_name
- corporate_identifiers.trade_name

Se qualquer entrada obrigatória estiver ausente ou inválida, NÃO prossiga.

---

## Instruções ao agente
- Não analisar o alvo
- Não enriquecer com fontes externas
- Apenas normalizar e preparar handoff
- Não inventar dados ausentes
- Não inferir além do input
- Tratar `corporate_identifiers` como contexto corporativo, não como prova validada

---

## Tarefas

1. Normalizar o alvo em estrutura padronizada (`normalized_target`)
2. Reescrever o objetivo em linguagem operacional (`analysis_goal_normalized`)
3. Preservar integralmente os módulos de escopo (`scope_modules`)
4. Preservar integralmente as restrições
5. Preservar identificadores corporativos fornecidos, sem validá-los
6. Identificar informações faltantes úteis para continuidade
7. Produzir um handoff mínimo e objetivo para o módulo 02

---

## Saída obrigatória

Retorne **APENAS JSON válido**, sem texto adicional.

```json
{
  "case_id": "",
  "normalized_target": {
    "name": "",
    "url": "",
    "scope_type": ""
  },
  "analysis_goal_normalized": "",
  "scope_modules": [],
  "corporate_identifiers": {
    "cnpj": "",
    "legal_name": "",
    "trade_name": ""
  },
  "restrictions": [],
  "missing_information": [],
  "handoff_summary": ""
}
