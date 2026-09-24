"""Dictionary frequency problems.

Problem: group words that have the same letters. Example: ["eat", "tea"] -> one group.
Practice variation: make grouping case-insensitive.
Time: O(n * k log k), where k is average word length. Space: O(nk).
"""


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: dict[tuple[str, ...], list[str]] = {}
    for word in words:
        key = tuple(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())
