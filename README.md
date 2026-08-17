![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
![Version](https://img.shields.io/badge/Version-0.3-informational)
![Format](https://img.shields.io/badge/Format-JSON%20%26%20Agent%20Specs-orange)
![Framework](https://img.shields.io/badge/Framework-OpenCode-blueviolet)

# OSINT Agentic Framework for OpenCode

---
🇬🇧 For english version, please change to the "en" branch

---

## 1. Visão Geral

Este framework operacional foi refatorado para suportar múltiplos propósitos de investigação OSINT. Agora, o operador define o **propósito da operação** no início do processo, e o framework sugere dinamicamente a pipeline mais adequada.

### Propósitos Suportados:
- **Instituições**: Focado em empresas, domínios e ativos corporativos (Pipeline Padrão).
- **Indivíduos**: Focado em pegada digital de pessoas físicas, exposição e vínculos.
- **Campanha de Desinformação**: Análise de narrativas, coordenação e amplificação.
- **Análise de Narrativas**: Mapeamento de ecossistemas de informação e influência.
- **Vazamento de Dados**: Avaliação de impacto, sensibilidade e origem de vazamentos.

---

## 2. ⚠️ Disclaimer e Uso Ético

Este framework é uma ferramenta de **automação de inteligência de fontes abertas (OSINT)**. O uso deste material deve respeitar as seguintes diretrizes:

- **Legalidade**: Certifique-se de que suas atividades estão em conformidade com as leis locais (como LGPD no Brasil ou GDPR na Europa).
- **Ética**: Não utilize este framework para assédio, doxing, perseguição ou qualquer atividade ilegal.
- **Responsabilidade**: O autor não se responsabiliza pelo uso indevido das informações coletadas ou pelas ações tomadas com base nos relatórios gerados.
- **Transparência**: Este framework foca em dados **públicos e abertos**. Não utilize para tentar acessar sistemas privados ou protegidos.

---

## 3. Como Funciona a Pipeline Dinâmica

Diferente de sistemas automáticos, este framework utiliza **orientação dinâmica**. Ao final de cada comando, o agente sugere o próximo passo baseado no tipo de operação escolhido.

1. **Case Intake**: O operador define o `operation_type` no `intake.json`.
2. **Sugestão de Comando**: O output de cada etapa contém o campo `next_command`.
3. **Execução Manual**: O operador mantém o controle total, executando o comando sugerido após validar o resultado anterior.

---

## 4. Loop de Aprendizado Automático (Memória Global)

A partir da **v0.3**, o framework **aprende sozinho**: quanto mais casos você roda, mais
especialista ele fica. O aprendizado é **automático** e embutido nas etapas que **já existem** —
**nada muda nos comandos que você digita** e **nenhum comando novo** é adicionado.

O loop se apoia nos dois únicos pontos que as **5 pipelines compartilham**:

- **`/case-intake`** (início de qualquer pipeline) → **reinjeta** os pivôs comprovados.
- **`/postmortem`** (fim de qualquer pipeline) → **consolida** o que funcionou na memória global.

```
/case-intake   → lê memory/global/playbooks.json, filtra pelo operation_type do caso
                 e injeta os top pivôs em `applicable_playbooks`
   ↓ ...miolo específico da pipeline (intocado)...
/report → /postmortem
   ↓
/postmortem    → além do postmortem do caso, funde os padrões reutilizáveis na memória
                 global (mesmo operation_type), deduplica e REFORÇA (reinforcement_count++)
   ↓
próximo caso do mesmo tipo começa mais especialista
```

**Como a expertise cresce:** cada pivô confirmado em um novo caso tem seu `reinforcement_count`
incrementado; pivôs recorrentes sobem para `confidence_tier` `media`/`alta` e passam a ser
reinjetados no topo. A consolidação é **idempotente** (rodar o mesmo caso duas vezes não infla a
contagem) e **segmentada por `operation_type`** — aprendizado de um tipo de operação (ex.:
vazamentos) nunca contamina outro (ex.: narrativas). Pivôs transversais usam o balde `all`.

- Schema: `schemas/playbook-memory.schema.json`
- Memória: `memory/global/playbooks.json`

---

## 5. Estrutura de Pastas

```
specs/ → Definições lógicas (específicas por tipo de operação).
.opencode/commands/ → Comandos executáveis.
schemas/ → Contratos JSON (inclui playbook-memory.schema.json).
memory/
  └── global/
      └── playbooks.json → Memória global de pivôs (loop de aprendizado).
cases/ → Dados dos casos.
  ├── <case-id>/
  │   ├── intake.json → Definição do propósito e alvo.
  │   ├── runs/ → Outputs de cada etapa.
  │   └── memory/ → Lições aprendidas do caso (postmortem).
```

---

## 6. Passo a Passo: Iniciando uma Operação

### 6.1. Preparar o Intake
Crie a pasta do caso e edite o `intake.json`. Abaixo estão exemplos para cada tipo de operação:

#### Instituições
```json
{
  "case_id": "CORP-001",
  "operation_type": "institutions",
  "target_name": "Empresa Alvo S.A.",
  "target_url": "https://alvo.com.br",
  "scope_type": "empresa",
  "analysis_goal": "Mapear QSA e ativos técnicos.",
  "restrictions": ["Apenas fontes públicas"]
}
```

#### Indivíduos
```json
{
  "case_id": "IND-001",
  "operation_type": "individuals",
  "target_name": "Nome do Alvo",
  "analysis_goal": "Mapear pegada digital e exposição social.",
  "restrictions": ["Respeitar LGPD"]
}
```

#### Desinformação
```json
{
  "case_id": "DIS-001",
  "operation_type": "disinformation_campaign",
  "target_name": "Narrativa X sobre Assunto Y",
  "analysis_goal": "Identificar origem e amplificadores.",
  "restrictions": ["Focar em redes abertas"]
}
```

#### Narrativas
```json
{
  "case_id": "NAR-001",
  "operation_type": "narrative_analysis",
  "target_name": "Tema de Interesse",
  "analysis_goal": "Mapear ecossistema de influência.",
  "restrictions": ["Análise qualitativa"]
}
```

#### Vazamentos
```json
{
  "case_id": "LEAK-001",
  "operation_type": "data_leak",
  "target_name": "Entidade Afetada",
  "analysis_goal": "Validar extensão e sensibilidade do vazamento.",
  "restrictions": ["Não baixar bases completas"]
}
```

### 6.2. Executar o Intake
```bash
/case-intake
```
O agente validará o tipo de operação e sugerirá o próximo comando (ex: `/framing` para instituições ou `/framing-indiv` para indivíduos).

### 6.3. Seguir a Pipeline
Execute os comandos sugeridos sequencialmente. O framework guiará você através do campo `next_command`.

#### Exemplo: Pipeline de Instituições
1. `/case-intake` -> Sugere `/framing`
2. `/framing` -> Sugere `/corporate-collection`
3. `/corporate-collection` -> Sugere `/expansion`
4. `/expansion` -> Sugere `/entity-graph`
5. `/entity-graph` -> Sugere `/institutional-validation`
6. `/institutional-validation` -> Sugere `/technical-surface`
7. `/technical-surface` -> Sugere `/brand-social-analysis`
8. `/brand-social-analysis` -> Sugere `/unstructured-extraction`
9. `/unstructured-extraction` -> Sugere `/geo-context`
10. `/geo-context` -> Sugere `/correlation`
11. `/correlation` -> Sugere `/report`
12. `/report` -> Sugere `/postmortem`

#### Exemplo: Pipeline de Indivíduos
1. `/case-intake` -> Sugere `/framing-indiv`
2. `/framing-indiv` -> Sugere `/individual-collection`
3. `/individual-collection` -> Sugere `/expansion`
4. `/expansion` -> Sugere `/entity-graph`
5. `/entity-graph` -> Sugere `/identity-validation`
6. `/identity-validation` -> Sugere `/individual-footprint`
7. `/individual-footprint` -> Sugere `/individual-social-analysis`
8. `/individual-social-analysis` -> Sugere `/unstructured-extraction`
9. `/unstructured-extraction` -> Sugere `/geo-context`
10. `/geo-context` -> Sugere `/correlation`
11. `/correlation` -> Sugere `/report`
12. `/report` -> Sugere `/postmortem` *(consolida o aprendizado na memória global)*

> Em todas as 5 pipelines o `/report` encaminha para `/postmortem`, que é a etapa final e onde o
> loop de aprendizado é fechado automaticamente (ver seção 4).

#### Outras Pipelines (Fluxos Especializados)

- **Desinformação**: 
  `/case-intake` -> `/framing-disinfo` -> `/disinfo-collection` -> `/expansion` -> `/content-analysis` -> `/disinfo-actor-mapping` -> `/correlation` -> `/report` -> `/postmortem`

- **Narrativas**: 
  `/case-intake` -> `/framing-narrative` -> `/narrative-collection` -> `/expansion` -> `/content-analysis` -> `/narrative-ecosystem-map` -> `/correlation` -> `/report` -> `/postmortem`

- **Vazamentos**: 
  `/case-intake` -> `/framing-leak` -> `/leak-collection` -> `/expansion` -> `/leak-impact-analysis` -> `/leak-data-audit` -> `/unstructured-extraction` -> `/correlation` -> `/report` -> `/postmortem`

---

## 7. Pré-requisitos
- **OpenCode** instalado.
- **EXA** habilitado (`OPENCODE_ENABLE_EXA=1`).

---

## 8. Customização
Para adicionar novas pipelines ou ajustar as existentes, edite os arquivos em `specs/` e os comandos correspondentes em `.opencode/commands/`. O framework é modular e desenhado para evoluir com a necessidade do operador.

---

## 9. Créditos e Licença
Desenvolvido para uso com a plataforma **OpenCode**.
Licença: **GPL v3**.
