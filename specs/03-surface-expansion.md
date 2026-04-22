# 03 — Surface Expansion

## Objetivo
Expandir a superfície pública institucional do alvo a partir do seed inicial, mantendo relevância, coerência e utilidade analítica.

---

## Entradas obrigatórias
- target_summary
- investigation_vectors
- known_gaps

Se qualquer entrada estiver ausente ou inválida, NÃO prossiga.

## Entradas opcionais
- corporate_identity
- official_channels
- corporate_registry_signals
- public_litigation_signals


---

## Instruções ao agente

- Quando houver artefato de corporate collection, usá-lo para priorizar ativos e canais confirmados
- Expandir apenas ativos institucionais e públicos
- Não investigar pessoas físicas
- Não inferir dados não observáveis
- Não enriquecer com conhecimento externo não suportado
- Priorizar qualidade e relevância, não volume
- Diferenciar claramente:
  - ativo observado
  - ativo inferido
  - ativo suspeito

---

## Tarefas

1. Identificar ativos institucionais diretamente relacionados ao alvo
2. Identificar canais públicos oficiais (redes sociais, diretórios, etc.)
3. Classificar ativos em:
   - primários (centrais à operação)
   - secundários (apoio)
   - residuais/legados (não mantidos ou inconsistentes)
4. Identificar possíveis inconsistências ou sinais de governança digital fraca
5. Sugerir pivôs empresariais úteis para aprofundamento

---

## Saída obrigatória

Retorne **APENAS JSON válido**, sem texto adicional.

```json
{
  "primary_assets": [],
  "secondary_assets": [],
  "public_channels": [],
  "residual_or_legacy_assets": [],
  "business_pivots": [],
  "expansion_notes": ""
}
