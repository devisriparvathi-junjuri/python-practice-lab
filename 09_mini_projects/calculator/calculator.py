"""A safe, small calculator command-line application."""

import argparse


def calculate(operation: str, left: float, right: float) -> float:
    if operation == "add":
        return left + right
    if operation == "subtract":
        return left - right
    if operation == "multiply":
        return left * right
    if operation == "divide":
        if right == 0:
            raise ValueError("cannot divide by zero")
        return left / right
    raise ValueError(f"unknown operation: {operation}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"])
    parser.add_argument("left", type=float)
    parser.add_argument("right", type=float)
    args = parser.parse_args()
    try:
        print(calculate(args.operation, args.left, args.right))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
