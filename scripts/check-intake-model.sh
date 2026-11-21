#!/bin/sh
set -eu

project_dir=$(CDPATH='' cd "$(dirname "$0")/.." && pwd)
cd "$project_dir"
intake_command=.opencode/commands/case-intake.md

model=$(awk '
    NR == 1 && $0 != "---" { exit }
    NR > 1 && $0 == "---" { exit }
    /^model:[[:space:]]+/ { print $2; exit }
' "$intake_command")

if [ -z "$model" ]; then
    printf 'Modelo do intake ausente em %s.\n' "$intake_command" >&2
    exit 1
fi

if ! command -v opencode >/dev/null 2>&1; then
    printf 'OpenCode não encontrado no PATH.\n' >&2
    exit 1
fi

if ! models=$(opencode models); then
    printf 'Falha ao consultar os modelos do OpenCode.\n' >&2
    exit 1
fi

if ! printf '%s\n' "$models" | grep -Fxq -- "$model"; then
    printf 'Modelo do intake indisponível: %s. Confira a lista com opencode models.\n' "$model" >&2
    exit 1
fi

printf 'Modelo do intake disponível: %s\n' "$model"
