"""Creates BankAccount objects, each with its own list of transactions."""

from abc import ABC, abstractmethod

class FeeStrategy(ABC):
    @abstractmethod
    def calculate(self, balance: float) -> float:
        ...

class NoFee(FeeStrategy):
    def calculate(self, balance):
        return 0

class FlatFee(FeeStrategy):
    def __init__(self, amount):
        self.amount = amount

    def calculate(self, balance):
        return self.amount

class OverdraftFee(FeeStrategy):
    def calculate(self, balance):
        if balance < 0:
            return 15
        return  5



class BankAccount:          # parent (base class)
    """A Bank Account with a balance of 0 by default .
    Attributes:
        owner (str): The owner of the Bank Account, for example "Luiza".
        balance (int): The value of the balance, for example 1000.
        transactions(list[str]): This account's own transaction history.
    """

    bank_name = "Python Bank"      # class attribute: the same for every account
    interest_rate = 0.05           # class attribute: the default rate for all accounts
    accounts_created = 0           # class attribute: a counter shared by all

    def __init__(self, owner, balance=0, fee_strategy=None):
        self.owner = owner
        self.balance = balance
        self.transactions = []
        self.fee_strategy = fee_strategy if fee_strategy else NoFee()
        BankAccount.accounts_created += 1

    def deposit(self, *amounts, note=None):
        if not amounts:
            raise ValueError("No amounts given!")

        # 1. Check EVERYTHING first. Nothing changes in this loop
        for amount in amounts:
            if not self.is_valid_amount(amount):
                raise ValueError(f"Amount must be greater than 0, got {amount}")

        # 2. Only now change state. Every amount is known to be valid
        for amount in amounts:
            self.balance += amount
            if note:
                self.transactions.append(f"deposit {amount} ({note})")
            else:
                self.transactions.append(f"deposit {amount}")

    def withdraw(self, *amounts):
        if not amounts:
            raise ValueError("No amounts given")
        for amount in amounts:
            if not self.is_valid_amount(amount):
                raise ValueError(f"The withdrawal amount must be greater than 0! Got {amount}")
            self._check_single_withdrawal(amount)

        self._check_funds(sum(amounts))

        for amount in amounts:
            self.balance -= amount
            self.transactions.append(f"withdraw {amount}")

    def _check_funds(self, amount):
        if self.balance < amount:
            raise ValueError(f"Insufficient balance for amount {amount}!")

    def _check_single_withdrawal(self, amount):
        pass

    def statement(self) -> str:
        return f"{self.owner}: {self.balance}"

    def apply_interest(self):
        applied_interest = self.balance * self.interest_rate
        self.balance += applied_interest
        self.transactions.append(f"interest {applied_interest}")

    def month_end(self):
        """The template: same skeleton for every account."""
        interest = self._calculate_interest()       #hook
        # pyrefly: ignore[redundant-condition]
        if interest:
            self.balance += interest
            self.transactions.append(f"interest {interest}")
        fee = self._monthly_fee()       # hook
        # pyrefly: ignore[redundant-condition]
        if fee:
            self.balance -= fee             # bank fees skip _check_funds on purpose
            self.transactions.append(f"fee {fee}")

    def charge_fee(self):
        fee = self.fee_strategy.calculate(self.balance)  # ask the strategy
        if fee:  # only if there is a fee
            self.balance -= fee
            self.transactions.append(f"fee {fee}")

    def _calculate_interest(self):
        return 0

    def _monthly_fee(self):
        return 0

    @staticmethod
    def is_valid_amount(amount):
        if isinstance(amount,bool) or not isinstance(amount, (int, float)):
            return False    # rejects None, strings, True/False, lists...
        return amount > 0

    @classmethod
    def from_string(cls, text: str):
        """Create an account from text like "Luiza,1000"."""
        # 1. Split, then check the number of parts BEFORE unpacking
        parts = text.split(",")
        if len(parts) != 2:
            raise ValueError(f"Expected 'owner,balance', got {text!r}")

        # 2. Now it's safe to unpack, and clean each part separately
        owner = parts[0].strip()
        balance_text = parts[1].strip()

        # 3. Check the owner
        if not owner:
            raise ValueError("Owner name is missing")

        # 4. Convert ONCE, replacing Python's message with ours
        try:
            balance = int(balance_text)
        except ValueError:
            raise ValueError(f"Balance must be a whole number, got {balance_text!r}") from None

        # 5. Business rule on the converted number
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        return cls(owner, balance)

    def __str__(self):
        return (f"Type: {self.__class__.__name__}, "
                f"Owner: {self.owner}, "
                f"Balance: {self.balance}, "
                f"Transaction history: {self.transactions}, "
                f"Accounts created: {self.accounts_created}")

    def __repr__(self):
        return (f"{self.__class__.__name__}, "
                f"{self.owner}, "
                f"{self.balance}, "
                f"{self.transactions}, "
                f"{self.accounts_created}")

    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        if self.owner == other.owner and self.balance == other.balance:
            return True
        return False

    def __lt__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.balance < other.balance

    def __len__(self):
        return len(self.transactions)



class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, min_balance=100, rate = 0.05):
        if balance < min_balance:
            raise ValueError(f"Opening balance must be at least {min_balance}, got {balance}!")
        super().__init__(owner, balance)
        self.min_balance = min_balance
        self.rate = rate

    def _check_funds(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError(f"Below minimum balance of {self.min_balance}!")

    def statement(self) -> str:
        return f"{super().statement()} (savings)"

    def _calculate_interest(self):
        return round(self.balance * self.rate, 2)



class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        if overdraft_limit < 0:
            raise ValueError(f"Overdraft limit must be 0 or more, got {overdraft_limit}!")
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def _check_funds(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded")

    def _monthly_fee(self):
        fee =  5             # maintenance
        if self.balance < 0:
            fee +=10         # overdraft penalty
        return fee



class StudentAccount(BankAccount):
    def __init__(self, owner, balance=0, max_withdrawal=200):
        if max_withdrawal < 0:
            raise ValueError(f"Withdrawal limit must be 0 or more, got {max_withdrawal}!")
        super().__init__(owner, balance)
        self.max_withdrawal = max_withdrawal

    def _check_single_withdrawal(self, amount):
        if self.max_withdrawal < amount:
            raise ValueError("Over the withdrawal limit!")


if __name__ == '__main__':
    pass
    """============== 73 passed in 0.06s ============="""