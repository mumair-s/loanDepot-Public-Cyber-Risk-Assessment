#!/usr/bin/env python3
from pathlib import Path
import csv
import sys

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"

def read_dicts(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def rating(score):
    score = int(score)
    if score <= 4:
        return "Low"
    if score <= 9:
        return "Medium"
    if score <= 15:
        return "High"
    return "Critical"

def split_ids(value):
    return [x.strip() for x in value.split(";") if x.strip()]

def main():
    errors = []
    risks = read_dicts("risk-register.csv")
    evidence = read_dicts("evidence-register.csv")
    controls = read_dicts("control-observations.csv")
    sources = read_dicts("sources.csv")

    evidence_ids = {row["Evidence ID"] for row in evidence}
    source_ids = {row["Source ID"] for row in sources}

    for collection, key, name in [
        (risks, "Risk ID", "risk"),
        (evidence, "Evidence ID", "evidence"),
        (controls, "Control ID", "control"),
        (sources, "Source ID", "source"),
    ]:
        ids = [r[key] for r in collection]
        if len(ids) != len(set(ids)):
            errors.append(f"Duplicate {name} IDs found.")

    for e in evidence:
        if e["Source ID"] not in source_ids:
            errors.append(f'{e["Evidence ID"]}: unknown Source ID {e["Source ID"]}')

    for r in risks:
        try:
            likelihood = int(r["Likelihood"])
            impact = int(r["Impact"])
            score = int(r["Risk Score"])
        except ValueError:
            errors.append(f'{r["Risk ID"]}: likelihood/impact/score is not an integer')
            continue

        if likelihood not in range(1, 6):
            errors.append(f'{r["Risk ID"]}: likelihood must be 1-5')
        if impact not in range(1, 6):
            errors.append(f'{r["Risk ID"]}: impact must be 1-5')
        if score != likelihood * impact:
            errors.append(f'{r["Risk ID"]}: score does not equal likelihood x impact')
        if r["Risk Rating"] != rating(score):
            errors.append(f'{r["Risk ID"]}: rating does not match score')

        for evidence_id in split_ids(r["Evidence IDs"]):
            if evidence_id not in evidence_ids:
                errors.append(f'{r["Risk ID"]}: unknown Evidence ID {evidence_id}')

    for c in controls:
        for evidence_id in split_ids(c["Evidence IDs"]):
            if evidence_id not in evidence_ids:
                errors.append(f'{c["Control ID"]}: unknown Evidence ID {evidence_id}')

    print("loanDepot Public-Source Cyber Risk Assessment")
    print("Validation Summary")
    print("=" * 49)
    print(f"Sources: {len(sources)}")
    print(f"Evidence items: {len(evidence)}")
    print(f"Risks: {len(risks)}")
    print(f"Public control observations: {len(controls)}")

    if errors:
        print(f"\nFAILED — {len(errors)} issue(s):")
        for err in errors:
            print(f"- {err}")
        return 1

    print("\nPASS — IDs, evidence references, risk calculations, and ratings are consistent.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
