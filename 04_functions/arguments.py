"""Positional, keyword, default, and unpacked arguments."""


def profile(name: str, age: int, *, role: str = "learner") -> dict[str, str | int]:
    return {"name": name, "age": age, "role": role}


values = ("Asha", 21)
print(profile(*values, role="developer"))
