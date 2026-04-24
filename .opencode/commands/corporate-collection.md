---
description: Executa o módulo 04 com coleta web avançada e correlações corporativas
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/04-corporate-collection.md.

Use como insumos obrigatórios os arquivos:
@cases/{{case_id}}/runs/01-case-intake.json
@cases/{{case_id}}/runs/02-framing-gpt.json

Objetivo desta execução:
- consolidar dados corporativos públicos do alvo
- identificar prioritariamente CNPJ, razão social, nome fantasia e status cadastral
- identificar obrigatoriamente o Quadro de Sócios e Administradores (QSA)
- identificar empresas relacionadas, domínios semelhantes, redes sociais, contatos e WhatsApp
- executar Google Dorks para encontrar documentos e menções ocultas
- preparar artefato de coleta com máxima cobertura e correlações para os próximos módulos

Instruções operacionais obrigatórias:
- Leia @cases/{{case_id}}/runs/01-case-intake.json
- Leia @cases/{{case_id}}/runs/02-framing-gpt.json
- Use websearch para descoberta de fontes públicas antes de concluir ausência de dado
- Use webfetch para abrir URLs específicas encontradas pelo websearch
- Priorize encontrar CNPJ e razão social antes de expandir para outros sinais
- NÃO encerrar a coleta sem executar a estratégia completa da spec
- NÃO aceitar ausência de CNPJ enquanto houver match plausível não aberto em diretório ou agregador corporativo
- Se houver resultado promissor em diretório corporativo, faça webfetch obrigatoriamente antes de concluir ausência
- Se uma fonte trouxer match plausível mas não definitivo, registre como `candidate`
- Se houver convergência coerente em pelo menos 2 fontes públicas plausíveis e independentes, registre como `confirmed`
- Reutilize cada achado parcial como pivô para nova busca

Fluxo de busca obrigatório:
1. Site oficial
   - home
   - páginas de contato, sobre, rodapé, políticas, FAQ, termos, imprensa
   - extrair: razão social, CNPJ, endereço, telefone, e-mail, WhatsApp, domínios, redes sociais
2. Busca por marca e domínio
   - nome fantasia
   - nome legal
   - domínio
   - domínio sem TLD
   - site:<domínio> CNPJ
   - site:<domínio> razão social
3. Diretórios corporativos obrigatórios (Foco em QSA)
   - site:casadosdados.com.br (Prioridade para QSA)
   - site:transparencia.cc (Prioridade para QSA)
   - site:cnpj.biz
   - site:econodata.com.br
   - site:empresas.serasaexperian.com.br
   - Junta Comercial / Receita Federal
   - NÃO aceitar "necessidade de login" sem antes abrir pelo menos 2 desses diretórios via webfetch.
4. Busca por empresas parecidas e relacionadas
   - variações de nome fantasia
   - variações de razão social
   - grafias abreviadas
   - nome + cidade/estado
   - nome + atividade
   - listar todos os CNPJs plausíveis encontrados
5. Correlação obrigatória dos candidatos
   - sócios / administradores
   - endereço
   - telefone
   - e-mail
   - domínio
   - CNAE / atividade econômica
   - redes sociais
   - WhatsApp
6. Domínios parecidos
   - gerar e buscar:
     - grafias próximas
     - variações sem acento
     - hífens e números
     - extensões diferentes (.com, .com.br, .net, .org)
   - tentar correlacionar os domínios com a empresa-alvo e empresas relacionadas
7. Redes sociais e presença pública
   - LinkedIn
   - Instagram
   - Facebook
   - YouTube
   - outras plataformas relevantes
   - extrair handles, URLs, descrição, localização e contatos
8. Contatos e WhatsApp
   - capturar telefones encontrados em:
     - site oficial
     - redes sociais
     - diretórios
     - mapas e listagens públicas
   - identificar números com sinal de WhatsApp quando isso estiver explícito na fonte
