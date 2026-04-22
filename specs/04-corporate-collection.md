# 04 — Corporate Collection

## Objetivo
Coletar e consolidar identificadores corporativos públicos e sinais institucionais verificáveis do alvo, com foco em due diligence corporativa leve.

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
- Use o site cnpj.biz + nome de domínio para tentar inferir o CNPJ
- Se encontrar match plausível mas não definitivo, registrar como `candidate`, não descartar
- Se encontrar dado em fonte pública plausível e coerente com o alvo, promover para `confirmed`
- Separar claramente:
  - dado confirmado
  - dado candidato
  - lacuna remanescente

---

## Estratégia de busca obrigatória

A coleta deve seguir um fluxo progressivo baseado em classes de fonte.

O agente NÃO pode encerrar a coleta sem executar todas as camadas abaixo:

1. Fonte primária
   - site oficial
   - páginas internas do site (contato, sobre, rodapé, políticas, footer)

2. Busca geral
   - nome da entidade + identificador corporativo
   - domínio + identificador corporativo

3. Busca expandida
   - nome da entidade + termos institucionais
   - domínio + termos institucionais
   - nome da entidade + razão social
   - nome da entidade + registro empresarial
   - nome da entidade + CNPJ

4. Diretórios e agregadores corporativos
   - plataformas públicas que indexam dados empresariais
   - diretórios comerciais
   - agregadores de CNPJ
   - listagens empresariais públicas

5. Revalidação
   - qualquer resultado parcial deve ser reutilizado como pivô, inclusive podem ser usados de maneira cruzada (exemplo: dado A usado para validar o dado B)
   - executar nova busca usando:
     - nome legal, se encontrado
     - CNPJ candidato, se encontrado
     - endereço, telefone ou e-mail corporativo, se encontrados
     - domínio e nome fantasia em combinação

O agente deve:

- avançar de camada se não encontrar resultado
- NÃO parar após a camada 1
- NÃO considerar ausência de dado sem executar a camada 4
- usar a camada 5 para tentar confirmar candidate matches
- registrar no `search_trace` quais classes de fonte foram usadas

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

3. Se um resultado parcial aparecer, reutilizá-lo como pivô de segunda busca

4. Consolidar o melhor match disponível, sem inventar

5. Registrar o que permaneceu ausente

6. Produzir um resumo curto de coleta para os próximos módulos

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
    "evidence_level": "confirmed|candidate|unresolved"
  },
  "official_channels": [],
  "corporate_registry_signals": [],
  "public_litigation_signals": [],
  "search_trace": [],
  "unresolved_gaps": [],
  "collection_summary": "",
  "confidence": "low|medium|high"
}
