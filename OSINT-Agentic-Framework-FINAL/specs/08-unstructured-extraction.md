
---

# 08 — `specs/08-unstructured-extraction.md`

```md
# 08 — Unstructured Extraction

## Objetivo

Extrair dados relevantes de conteúdo não estruturado.

---

## Entradas obrigatórias

- páginas públicas
- conteúdos coletados anteriormente

---

## Instruções ao agente

- Trabalhar apenas com conteúdo disponível
- NÃO buscar novas fontes (já coletadas)
- NÃO interpretar além do texto

---

## Tarefas

### 1. Extrair dados relevantes

- e-mails
- telefones
- endereços
- nomes institucionais

---

### 2. Normalizar dados

- remover duplicados
- padronizar formato

---

## Saída obrigatória

```json
{
  "emails": [],
  "phones": [],
  "addresses": [],
  "names": [],
  "confidence": "low | medium | high"
}
