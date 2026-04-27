# 06 — Technical Surface

## Objetivo

Mapear a superfície técnica pública do alvo, identificando ativos e sinais de infraestrutura digital visíveis externamente.

Este módulo foca em ENUMERAÇÃO técnica com enriquecimento passivo.

---

## Entradas obrigatórias

- primary_assets (domínio principal, subdomínios conhecidos)
- residual_or_legacy_assets

## Entradas opcionais

- supporting_signals

Se não houver domínio ou ativo técnico definido, NÃO prossiga.

---

## Instruções ao agente

- Trabalhar apenas com dados públicos
- É PERMITIDO enriquecer dados usando:
  - DNS público
  - registros WHOIS
  - resolução de domínio
  - certificate transparency (crt.sh)
- NÃO realizar varredura ativa ou intrusiva
- NÃO testar vulnerabilidades

---

## Regras de execução

- Todos os campos de lista devem ser arrays JSON válidos
- Cada item deve ser um valor simples (string ou objeto estruturado)
- NÃO incluir texto explicativo dentro dos campos
- NÃO incluir inferências sem evidência observável
- Se não houver evidência clara, NÃO incluir o item
- Não descrever itens — apenas listar valores

---

## Tarefas

### 1. Identificar domínios e subdomínios

- domínio principal
- subdomínios descobertos via:
  - DNS
  - certificados
  - padrões comuns (www, api, mail)

---

### 2. Identificar registros DNS

Buscar:

- A / AAAA
- MX
- NS
- TXT (SPF, DKIM, DMARC)

---

### 3. Identificar IPs e infraestrutura

- IPs associados aos domínios
- CDN ou proxy (se visível)
- provedores

---

### 4. Identificar ASN (quando possível)

- ASN
- organização

---

### 5. Identificar serviços técnicos

- web (http/https)
- e-mail (MX)
- CDN
- proxy

---

### 6. Identificar sinais técnicos

- SPF presente
- DMARC presente
- uso de CDN
- uso de terceiros

---

## Saída obrigatória

```json
{
  "domains": [],
  "subdomains": [],
  "dns_records": {
    "a_records": [],
    "mx_records": [],
    "ns_records": [],
    "txt_records": []
  },
  "ip_addresses": [],
  "asn_info": [
    {
      "asn": "",
      "organization": ""
    }
  ],
  "providers": [],
  "exposed_services": [],
  "technical_signals": [],
  "confidence": "low | medium | high"
}
