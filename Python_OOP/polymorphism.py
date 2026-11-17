import decimal

from Python_OOP.bank_account import BankAccount, SavingsAccount

class Loan:
    def __init__(self, owner, principal, annual_rate=0.07):
        if not isinstance(annual_rate, (int, float)):
            raise ValueError(f"Unknown format {annual_rate}!")
        if annual_rate is None:
            raise ValueError(f"No annual rate was given, got {annual_rate}")
        if annual_rate < 0.0:
            raise ValueError("Negative annual rate is not allowed")

        self.owner= owner
        self.principal = principal
        self.annual_rate= annual_rate

    def statement(self):
        return f"{self.owner}: loan {self.principal} at {self.annual_rate:.0%}"

    def __repr__(self):
        return f"{self.owner}, {self.principal}, {self.annual_rate}"


class Card:
    def __init__(self, owner, last4):
        self.owner= owner
        self.last4 = last4

"""LBYL style - Look before you leap 
- check first whether something is possible, 
and only act if the check passes"""
def print_all_statements(items: list):
    for account in items:
        item = getattr(account, "statement", None)
        if item is None:
            print(f"{type(account).__name__}: no statement")
        else:
            print(item())


if __name__ == '__main__':
    bad_inputs = [
        ("Ion", 5000, None),
        ("Eve", 1000, "abc"),
        ("No joke", 1000, -0.10)]
    for name, amount, annual_rate in bad_inputs:
        try:
            user = Loan(name, amount, annual_rate)
            print(user.__repr__())
        except Exception as e:
            print(f"Error: {e}")

    items = [
        BankAccount("Ana", 100),
        SavingsAccount("Mara", 300),
        Loan("Ion", 5000),
        Card("Dan", "4417")]

    print_all_statements(items)