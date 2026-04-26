![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
![Version](https://img.shields.io/badge/Version-1.0.0-informational)
![Format](https://img.shields.io/badge/Format-JSON%20%26%20Agent%20Specs-orange)
![Framework](https://img.shields.io/badge/Framework-OpenCode-blueviolet)
![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)

# OSINT Agentic Framework for OpenCode

## DISCLAIMER

This repository is neither an OSINT tool nor an autonomous investigative agent. It is an **operational framework for disciplined use of LLMs in an intelligence context**, designed to solve a common problem: the use of unstructured language models, which leads to fragile correlations, implicit validations, and loss of analytical control.

In this model, the LLM acts as the executor of specific steps, while the operator maintains full control over scope, validation, and correlation. The proposal is not to automate the analysis, but to **structure the process, reduce bias, ensure traceability, and preserve OPSEC** — especially in scenarios where generalist agents produce results that are difficult to audit.

The proposal is not to automate the analysis, but rather to **structure the investigative process** to reduce biases, increase traceability, and preserve operational security (**OPSEC**). This method is essential in scenarios where exclusive reliance on generalist agents can compromise the quality and reliability of results.

---

### Framework Pillars

This modular system was developed to provide a structured and controlled process of **AI-assisted OSINT investigations**, highlighted by:

- **Operator Control**: each step is explicitly executed and validated, avoiding implicit model decisions  
- **Modularity**: the pipeline separates critical functions, preventing mixing of collection, validation, and correlation  
- **Separation of Duties**: each phase has a defined role, reducing interpretation and inference errors  
- **Disciplined Use of LLMs**: the model is limited to specific tasks, avoiding hallucinations and unverified correlations  

The goal is to serve as a **base framework for intelligence production with LLMs under control**, enabling operators to build their own investigation pipelines with clear validation, correlation, and evidence criteria, adapting the flow according to operational needs.

---

## 1. Framework Overview

It is essential to understand that this project **is not** an automatic OSINT tool. Instead, it functions as an **operational framework** where:

- Each step of the investigation is represented by a specific command.
- The operator is responsible for controlling the execution of each command.
- AI models (LLMs) are employed to perform specific and auxiliary tasks.
- There is no full autonomy of the AI agent; human supervision is constant.

---

## 2. Pipeline Scope

The current version of this pipeline has been designed under the premise that the **operation target is an institution** (such as a company, organization, brand, or domain). The steps were carefully developed to:

- Map the institutional digital presence and that of its partners.
- Identify technical assets associated with the institution.
- Validate corporate signals and corporate structure (QSA).
- Execute Google Dorks for discovery of hidden documents and mentions.
- Correlate structured data and social media in the context of *due diligence*.

### 2.1. Individual Investigation: Specific Considerations

If the objective is the investigation of **individuals**, it is crucial to note that the current pipeline **is not optimized for this scenario**. Existing modules:

- Allow analysis of natural persons when identified as partners or administrators.
- Prioritize institutional assets and correlation of these with their legal representatives.
- Include search vectors for partners' social media to validate institutional link.

#### 2.1.1. Necessary Adjustments for Individuals

To adapt the framework to individual investigation, it is recommended to:

- **Redefine the `scope_definition`**: Adjust the scope in the `case-intake` file to reflect the new objective.
- **Adapt Collection Modules**: Modify collection modules (especially 03 to 09) for sources relevant to individuals.
- **Include Specific Sources and Vectors**: Add sources like personal social networks, public records, digital identity correlation, and exposure analysis.

#### 2.1.2. Legal and Ethical Considerations

Investigating individuals entails **additional risks** related to privacy, local legislation, and misuse of personal data. This framework was designed to work with **public data and institutional context**. Any adaptation for individuals must rigorously respect:

- Applicable legal limits.
- Principles of necessity and proportionality.
- Restrictions defined in the `scope_definition`.

**Recommendation**: For use with individuals, **do not use the standard pipeline without adjustments**. Treat each case separately and explicitly adapt the modules for this context.

---

## 3. Prerequisites

To use the framework, the following prerequisites must be met:

### 3.1. OpenCode

Install and configure OpenCode according to the standard instructions.

### 3.2. Execution with EXA

To enable external search functionality and ensure effectiveness of collection modules, OpenCode must be run with the environment variable `OPENCODE_ENABLE_EXA` enabled:

```bash
OPENCODE_ENABLE_EXA=1 opencode .
```

**Importance of EXA**: Without EXA, collection modules (03 to 09) will have limited capabilities, resulting in incomplete information and significantly reducing the pipeline's operational utility.

---

## 4. Project Structure

The project is organized as follows:

```
specs/ → Logical definition of pipeline steps.
.opencode/commands/ → Contains executable commands of the framework.
cases/ → Stores specific data for each investigation case.
  ├── <case-id>/ → Directory for a specific case.
  │   └── intake.json → Raw input file for the case.
runs/ → Stores outputs generated by each execution step.
```

The pipeline operates sequentially:

1.  The operator defines the investigation case.
2.  Commands are executed one by one.
3.  Each command generates a structured JSON output file.
4.  Outputs from one step feed the subsequent step.
5.  The operator validates each step before proceeding.

### 4.1. Mandatory Step: Case Intake

Before starting any execution, it is mandatory to create the `intake.json` file inside the case directory (`cases/<case-id>/intake.json`). This file serves as the raw input for the investigation.

**Example of `intake.json`:**

```json
{
  "target": "domain.com.br",
  "analysis_goal": "map digital presence and infrastructure",
  "scope_definition": "public data only, no natural person analysis"
}
```

---

## 5. How To Run

Start OpenCode with EXA enabled and run each command individually, validating outputs at each step:

1.  Start OpenCode:
    ```bash
    OPENCODE_ENABLE_EXA=1 opencode .
    ```
2.  Execute commands in sequence (example):
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

## 6. Starting a New Project

When starting a new investigation, follow these steps:

1.  **Edit `cases/<case-id>/intake.json`**: Update with data from the new operation.
2.  **Clear Runs History**: Delete outputs from previous executions to avoid conflicts:
    ```bash
    rm -rf cases/<case-id>/runs/*
    ```
    *Alternatively, to keep history, move the previous case directory (e.g., `cases/test-01` to `cases/test-02`) and create a new `intake.json` for the new operation.*

---

## 7. How to Adapt the Pipeline for Different Operation Types

This pipeline was designed as a base structure. This means that **the logic can (and should) be adjusted depending on the investigation type, target, and operational objective**.

Adaptation occurs on two levels:

- `specs/` → defines analytical logic  
- `.opencode/commands/` → defines execution  

---

## Adjusting the Logic (files in `specs/`)

### 01 — `case-intake`

Defines **the investigation entry point**.

Edit when you want to change:
- target type (company, individual, domain)
- mandatory data
- scope restrictions
- minimum criteria to start execution

---

### 02 — `case-framing`

Defines **how the problem will be structured before collection**.

Edit to adjust:
- hypothesis construction
- investigation vectors
- analytical rigor level
- gap registration

---

### 03 — `surface-expansion`

Defines **how initial collection is performed**.

Edit to adjust:
- which signals to search first
- allowed sources
- priority among identifiers (domain, name, brand)
- expansion depth

---

### 04 — `entity-graph`

Defines **the entity structure of the investigation**.

Edit to adjust:
- entity types (company, domain, person, channel, etc.)
- graph granularity level
- inclusion/exclusion criteria
- identifier normalization

Use this module when you want to change **how data is organized**.

---

### 04 — `corporate-collection`

Defines **deep corporate collection**.

Edit to adjust:
- priority among:
  - CNPJ
  - corporate name
  - trade name (fantasy name)
- use of directories (cnpj.biz, econodata, etc.)
- search for similar companies
- correlation among multiple CNPJs
- identification of related domains
- collection of corporate social networks
- identification of public contacts (including WhatsApp when explicit)

Use this module when you want to change **collection behavior**.

---

### 05 — `institutional-validation`

Defines **how corporate data is validated**.

Edit to adjust:
- confirmation criterion (`candidate` vs `confirmed`)
- minimum number of sources
- points of convergence (address, domain, partners, etc.)
- inconsistency tolerance

Use this module to control **quality and trustworthiness of information**.

---

### 06 — `technical-surface`

Defines **technical infrastructure analysis**.

Edit to adjust:
- collection of:
  - DNS
  - IP
  - ASN
  - email
- identification of exposed services
- technical depth level

Use this module to control **infrastructure visibility**.

---

### 07 — `brand-social-analysis`

Defines **analysis of public presence and official channels**.

Edit to adjust:
- platforms analyzed
- official channel validation criteria
- branding consistency signals
- related profile identification

---

### 08 — `unstructured-extraction`

Defines **extraction of data from unstructured content**.

Edit to adjust:
- types of extracted data:
  - emails
  - phones
  - URLs
- normalization rules
- duplicate handling
- filtering out weak data

---

### 09 — `geo-context`

Defines **how geographic context is factored into analysis**.

Edit to adjust:
- allowed detail level
- types of geographic signals
- inference boundaries

---

### 10 — `correlation`

Defines **the analytical core of the pipeline**.

Edit to adjust:
- relationship construction
- definition of:
  - patterns
  - anomalies
  - gaps
- evidence criteria
- separation between direct and indirect relations

This module most affects **intelligence quality**.

---

### 11 — `report`

Defines **how the final output is presented**.

Edit to adjust:
- report structure
- detail level
- risk and hypothesis communication style

---

### 12 — `postmortem`

Defines **execution learning**.

Edit to adjust:
- failure logging
- continuous improvement
- knowledge reuse

---

## Adjusting the Execution (files in `.opencode/commands/`)

Commands control **how the pipeline runs**.

Edit when you want to change:

- execution order
- chaining between steps
- model used
- operational rules of the step
- agent behavior

---

### Main Points for Editing

#### Inputs
Define which files feed each step.

#### Output
Defines where the result will be saved.

#### Operational Instructions
Allow adjustment of behavior, e.g.:
- require websearch/webfetch
- prevent inference
- force multiple sources
- block progress without minimum evidence

---

## Practical Rule

- `specs/` → change **what the model does**
- `commands/` → change **how and when it does it**

---

## Adaptation Examples

### Data Leak / Breach Analysis

Objective: identify origin, impact, and possible correlations of a public leak.

Main adjustments:
- `03-surface-expansion` → prioritize search for dumps, forums, paste sites  
- `08-unstructured-extraction` → extract emails, usernames, data patterns  
- `04-entity-graph` → organize identities, domains, and relations  
- `10-correlation` → identify patterns, data reuse, and clusters  

---

### Digital Identity Attribution (username / alias)

Objective: correlate multiple profiles and identify consistency between aliases.

Main adjustments:
- `03-surface-expansion` → search for usernames and variations  
- `04-entity-graph` → map profiles, aliases, and platforms  
- `07-brand-social-analysis` → validate presence and consistency across channels  
- `05-identity-validation` (or equivalent) → validate signal convergence  
- `10-correlation` → consolidate relationships between profiles  

---

### Disinformation Campaign Analysis

Objective: identify dissemination patterns, origin, and coordinated behavior.

Main adjustments:
- `03-surface-expansion` → collect initial content and sources  
- `07-brand-social-analysis` → map involved channels and profiles  
- `08-unstructured-extraction` → extract messages, links, and language patterns  
- `04-entity-graph` → organize actors, channels, and contents  
- `10-correlation` → identify patterns, repetition, and coordination  

---

## Final Recommendation

Avoid changing multiple modules simultaneously.

Ideal practice is:

1. adjust one step  
2. run a test case  
3. validate output  
4. iterate  

This preserves consistency, eases debugging, and avoids pipeline degradation.

---

## 8. Operational Principles and Limitations

### 8.1. Operational Principles

The pipeline design is guided by the following principles aimed at optimizing LLM use and guaranteeing investigation quality:

-   **One Step at a Time**: Focus on execution and validation of each module individually.
-   **No Complete Automatic Execution**: The operator retains control at all stages.
-   **No Inference Without Evidence**: Conclusions are based on collected and correlated data.
-   **Separation Between Collection and Analysis**: Clear distinction of responsibilities in each step.
-   **Always Structured Outputs**: Facilitates integration and consumption of generated data.
-   **Human Validation Between Steps**: Essential to ensure accuracy and relevance.

### 8.2. What the Framework Does Not Do

It is important to highlight the framework's limitations:

-   **Does not automate complete investigation**: Requires human intervention and decision.
-   **Does not replace OSINT tools**: Complements but does not substitute specialized tools.
-   **Does not perform active scanning**: Focuses on publicly available and passive data.
-   **Does not generate autonomous conclusions**: Analyses and reports are built under operator supervision.
-   **Does not eliminate need for operator review**: Human validation is a critical component.

---

## 9. Expected Result

At the end of pipeline execution, the operator will have:

-   **Structured Data**: Information organized by investigation step.
-   **Entity and Asset Correlation**: Clear relationships between different discovered elements.
-   **Explicit Gaps**: Identification of areas where information is scarce or missing.
-   **Coherent Report**: A final report aligned with the investigation's initial objective.

This framework is a valuable tool to demonstrate that, although LLMs are powerful, they do not replace a well-defined investigative process. The real value lies in using the model with:

-   A clearly defined scope.
-   Appropriate commands.
-   Continuous validation between steps.
-   Active operator control.