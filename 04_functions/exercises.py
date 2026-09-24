"""Function practice: validation, calculators, and list processing."""

from collections.abc import Callable


def calculator(left: float, operator: str, right: float) -> float:
    operations: dict[str, Callable[[float, float], float]] = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }
    if operator not in operations or (operator == "/" and right == 0):
        raise ValueError("unsupported operation")
    return operations[operator](left, right)


def keep_even(values: list[int]) -> list[int]:
    return [value for value in values if value % 2 == 0]
