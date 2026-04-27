# 04 — Individual Collection

## Objetivo

Realizar a coleta profunda de dados públicos sobre um indivíduo, focando em identidade, pegada digital e vínculos profissionais/pessoais.

---

## Entradas obrigatórias

- target_name
- framing_output (hipóteses e vetores)

---

## Tarefas

1. **Validação de Identidade**: Buscar por homônimos e confirmar identificadores únicos (se disponíveis publicamente).
2. **Pegada em Redes Sociais**: Mapear perfis em LinkedIn, Instagram, Twitter, Facebook, etc.
3. **Histórico Profissional**: Coletar dados de cargos, empresas passadas e conselhos profissionais.
4. **Registros Públicos**: Buscar menções em Diários Oficiais, processos judiciais públicos e registros de propriedade.
5. **Google Dorks para Indivíduos**:
   - `"nome completo" filetype:pdf`
   - `"nome completo" site:jusbrasil.com.br`
   - `"nome completo" (email OR telefone OR contato)`

---

## Saída obrigatória

```json
{
  "confirmed_identity": {},
  "social_profiles": [],
  "professional_history": [],
  "public_records": [],
  "exposure_signals": [],
  "confidence": "low | medium | high"
}
```
