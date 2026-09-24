"""Track expenses and calculate category totals."""

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Expense:
    description: str
    category: str
    amount: Decimal

class ExpenseTracker:
    def __init__(self) -> None:
        self.expenses: list[Expense] = []

    def add(self, description: str, category: str, amount: Decimal) -> None:
        if not description.strip() or not category.strip() or amount <= 0:
            raise ValueError("description, category, and positive amount are required")
        self.expenses.append(Expense(description, category, amount))

    def totals_by_category(self) -> dict[str, Decimal]:
        totals: dict[str, Decimal] = {}
        for expense in self.expenses:
            totals[expense.category] = totals.get(expense.category, Decimal(0)) + expense.amount
        return totals

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.add("Notebook", "study", Decimal("4.50"))
    print(tracker.totals_by_category())
