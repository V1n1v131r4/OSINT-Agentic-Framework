# 04 — Entity Graph

## Objetivo

Identificar e organizar entidades relevantes relacionadas ao alvo.

Este módulo foca em ENUMERAÇÃO de entidades, não em correlação profunda.

---

## Entradas obrigatórias

- primary_assets
- residual_or_legacy_assets

---

## Instruções ao agente

- É PERMITIDO enriquecer dados usando fontes públicas
- NÃO expandir para pessoas físicas fora do escopo
- NÃO criar relações complexas
- Apenas identificar entidades observáveis

---

## Tarefas

### 1. Identificar entidades

- empresa
- domínios
- e-mails institucionais
- marcas associadas
- perfis institucionais

---

### 2. Classificar entidades

Classificar como:

- `organization`
- `domain`
- `email`
- `brand`
- `profile`
- `other`

---

## Saída obrigatória

```json
{
  "entities": [
    {
      "name": "",
      "type": "organization | domain | email | brand | profile | other"
    }
  ],
  "confidence": "low | medium | high"
}
