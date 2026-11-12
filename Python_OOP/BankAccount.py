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
        if amount <= 0:
            raise ValueError("The inserted amount must be greater than 0!")
        self.balance += amount
        self.transactions.append(f"deposit {amount}")

    def withdraw(self, amount: int):
        if amount <= 0:
            raise ValueError("The inserted amount must be greater than 0!")
        if self.balance < amount:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self.transactions.append(f"withdraw {amount}")

    def statement(self) -> str:
        return f"{self.owner}: {self.balance}"

    def apply_interest(self):
        self.transactions.append(f"interest {self.interest_rate}")
        var = (self.balance * self.interest_rate) + self.balance
        self.balance = var

if __name__ == '__main__':

    luiza = BankAccount("Luiza", 1000)
    andrew = BankAccount("Andrew", 500)
    print("No of accounts created:",BankAccount.accounts_created)

    luiza.interest_rate = 0.10
    luiza.apply_interest()
    andrew.apply_interest()
    print(F"{luiza.owner} interest: ",luiza.interest_rate)
    print(f"{andrew.owner} interest: ", andrew.interest_rate)
    print(f"{luiza.owner} statement:\n",luiza.statement())
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
