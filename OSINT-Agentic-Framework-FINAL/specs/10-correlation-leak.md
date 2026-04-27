# 10 — Correlation & Anomalies (Vazamentos)

## Objetivo
Consolidar a auditoria técnica e a análise de impacto para identificar a origem provável do vazamento, a extensão real da exposição e os riscos correlacionados.

---

## Entradas obrigatórias
- outputs de leak-impact-analysis e leak-data-audit.

---

## Tarefas
1. **Correlacionar Dados e Origem**: Ligar a estrutura dos dados vazados a sistemas ou vetores de ataque prováveis.
2. **Identificar Padrões de Exposição**: Listar categorias de dados que se repetem ou que indicam um alvo específico (ex: apenas dados de RH).
3. **Detectar Anomalias de Veracidade**: Identificar dados falsos (honeypots) ou misturas de vazamentos antigos.
4. **Mapear Riscos de Atribuição**: Correlacionar o "modus operandi" da publicação com grupos conhecidos.

---

## Saída obrigatória
```json
{
  "leak_origin_correlation": [],
  "exposure_patterns": [],
  "veracity_anomalies": [],
  "attribution_signals": [],
  "known_gaps": [],
  "confidence": "low | medium | high"
}
```
