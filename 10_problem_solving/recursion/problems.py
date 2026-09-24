"""Basic recursion: each call reduces the problem toward a base case.

Problem: calculate factorial. Example: factorial(5) -> 120.
Practice variation: write an iterative version and compare readability.
Time: O(n). Space: O(n) call stack.
"""


def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("number must be non-negative")
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)


def fibonacci(number: int) -> int:
    if number < 0:
        raise ValueError("number must be non-negative")
    if number < 2:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)
