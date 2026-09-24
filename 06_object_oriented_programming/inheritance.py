"""Inheritance specializes a base class when the relationship is clear."""

class Employee:
    def __init__(self, name: str) -> None:
        self.name = name

    def describe(self) -> str:
        return f"Employee: {self.name}"


class Developer(Employee):
    def describe(self) -> str:
        return f"Developer: {self.name}"


print(Developer("Asha").describe())
