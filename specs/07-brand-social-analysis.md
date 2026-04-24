
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
- É PERMITIDO investigar perfis pessoais de sócios e funcionários identificados para correlação institucional
- NÃO inferir vínculo sem evidência

---

## Tarefas

### 1. Identificar canais oficiais e de sócios

- site institucional
- redes sociais corporativas
- plataformas profissionais (LinkedIn da empresa e dos sócios)
- perfis sociais de sócios e funcionários (para validar vínculo com a empresa)

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
  "partner_channels": [
    {
      "partner_name": "",
      "platform": "",
      "handle": "",
      "url": "",
      "correlation_evidence": "menção à empresa na bio | fotos no local | posts relacionados",
      "evidence_level": "confirmed|candidate|unresolved"
    }
  ],
  "candidate_channels": [],
  "signals": [],
  "confidence": "low | medium | high"
}
```
