# Rastreabilidade de evidências em análise de narrativas

Este contrato se aplica ao tipo de operação `narrative_analysis`.

## Coleta

Acrescente `evidence` ao artefato de coleta. Registre somente material efetivamente lido. Use IDs `E-…` estáveis no caso e preserve os IDs existentes quando a mesma evidência for coletada novamente. No corpus local com itens rotulados A–D, use `E-A` a `E-D`.

```json
{
  "id": "E-D",
  "source": "cases/exemplo/corpus.md#D",
  "collected_at": "2026-11-20",
  "excerpt": "Boletim local reproduz a nota B",
  "origin_id": "E-B"
}
```

Use a URL ou o caminho do artefato com o identificador do item e registre um trecho literal curto. Em `collected_at`, registre a data em que o material foi consultado, no formato YYYY-MM-DD. A data de publicação pertence ao conteúdo da fonte. Use `null` em `collected_at` se a data da consulta não estiver disponível. Se a evidência for a própria origem conhecida, use seu próprio ID em `origin_id`. Para republicações de origem conhecida, use o ID da evidência da qual derivam. Use `null` quando a origem for incerta. Registre um array vazio se a coleta não encontrou evidências.

## Correlação

Acrescente `findings` ao artefato de correlação. Registre lacunas em `known_gaps` quando faltar suporte para um achado. Use IDs `F-…` estáveis no caso e selecione as evidências conforme a afirmação específica.

```json
{
  "id": "F-difusao",
  "claim": "O boletim republicou a nota da associação.",
  "kind": "observation",
  "supports": ["E-B", "E-D"],
  "contradicts": [],
  "supporting_origin_count": 1,
  "confidence": "medium",
  "confidence_rationale": "A nota e sua republicação documentam o fluxo, com uma origem comum."
}
```

Use `observation`, `inference` ou `hypothesis` e justifique a confiança. Separe evidências favoráveis das contraditórias. Conte em `supporting_origin_count` as origens conhecidas distintas das evidências em `supports`, seguindo a cadeia de republicações. Origens desconhecidas ficam fora da contagem. A contagem mede origens documentadas. Avalie a independência e a relevância de cada origem na justificativa, mesmo quando diferentes registros têm origens distintas.

Uma republicação pode sustentar um achado sobre difusão. Para um achado que atribui um argumento à publicação original, cite a publicação original e trate as republicações como derivadas. Um argumento publicado pode sustentar uma afirmação sobre o que foi defendido. A confirmação do seu efeito exige evidência própria.

## Relatório

Copie os objetos de `findings` selecionados da correlação para `key_findings`, preservando seus IDs, vínculos e justificativas. Em `hypotheses`, inclua apenas objetos da correlação com `kind: "hypothesis"`. Cada ID de evidência remete ao registro original no JSON da coleta.
