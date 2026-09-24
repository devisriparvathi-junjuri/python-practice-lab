"""Generators use yield for lazy iteration."""

from collections.abc import Iterator


def even_numbers(limit: int) -> Iterator[int]:
    yield from range(2, limit + 1, 2)


print(list(even_numbers(10)))
