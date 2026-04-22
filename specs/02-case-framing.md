# 02 — Case Framing

## Objetivo
Transformar o alvo normalizado em vetores investigativos, hipóteses iniciais e plano de coleta.

---

## Entradas obrigatórias
- normalized_target
- analysis_goal_normalized
- scope_modules
- restrictions
- handoff_summary

## Entradas opcionais
- corporate_identifiers

Se qualquer entrada obrigatória estiver ausente ou inválida, NÃO prossiga.

---

## Instruções ao agente
Analise somente em nível institucional e público.

- Não faça pivôs sobre pessoas físicas
- Não invente dados ausentes
- Não use conhecimento externo não derivado das entradas
- Separe claramente: fato observável, hipótese e lacuna
- Quando `scope_modules` incluir contexto corporativo, incluir vetores de due diligence empresarial leve

---

## Tarefas

1. Resumir o que o alvo aparenta ser com base exclusivamente no seed inicial
2. Listar vetores de investigação apropriados ao escopo
3. Formular hipóteses iniciais plausíveis, conservadoras e testáveis
4. Definir os dados mínimos necessários para continuidade da análise
5. Identificar sinais fracos e possíveis anomalias iniciais
6. Identificar lacunas críticas que impedem avanço seguro
7. Quando aplicável, incluir vetores de investigação corporativa, como:
   - identificação e validação de CNPJ
   - confirmação de razão social e nome fantasia
   - verificação de registro empresarial público
   - leitura de quadro societário em contexto corporativo
   - busca de processos públicos envolvendo a empresa
   - identificação de canais oficiais da empresa

---

## Saída obrigatória

Retorne **APENAS JSON válido**, sem texto adicional.

```json
{
  "target_summary": "",
  "investigation_vectors": [],
  "initial_hypotheses": [],
  "minimum_required_data": [],
  "weak_signals": [],
  "known_gaps": [],
  "confidence": "low|medium|high"
}
