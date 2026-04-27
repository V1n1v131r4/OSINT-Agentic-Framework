# 10 — Correlation & Anomalies (Indivíduos)

## Objetivo
Consolidar os dados coletados sobre o indivíduo, identificando relações entre identidades digitais, ativos pessoais, conexões sociais e possíveis anomalias ou lacunas de informação.

---

## Entradas obrigatórias
- outputs de identity-validation, individual-footprint e individual-social-analysis.

---

## Tarefas
1. **Mapear Relações de Identidade**: Conectar e-mails, handles, perfis sociais e registros profissionais ao indivíduo.
2. **Identificar Padrões de Comportamento**: Listar recorrências em horários de atividade, estilo de linguagem ou uso de plataformas.
3. **Detectar Anomalias**: Identificar perfis conflitantes, homônimos que causam ruído ou dados biográficos inconsistentes.
4. **Registrar Lacunas**: Listar informações críticas não encontradas (ex: telefone não confirmado, endereço não localizado).

---

## Saída obrigatória
```json
{
  "identity_map": [],
  "social_connections": [],
  "behavioral_patterns": [],
  "anomalies_detected": [],
  "known_gaps": [],
  "confidence": "low | medium | high"
}
```
