![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
![Version](https://img.shields.io/badge/Version-1.6.0-informational)
![Format](https://img.shields.io/badge/Format-JSON%20%26%20Agent%20Specs-orange)
![Framework](https://img.shields.io/badge/Framework-OpenCode-blueviolet)

# OSINT Agentic Framework for OpenCode

## 1. Overview

This operational framework has been refactored to support multiple OSINT investigation purposes. Now, the operator defines the **operation purpose** at the beginning of the process, and the framework dynamically suggests the most suitable pipeline.

### Supported Purposes:
- **Institutions**: Focused on companies, domains, and corporate assets (Standard Pipeline).
- **Individuals**: Focused on the digital footprint of natural persons, exposure, and links.
- **Disinformation Campaign**: Analysis of narratives, coordination, and amplification.
- **Narrative Analysis**: Mapping of information ecosystems and influence.
- **Data Leak**: Assessment of impact, sensitivity, and origin of leaks.

---

## 2. ⚠️ Disclaimer and Ethical Use

This framework is an **Open Source Intelligence (OSINT) automation tool**. The use of this material must respect the following guidelines:

- **Legality**: Ensure that your activities comply with local laws (such as LGPD in Brazil or GDPR in Europe).
- **Ethics**: Do not use this framework for harassment, doxing, stalking, or any illegal activity.
- **Responsibility**: The author is not responsible for the misuse of the collected information or for actions taken based on the generated reports.
- **Transparency**: This framework focuses on **public and open data**. Do not use it to attempt to access private or protected systems.

---

## 3. How the Dynamic Pipeline Works

Unlike automatic systems, this framework uses **dynamic guidance**. At the end of each command, the agent suggests the next step based on the chosen operation type.

1. **Case Intake**: The operator defines the `operation_type` in `intake.json`.
2. **Command Suggestion**: The output of each stage contains the `next_command` field.
3. **Manual Execution**: The operator maintains full control, executing the suggested command after validating the previous result.

---

## 4. Folder Structure

```
specs/ → Logical definitions (specific by operation type).
.opencode/commands/ → Executable commands.
cases/ → Case data.
  ├── <case-id>/
  │   ├── intake.json → Purpose and target definition.
  │   ├── runs/ → Outputs of each stage.
  │   └── memory/ → Lessons learned (postmortem).
```

---

## 5. Step by Step: Starting an Operation

### 5.1. Prepare the Intake
Create the case folder and edit the `intake.json`. Below are examples for each operation type:

#### Institutions
```json
{
  "case_id": "CORP-001",
  "operation_type": "institutions",
  "target_name": "Target Company S.A.",
  "target_url": "https://target.com",
  "scope_type": "company",
  "analysis_goal": "Map QSA and technical assets.",
  "restrictions": ["Public sources only"]
}
```

#### Individuals
```json
{
  "case_id": "IND-001",
  "operation_type": "individuals",
  "target_name": "Target Name",
  "analysis_goal": "Map digital footprint and social exposure.",
  "restrictions": ["Respect privacy laws"]
}
```

#### Disinformation
```json
{
  "case_id": "DIS-001",
  "operation_type": "disinformation_campaign",
  "target_name": "Narrative X about Subject Y",
  "analysis_goal": "Identify origin and amplifiers.",
  "restrictions": ["Focus on open networks"]
}
```

#### Narratives
```json
{
  "case_id": "NAR-001",
  "operation_type": "narrative_analysis",
  "target_name": "Theme of Interest",
  "analysis_goal": "Map influence ecosystem.",
  "restrictions": ["Qualitative analysis"]
}
```

#### Leaks
```json
{
  "case_id": "LEAK-001",
  "operation_type": "data_leak",
  "target_name": "Affected Entity",
  "analysis_goal": "Validate extent and sensitivity of the leak.",
  "restrictions": ["Do not download full databases"]
}
```

### 5.2. Execute the Intake
```bash
/case-intake
```
The agent will validate the operation type and suggest the next command (e.g., `/framing` for institutions or `/framing-indiv` for individuals).

### 5.3. Follow the Pipeline
Execute the suggested commands sequentially. The framework will guide you through the `next_command` field.

#### Example: Institutions Pipeline
1. `/case-intake` -> Suggests `/framing`
2. `/framing` -> Suggests `/corporate-collection`
3. `/corporate-collection` -> Suggests `/expansion`
4. `/expansion` -> Suggests `/entity-graph`
5. `/entity-graph` -> Suggests `/institutional-validation`
6. `/institutional-validation` -> Suggests `/technical-surface`
7. `/technical-surface` -> Suggests `/brand-social-analysis`
8. `/brand-social-analysis` -> Suggests `/unstructured-extraction`
9. `/unstructured-extraction` -> Suggests `/geo-context`
10. `/geo-context` -> Suggests `/correlation`
11. `/correlation` -> Suggests `/report`
12. `/report` -> Suggests `/postmortem`

#### Example: Individuals Pipeline
1. `/case-intake` -> Suggests `/framing-indiv`
2. `/framing-indiv` -> Suggests `/individual-collection`
3. `/individual-collection` -> Suggests `/expansion`
4. `/expansion` -> Suggests `/entity-graph`
5. `/entity-graph` -> Suggests `/identity-validation`
6. `/identity-validation` -> Suggests `/individual-footprint`
7. `/individual-footprint` -> Suggests `/individual-social-analysis`
8. `/individual-social-analysis` -> Suggests `/unstructured-extraction`
9. `/unstructured-extraction` -> Suggests `/geo-context`
10. `/geo-context` -> Suggests `/correlation`
11. `/correlation` -> Suggests `/report`

#### Other Pipelines (Specialized Flows)

- **Disinformation**: 
  `/case-intake` -> `/framing-disinfo` -> `/disinfo-collection` -> `/expansion` -> `/content-analysis` -> `/disinfo-actor-mapping` -> `/correlation` -> `/report`

- **Narratives**: 
  `/case-intake` -> `/framing-narrative` -> `/narrative-collection` -> `/expansion` -> `/content-analysis` -> `/narrative-ecosystem-map` -> `/correlation` -> `/report`

- **Leaks**: 
  `/case-intake` -> `/framing-leak` -> `/leak-collection` -> `/expansion` -> `/leak-impact-analysis` -> `/leak-data-audit` -> `/unstructured-extraction` -> `/correlation` -> `/report`

---

## 6. Prerequisites
- **OpenCode** installed.
- **EXA** enabled (`OPENCODE_ENABLE_EXA=1`).

---

## 7. Customization
To add new pipelines or adjust existing ones, edit the files in `specs/` and the corresponding commands in `.opencode/commands/`. The framework is modular and designed to evolve with the operator's needs.

---

## 8. Credits and License
Developed for use with the **OpenCode** platform.
License: **GPL v3**.
