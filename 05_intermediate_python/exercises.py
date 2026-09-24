"""Intermediate practice exercises."""

import csv
import io


def parse_scores(csv_text: str) -> dict[str, int]:
    rows = csv.DictReader(io.StringIO(csv_text))
    return {row["name"]: int(row["score"]) for row in rows}
