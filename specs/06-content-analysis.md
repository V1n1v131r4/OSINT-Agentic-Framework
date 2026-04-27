# 06 — Content & Narrative Analysis

## Objetivo

Analisar o conteúdo coletado para identificar padrões de linguagem, sentimentos, variantes de narrativas e sinais de coordenação ou inautenticidade.

---

## Entradas obrigatórias

- collection_output (disinfo ou narrative)
- expansion_output

---

## Tarefas

1. **Identificação de Narrativas**: Categorizar as diferentes versões da mensagem principal.
2. **Análise de Sentimento**: Avaliar a carga emocional e o tom das postagens/artigos.
3. **Detecção de Padrões**: Identificar repetição de frases, hashtags coordenadas ou uso de mídias idênticas em diferentes canais.
4. **Avaliação de Coordenação**: Verificar se as postagens ocorrem em intervalos de tempo suspeitos ou se há compartilhamento cruzado massivo.
5. **Mapeamento de Influência**: Identificar quais atores têm maior poder de pauta dentro do ecossistema.

---

## Saída obrigatória

```json
{
  "narrative_variants": [],
  "sentiment_profile": {},
  "coordination_signals": [],
  "key_influencers": [],
  "content_patterns": [],
  "confidence": "low | medium | high"
}
```
