"""Data-structure exercises."""


def marks_summary(marks: dict[str, int]) -> tuple[int, int, float]:
    if not marks:
        raise ValueError("marks cannot be empty")
    values = list(marks.values())
    return min(values), max(values), sum(values) / len(values)


def make_contact_book(names_and_numbers: list[tuple[str, str]]) -> dict[str, str]:
    return dict(names_and_numbers)
