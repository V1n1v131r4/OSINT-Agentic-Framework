# 02 — Case Framing (Vazamento de Dados)

## Objetivo

Estruturar a investigação de um vazamento de dados, focando em extensão, sensibilidade e origem.

---

## Entradas obrigatórias

- target_name (base de dados ou entidade afetada)
- analysis_goal
- operation_type (deve ser "data_leak")

---

## Tarefas

1. **Avaliar a sensibilidade dos dados**: Que tipo de PII (Personally Identifiable Information) foi exposto?
2. **Mapear a origem provável**: De onde os dados foram extraídos?
3. **Identificar riscos imediatos**: Possibilidade de fraude, extorsão ou danos reputacionais.

---

## Saída esperada

```json
{
  "leak_assessment": "",
  "data_types_exposed": [],
  "investigation_vectors": [
    "source_verification",
    "impact_analysis",
    "leak_correlation"
  ],
  "known_gaps": []
}
```
