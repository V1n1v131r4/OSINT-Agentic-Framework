# 05 — Identity Validation (Indivíduos)

## Objetivo

Validar a identidade do alvo, cruzando dados de múltiplas fontes para confirmar se os perfis e registros encontrados pertencem à mesma pessoa física.

---

## Entradas obrigatórias

- individual_collection_output
- entity_graph_output

---

## Tarefas

1. **Cruzamento de Identificadores**: Verificar se e-mails, telefones ou nomes de usuário se repetem em diferentes plataformas.
2. **Consistência Biográfica**: Validar se o histórico profissional e educacional é coerente entre LinkedIn, currículos e registros públicos.
3. **Análise de Vínculos**: Confirmar relações com empresas ou outras pessoas citadas no intake.
4. **Classificação de Confiança**:
   - `Confirmed`: Identidade validada por múltiplos pontos de convergência.
   - `Candidate`: Perfil provável, mas com ambiguidades (ex: homônimos).
   - `Unverified`: Sem dados suficientes para confirmação.

---

## Saída esperada

```json
{
  "validated_identity": {
    "full_name": "",
    "confirmed_identifiers": [],
    "status": "confirmed | candidate | unverified"
  },
  "identity_conflicts": [],
  "biographical_summary": ""
}
```
