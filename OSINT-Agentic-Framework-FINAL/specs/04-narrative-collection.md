# 04 — Narrative Collection

## Objetivo

Coletar dados sobre o ecossistema de uma narrativa, focando em atores principais, volume de menções e canais de influência.

---

## Entradas obrigatórias

- target_topic
- framing_output

---

## Tarefas

1. **Identificação de Atores**: Mapear influenciadores, veículos de mídia e perfis institucionais que pautam o tema.
2. **Coleta de Menções**: Extrair amostras de postagens, artigos e comentários.
3. **Mapeamento de Canais**: Identificar onde a narrativa é mais forte (redes sociais, fóruns, blogs).
4. **Análise de Engajamento**: Coletar sinais de volume (likes, shares, views) para medir impacto.
5. **Google Dorks para Narrativas**:
   - `"tema específico" (opinião OR análise OR editorial)`
   - `"tema específico" site:youtube.com`
   - `"tema específico" site:medium.com OR site:substack.com`

---

## Saída obrigatória

```json
{
  "key_actors": [],
  "content_ecosystem": [],
  "engagement_signals": [],
  "platform_distribution": [],
  "narrative_variants": [],
  "confidence": "low | medium | high"
}
```
