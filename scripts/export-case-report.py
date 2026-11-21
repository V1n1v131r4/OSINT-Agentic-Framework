#!/usr/bin/env python3
"""Export the saved JSON report as Markdown in the case directory."""

import argparse
import json
from pathlib import Path
import re
import sys
from tempfile import NamedTemporaryFile


SECTIONS = (
    ("key_findings", "Principais achados"),
    ("hypotheses", "Hipóteses e interpretações"),
    ("gaps", "Lacunas"),
    ("risks", "Riscos e implicações"),
    ("next_steps", "Próximos passos"),
)

LABELS = {
    "id": "ID",
    "kind": "Tipo",
    "supports": "Evidências favoráveis",
    "contradicts": "Evidências contraditórias",
    "supporting_origin_count": "Origens de suporte",
    "confidence": "Confiança",
    "confidence_rationale": "Justificativa da confiança",
}


def markdown_text(value):
    if not isinstance(value, str):
        value = json.dumps(value, ensure_ascii=False)
    value = " ".join(value.splitlines())
    return re.sub(r"([\\`*_{}\[\]()<>#+!|~&-])", r"\\\1", value)


def render_item(item, level=0):
    prefix = "    " * level + "- "
    if isinstance(item, dict):
        heading = item.get("claim") or item.get("description")
        lines = [prefix + markdown_text(heading if heading else "Detalhes")]
        for field, value in item.items():
            if heading and field == ("claim" if item.get("claim") else "description"):
                continue
            label = LABELS.get(field, field.replace("_", " ").capitalize())
            label_line = "    " * (level + 1) + "- **" + markdown_text(label) + "**"
            if isinstance(value, dict) or (
                isinstance(value, list) and any(isinstance(entry, (dict, list)) for entry in value)
            ):
                lines.append(label_line)
                lines.extend(render_item(value, level + 2))
            else:
                text = ", ".join(map(markdown_text, value)) or "—" if isinstance(value, list) else markdown_text(value)
                lines.append(f"{label_line} {text}")
        return lines
    if isinstance(item, list):
        if all(not isinstance(value, (dict, list)) for value in item):
            return [prefix + (", ".join(map(markdown_text, item)) or "—")]
        lines = [prefix + "Itens"]
        for value in item:
            lines.extend(render_item(value, level + 1))
        return lines
    return [prefix + markdown_text(item)]


def render_report(case_id, report):
    if not isinstance(report, dict):
        raise ValueError("esperado um objeto JSON")
    summary = report.get("executive_summary")
    confidence = report.get("confidence")
    if not isinstance(summary, str) or confidence not in ("low", "medium", "high"):
        raise ValueError("executive_summary ou confidence inválido")

    lines = [
        "# Relatório do caso " + markdown_text(case_id), "",
        "**Confiança geral** " + {"low": "Baixa", "medium": "Média", "high": "Alta"}[confidence],
        "", "## Resumo executivo", "", markdown_text(summary), "",
    ]
    for field, title in SECTIONS:
        items = report.get(field)
        if not isinstance(items, list):
            raise ValueError(f"{field}: esperado um array")
        lines.extend(["## " + title, ""])
        for item in items:
            lines.extend(render_item(item))
        if not items:
            lines.append("Nenhum item registrado.")
        lines.append("")
    return "\n".join(lines)


def write_atomic(path, content):
    temporary_path = None
    try:
        with NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as output:
            temporary_path = Path(output.name)
            output.write(content)
        temporary_path.replace(path)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case_dir", type=Path)
    args = parser.parse_args()
    case_dir = args.case_dir
    source = case_dir / "runs" / "11-report-gpt.json"
    postmortem = case_dir / "memory" / "13-postmortem.json"
    try:
        if not postmortem.is_file():
            raise ValueError(f"postmortem ainda não salvo em {postmortem}")
        case_id = case_dir.resolve().name
        destination = case_dir / f"report_{case_id}.md"
        report = json.loads(source.read_text(encoding="utf-8"))
        write_atomic(destination, render_report(case_id, report))
    except (OSError, ValueError) as error:
        print(json.dumps({"status": "error", "message": f"Falha ao exportar {source}: {error}"},
                         ensure_ascii=False))
        return 1
    print(json.dumps({
        "status": "ok",
        "final_report": str(destination),
        "message": f"Relatório {destination.name} gerado no diretório {case_dir}.",
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
