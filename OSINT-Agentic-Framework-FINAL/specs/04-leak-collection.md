# 04 — Leak Collection

## Objetivo

Coletar evidências e amostras de vazamentos de dados, focando em validar a autenticidade e a extensão da exposição.

---

## Entradas obrigatórias

- target_entity
- framing_output

---

## Tarefas

1. **Busca em Repositórios de Vazamentos**: Pesquisar menções em fóruns especializados, pastebins e canais de Telegram.
2. **Validação de Amostras**: Analisar amostras públicas para confirmar se os dados pertencem ao alvo.
3. **Mapeamento de Metadados**: Identificar datas de exposição e possíveis vetores de exfiltração.
4. **Identificação de Atribuição**: Coletar sinais sobre quem publicou ou está vendendo os dados.
5. **Google Dorks para Vazamentos**:
   - `site:github.com "nome_alvo" (password OR secret OR key)`
   - `site:pastebin.com "nome_alvo"`
   - `"nome_alvo" (database leak OR sql dump)`

---

## Saída obrigatória

```json
{
  "leak_sources": [],
  "data_samples_metadata": [],
  "exposure_timeline": [],
  "attribution_signals": [],
  "technical_indicators": [],
  "confidence": "low | medium | high"
}
```
