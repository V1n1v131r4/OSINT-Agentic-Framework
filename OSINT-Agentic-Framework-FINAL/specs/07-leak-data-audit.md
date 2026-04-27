# 07 — Leak Data Audit

## Objetivo
Realizar uma auditoria detalhada sobre as amostras de dados vazados, focando na identificação de padrões técnicos que revelem a origem do vazamento e a profundidade da exposição.

---

## Entradas obrigatórias
- leak_impact_analysis_output
- leak_collection_output

---

## Tarefas
1. **Análise de Estrutura de Dados**: Identificar se os dados provêm de um dump de banco de dados (SQL), logs de servidor, ou extração via API.
2. **Auditoria de PII**: Listar campos específicos expostos (ex: CPF, Hash de Senha, Endereço IP, Token de Sessão).
3. **Verificação de Autenticidade**: Cruzar amostras com dados públicos conhecidos para confirmar a veracidade.
4. **Busca por Segredos Técnicos**: Identificar se há chaves de API, segredos de configuração ou credenciais administrativas no vazamento.

---

## Saída obrigatória
```json
{
  "technical_audit_summary": "",
  "exposed_pii_details": [],
  "technical_secrets_found": [],
  "data_origin_hypotheses": [],
  "confidence": "low | medium | high"
}
```
