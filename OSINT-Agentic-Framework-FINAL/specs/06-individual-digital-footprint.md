# 06 — Individual Digital Footprint

## Objetivo
Mapear a pegada digital técnica de um indivíduo, focando em identificadores expostos, e-mails, domínios pessoais e presença em bases de dados de serviços.

---

## Entradas obrigatórias
- identity_validation_output
- individual_collection_output

---

## Tarefas
1. **Mapeamento de Identificadores**: Consolidar e-mails (pessoais e profissionais), handles de usuários e possíveis números de telefone.
2. **Enumeração de Ativos Pessoais**: Identificar domínios registrados no nome do indivíduo ou blogs/sites pessoais.
3. **Verificação de Exposição em Serviços**: Checar presença em plataformas (ex: Gravatar, Keybase, GitHub) que revelem metadados técnicos.
4. **Análise de Metadados de Documentos**: Se houver documentos coletados, extrair metadados que revelem softwares usados ou caminhos de diretórios.

---

## Saída obrigatória
```json
{
  "technical_identifiers": {
    "emails": [],
    "handles": [],
    "phones": []
  },
  "personal_assets": [],
  "service_exposure": [],
  "metadata_findings": [],
  "confidence": "low | medium | high"
}
```
