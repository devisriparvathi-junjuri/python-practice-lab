"""Strings support indexing, slicing, and useful text methods."""

message = "Python practice"
print(message[0], message[:6], message.lower(), message.replace("practice", "lab"))


def character_frequency(text: str) -> dict[str, int]:
    frequency: dict[str, int] = {}
    for character in text:
        frequency[character] = frequency.get(character, 0) + 1
    return frequency


if __name__ == "__main__":
    print(character_frequency("banana"))
