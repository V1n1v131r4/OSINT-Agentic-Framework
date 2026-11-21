#!/usr/bin/env python3
"""Check the saved inputs for the expansion stage."""

import argparse
import json
from pathlib import Path
import sys


COLLECTION_NAMES = {
    "institutions": "corporate",
    "individuals": "individual",
    "disinformation_campaign": "disinfo",
    "narrative_analysis": "narrative",
    "data_leak": "leak",
}


def reject_json_constant(value):
    raise ValueError(f"valor JSON inválido: {value}")


def read_object(path):
    try:
        data = json.loads(path.read_text(encoding="utf-8"), parse_constant=reject_json_constant)
    except (OSError, ValueError) as error:
        raise ValueError(f"{path}: {error}") from error
    if not isinstance(data, dict):
        raise ValueError(f"{path}: esperado um objeto JSON")
    return data


def require_field(data, path, field, expected, check):
    if field not in data:
        raise ValueError(f"{path}: campo obrigatório ausente: {field}")
    value = data[field]
    if not check(value):
        raise ValueError(f"{path}: campo {field}: esperado {expected}")
    return value


def is_nonempty_text(value):
    return isinstance(value, str) and bool(value.strip())


def validate_inputs(case_dir, prefer_claude):
    runs = case_dir / "runs"
    intake_path = runs / "01-case-intake.json"
    intake = read_object(intake_path)
    for field in ("target_name", "analysis_goal", "scope_definition"):
        require_field(intake, intake_path, field, "texto não vazio", is_nonempty_text)
    operation_type = require_field(
        intake, intake_path, "operation_type", ", ".join(COLLECTION_NAMES),
        lambda value: isinstance(value, str) and value in COLLECTION_NAMES,
    )

    framing_path = runs / "02-framing-gpt.json"
    claude_path = runs / "02-framing-claude.json"
    if prefer_claude and claude_path.exists():
        framing_path = claude_path
    framing = read_object(framing_path)
    for field in ("investigation_vectors", "known_gaps"):
        require_field(framing, framing_path, field, "array", lambda value: isinstance(value, list))

    collection_path = runs / f"04-{COLLECTION_NAMES[operation_type]}-collection-gpt.json"
    collection = read_object(collection_path)
    require_field(
        collection, collection_path, "confidence", "low, medium ou high",
        lambda value: value in ("low", "medium", "high"),
    )
    return (intake_path, framing_path, collection_path)


def main():
    parser = argparse.ArgumentParser(description="Valida os artefatos de entrada da expansão.")
    parser.add_argument("--claude", action="store_true", help="Prefere o framing do Claude.")
    parser.add_argument("case_dir", type=Path, help="Diretório do caso.")
    args = parser.parse_args()
    try:
        paths = validate_inputs(args.case_dir, args.claude)
    except ValueError as error:
        print(json.dumps({"status": "error", "message": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps({"status": "ok", "inputs": [str(path) for path in paths]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
