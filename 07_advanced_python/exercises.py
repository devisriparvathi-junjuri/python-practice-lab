"""Advanced practice: a small context manager and lazy pipeline."""

from collections.abc import Iterator
from contextlib import contextmanager


@contextmanager
def labelled_section(label: str) -> Iterator[None]:
    print(f"start: {label}")
    try:
        yield
    finally:
        print(f"end: {label}")


def positive_squares(values: list[int]) -> Iterator[int]:
    yield from (value * value for value in values if value > 0)