9. Google Dorks (Recuperação de QSA, Documentos Públicos e Repositórios)
   - **Para Sócios e Documentos Legais:**
     - `filetype:pdf "nome da empresa" (sócio OR administrador OR "quadro societário")`
     - `filetype:pdf "nome da empresa" ("contrato social" OR "alteração contratual")`
     - `filetype:pdf "nome da empresa" "ata de assembleia"`
     - `site:linkedin.com/in "nome da empresa" (sócio OR owner OR "founder at")`
     - `site:facebook.com "nome da empresa" (proprietário OR dono)`
     - `site:instagram.com "nome da empresa" (proprietário OR dono)`
     - `"nome da empresa" "quadro de sócios" site:jusbrasil.com.br`
   - **Para Documentos Públicos Gerais:**
     - `filetype:pdf OR filetype:docx OR filetype:xlsx "nome da empresa" (relatório OR manual OR política OR "demonstrativo financeiro")`
     - `"nome da empresa" intitle:index.of (manual OR docs OR backup)`
     - `"nome da empresa" inurl:admin OR inurl:login`
   - **Para Repositórios de Código (GitHub/GitLab):**
     - `site:github.com "nome da empresa"`
     - `site:gitlab.com "nome da empresa"`
     - `site:github.com "nome da empresa" (api_key OR password OR secret)` (para identificar vazamentos)
   - Se o QSA não foi encontrado nos diretórios, estas buscas são MANDATÓRIAS. Extrair nomes de pessoas físicas para `partners` e URLs de documentos/repositórios para `public_documents` e `code_repositories`.
10. Listagem de Funcionários (LinkedIn e Outros Diretórios)
   - `site:linkedin.com/company/"nome da empresa"/people` (para listar funcionários)
   - `site:linkedin.com/in "nome do funcionário" "nome da empresa"` (para perfis específicos)
   - `"nome da empresa" "lista de funcionários"` (para outros diretórios)
   - Coletar nomes de funcionários, cargos e handles de LinkedIn/outras mídias sociais, correlacionando-os com a empresa para o campo `employees`.
11. Rebusca por pivôs
   - nome legal, se encontrado
   - CNPJ candidato, se encontrado
   - endereço, telefone ou e-mail corporativo, se encontrados
   - domínio e nome fantasia em combinação
   - nome fantasia + razão social
   - nome fantasia + CNPJ
   - domínio + CNPJ

Buscas mínimas obrigatórias antes de concluir `unresolved` para CNPJ:
- pelo menos 1 busca com domínio
- pelo menos 1 busca com nome fantasia ou marca
- pelo menos 1 busca em diretório corporativo
- pelo menos 1 webfetch em resultado plausível de diretório, se houver
- pelo menos 1 tentativa de buscar empresas parecidas
- pelo menos 1 tentativa de buscar domínios parecidos
- pelo menos 3 pivôs distintos no total

Critério mínimo de validação para `confirmed`:
- pelo menos 2 fontes públicas plausíveis e independentes
- convergência coerente em pelo menos 2 dos seguintes pontos, quando disponíveis:
  - CNPJ
  - razão social
  - nome fantasia
  - endereço
  - telefone
  - e-mail
  - domínio
  - CNAE / atividade
  - redes sociais

Gere APENAS JSON válido compatível com a spec 04.
Salve o resultado em @cases/{{case_id}}/runs/04-corporate-collection-gpt.json.
Se a pasta @cases/{{case_id}}/runs não existir, crie-a.

Após salvar, responda apenas com um JSON curto de status neste formato:

{
  "status": "ok",
  "output_file": "cases/{{case_id}}/runs/04-corporate-collection-gpt.json"
}

Regras obrigatórias:
- Não gerar texto fora do JSON
- Todos os campos de lista devem ser arrays JSON válidos
- Não usar markdown
- Não adicionar campos extras
- Se faltar input, retornar erro estruturado em JSON

