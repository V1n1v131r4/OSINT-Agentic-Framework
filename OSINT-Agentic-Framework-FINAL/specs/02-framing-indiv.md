# 02 — Case Framing (Indivíduos)

## Objetivo

Transformar o intake de um indivíduo em uma estrutura analítica, definindo hipóteses sobre pegada digital, exposição e vínculos.

---

## Entradas obrigatórias

- target_name
- analysis_goal
- operation_type (deve ser "individuals")

---

## Tarefas

1. **Definir hipóteses de identidade**: Confirmar se o alvo é uma pessoa única ou se há homônimos.
2. **Mapear vetores de exposição**: Redes sociais, registros profissionais, vazamentos conhecidos, processos judiciais.
3. **Identificar lacunas**: Dados faltantes como e-mails, telefones ou endereços.

---

## Saída esperada

```json
{
  "hypotheses": [],
  "investigation_vectors": [
    "social_media_footprint",
    "professional_background",
    "public_records_search"
  ],
  "known_gaps": []
}
```
