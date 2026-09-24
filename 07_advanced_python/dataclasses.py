"""Dataclasses reduce boilerplate for data-focused objects."""

from dataclasses import dataclass, field
from enum import StrEnum


class Status(StrEnum):
    TODO = "todo"
    DONE = "done"

@dataclass
class Task:
    title: str
    status: Status = Status.TODO
    tags: list[str] = field(default_factory=list)

print(Task("Practice generators", tags=["python"]))
