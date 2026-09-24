"""Functions package behavior into reusable, testable units."""


def greet(name: str, punctuation: str = "!") -> str:
    """Return a greeting using a default argument."""
    return f"Hello, {name}{punctuation}"


def statistics(*numbers: float) -> tuple[float, float]:
    """Return the minimum and maximum of positional arguments."""
    if not numbers:
        raise ValueError("at least one number is required")
    return min(numbers), max(numbers)


def describe_person(**details: str) -> str:
    """Accept named details through ``**kwargs``."""
    return ", ".join(f"{key}={value}" for key, value in details.items())


if __name__ == "__main__":
    print(greet("Asha"))
    print(statistics(3, 8, 2))
    print(describe_person(name="Asha", role="student"))
