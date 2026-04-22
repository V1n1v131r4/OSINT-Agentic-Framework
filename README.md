# OSINT AI Framework for OpenCode

Framework modular para análises públicas assistidas por IA com execução etapa por etapa, comparação entre modelos e memória operacional.

## Princípios

- Uma spec por etapa para evitar respostas rasas.
- Entradas e saídas rigidamente estruturadas.
- Separação explícita entre fato, hipótese, lacuna e recomendação.
- Comparação entre modelos no mesmo schema.
- Aprendizado feito na camada de memória do caso, não assumido como treinamento do modelo.
- Limites de segurança: sem pivot indevido sobre pessoas físicas, sem dossiês pessoais, sem coleta intrusiva.

## Fluxo

1. `01-case-intake`
2. `02-case-framing`
3. `03-surface-expansion`
4. `04-entity-graph`
5. `05-institutional-validation`
6. `06-technical-surface`
7. `07-brand-social-analysis`
8. `08-unstructured-extraction`
9. `09-geo-context`
10. `10-correlation-anomalies`
11. `11-reporting`
12. `12-model-comparison`
13. `13-postmortem-learning`

## Como usar no OpenCode

- Cada spec pode virar um `agent` dedicado ou um comando.
- Recomenda-se dois agentes coletores (`collector-gpt`, `collector-claude`) e dois agentes de controle (`comparator`, `reviewer`).
- Os agentes devem escrever saída em JSON nos diretórios `cases/<case-id>/runs/`.

## Pastas

- `specs/`: definição de cada etapa.
- `schemas/`: contratos JSON.
- `rubrics/`: critérios de evidência, utilidade e risco de alucinação.
- `.opencode/agents/`: agentes prontos para OpenCode.
- `templates/`: arquivos base de intake e de memória.

