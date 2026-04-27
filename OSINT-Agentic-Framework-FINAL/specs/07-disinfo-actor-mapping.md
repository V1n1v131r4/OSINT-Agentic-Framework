# 07 — Disinfo Actor Mapping

## Objetivo
Mapear e categorizar os atores envolvidos em uma campanha de desinformação, diferenciando entre fontes originais, amplificadores inautênticos (bots/cyborgs) e usuários orgânicos influenciados.

---

## Entradas obrigatórias
- content_analysis_output
- disinfo_collection_output

---

## Tarefas
1. **Categorização de Perfis**: Classificar perfis em:
   - `Source`: Criadores do conteúdo original.
   - `Amplifier`: Perfis que apenas replicam sem adicionar conteúdo.
   - `Influencer`: Perfis reais que dão credibilidade à narrativa.
2. **Análise de Redes**: Identificar conexões entre perfis (seguidores mútuos, interações frequentes).
3. **Detecção de Inautenticidade**: Buscar sinais de automação (datas de criação próximas, padrões de nomes, fotos de perfil geradas por IA).
4. **Mapeamento de Plataformas**: Identificar se os atores operam de forma coordenada em múltiplas redes (X, Telegram, Facebook).

---

## Saída obrigatória
```json
{
  "actor_network": [],
  "bot_signals_detected": [],
  "key_amplifiers": [],
  "cross_platform_presence": [],
  "confidence": "low | medium | high"
}
```
