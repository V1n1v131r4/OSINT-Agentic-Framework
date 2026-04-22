---
description: Executa o módulo 04 com coleta web explícita e salva automaticamente o output em runs
agent: collector-gpt
model: openai/gpt-5-mini
---

Siga estritamente a spec em @specs/04-corporate-collection.md.

Use como insumos obrigatórios os arquivos:
@cases/test-01/runs/01-case-intake.json
@cases/test-01/runs/02-framing-gpt.json

Objetivo desta execução:
- consolidar dados corporativos públicos do alvo
- tentar identificar CNPJ, razão social, nome fantasia, sinais registrais e sinais processuais corporativos
- preparar artefato de coleta para os próximos módulos

Instruções operacionais obrigatórias:
- Leia @cases/test-01/runs/01-case-intake.json
- Leia @cases/test-01/runs/02-framing-gpt.json
- Use websearch para descoberta de fontes públicas antes de concluir ausência de dado
- Use webfetch para abrir URLs específicas encontradas pelo websearch
- Priorize, nesta ordem:
  1. site oficial
  2. páginas de contato/sobre/rodapé
  3. registros empresariais públicos
  4. diretórios corporativos públicos
  5. bases públicas de processos
- Faça buscas como:
- Use websearch para descobrir fontes públicas antes de concluir ausência de dado
- Use webfetch para abrir páginas promissoras encontradas pelo websearch
- Priorize encontrar CNPJ e razão social antes de expandir para outros sinais
- Se uma fonte trouxer match plausível mas não definitivo, registre como candidate
- Faça buscas iterativas usando:
  - nome fantasia
  - domínio
  - nome fantasia + CNPJ
  - domínio + CNPJ
  - nome fantasia + razão social
  - site:<domínio> CNPJ
- Não parar na primeira busca sem resultado
- Reutilizar cada achado parcial como pivô para nova busca
- Gere APENAS JSON válido compatível com a spec 04
- Salve o resultado em @cases/test-01/runs/04-corporate-collection-gpt.json
- Se a pasta @cases/test-01/runs não existir, crie-a
- Após salvar, responda apenas com um JSON curto de status neste formato:

{
  "status": "ok",
  "output_file": "cases/test-01/runs/04-corporate-collection-gpt.json"
}

Regras obrigatórias:
- Não gerar texto fora do JSON
- Todos os campos de lista devem ser arrays JSON válidos
- Não usar markdown
- Não adicionar campos extras
- Se faltar input, retornar erro estruturado em JSON
