"""Focused tests for mini-project domain logic."""

from decimal import Decimal
import importlib.util
from pathlib import Path

ROOT = Path(__file__).parent

def load(folder: str, module: str):
    path = ROOT / folder / module
    spec = importlib.util.spec_from_file_location(module, path)
    assert spec and spec.loader
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def test_calculator_and_student() -> None:
    calculator = load("calculator", "calculator.py")
    student_management = load("student_management", "student_management.py")
    assert calculator.calculate("add", 2, 3) == 5
    student = student_management.Student("Asha")
    student.add_mark("Python", 90)
    assert student.average == 90


def test_expense_and_contact() -> None:
    expense_tracker = load("expense_tracker", "expense_tracker.py")
    contact_book = load("contact_book", "contact_book.py")
    tracker = expense_tracker.ExpenseTracker()
    tracker.add("Book", "study", Decimal("5.00"))
    assert tracker.totals_by_category()["study"] == Decimal("5.00")
    contacts = contact_book.ContactBook()
    contacts.add("Asha", "555")
    assert contacts.find("ASHA") == "555"
