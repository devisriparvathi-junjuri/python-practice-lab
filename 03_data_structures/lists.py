"""Lists are mutable ordered collections."""

scores = [72, 88, 91]
scores.append(95)
print(scores[0], scores[1:], max(scores), min(scores))


def remove_duplicates(values: list[int]) -> list[int]:
    return list(dict.fromkeys(values))


def find_duplicates(values: list[int]) -> set[int]:
    seen: set[int] = set()
    duplicates: set[int] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates
