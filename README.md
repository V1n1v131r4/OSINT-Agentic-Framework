![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
![Version](https://img.shields.io/badge/Version-1.0.0-informational)
![Format](https://img.shields.io/badge/Format-JSON%20%26%20Agent%20Specs-orange)
![Framework](https://img.shields.io/badge/Framework-OpenCode-blueviolet)
![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)

# OSINT Agentic Framework for OpenCode

## DISCLAIMER

Este repositório não é uma ferramenta de OSINT nem um agente autônomo de investigação. Trata-se de um **framework operacional para uso disciplinado de LLMs em contexto de inteligência**, projetado para resolver um problema comum: o uso de modelos de linguagem sem estrutura, que leva a correlações frágeis, validações implícitas e perda de controle analítico.

Neste modelo, o LLM atua como executor de etapas específicas, enquanto o operador mantém controle total sobre escopo, validação e correlação. A proposta não é automatizar a análise, mas **estruturar o processo, reduzir viés, garantir rastreabilidade e preservar OPSEC** — especialmente em cenários onde agentes generalistas produzem resultados difíceis de auditar.

A proposta não é automatizar a análise, mas sim **estruturar o processo investigativo** para reduzir vieses, aumentar a rastreabilidade e preservar a segurança operacional (**OPSEC**). Este método é essencial em cenários onde a dependência exclusiva de agentes generalistas pode comprometer a qualidade e a confiabilidade dos resultados.

---

### Pilares do Framework

Este sistema modular foi desenvolvido para proporcionar um processo estruturado e controlado de **investigações OSINT assistidas por IA**, destacando-se por:

- **Controle do Operador**: cada etapa é executada e validada explicitamente, evitando decisões implícitas do modelo  
- **Modularidade**: a pipeline separa funções críticas, impedindo que coleta, validação e correlação se misturem  
- **Separação de Funções**: cada fase possui papel definido, reduzindo erros de interpretação e inferência  
- **Uso Disciplinado de LLMs**: o modelo é limitado a tarefas específicas, evitando alucinações e correlações não verificadas  

O objetivo é servir como uma **estrutura base para produção de inteligência com LLMs sob controle**, permitindo que operadores construam suas próprias pipelines de investigação com critérios claros de validação, correlação e evidência, adaptando o fluxo conforme a necessidade operacional.


---

## 1. Visão Geral do Framework

É fundamental compreender que este projeto **não** é uma ferramenta automática de OSINT. Em vez disso, ele atua como um **framework operacional** onde:

- Cada etapa da investigação é representada por um comando específico.
- O operador é o responsável por controlar a execução de cada comando.
- Modelos de IA (LLMs) são empregados para executar tarefas específicas e auxiliares.
- Não há autonomia completa do agente de IA; a supervisão humana é constante.

---

## 2. Escopo da Pipeline

A versão atual desta pipeline foi projetada com a premissa de que o **alvo da operação é uma instituição** (como uma empresa, organização, marca ou domínio). As etapas foram cuidadosamente elaboradas para:

- Mapear a presença digital institucional e de seus sócios.
- Identificar ativos técnicos associados à instituição.
- Validar sinais corporativos e quadros societários (QSA).
- Executar Google Dorks para descoberta de documentos e menções ocultas.
- Correlacionar dados estruturados e mídias sociais no contexto de *due diligence*.

### 2.1. Investigação de Indivíduos: Considerações Específicas

Caso o objetivo seja a investigação de **indivíduos**, é crucial observar que a pipeline atual **não está otimizada para esse cenário**. Os módulos existentes:

- Permitem a análise de pessoas físicas quando identificadas como sócios ou administradores.
- Priorizam ativos institucionais e a correlação destes com seus representantes legais.
- Incluem vetores de busca por mídias sociais de sócios para validação de vínculo institucional.

#### 2.1.1. Ajustes Necessários para Indivíduos

Para adaptar o framework à investigação de indivíduos, recomenda-se:

- **Redefinir o `scope_definition`**: Ajustar o escopo no arquivo `case-intake` para refletir o novo objetivo.
- **Adaptar Módulos de Coleta**: Modificar os módulos de coleta (especialmente os de 03 a 09) para fontes relevantes a indivíduos.
- **Incluir Fontes e Vetores Específicos**: Adicionar fontes como redes sociais pessoais, registros públicos, correlação de identidade digital e análise de exposição.

#### 2.1.2. Considerações Legais e Éticas

A investigação de indivíduos acarreta **riscos adicionais** relacionados à privacidade, legislação local e uso indevido de dados pessoais. Este framework foi concebido para trabalhar com **dados públicos e contexto institucional**. Qualquer adaptação para indivíduos deve rigorosamente respeitar:

- Os limites legais aplicáveis.
- Os princípios de necessidade e proporcionalidade.
- As restrições definidas no `scope_definition`.

**Recomendação**: Para uso com indivíduos, **não utilize a pipeline padrão sem ajustes**. Trate cada caso como separado e adapte os módulos explicitamente para esse contexto.

---

## 3. Pré-requisitos

Para utilizar o framework, os seguintes pré-requisitos devem ser atendidos:

### 3.1. OpenCode

Instale e configure o OpenCode conforme as instruções padrão.

### 3.2. Execução com EXA

Para habilitar a funcionalidade de busca externa e garantir a eficácia dos módulos de coleta, o OpenCode deve ser executado com a variável de ambiente `OPENCODE_ENABLE_EXA` ativada:

```bash
OPENCODE_ENABLE_EXA=1 opencode .
```

**Importância do EXA**: Sem o EXA, os módulos de coleta (03 a 09) terão suas capacidades limitadas, resultando em informações incompletas e reduzindo significativamente a utilidade operacional da pipeline.

---

## 4. Estrutura do Projeto

O projeto é organizado da seguinte forma:

```
specs/ → Definição lógica das etapas da pipeline.
.opencode/commands/ → Contém os comandos executáveis do framework.
cases/ → Armazena os dados específicos de cada caso de investigação.
  ├── <case-id>/ → Diretório para um caso específico.
  │   └── intake.json → Arquivo de input bruto para o caso.
runs/ → Guarda os outputs gerados por cada etapa da execução.
```

A pipeline opera sequencialmente:

1.  O operador define o caso de investigação.
2.  Os comandos são executados um a um.
3.  Cada comando gera um arquivo JSON estruturado como output.
4.  Os outputs de uma etapa alimentam a etapa subsequente.
5.  O operador valida cada passo antes de prosseguir.

### 4.1. Passo Obrigatório: Case Intake

Antes de iniciar qualquer execução, é mandatório criar o arquivo `intake.json` dentro do diretório do caso (`cases/<case-id>/intake.json`). Este arquivo serve como o input bruto para a investigação.

**Exemplo de `intake.json`:**

```json
{
  "target": "dominio.com.br",
  "analysis_goal": "mapear presença digital e infraestrutura",
  "scope_definition": "apenas dados públicos, sem análise de pessoas físicas"
}
```

---

## 5. Como Executar


Inicie o OpenCode com EXA habilitado e execute cada comando individualmente, validando os outputs a cada passo:

1.  Inicie o OpenCode:
    ```bash
    OPENCODE_ENABLE_EXA=1 opencode .
    ```
2.  Execute os comandos na sequência (exemplo):
    ```
    /case-intake
    /framing
    /corporate-collection
    /expansion
    /entity-graph
    /institutional-validation
    /technical-surface
    /brand-social-analysis
    /unstructured-extraction
    /geo-context
    /correlation
    /report
    ```

---


## 6. Iniciando um Novo Projeto

Ao iniciar uma nova investigação, siga estes passos:

1.  **Edite o `cases/<case-id>/intake.json`**: Atualize com os dados da nova operação.
2.  **Limpe o Histórico de Runs**: Apague os outputs de execuções anteriores para evitar conflitos:
    ```bash
    rm -rf cases/<case-id>/runs/*
    ```
    *Alternativamente, para manter o histórico, mova o diretório do caso anterior (ex: `cases/test-01` para `cases/test-02`) e crie um novo `intake.json` para a nova operação.*

---


## 7. Como adaptar a pipeline para diferentes tipos de operação

Esta pipeline foi desenhada como uma estrutura base. Isso significa que **a lógica pode (e deve) ser ajustada conforme o tipo de investigação, alvo e objetivo operacional**.

A adaptação ocorre em dois níveis:

- `specs/` → define a lógica analítica  
- `.opencode/commands/` → define a execução  

---

## Ajustando a lógica (arquivos em `specs/`)

### 01 — `case-intake`

Define **o ponto de entrada da investigação**.

Edite quando quiser mudar:
- tipo de alvo (empresa, indivíduo, domínio)
- dados obrigatórios
- restrições de escopo
- critérios mínimos para iniciar execução

---

### 02 — `case-framing`

Define **como o problema será estruturado antes da coleta**.

Edite para ajustar:
- construção de hipóteses
- vetores de investigação
- nível de rigor analítico
- registro de lacunas

---

### 03 — `surface-expansion`

Define **como a coleta inicial é feita**.

Edite para ajustar:
- quais sinais buscar primeiro
- quais fontes são permitidas
- prioridade entre identificadores (domínio, nome, marca)
- profundidade da expansão

---

### 04 — `entity-graph`

Define **a estrutura de entidades da investigação**.

Edite para ajustar:
- tipos de entidades (empresa, domínio, pessoa, canal, etc.)
- nível de granularidade do grafo
- critérios de inclusão/exclusão
- normalização de identificadores

Use este módulo quando quiser mudar **como os dados são organizados**.

---

### 04 — `corporate-collection`

Define **a coleta corporativa profunda**.

Edite para ajustar:
- prioridade entre:
  - CNPJ
  - razão social
  - nome fantasia
- uso de diretórios (cnpj.biz, econodata, etc.)
- busca por empresas similares
- correlação entre múltiplos CNPJs
- identificação de domínios relacionados
- coleta de redes sociais corporativas
- identificação de contatos públicos (incluindo WhatsApp quando explícito)

Use este módulo quando quiser mudar **o comportamento da coleta**.

---

### 05 — `institutional-validation`

Define **como dados corporativos são validados**.

Edite para ajustar:
- critério de confirmação (`candidate` vs `confirmed`)
- número mínimo de fontes
- pontos de convergência (endereço, domínio, sócios, etc.)
- tolerância a inconsistência

Use este módulo para controlar **qualidade e confiança da informação**.

---

### 06 — `technical-surface`

Define **a análise de infraestrutura técnica**.

Edite para ajustar:
- coleta de:
  - DNS
  - IP
  - ASN
  - e-mail
- identificação de serviços expostos
- nível de profundidade técnica

Use este módulo para controlar **visibilidade de infraestrutura**.

---

### 07 — `brand-social-analysis`

Define **análise de presença pública e canais oficiais**.

Edite para ajustar:
- plataformas analisadas
- critérios de validação de canais oficiais
- sinais de consistência de branding
- identificação de perfis relacionados

---

### 08 — `unstructured-extraction`

Define **extração de dados de conteúdo não estruturado**.

Edite para ajustar:
- tipos de dado extraídos:
  - e-mails
  - telefones
  - URLs
- regras de normalização
- tratamento de duplicidade
- descarte de dados fracos

---

### 09 — `geo-context`

Define **como contexto geográfico entra na análise**.

Edite para ajustar:
- nível de detalhe permitido
- tipos de sinal geográfico
- limites de inferência

---

### 10 — `correlation`

Define **o núcleo analítico da pipeline**.

Edite para ajustar:
- construção de relações
- definição de:
  - padrões
  - anomalias
  - lacunas
- critérios de evidência
- separação entre relação direta e indireta

Este é o módulo que mais impacta **qualidade da inteligência**.

---

### 11 — `report`

Define **como o output final é apresentado**.

Edite para ajustar:
- estrutura do relatório
- nível de detalhe
- forma de comunicar riscos e hipóteses

---

### 12 — `postmortem`

Define **aprendizado da execução**.

Edite para ajustar:
- registro de falhas
- melhoria contínua
- reutilização de conhecimento

---

## Ajustando a execução (arquivos em `.opencode/commands/`)

Os comandos controlam **como a pipeline roda**.

Edite quando quiser mudar:

- ordem de execução
- encadeamento entre etapas
- modelo utilizado
- regras operacionais da etapa
- comportamento do agente

---

### Pontos principais para edição

#### Inputs
Definem quais arquivos alimentam cada etapa.

#### Output
Define onde o resultado será salvo.

#### Instruções operacionais
Permitem ajustar comportamento, por exemplo:
- exigir websearch/webfetch
- impedir inferência
- forçar múltiplas fontes
- bloquear avanço sem evidência mínima

---

## Regra prática

- `specs/` → mudam **o que o modelo faz**
- `commands/` → mudam **como e quando ele faz**

---

## Exemplos de adaptação

### Análise de vazamento de dados (data leak / breach)

Objetivo: identificar origem, impacto e possíveis correlações de um vazamento público.

Ajustar principalmente:
- `03-surface-expansion` → priorizar busca por dumps, fóruns, paste sites  
- `08-unstructured-extraction` → extrair e-mails, usernames, padrões de dados  
- `04-entity-graph` → organizar identidades, domínios e relações  
- `10-correlation` → identificar padrões, reutilização de dados e clusters  

---

### Atribuição de identidade digital (username / alias)

Objetivo: correlacionar múltiplos perfis e identificar consistência entre aliases.

Ajustar principalmente:
- `03-surface-expansion` → buscar usernames e variações  
- `04-entity-graph` → mapear perfis, aliases e plataformas  
- `07-brand-social-analysis` → validar presença e consistência entre canais  
- `05-identity-validation` (ou equivalente) → validar convergência de sinais  
- `10-correlation` → consolidar relações entre perfis  

---

### Análise de campanha de desinformação

Objetivo: identificar padrões de disseminação, origem e comportamento coordenado.

Ajustar principalmente:
- `03-surface-expansion` → coletar conteúdo e fontes iniciais  
- `07-brand-social-analysis` → mapear canais e perfis envolvidos  
- `08-unstructured-extraction` → extrair mensagens, links e padrões de linguagem  
- `04-entity-graph` → organizar atores, canais e conteúdos  
- `10-correlation` → identificar padrões, repetição e coordenação  

---

## Recomendação final

Evite alterar múltiplos módulos simultaneamente.

O ideal é:

1. ajustar uma etapa  
2. executar um caso de teste  
3. validar saída  
4. iterar  

Isso preserva consistência, facilita debugging e evita degradação da pipeline.


---

## 8. Princípios Operacionais e Limitações

### 8.1. Princípios Operacionais

O design da pipeline é guiado pelos seguintes princípios, que visam otimizar o uso de LLMs e garantir a qualidade da investigação:

-   **Uma Etapa por Vez**: Foco na execução e validação de cada módulo individualmente.
-   **Sem Execução Automática Completa**: O operador mantém o controle em todas as fases.
-   **Sem Inferência sem Evidência**: Conclusões são baseadas em dados coletados e correlacionados.
-   **Separação entre Coleta e Análise**: Distinção clara das responsabilidades de cada etapa.
-   **Outputs Sempre Estruturados**: Facilita a integração e o consumo dos dados gerados.
-   **Validação Humana entre Etapas**: Essencial para garantir a precisão e relevância dos resultados.

### 8.2. O que o Framework Não Faz

É importante ressaltar as limitações do framework:

-   **Não automatiza a investigação completa**: Requer intervenção e decisão humana.
-   **Não substitui ferramentas OSINT**: Complementa, mas não substitui ferramentas especializadas.
-   **Não executa varredura ativa**: Foca em dados publicamente disponíveis e passivos.
-   **Não gera conclusões autônomas**: As análises e relatórios são construídos com base na supervisão do operador.
-   **Não elimina a necessidade de revisão do operador**: A validação humana é um componente crítico.

---

## 9. Resultado Esperado

Ao final da execução da pipeline, o operador terá:

-   **Dados Estruturados**: Informações organizadas por etapa da investigação.
-   **Correlação de Entidades e Ativos**: Relações claras entre os diferentes elementos encontrados.
-   **Lacunas Explícitas**: Identificação de áreas onde a informação é escassa ou ausente.
-   **Relatório Coerente**: Um relatório final alinhado com o objetivo inicial da investigação.

Este framework é uma ferramenta valiosa para demonstrar que, embora os LLMs sejam poderosos, eles não substituem um processo investigativo bem definido. O verdadeiro valor reside em utilizar o modelo com:

-   Um escopo claramente definido.
-   Comandos apropriados.
-   Validação contínua entre as etapas.
-   Controle ativo do operador.
