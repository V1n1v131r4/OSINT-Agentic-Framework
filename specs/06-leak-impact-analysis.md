# 06 — Leak Impact Analysis

## Objetivo

Analisar a extensão e o impacto real de um vazamento de dados, focando na sensibilidade das informações e nos riscos para a entidade e indivíduos afetados.

---

## Entradas obrigatórias

- leak_collection_output
- expansion_output

---

## Tarefas

1. **Classificação de Dados**: Categorizar os tipos de PII (nomes, e-mails, senhas, documentos, dados financeiros).
2. **Avaliação de Volume**: Estimar a quantidade de registros únicos expostos.
3. **Análise de Recência**: Verificar se os dados são atuais ou de vazamentos antigos (rehash).
4. **Identificação de Riscos**: Listar riscos imediatos (phishing, personificação, fraude financeira).
5. **Correlação de Atribuição**: Tentar ligar o vazamento a grupos de ameaça ou vetores de ataque conhecidos.

---

## Saída obrigatória

```json
{
  "data_sensitivity_score": "low | medium | high | critical",
  "exposed_data_categories": [],
  "estimated_record_count": 0,
  "risk_assessment": [],
  "attribution_hypotheses": [],
  "confidence": "low | medium | high"
}
```
