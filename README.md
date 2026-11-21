![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
![Version](https://img.shields.io/badge/Version-0.3-informational)
![Framework](https://img.shields.io/badge/Framework-OpenCode-blueviolet)

# OSINT Agentic Framework for OpenCode

Este framework guia investigações de fontes abertas no OpenCode. Você define o objetivo e o escopo do caso, revisa o resultado de cada etapa e segue o comando indicado pelo framework. Ao fechar o caso, o OpenCode exporta o relatório final em Markdown.

A versão em inglês está na branch `en`.

## Primeiro caso: do clone ao relatório

O exemplo analisa quatro textos fictícios sobre uma proposta de ampliar o horário de uma biblioteca. O material está todo em um arquivo local.

### 1. Prepare o ambiente

Você precisa de Git, OpenCode, Python 3 e acesso ao provedor do modelo configurado. Para o exemplo local, basta o acesso ao modelo. Para casos que usam busca na web, habilite a integração EXA com `OPENCODE_ENABLE_EXA=1` no ambiente em que vai iniciar o OpenCode.

No terminal:

```sh
git clone https://github.com/V1n1v131r4/OSINT-Agentic-Framework.git
cd OSINT-Agentic-Framework
sh scripts/check-intake-model.sh
```

Se a checagem indicar que o modelo está indisponível, configure o provedor ou ajuste os modelos antes de seguir. Veja [Solução de problemas](#solução-de-problemas).

### 2. Crie os arquivos do caso

Ainda no terminal, execute o bloco abaixo. Use `NAR-001` tanto no nome da pasta quanto no campo `case_id`.

```sh
mkdir -p cases/NAR-001
cat > cases/NAR-001/intake.json <<'JSON'
{
  "case_id": "NAR-001",
  "operation_type": "narrative_analysis",
  "target_name": "Proposta fictícia de ampliar o horário de uma biblioteca",
  "analysis_goal": "Comparar os argumentos do corpus e identificar como foram republicados.",
  "restrictions": ["Use exclusivamente o corpus fictício local. Sem acesso a fontes externas."],
  "source_seed": ["cases/NAR-001/corpus.md"]
}
JSON
cat > cases/NAR-001/corpus.md <<'CORPUS'
Corpus fictício.
A — 2026-01-05 — Comunicado da biblioteca: proposta de ampliar o horário em duas noites.
B — 2026-01-06 — Associação de leitores: estudantes teriam mais acesso.
C — 2026-01-07 — Comissão de orçamento: questiona o custo da proposta.
D — 2026-01-08 — Boletim local reproduz a nota B, sem apuração independente.
CORPUS
```

### 3. Abra o OpenCode e siga a trilha

No terminal, a partir da raiz do projeto, execute `opencode`. Na caixa de entrada da **interface interativa do OpenCode**, digite:

```text
/case-intake cases/NAR-001/intake.json
```

O status deve incluir `"status": "ok"`, `"output_file": "cases/NAR-001/runs/01-case-intake.json"` e `"next_command": "/framing-narrative"`. Confira o arquivo e execute o próximo comando na mesma sessão. Você pode indicar o caso explicitamente, por exemplo com `/framing-narrative cases/NAR-001`.

Para esse exemplo, a sequência é `/framing-narrative` → `/narrative-collection` → `/expansion` → `/content-analysis` → `/narrative-ecosystem-map` → `/correlation` → `/report` → `/postmortem`. A cada etapa, revise o resultado e siga o `next_command` se o status for `ok`. O OpenCode pode solicitar autorização para gravar arquivos ou executar os scripts locais de validação e exportação.

### 4. Encontre o relatório final

O `/report` grava o relatório estruturado em `cases/NAR-001/runs/11-report-gpt.json`. Execute o `/postmortem` sugerido para fechar o caso e gerar o Markdown. O status final contém o caminho e o aviso:

> Relatório report_NAR-001.md gerado no diretório cases/NAR-001.

Abra `cases/NAR-001/report_NAR-001.md`. No exemplo, confira se o relatório distingue a republicação da nota B de uma confirmação independente do argumento.

## Escolha a trilha do seu caso

Para iniciar um novo caso, crie `cases/<case-id>/intake.json` a partir de [templates/intake.json](templates/intake.json). Preencha `case_id`, `operation_type`, `target_name`, `analysis_goal` e `restrictions`. Use `source_seed` para indicar documentos ou fontes de partida. O [schema do intake](schemas/intake.schema.json) lista os campos aceitos.

| `operation_type` | Finalidade | Primeiro comando após o intake |
| --- | --- | --- |
| `institutions` | Analisar uma instituição e seus registros e ativos públicos. | `/framing` |
| `individuals` | Avaliar presença pública de uma pessoa dentro do escopo definido. | `/framing-indiv` |
| `disinformation_campaign` | Examinar a disseminação de mensagens e as evidências de coordenação. | `/framing-disinfo` |
| `narrative_analysis` | Comparar narrativas, atores e circulação de conteúdo. | `/framing-narrative` |
| `data_leak` | Avaliar escopo, sensibilidade e impacto de uma exposição de dados. | `/framing-leak` |

Em todas as trilhas, a correlação alimenta o relatório e o postmortem fecha o caso. Em Narrativas, a coleta registra as evidências. A correlação vincula cada achado às fontes e conta as origens conhecidas. Para usar esse contrato em um caso antigo, reexecute a coleta e a correlação antes de gerar o relatório. [Contrato de evidências](specs/narrative-evidence.md)

## Solução de problemas

- **Modelo indisponível.** Execute `opencode models` para listar os modelos disponíveis e `sh scripts/check-intake-model.sh` para conferir o modelo do intake. Ao trocar de modelo, reveja `opencode.json` e os campos `model:` dos comandos da trilha em `.opencode/commands/`. A checagem inicial cobre o intake.
- **O comando não aparece ou o caso errado foi selecionado.** Abra o OpenCode a partir da raiz do repositório e informe o caminho de `intake.json` no comando interativo. Mantenha um caso por sessão.
- **A validação aponta um arquivo ou campo ausente.** Revise a saída da etapa que gera esse arquivo em `runs/` e reexecute a etapa antes de avançar.
- **O Markdown não apareceu.** Confirme que `/postmortem` terminou com `status: ok` e retornou `final_report`. Após salvar o postmortem, é possível repetir apenas a exportação no terminal com `python3 scripts/export-case-report.py -- "cases/NAR-001"`.

## Artefatos e memória

```text
cases/<case-id>/
├── intake.json                 # objetivo, alvo e restrições
├── runs/                       # artefatos JSON, incluindo 11-report-gpt.json
├── memory/13-postmortem.json    # revisão metodológica do caso
└── report_<case-id>.md          # relatório final
```

O postmortem também registra métodos reutilizáveis em `memory/global/playbooks.json`. O intake consulta essa memória e sugere até cinco métodos por recorrência, considerando o tipo do caso e os métodos transversais marcados como `all`. O reforço de cada método conta casos distintos. [Schema da memória](schemas/playbook-memory.schema.json) · [Regras de consolidação](specs/13-postmortem-learning.md)

As instruções analíticas ficam em `specs/`, os comandos interativos em `.opencode/commands/` e os contratos JSON em `schemas/`. A [rubrica de qualidade](rubrics/quality-rubric.md) define os critérios para revisar as saídas.

## Uso responsável e licença

Use fontes públicas e respeite o escopo autorizado e as leis aplicáveis, incluindo as regras de proteção de dados. É vedado usar o framework para assédio, doxing, perseguição, acesso a sistemas privados ou outras atividades ilegais. O operador é responsável pelas informações coletadas e pelas ações tomadas com base nos relatórios.

Licença GPL v3.
