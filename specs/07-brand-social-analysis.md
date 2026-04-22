
---

# 07 — `specs/07-brand-social-analysis.md`

```md
# 07 — Brand & Social Analysis

## Objetivo

Identificar presença pública do alvo em plataformas e canais institucionais.

---

## Entradas obrigatórias

- entities

---

## Instruções ao agente

- É PERMITIDO buscar em:
  - redes sociais
  - diretórios públicos
  - sites institucionais
- NÃO investigar perfis pessoais
- NÃO inferir vínculo sem evidência

---

## Tarefas

### 1. Identificar canais oficiais

- site institucional
- redes sociais
- plataformas profissionais

---

### 2. Identificar padrões

- consistência de nome
- uso de domínio institucional
- presença ativa vs inativa

---

## Saída obrigatória

```json
{
  "official_channels": [],
  "candidate_channels": [],
  "signals": [],
  "confidence": "low | medium | high"
}
