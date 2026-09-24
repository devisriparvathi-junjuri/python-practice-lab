"""Beginner exercises: personal information, conversion, and geometry."""


def temperature_c_to_f(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def rectangle_measurements(length: float, width: float) -> tuple[float, float]:
    if length < 0 or width < 0:
        raise ValueError("dimensions cannot be negative")
    return length * width, 2 * (length + width)


def basic_number_operations(left: float, right: float) -> dict[str, float]:
    if right == 0:
        raise ValueError("right operand cannot be zero")
    return {"sum": left + right, "difference": left - right, "product": left * right, "quotient": left / right}


if __name__ == "__main__":
    print("Student: Asha | Goal: software engineering")
    print("20 C ->", temperature_c_to_f(20), "F")
    print("Rectangle:", rectangle_measurements(5, 3))
