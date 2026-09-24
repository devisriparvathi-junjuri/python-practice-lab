"""Decorators wrap a function to add reusable behavior."""

from collections.abc import Callable
from functools import wraps
from typing import TypeVar

ReturnT = TypeVar("ReturnT")


def announce(function: Callable[..., ReturnT]) -> Callable[..., ReturnT]:
    @wraps(function)
    def wrapper(*args: object, **kwargs: object) -> ReturnT:
        print(f"Running {function.__name__}")
        return function(*args, **kwargs)
    return wrapper


@announce
def add(left: int, right: int) -> int:
    return left + right

print(add(2, 3))
