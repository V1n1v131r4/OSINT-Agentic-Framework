# 04 — Corporate Collection

## Objetivo

Coletar e consolidar identificadores corporativos públicos e sinais institucionais verificáveis do alvo, com foco em due diligence corporativa leve e correlação empresarial ampliada.

---

## Entradas obrigatórias

- normalized_target
- analysis_goal_normalized
- scope_modules
- investigation_vectors
- minimum_required_data
- known_gaps
- restrictions

## Entradas opcionais

- corporate_identifiers

Se qualquer entrada obrigatória estiver ausente ou inválida, NÃO prossiga.

---

## Instruções ao agente

- Coletar apenas dados corporativos e públicos
- Antes de concluir ausência de dado, usar websearch e webfetch
- Priorizar fontes e diretórios corporativos brasileiros presentes no repositório https://github.com/osintbrazuca/osint-brazuca como base de descoberta durante a coleta
- Priorizar fontes públicas que exibam:
  - CNPJ
  - razão social
  - nome fantasia
  - status cadastral
  - diretórios empresariais
  - sinais de processos públicos da empresa
- Se encontrar match plausível mas não definitivo, registrar como `candidate`, não descartar
- Se houver convergência coerente em pelo menos 2 fontes públicas plausíveis e independentes, promover para `confirmed`
- Separar claramente:
  - dado confirmado
  - dado candidato
  - lacuna remanescente

---

## Regra crítica

Esta etapa só pode concluir `unresolved` para CNPJ após:

- consultar o site oficial
- consultar pelo menos 2 classes de busca diferentes
- consultar pelo menos 1 diretório corporativo
- abrir via webfetch pelo menos 1 resultado plausível de diretório, se houver
- tentar pelo menos 3 pivôs distintos de nome, marca ou domínio
- tentar identificar nomes empresariais parecidos
- tentar identificar domínios parecidos

Se houver resultado plausível em diretório corporativo não aberto, a coleta NÃO pode ser encerrada.

---

## Regra de confirmação

Um dado corporativo pode ser promovido para `confirmed` quando houver:

- pelo menos 2 fontes públicas plausíveis e independentes
- convergência coerente entre essas fontes

A convergência pode usar, quando disponíveis:
- CNPJ
- razão social
- nome fantasia
- endereço
- telefone
- e-mail
- domínio
- CNAE / atividade econômica
- redes sociais
- outros sinais institucionais consistentes

Se houver apenas uma fonte plausível, ou convergência parcial insuficiente, registrar como `candidate`.

---

## Estratégia de busca obrigatória

A coleta deve seguir um fluxo progressivo baseado em classes de fonte.

O agente NÃO pode encerrar a coleta sem executar todas as camadas abaixo:

### 1. Fonte primária
- site oficial
- páginas internas do site:
  - contato
  - sobre
  - rodapé
  - políticas
  - footer
  - FAQ
  - termos
  - imprensa

Extrair, quando houver:
- razão social
- CNPJ
- endereço
- telefone
- e-mail
- WhatsApp
- domínios
- redes sociais

### 2. Busca geral
- nome da entidade + CNPJ
- domínio + CNPJ
- nome da entidade + razão social
- domínio + razão social
- site:<domínio> CNPJ
- site:<domínio> "razão social"

### 3. Busca expandida
- nome da entidade + registro empresarial
- nome da entidade + nome legal
- domínio sem TLD + CNPJ
- domínio sem TLD + razão social
- nome da entidade + cidade/estado, se disponível
- domínio + cidade/estado, se disponível
- nome da entidade + atividade econômica

### 4. Diretórios e agregadores corporativos (Foco em QSA)
O agente NÃO pode alegar necessidade de login sem antes exaurir estas fontes que fornecem o Quadro de Sócios e Administradores (QSA) publicamente:
- `casadosdados.com.br` (Altamente recomendado para QSA detalhado)
- `transparencia.cc` (Excelente para vínculos societários)
- `cnpj.biz`
- `econodata.com.br`
- `empresas.serasaexperian.com.br`
- Portais de transparência e Diários Oficiais

Extrair obrigatoriamente o Quadro de Sócios e Administradores (QSA). Se não encontrado em uma fonte, DEVE tentar as outras.

### 5. Empresas parecidas e relacionadas
Buscar:
- variações de nome fantasia
- variações de razão social
- abreviações
- grafias alternativas
- nomes parecidos no mesmo setor ou cidade
- múltiplos CNPJs potencialmente relacionados

Para cada candidato, tentar correlacionar por:
- sócios / administradores
- endereço
- telefone
- e-mail
- CNAE / atividade
- domínios
- redes sociais

### 6. Domínios parecidos
Buscar:
- grafias próximas
- domínios sem acento
- hífens
- números
- TLDs alternativos
- combinações com marca, cidade ou atividade

Correlacionar os domínios encontrados com:
- empresa principal
- empresas relacionadas
- contatos
- redes sociais

### 7. Redes sociais e presença pública
Buscar:
- LinkedIn
- Instagram
- Facebook
- YouTube
- outras plataformas relevantes

Extrair, quando houver:
- handle
- URL
- descrição
- localização
- e-mail
- telefone
- domínio associado

### 8. Contatos e WhatsApp
Buscar e consolidar:
- telefones
- e-mails
- formulários públicos
- links de WhatsApp
- botões ou menções explícitas a WhatsApp

Só registrar WhatsApp quando a associação estiver explícita na fonte.

### 9. Google Dorks (Recuperação de QSA, Documentos Públicos e Repositórios)
Se o QSA não for encontrado nos diretórios, o uso de Google Dorks é OBRIGATÓRIO para localizar sócios em documentos indexados. Além disso, os Google Dorks devem ser usados para encontrar outros documentos públicos e repositórios de código:

