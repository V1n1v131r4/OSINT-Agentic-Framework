#!/usr/bin/env python3
"""Validate the evidence chain for the narrative pipeline."""

import argparse
from datetime import date
import json
from pathlib import Path
import sys


def read_object(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path.name}: esperado um objeto JSON")
    return data


def require(condition, message):
    if not condition:
        raise ValueError(message)


def index_records(data, field, prefix):
    records = data.get(field)
    require(isinstance(records, list), f"{field}: esperado um array")
    indexed = {}
    for record in records:
        require(isinstance(record, dict), f"{field}: esperado um objeto")
        record_id = record.get("id")
        require(isinstance(record_id, str) and record_id.startswith(prefix)
                and len(record_id) > len(prefix) and record_id not in indexed,
                f"{field}: ID inválido ou duplicado: {record_id}")
        indexed[record_id] = record
    return indexed


def origin_index(evidence):
    for record_id, record in evidence.items():
        for field in ("source", "excerpt"):
            value = record.get(field)
            require(isinstance(value, str) and value.strip(), f"{record_id}: {field} obrigatório")
        require("collected_at" in record, f"{record_id}: collected_at obrigatório")
        collected_at = record["collected_at"]
        if collected_at is not None:
            try:
                valid_date = isinstance(collected_at, str) and date.fromisoformat(collected_at).isoformat() == collected_at
            except ValueError:
                valid_date = False
            require(valid_date, f"{record_id}: collected_at deve ser uma data YYYY-MM-DD ou null")
        require("origin_id" in record, f"{record_id}: origin_id obrigatório")
        origin = record["origin_id"]
        require(origin is None or (isinstance(origin, str) and origin in evidence),
                f"{record_id}: origem inexistente: {origin}")

    roots = {}
    for record_id in evidence:
        seen = set()
        current = record_id
        while current is not None:
            require(current not in seen, f"{record_id}: ciclo nas referências de origem")
            seen.add(current)
            origin = evidence[current]["origin_id"]
            if origin == current:
                break
            current = origin
        roots[record_id] = current
    return roots


def validate_findings(correlation, origins):
    findings = index_records(correlation, "findings", "F-")
    for finding_id, finding in findings.items():
        require(finding.get("kind") in ("observation", "inference", "hypothesis"),
                f"{finding_id}: kind inválido")
        require(finding.get("confidence") in ("low", "medium", "high"),
                f"{finding_id}: confidence inválida")
        for field in ("claim", "confidence_rationale"):
            value = finding.get(field)
            require(isinstance(value, str) and value.strip(), f"{finding_id}: {field} obrigatório")
        references = set()
        for field in ("supports", "contradicts"):
            ids = finding.get(field)
            require(isinstance(ids, list), f"{finding_id}: {field} deve ser um array")
            require(field != "supports" or ids, f"{finding_id}: supports deve citar evidência")
            for evidence_id in ids:
                require(isinstance(evidence_id, str) and evidence_id in origins,
                        f"{finding_id}: {field}: evidência inexistente: {evidence_id}")
                require(evidence_id not in references, f"{finding_id}: referência repetida: {evidence_id}")
                references.add(evidence_id)
        known_origins = {origins[evidence_id] for evidence_id in finding["supports"]} - {None}
        count = finding.get("supporting_origin_count")
        require(type(count) is int and count == len(known_origins),
                f"{finding_id}: supporting_origin_count esperado: {len(known_origins)}")
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case_dir", type=Path)
    parser.add_argument("--collection-only", action="store_true")
    args = parser.parse_args()
    runs = args.case_dir / "runs"
    collection = runs / "04-narrative-collection-gpt.json"
    correlation = runs / "10-correlation-gpt.json"
    path = collection
    try:
        evidence = index_records(read_object(collection), "evidence", "E-")
        origins = origin_index(evidence)
        if not args.collection_only:
            path = correlation
            validate_findings(read_object(correlation), origins)
    except (OSError, ValueError) as error:
        print(json.dumps({"status": "error", "file": str(path), "message": str(error)},
                         ensure_ascii=False))
        return 1
    print(json.dumps({"status": "ok", "evidence_origins": origins}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
