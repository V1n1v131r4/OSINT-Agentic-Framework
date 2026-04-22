---
description: Executa automaticamente a pipeline completa OSINT em sequência
agent: collector-gpt
model: openai/gpt-5-mini
subtask: true
return:
  - /framing
  - /expansion
  - /entity-graph
  - /institutional-validation
  - /technical-surface
  - /brand-social-analysis
  - /unstructured-extraction
  - /geo-context
  - /correlation
  - /report
  - /postmortem
---

## REGRA CRÍTICA (EXECUÇÃO)

Você NÃO deve:

- executar módulos manualmente
- gerar JSON de módulos seguintes
- interpretar dados para próximas etapas
- continuar a pipeline por conta própria

Você DEVE:

- executar APENAS o comando desta etapa
- retornar o resultado
- deixar o encadeamento ocorrer via `return`

---

## COMPORTAMENTO OBRIGATÓRIO

Após executar o comando:

- PARE imediatamente
- NÃO continue raciocinando sobre o próximo módulo
- NÃO gere saída adicional
- NÃO antecipe etapas

---

## EXECUÇÃO

Execute exclusivamente:

@.opencode/commands/case-intake.md

---

## RESTRIÇÃO FINAL

Se você gerar qualquer conteúdo além do JSON do comando executado:

→ isso é considerado erro de execução
