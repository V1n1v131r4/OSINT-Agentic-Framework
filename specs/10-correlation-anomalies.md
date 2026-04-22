# 10 — Correlation and Anomalies

## Objetivo
Correlacionar os achados dos módulos anteriores para identificar convergências, inconsistências e sinais relevantes com utilidade analítica.

---

## Entradas obrigatórias
- target_summary
- investigation_vectors
- primary_assets
- secondary_assets
- public_channels
- residual_or_legacy_assets
- weak_signals
- known_gaps

Se qualquer entrada estiver ausente ou inválida, NÃO prossiga.

## Entradas opcionais
- corporate_identity
- official_channels
- corporate_registry_signals
- public_litigation_signals

---

## Instruções ao agente

- Correlacionar apenas dados provenientes das entradas
- Não inferir além do que está disponível
- Não enriquecer com conhecimento externo
- Não investigar pessoas físicas
- Separar claramente:
  - convergência real
  - inconsistência
  - limitação de evidência
  - problema cosmético

---

## Tarefas

1. Identificar convergências fortes entre ativos e sinais
2. Identificar inconsistências ou anomalias
3. Classificar anomalias em:
   - operacionais (potencial impacto real)
   - maturidade digital (baixo impacto)
   - cosméticas (irrelevantes)
4. Identificar o que realmente exige validação adicional
5. Produzir uma leitura integrada, conservadora e acionável

---

## Saída obrigatória

Retorne **APENAS JSON válido**, sem texto adicional.

```json
{
  "strong_convergences": [],
  "identified_anomalies": [],
  "operational_risks": [],
  "maturity_only_issues": [],
  "cosmetic_issues": [],
  "requires_additional_validation": [],
  "integrated_assessment": "",
  "confidence": "low|medium|high"
}
