# 03 — Surface Expansion

## Objetivo
Expandir a superfície pública do alvo a partir dos insumos do caso, respeitando seu propósito e escopo.

---

## Entradas obrigatórias
- Do intake normalizado (`01-case-intake.json`): `operation_type`, `target_name`, `analysis_goal` e `scope_definition`.
- Do framing: `investigation_vectors` e `known_gaps`.
- Da coleta correspondente ao `operation_type`: o artefato JSON com o campo `confidence` (`low`, `medium` ou `high`).

Use `target_name`, `analysis_goal` e `scope_definition` diretamente como contexto do alvo. Se qualquer entrada obrigatória estiver ausente ou inválida, informe o arquivo e o campo e interrompa a etapa.

## Entradas opcionais
- corporate_identity
- official_channels
- corporate_registry_signals
- public_litigation_signals


---

## Instruções ao agente

- Quando houver artefato de corporate collection, usá-lo para priorizar ativos e canais confirmados
- Limitar a expansão a ativos e canais públicos pertinentes ao `operation_type` e ao escopo do intake
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

1. Identificar ativos diretamente relacionados ao alvo
2. Identificar canais públicos relevantes para o propósito do caso
3. Classificar ativos em:
   - primários (centrais à operação)
   - secundários (apoio)
   - residuais/legados (não mantidos ou inconsistentes)
4. Identificar inconsistências pertinentes ao caso
5. Sugerir pivôs empresariais quando aplicáveis. Use `business_pivots: []` quando não se aplicarem.

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
