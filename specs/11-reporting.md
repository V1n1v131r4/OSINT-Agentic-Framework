
---

## `specs/11-reporting.md`

```md
# 11 — Reporting

## Objetivo

Transformar os achados já correlacionados em um relatório curto, executivo e rastreável.

Este módulo foca em COMUNICAÇÃO FINAL, não em nova análise.

---

## Entradas obrigatórias

- case intake
- output do módulo 10
- outros outputs anteriores somente se necessários para coerência do resumo

Se o output de correlação não estiver disponível, NÃO prossiga.

---

## Instruções ao agente

- Trabalhar apenas com os insumos fornecidos
- NÃO buscar novas fontes
- NÃO expandir escopo
- NÃO reinterpretar o caso além do que já foi consolidado
- O relatório deve refletir apenas:
  - relações observadas
  - padrões identificados
  - anomalias registradas
  - lacunas já conhecidas

---

## Regras de execução

- Gerar APENAS JSON válido
- Não adicionar campos fora da saída obrigatória
- Todos os campos de lista devem ser arrays JSON válidos
- O resumo executivo deve ser curto, claro e coerente com o objetivo analítico original
- Não transformar hipótese em fato
- Não omitir limitações
- Não usar linguagem inflada ou genérica

---

## Estrutura esperada

### 1. Resumo executivo

Síntese curta do caso, destacando:

- o que foi possível observar
- o nível geral de confiança
- o principal limite da análise

### 2. Principais achados

Listar os pontos mais relevantes e rastreáveis.

### 3. Hipóteses e interpretações

Listar apenas hipóteses ainda sustentadas pelos dados anteriores.

### 4. Lacunas

Listar o que ainda precisa de validação.

### 5. Riscos e implicações

Listar implicações práticas dos achados, sem exagero.

### 6. Próximos passos

Listar validações e coletas complementares úteis.

---

## Saída obrigatória

```json
{
  "executive_summary": "",
  "key_findings": [],
  "hypotheses": [],
  "gaps": [],
  "risks": [],
  "next_steps": [],
  "confidence": "low | medium | high"
}
