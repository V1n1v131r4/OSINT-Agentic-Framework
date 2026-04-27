# 07 — Individual Social Analysis

## Objetivo
Analisar a presença e o comportamento de um indivíduo em redes sociais, focando em conexões, estilo de vida, círculo de influência e exposição de informações sensíveis.

---

## Entradas obrigatórias
- individual_footprint_output
- identity_validation_output

---

## Tarefas
1. **Análise de Perfil**: Avaliar biografias, fotos e postagens para extrair sinais de localização, hábitos e interesses.
2. **Mapeamento de Conexões**: Identificar familiares, amigos próximos e colegas de trabalho frequentes.
3. **Análise de Atividade**: Verificar horários de postagem e frequência para inferir rotinas ou fusos horários.
4. **Identificação de Riscos de OPSEC**: Notar se o indivíduo expõe dados sensíveis (fotos de crachás, passaportes, geolocalização em tempo real).

---

## Saída obrigatória
```json
{
  "social_behavior_summary": "",
  "key_connections": [],
  "lifestyle_signals": [],
  "opsec_vulnerabilities": [],
  "activity_patterns": {},
  "confidence": "low | medium | high"
}
```