**Para Sócios e Documentos Legais:**
- `filetype:pdf "nome da empresa" (sócio OR administrador OR "quadro societário")`
- `filetype:pdf "nome da empresa" ("contrato social" OR "alteração contratual")`
- `filetype:pdf "nome da empresa" "ata de assembleia"`
- `site:linkedin.com/in "nome da empresa" (sócio OR owner OR "founder at")`
- `site:facebook.com "nome da empresa" (proprietário OR dono)`
- `site:instagram.com "nome da empresa" (proprietário OR dono)`
- `"nome da empresa" "quadro de sócios" site:jusbrasil.com.br`

**Para Documentos Públicos Gerais:**
- `filetype:pdf OR filetype:docx OR filetype:xlsx "nome da empresa" (relatório OR manual OR política OR "demonstrativo financeiro")`
- `"nome da empresa" intitle:index.of (manual OR docs OR backup)`
- `"nome da empresa" inurl:admin OR inurl:login`

**Para Repositórios de Código (GitHub/GitLab):**
- `site:github.com "nome da empresa"`
- `site:gitlab.com "nome da empresa"`
- `site:github.com "nome da empresa" (api_key OR password OR secret)` (para identificar vazamentos)

O agente deve extrair nomes de pessoas físicas desses documentos para alimentar o campo `partners` e URLs de documentos/repositórios para os campos `public_documents` e `code_repositories` (a serem adicionados).

### 10. Listagem de Funcionários (LinkedIn e Outros Diretórios)
- `site:linkedin.com/company/"nome da empresa"/people` (para listar funcionários)
- `site:linkedin.com/in "nome do funcionário" "nome da empresa"` (para perfis específicos)
- `"nome da empresa" "lista de funcionários"` (para outros diretórios)

O agente deve coletar nomes de funcionários, cargos e handles de LinkedIn/outras mídias sociais, correlacionando-os com a empresa.

### 11. Revalidação
Qualquer resultado parcial deve ser reutilizado como pivô, inclusive de maneira cruzada.

Executar nova busca usando:
- nome legal, se encontrado
- CNPJ candidato, se encontrado
- endereço, telefone ou e-mail corporativo, se encontrados
- domínio e nome fantasia em combinação
- nome fantasia + razão social
- nome fantasia + CNPJ
- domínio + CNPJ

O agente deve:
- avançar de camada se não encontrar resultado
- NÃO parar após a camada 1
- NÃO considerar ausência de dado sem executar a camada 4
- usar as camadas 5, 6, 7 e 8 para ampliar a cobertura e confirmar candidatos
- registrar no `search_trace` quais classes de fonte foram usadas
- registrar também queries e URLs abertas mais relevantes

---

## Tarefas

1. Tentar identificar prioritariamente:
   - CNPJ
   - razão social
   - nome fantasia
   - status cadastral

2. Tentar identificar sinais públicos de:
   - quadro societário em nível corporativo
   - canais oficiais da empresa
   - processos públicos envolvendo a empresa

3. Tentar identificar:
   - empresas relacionadas ou parecidas
   - múltiplos CNPJs plausíveis
   - domínios parecidos
   - handles de redes sociais
   - contatos públicos, incluindo WhatsApp quando explícito

4. Se um resultado parcial aparecer, reutilizá-lo como pivô de segunda busca

5. Consolidar o melhor match disponível, sem inventar

6. Registrar o que permaneceu ausente

7. Produzir um resumo curto de coleta para os próximos módulos

---

## Saída obrigatória

Retorne APENAS JSON válido, sem texto adicional.

```json
{
  "corporate_identity": {
    "cnpj": "",
    "legal_name": "",
    "trade_name": "",
    "registration_status": "",
    "partners": [
      {
        "name": "",
        "role": "",
        "social_handles": [],
        "evidence_level": "confirmed|candidate|unresolved"
      }
    ],
    "evidence_level": "confirmed|candidate|unresolved"
  },
  "related_companies": [
    {
      "cnpj": "",
      "legal_name": "",
      "trade_name": "",
      "relationship_type": "same_group|subsidiary|parent|partner|possible",
      "evidence_level": "confirmed|candidate|unresolved",
      "correlation_points": {
        "partners": [],
        "address": [],
        "phone": [],
        "email": [],
        "domain": [],
        "cnae": [],
        "social_handles": []
      }
    }
  ],
  "domains": [
    {
      "domain": "",
      "type": "official|related|similar",
      "evidence_level": "confirmed|candidate|unresolved",
      "notes": ""
    }
  ],
  "social_handles": [
    {
      "platform": "",
      "handle": "",
      "url": "",
      "evidence_level": "confirmed|candidate|unresolved"
    }
  ],
  "contacts": [
    {
      "type": "phone|email|whatsapp",
      "value": "",
      "source": "",
      "notes": ""
    }
  ],
  "official_channels": [],
  "corporate_registry_signals": [],
  "public_litigation_signals": [],
  "google_dorks_results": [
    {
      "query": "string",
      "finding": "string",
      "url": "string"
    }
  ],
  "public_documents": [
    {
      "title": "string",
      "url": "string",
      "type": "string (pdf, docx, xlsx, etc)",
      "source": "string"
    }
  ],
  "code_repositories": [
    {
      "name": "string",
      "url": "string",
      "platform": "string (github, gitlab, etc)",
      "owner": "string"
    }
  ],
  "employees": [
    {
      "name": "string",
      "role": "string",
      "social_handles": [
        {
          "platform": "string",
          "handle": "string",
          "url": "string"
        }
      ],
      "evidence_level": "confirmed|candidate"
    }
  ],
  "search_trace": [],
  "unresolved_gaps": [],
  "collection_summary": "",
  "confidence": "low|medium|high"
}

