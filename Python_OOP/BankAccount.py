"""Creates BankAccount objects, each with its own list of transactions."""


class BankAccount:
    """A Bank Account with a balance of 0 by default .
    Attributes:
        owner (str): The owner of the Bank Account, for example "Luiza".
        balance (int): The value of the balance, for example 1000.
        transactions(list[str]): This account's own transaction history.
    """

    bank_name = "Python Bank"      # class attribute: the same for every account
    interest_rate = 0.05           # class attribute: the default rate for all accounts
    accounts_created = 0           # class attribute: a counter shared by all

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []
        BankAccount.accounts_created += 1


    def deposit(self, amount: int):
        if not self.is_valid_amount(amount):
            raise ValueError("The deposit amount must be greater than 0!")
        self.balance += amount
        self.transactions.append(f"deposit {amount}")

    def withdraw(self, amount: int):
        if not self.is_valid_amount(amount) :
            raise ValueError("The withdrawal amount must be greater than 0!")
        if self.balance < amount:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self.transactions.append(f"withdraw {amount}")

    def statement(self) -> str:
        return f"{self.owner}: {self.balance}"

    def apply_interest(self):
        applied_interest = self.balance * self.interest_rate
        self.balance += applied_interest
        self.transactions.append(f"interest {applied_interest}")

    @staticmethod
    def is_valid_amount(amount):
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

if __name__ == '__main__':

    luiza = BankAccount("Luiza", 1000)
    andrew = BankAccount("Andrew", 500)
    print("Number of accounts created:", BankAccount.accounts_created)

    luiza.interest_rate = 0.10
    luiza.apply_interest()
    andrew.apply_interest()
    print("Luiza transaction history: ", luiza.transactions)
    print("Andrew transaction history: ", andrew.transactions)
    print(f"{luiza.owner} interest: ", luiza.interest_rate)
    print(f"{andrew.owner} interest: ", andrew.interest_rate)
    print(f"{luiza.owner} statement:\n", luiza.statement())
    print(f"{andrew.owner} statement:\n", andrew.statement())

    BankAccount.interest_rate = 0.02
    print(f"{luiza.owner} interest rate: ",luiza.interest_rate)
    print(f"{andrew.owner} interest rate:", andrew.interest_rate)
    luiza.deposit(100)
    luiza.withdraw(50)
    try:
        andrew.withdraw(10000)
    except ValueError as e:
        print(f"\n\nError: {e}")

    try:
        luiza.deposit(-100)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        luiza.withdraw(-100)
    except ValueError as e:
        print(f"Error: {e}\n\n")

    print(luiza.transactions)
    print(andrew.transactions)

    print("""------------------Exercise 4-----------------------""")
    print(BankAccount.is_valid_amount(50))  # True
    print(BankAccount.is_valid_amount(-5))  # False

    luiza = BankAccount.from_string("Luiza,1000")
    print(luiza.statement())  # Luiza: 1000
    print(type(luiza.balance))  # <class 'int'>
    print(BankAccount.accounts_created)  # 3

    try:
        luiza.deposit(0)
    except ValueError as e:
        print(f"Error: {e}")

    print("""------------------from_string tests-----------------------""")

    bad_inputs = ["Luiza", "Luiza,1000,extra", "Luiza,abc", ",1000", "Luiza,-50"]

    for text in bad_inputs:
        try:
            BankAccount.from_string(text)
            print(f"{text!r}")
        except ValueError as e:
            print(f"{text!r} → Error: {e}")

    ok = BankAccount.from_string(" Luiza , 1000 ")
    print(ok.statement())  # Luiza: 1000