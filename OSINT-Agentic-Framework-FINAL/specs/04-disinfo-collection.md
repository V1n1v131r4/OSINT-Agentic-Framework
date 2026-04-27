# 04 — Disinfo Collection

## Objetivo

Coletar evidências de campanhas de desinformação, focando em fontes originais, padrões de propagação e metadados de conteúdo.

---

## Entradas obrigatórias

- target_narrative
- framing_output

---

## Tarefas

1. **Mapeamento de Fontes**: Identificar os primeiros perfis ou sites a publicar a narrativa.
2. **Coleta de Conteúdo**: Extrair textos, imagens e vídeos associados à campanha.
3. **Análise de Metadados**: Verificar datas de criação de perfis, domínios e arquivos (se disponíveis).
4. **Identificação de Amplificadores**: Listar perfis com alto volume de compartilhamento ou comportamento suspeito.
5. **Google Dorks para Desinformação**:
   - `"narrativa específica" site:twitter.com`
   - `"narrativa específica" site:t.me` (Telegram)
   - `intext:"narrativa específica" -site:veiculos_oficiais.com`

---

## Saída obrigatória

```json
{
  "source_nodes": [],
  "content_samples": [],
  "amplification_nodes": [],
  "timeline_signals": [],
  "technical_artifacts": [],
  "confidence": "low | medium | high"
}
```
