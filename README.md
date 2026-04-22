# OSINT Agentic Framework for OpenCode

Framework modular para execução de investigações OSINT assistidas por IA, com foco em:

- controle de execução pelo operador
- modularidade por etapa
- separação entre coleta, correlação e comunicação
- uso disciplinado de LLMs em contexto investigativo

---

## Visão geral

Este projeto **não** é uma ferramenta automática de OSINT.

Ele é um **framework operacional**, onde:

- cada etapa é um comando
- o operador controla a execução
- o modelo executa tarefas específicas
- não existe autonomia completa do agente

---

## Pré-requisitos

### 1. OpenCode

Instale e configure o OpenCode normalmente.

### 2. Execução com EXA

Para permitir busca externa, execute sempre com:

```bash
OPENCODE_ENABLE_EXA=1 opencode .

Sem EXA:

módulos de coleta (03 a 09) ficam limitados
os resultados tendem a ser incompletos
a pipeline perde boa parte da utilidade operacional
Estrutura do projeto
specs/ → definição lógica das etapas
.opencode/commands/ → comandos executáveis
cases/ → dados por caso
intake.json → input bruto
runs/ → outputs por etapa
Modelo de execução

A pipeline funciona assim:

o operador define o caso
os comandos são executados sequencialmente
cada comando gera um JSON estruturado
os outputs alimentam a próxima etapa
o operador valida cada passo
Passo obrigatório: Case Intake

Antes de qualquer execução, você deve criar:

cases/<case-id>/intake.json

Exemplo:

{
  "target": "camilapimentaarquitetura.com.br",
  "analysis_goal": "mapear presença digital e infraestrutura",
  "scope_definition": "apenas dados públicos, sem análise de pessoas físicas"
}

Esse arquivo é o input bruto do caso.

Como executar
Modo recomendado: execução guiada com run-case

Inicie o OpenCode:

OPENCODE_ENABLE_EXA=1 opencode .

Depois execute:

@run-case
Como funciona o run-case

O run-case é um orquestrador guiado.

Ele:

executa uma etapa por vez
valida o JSON retornado
informa o arquivo gerado
pergunta ao operador se deseja continuar

Fluxo de interação esperado:

Etapa concluída: 03-surface-expansion
Arquivo: cases/test-01/runs/03-surface-expansion-gpt.json
Próxima etapa: entity-graph

seguir, revisar ou parar?
Comportamento do intake

O run-case funciona em dois modos.

1. Intake já existe

Se existir:

cases/<case-id>/intake.json

O run-case:

não pede dados novamente
executa @case-intake
normaliza o arquivo bruto para o formato do módulo 01
2. Intake não existe

Se o arquivo não existir, o operador deverá fornecer manualmente:

target
analysis_goal
scope_definition
Fluxo completo
01 case-intake
02 framing
03 surface-expansion
04 entity-graph
05 institutional-validation
06 technical-surface
07 brand-social-analysis
08 unstructured-extraction
09 geo-context
10 correlation
11 report
12 postmortem
Fluxo mínimo recomendado

Para uso rápido ou validação inicial:

01 → 02 → 03 → 04 → 06 → 10 → 11
Modelo mental
Etapa	Tipo	Usa fontes externas
01–02	definição	❌ não
03–09	coleta	✔ sim
10	correlação	❌ não
11	relatório	❌ não

Esse ponto é fundamental.

A pipeline foi desenhada para separar:

definição do caso
coleta
correlação
comunicação final

Isso reduz confusão, alucinação e mistura de camadas.

Princípios operacionais
uma etapa por vez
sem execução automática completa
sem inferência sem evidência
separação entre coleta e análise
outputs sempre estruturados
validação humana entre etapas
O que o framework não faz
não automatiza investigação completa
não substitui ferramentas OSINT
não executa varredura ativa
não gera conclusões autônomas
não elimina a necessidade de revisão do operador
Resultado esperado

Ao final da pipeline, você terá:

dados estruturados por etapa
correlação entre entidades e ativos
lacunas explícitas
relatório coerente com o objetivo inicial
Uso em treinamento

Este framework foi desenhado para:

ensino de OSINT com LLM
controle de viés e alucinação
execução disciplinada
análise passo a passo

Ele é útil para mostrar ao aluno que LLM não substitui processo.

O valor está em usar o modelo com:

escopo definido
comando certo
validação entre etapas
controle do operador
