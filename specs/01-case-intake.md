# 01 — Case Intake

## Objetivo

Registrar de forma estruturada o contexto inicial do caso, garantindo clareza sobre:

- alvo da análise
- objetivo da investigação
- escopo permitido
- restrições operacionais

---

## Entradas obrigatórias

- target (empresa, domínio ou entidade institucional)
- analysis_goal
- scope_definition

---

## Entradas opcionais

- known_data
- constraints
- priority_questions

Se entradas obrigatórias estiverem ausentes ou ambíguas, NÃO prossiga.

---

## Instruções ao agente

- Não iniciar coleta
- Não gerar hipóteses
- Não interpretar dados

Este módulo é apenas estrutural.

---

## Saída esperada

```json
{
  "target": "",
  "analysis_goal": "",
  "scope_definition": "",
  "known_data": [],
  "constraints": [],
  "priority_questions": []
}
