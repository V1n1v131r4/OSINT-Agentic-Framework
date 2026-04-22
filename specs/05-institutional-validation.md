
---

# 05 — `specs/05-institutional-validation.md`

```md
# 05 — Institutional Validation

## Objetivo

Validar sinais institucionais do alvo em fontes públicas confiáveis.

---

## Entradas obrigatórias

- entities

---

## Instruções ao agente

- É PERMITIDO consultar:
  - registros públicos
  - agregadores empresariais
  - bases institucionais
- NÃO validar pessoas físicas fora do escopo
- NÃO assumir validade sem evidência

---

## Tarefas

### 1. Validar existência institucional

- CNPJ (se aplicável)
- razão social
- endereço
- atividade

---

### 2. Identificar consistência

- nome da empresa
- domínio
- contatos institucionais

---

## Saída obrigatória

```json
{
  "validated_entities": [],
  "inconsistencies": [],
  "unverified_entities": [],
  "confidence": "low | medium | high"
}
