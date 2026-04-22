# 11 — Reporting

## Objetivo
Transformar os achados em um relatório curto, executivo, acionável e rastreável.

---

## Entradas obrigatórias

- strong_convergences
- identified_anomalies
- operational_risks
- maturity_only_issues
- cosmetic_issues
- requires_additional_validation
- integrated_assessment
- confidence
- analysis_goal_normalized

Se qualquer entrada estiver ausente ou inválida, NÃO prossiga.

---

## Instruções ao agente

- Escrever para analista ou decisor
- Não dramatizar
- Não incluir nada fora dos inputs
- Não enriquecer com conhecimento externo
- Não investigar pessoas físicas
- Priorizar utilidade operacional
- Ser direto, denso e objetivo

---

## Tarefas

1. Produzir um sumário executivo claro e direto
2. Destacar os principais achados relevantes
3. Classificar risco de forma conservadora
4. Sugerir próximos passos seguros e proporcionais
5. Registrar limitações da análise

---

## Saída obrigatória

Retorne **APENAS JSON válido**, sem texto adicional.

```json
{
  "executive_summary": "",
  "key_findings": [],
  "risk_assessment": "",
  "recommended_safe_next_steps": [],
  "limitations": [],
  "confidence": "low|medium|high"
}
