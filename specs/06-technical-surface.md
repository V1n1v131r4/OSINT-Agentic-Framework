# 06 — Technical Surface

## Objetivo
Ler a superfície técnica pública como fonte de inteligência institucional.

## Entradas obrigatórias
- primary_assets
- residual_or_legacy_assets
- public_channels
- supporting_signals

## Instruções ao agente
Foque em sinais públicos e visíveis sem varredura intrusiva. A leitura deve priorizar governança digital, heranças de stack, erros públicos e coerência operacional.

## Tarefas
1. Identificar indícios de stack, publicação ou plataforma.
2. Identificar ativos residuais, referências herdadas ou erros públicos.
3. Avaliar o que isso revela sobre governança digital.
4. Classificar riscos em termos de maturidade, não de exploração ofensiva.
5. Sugerir validações complementares seguras.

## Saída obrigatória
```json
{
  "observed_stack_signals": [],
  "legacy_or_broken_signals": [],
  "governance_readout": "",
  "risk_assessment": {
    "digital_governance": "low|moderate|high",
    "technical_exposure_inferred": "low|moderate|high"
  },
  "safe_followup_checks": []
}
```

## Critérios de qualidade
- não transformar pista de stack em prova de vulnerabilidade
- evitar linguagem ofensiva
