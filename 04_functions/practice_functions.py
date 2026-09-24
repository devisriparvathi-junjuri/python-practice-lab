"""Reusable functions used by examples and tests."""

from collections.abc import Callable, Iterable


def add(left: float, right: float) -> float:
    """Return the sum of two numbers."""
    return left + right


def divide(dividend: float, divisor: float) -> float:
    """Divide two numbers, rejecting division by zero."""
    if divisor == 0:
        raise ValueError("divisor cannot be zero")
    return dividend / divisor


def is_valid_email(value: str) -> bool:
    """Perform a small, readable validation check for an email-like value."""
    local, separator, domain = value.partition("@")
    return bool(local and separator and "." in domain and not domain.startswith("."))


def normalize_words(words: Iterable[str]) -> list[str]:
    """Strip whitespace, lowercase words, and omit blank values."""
    return [word.strip().lower() for word in words if word.strip()]


def transform_values(values: Iterable[int], transform: Callable[[int], int]) -> list[int]:
    """Apply a higher-order function to every value."""
    return [transform(value) for value in values]
