# 01 — Case Intake

## Objetivo

Registrar de forma estruturada o contexto inicial do caso, garantindo clareza sobre o propósito da operação e definindo a pipeline a ser seguida.

---

## Entradas obrigatórias

- **case_id**: Identificador único do caso.
- **operation_type**: Tipo de operação (institutions, individuals, disinformation_campaign, narrative_analysis, data_leak).
- **target_name**: Alvo principal.
- **analysis_goal**: Objetivo da investigação.
- **restrictions**: Limites operacionais.

---

## Entradas opcionais

- target_url
- scope_type
- known_data
- analyst_notes
- source_seed

Se entradas obrigatórias estiverem ausentes ou ambíguas, NÃO prossiga.

---

## Instruções ao agente

- Valide se o `operation_type` é um dos tipos suportados.
- Não iniciar coleta.
- Não gerar hipóteses.
- Este módulo é apenas estrutural e de roteamento.
- **Reinjetar a memória global de playbooks** (ver "Loop de Aprendizado" abaixo).

---

## Loop de Aprendizado (Reinjeção de Playbooks)

Este é o **ponto de entrada de todas as 5 pipelines**. Antes de rotear, ele **reinjeta o
conhecimento acumulado** pelo framework em casos anteriores — é isto que faz "quanto mais usar,
mais especialista".

1. Leia `memory/global/playbooks.json` (se não existir, siga sem playbooks).
2. **Filtre pelo `operation_type` deste caso** — inclua também os de `operation_type: "all"`
   (transversais). Nunca traga playbooks de outros tipos de operação.
3. Ordene por `reinforcement_count` (desc) e selecione o **top-5**.
4. Emita-os no campo `applicable_playbooks` do output, como **contexto de método** para as
   etapas seguintes. Não são hipóteses nem coleta — são pivôs comprovados a priorizar.

---

## Saída esperada

O agente deve retornar o JSON estruturado e, em sua resposta textual (se houver), indicar o próximo comando sugerido com base no `operation_type`.

```json
{
  "case_id": "",
  "operation_type": "",
  "target_name": "",
  "analysis_goal": "",
  "scope_definition": "",
  "applicable_playbooks": [
    {
      "id": "",
      "pivot": "",
      "confidence_tier": "",
      "reinforcement_count": 0
    }
  ],
  "next_step_suggestion": "/framing"
}
```

### Mapeamento de Próximo Passo:
- **institutions**: `/framing`
- **individuals**: `/framing-indiv`
- **disinformation_campaign**: `/framing-disinfo`
- **narrative_analysis**: `/framing-narrative`
- **data_leak**: `/framing-leak`
