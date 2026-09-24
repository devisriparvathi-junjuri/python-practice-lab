"""Classes combine state and behavior."""

class Student:
    school = "Python Practice Lab"  # class attribute

    def __init__(self, name: str, marks: list[int]) -> None:
        self.name = name
        self.marks = marks

    def average(self) -> float:
        return sum(self.marks) / len(self.marks)

    def __str__(self) -> str:
        return f"Student({self.name}, average={self.average():.1f})"

    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, marks={self.marks!r})"


if __name__ == "__main__":
    print(Student("Asha", [80, 90]))
