
---

# 09 — `specs/09-geo-context.md`

```md
# 09 — Geo Context

## Objetivo

Identificar o contexto geográfico do alvo com base em sinais observáveis.

---

## Entradas obrigatórias

- addresses
- domains
- entities

---

## Instruções ao agente

- É PERMITIDO usar:
  - geolocalização básica
  - dados públicos
- NÃO inferir localização sem base

---

## Tarefas

### 1. Identificar localização

- cidade
- estado
- país

---

### 2. Correlacionar sinais geográficos

- endereço institucional
- TLD do domínio
- presença regional

---

## Saída obrigatória

```json
{
  "locations": [],
  "geo_signals": [],
  "confidence": "low | medium | high"
}
