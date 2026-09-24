"""Type hints document intended inputs and outputs for tools and readers."""

from typing import TypeAlias

UserRecord: TypeAlias = dict[str, str | int]


def display_user(user: UserRecord) -> str:
    return f"{user['name']} ({user['age']})"

print(display_user({"name": "Asha", "age": 21}))
