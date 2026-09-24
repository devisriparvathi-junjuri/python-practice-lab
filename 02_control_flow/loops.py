"""for, while, range, break, continue, pass, and nested loops."""

for number in range(1, 6):
    if number == 3:
        continue
    print(number, end=" ")
print()

countdown = 3
while countdown:
    print(countdown)
    countdown -= 1

for row in range(1, 4):
    for column in range(1, 4):
        print(f"{row * column:2}", end=" ")
    print()


def future_exercise() -> None:
    """A pass statement keeps a planned function syntactically valid."""
    pass  # noqa: PIE790
