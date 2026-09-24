"""Control-flow practice functions."""


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def fizzbuzz(limit: int) -> list[str]:
    return ["FizzBuzz" if n % 15 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else str(n) for n in range(1, limit + 1)]


def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("factorial is undefined for negative values")
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def multiplication_table(number: int, size: int = 10) -> list[int]:
    return [number * multiplier for multiplier in range(1, size + 1)]
