"""Lambdas are small anonymous functions; use named functions for complex logic."""

numbers = [1, 4, 2, 9]
print(sorted(numbers, key=lambda number: -number))
print([number * number for number in numbers])
