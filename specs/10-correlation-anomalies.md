# 10 — Correlation & Anomalies

## Objetivo

Consolidar os dados coletados nas etapas anteriores, identificando:

- relações observáveis entre entidades e ativos
- padrões recorrentes
- inconsistências ou sinais conflitantes
- pontos que ainda exigem validação

Este módulo foca em CORRELAÇÃO ESTRUTURADA, não em narrativa investigativa final.

---

## Entradas obrigatórias

- outputs relevantes das etapas anteriores
- entidades identificadas
- ativos e sinais técnicos ou institucionais já coletados

Se não houver dados suficientes para correlacionar, NÃO prossiga.

---

## Instruções ao agente

- Trabalhar apenas com dados já coletados
- NÃO buscar novas fontes
- NÃO expandir escopo
- NÃO transformar correlação em conclusão definitiva
- Separar claramente:
  - relação observada
  - padrão
  - anomalia
  - lacuna

---

## Regras de execução

- Gerar APENAS JSON válido
- Todos os campos de lista devem ser arrays JSON válidos
- Não adicionar campos fora da saída obrigatória
- Se não houver evidência suficiente para uma relação, NÃO incluir
- Cada relação deve refletir apenas conexão observável ou inferência fraca explicitamente classificada
- Não criar narrativa longa dentro dos campos
- Não assumir causalidade
- Não usar linguagem especulativa sem classificar a incerteza

---

## Tarefas

### 1. Identificar relações

Mapear conexões entre:

- empresa
- domínio
- subdomínios
- e-mails
- ativos técnicos
- perfis institucionais
- identificadores corporativos

Classificar cada relação como:

- `direct` = vínculo observável de forma clara
- `indirect` = vínculo plausível, mas não confirmado diretamente

---

### 2. Identificar padrões

Listar recorrências observáveis, como:

- reutilização de identificadores
- consistência entre fontes
- concentração de infraestrutura
- repetição de contato institucional
- alinhamento entre presença institucional e ativos técnicos

---

### 3. Identificar anomalias

Listar sinais como:

- inconsistências entre fontes
- ativos ou dados que não se encaixam
- divergência de contato, naming ou infraestrutura
- ausência relevante de confirmação

---

### 4. Registrar lacunas

Listar o que ainda impede validação mais forte de relações ou hipóteses.

---

## Saída obrigatória

```json
{
  "relationships": [
    {
      "entity_a": "",
      "relation": "",
      "entity_b": "",
      "type": "direct | indirect",
      "confidence": "low | medium | high"
    }
  ],
  "patterns": [],
  "anomalies": [],
  "known_gaps": [],
  "confidence": "low | medium | high"
}
