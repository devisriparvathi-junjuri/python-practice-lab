"""Simple student management domain model."""

from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    marks: dict[str, int] = field(default_factory=dict)

    def add_mark(self, subject: str, mark: int) -> None:
        if not subject.strip() or not 0 <= mark <= 100:
            raise ValueError("subject is required and mark must be 0..100")
        self.marks[subject] = mark

    @property
    def average(self) -> float:
        return sum(self.marks.values()) / len(self.marks) if self.marks else 0.0

class StudentRegister:
    def __init__(self) -> None:
        self._students: dict[str, Student] = {}

    def add(self, student: Student) -> None:
        if student.name in self._students:
            raise ValueError("student already exists")
        self._students[student.name] = student

    def find(self, name: str) -> Student:
        try:
            return self._students[name]
        except KeyError as error:
            raise ValueError("student not found") from error

if __name__ == "__main__":
    register = StudentRegister()
    student = Student("Asha")
    student.add_mark("Python", 88)
    register.add(student)
    print(register.find("Asha"))
