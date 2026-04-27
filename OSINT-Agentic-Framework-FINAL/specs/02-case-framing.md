# 02 — Case Framing

## Objetivo

Transformar o intake em uma estrutura analítica inicial, definindo:

- hipóteses iniciais
- vetores de investigação
- lacunas críticas

Este módulo define COMO a investigação será conduzida.

---

## Entradas obrigatórias

- target
- analysis_goal
- scope_definition

---

## Entradas opcionais

- known_data
- constraints
- priority_questions

Se entradas obrigatórias estiverem ausentes, NÃO prossiga.

---

## Instruções ao agente

- Não realizar coleta extensa
- Trabalhar apenas com:
  - dados fornecidos
  - conhecimento geral
- Evitar afirmações categóricas

---

## Tarefas

### 1. Definir hipóteses iniciais

- Formular de 2 a 5 hipóteses plausíveis
- Cada hipótese deve:
  - ser testável
  - estar alinhada ao objetivo
  - evitar especulação excessiva

---

### 2. Definir vetores de investigação

Para cada hipótese, indicar:

- onde buscar evidência
- que tipo de dado pode confirmar ou refutar

---

### 3. Identificar lacunas críticas

Listar:

- informações essenciais ainda desconhecidas
- pontos que impedem validação das hipóteses

---

## Saída esperada

```json
{
  "hypotheses": [
    {
      "description": "",
      "rationale": "",
      "validation_vectors": []
    }
  ],
  "investigation_vectors": [],
  "known_gaps": []
}
