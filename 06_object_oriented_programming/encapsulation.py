"""Encapsulation protects invariants behind methods or properties."""

class BankAccount:
    def __init__(self, opening_balance: float = 0) -> None:
        if opening_balance < 0:
            raise ValueError("balance cannot be negative")
        self._balance = opening_balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if not 0 < amount <= self._balance:
            raise ValueError("insufficient funds or invalid amount")
        self._balance -= amount


if __name__ == "__main__":
    account = BankAccount(100)
    account.deposit(25)
    print(account.balance)
