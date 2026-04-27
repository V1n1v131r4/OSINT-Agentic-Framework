# Quality Rubric

Este documento define critérios mínimos para avaliar a qualidade das saídas geradas pelos agentes.

O objetivo não é maximizar volume de informação, mas garantir:

- utilidade operacional
- aderência à evidência
- disciplina analítica
- controle de escopo

---

## 1. Clareza e Estrutura

A resposta deve:

- ser organizada por seções claras
- evitar blocos longos e pouco estruturados
- priorizar pontos relevantes (máx. 5 por seção)
- evitar redundância

---

## 2. Aderência à Evidência

A resposta deve:

- basear afirmações em dados observáveis
- evitar afirmações categóricas sem suporte
- deixar claro quando algo é:
  - fato
  - inferência
  - hipótese

Evitar:

- extrapolação
- preenchimento de lacunas com suposição

---

## 3. Disciplina Analítica

A resposta deve:

- separar claramente:
  - fatos confirmados
  - hipóteses
  - lacunas (unknowns)
- reconhecer limitações da coleta
- evitar conclusões prematuras

---

## 4. Utilidade Operacional

A resposta deve:

- responder ao objetivo da spec
- priorizar informação acionável
- evitar “curiosidades” irrelevantes
- indicar próximos passos quando aplicável

---

## 5. Controle de Escopo

A resposta deve:

- respeitar o escopo definido na spec
- evitar pivôs não autorizados
- não investigar pessoas físicas fora do escopo

---

## 6. Sinais de Baixa Qualidade

A saída é considerada fraca quando apresenta:

- excesso de texto sem informação útil
- conclusões sem evidência
- mistura de fato e opinião
- ausência de lacunas ou incertezas
- linguagem vaga ("provavelmente", "pode indicar") sem contexto

---

## 7. Classificação Final

Cada saída deve ser avaliada como:

- **Alta** → clara, útil, disciplinada e baseada em evidência
- **Média** → útil, mas com lacunas ou pequenas extrapolações
- **Baixa** → superficial, especulativa ou desorganizada
