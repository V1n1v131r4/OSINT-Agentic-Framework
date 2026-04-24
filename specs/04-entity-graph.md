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
- `person` (sócios, administradores e funcionários identificados)
- `document` (documentos públicos encontrados)
- `code_repository` (repositórios de código encontrados)
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
      "type": "organization | person | domain | email | brand | profile | document | code_repository | other"
    }
  ],
  "confidence": "low | medium | high"
}

