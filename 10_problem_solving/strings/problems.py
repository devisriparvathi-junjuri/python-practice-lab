"""String problems with examples and complexity notes.

Problem: determine whether a phrase is a palindrome, ignoring case and spaces.
Example: ``Never odd or even`` -> True.
Practice variation: ignore punctuation as well.
Time: O(n). Space: O(n) for normalized text.
"""


def is_palindrome(text: str) -> bool:
    normalized = "".join(character.casefold() for character in text if not character.isspace())
    return normalized == normalized[::-1]


def first_unique_character(text: str) -> str | None:
    counts = {character: text.count(character) for character in set(text)}
    return next((character for character in text if counts[character] == 1), None)
