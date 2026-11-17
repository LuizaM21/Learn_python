"""Creates BankAccount objects, each with its own list of transactions."""


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

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []
        BankAccount.accounts_created += 1

    def deposit(self, *amounts, note=None):
        if not amounts:
            raise ValueError("No amounts given")

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
                raise ValueError("The withdrawal amount must be greater than 0!")

        self._check_funds(sum(amounts))

        for amount in amounts:
            self.balance -= amount
            self.transactions.append(f"withdraw {amount}")

    def _check_funds(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient balance!")

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
    def __init__(self, owner, balance=0, min_balance=100):
        if balance < min_balance:
            raise ValueError(f"Opening balance must be at least {min_balance}, got {balance}!")
        super().__init__(owner, balance)
        self.min_balance = min_balance

    def _check_funds(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError(f"Below minimum balance of {self.min_balance}!")

    def statement(self) -> str:
        return f"{super().statement()} (savings)"

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        if overdraft_limit < 0:
            raise ValueError(f"Overdraft limit must be 0 or more, got {overdraft_limit}!")
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def _check_funds(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded")


class StudentAccount(BankAccount):
    def __init__(self, owner, balance=0, max_withdrawal=200):
        if max_withdrawal < 0:
            raise ValueError(f"Withdrawal limit must be 0 or more, got {max_withdrawal}!")
        super().__init__(owner, balance)
        self.max_withdrawal = max_withdrawal

    def _check_funds(self, amount):
        if self.max_withdrawal < amount:
            raise ValueError("Over the withdrawal limit!")
        super()._check_funds(amount)


if __name__ == '__main__':
    luiza = BankAccount("Luiza", 1000)
    print(luiza.__repr__())
    print(luiza.__str__())
    andrew = BankAccount("Andrew", 500)
    print(andrew)
    print("Number of accounts created:", BankAccount.accounts_created)

    luiza.interest_rate = 0.10
    luiza.apply_interest()
    andrew.apply_interest()
    print("Luiza transaction history: ", luiza.transactions)
    print("Andrew transaction history: ", andrew.transactions)
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
    assert isinstance(luiza.balance, int)  # <class 'int'>
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

    print("------------------Inheritance-SavingsAccount class-----------------------")
    s = SavingsAccount("Mara", 1000)
    print("balance:", s.balance)
    s.withdraw(800)
    print("transactions:", s.transactions)
    print("balance:", s.balance)
    print("statement: ", s.statement())  # Mara: 200 (savings)


    try:
        s.withdraw(150)  # 200 - 150 = 50, below 100
    except ValueError as e:
        print(e)  # Balance below minimum 100!
    print("balance:", s.balance)
    print("transactions:", s.transactions)

    try:
        s.withdraw(-5)
    except ValueError as e:
        print(e)  # The withdrawal amount must be greater than 0!

    print(s.transactions)  # ['withdraw 800']
    print(isinstance(s, BankAccount))  # True
    print(repr(s))  # SavingsAccount: Mara, 200, ['withdraw 800'], ...

    t = SavingsAccount.from_string("Andrew,500")
    print(repr(t))
    print(type(t).__name__, t.min_balance)  # SavingsAccount 100
    print(t.transactions)
    print(t.statement())
    try:
        n = SavingsAccount.from_string("tim,50")
    except ValueError as e:
        print(f"Error: {e}")


    print("-----------------Inheritance-Overdraft Class-----------------------")
    before = BankAccount.accounts_created
    try:
        CheckingAccount("Ion", 100, overdraft_limit=-50)
    except ValueError as e:
        print(f"Error: {e}")
    print(BankAccount.accounts_created == before)   # True

    john = CheckingAccount("John", 100)
    print(john.statement(), john.overdraft_limit)     # John: 100 500

    try:
        john.withdraw(700)
    except ValueError as ve:
        print(f"Error: {ve}")

    print("-----------------polymorphism-StudentAccount Class-----------------------")
    st = StudentAccount("Dan", 1000)
    st.withdraw(150);  print(st.statement())                 # Dan: 850
    try: st.withdraw(300)
    except ValueError as e: print(e)                         # Over the withdrawal limit
    st2 = StudentAccount("Ema", 100)
    try: st2.withdraw(150)
    except ValueError as e: print(e)                         # Insufficient balance!
    print(st.transactions)
    before = BankAccount.accounts_created
    try: StudentAccount("Maria",1000, max_withdrawal=-50)
    except ValueError as e: print(e)
    print(BankAccount.accounts_created == before)  # True


    print("-----------------overriding of operators-BankAccount class-----------------------")
    a = BankAccount("Ana", 100)
    b = BankAccount("Ana", 100)
    c = BankAccount("Dan", 50)

    print(a == b)  # True
    print(a is b)  # False
    print(a == "Ana")  # False, no crash

    ranked = sorted([a, c, BankAccount("Ion", 75)])
    print([acc.owner for acc in ranked])  # ['Dan', 'Ion', 'Ana']

    a.deposit(10)
    a.withdraw(5)
    print(len(a))  # 2
    print(a.__lt__(b))  # False
    print(a < c)    # a:100 < c:50 -> False
    print(a > c)    # a:100 > c:50 -> True

    print("-----------------overloading of deposit(*args)-BankAccount class-----------------------")

    a = BankAccount("Ana", 0)
    a.deposit(50)  # one amount (existing calls must still work)
    a.deposit(100, note="salary")  # optional note
    a.deposit(10, 20, 30)  # several amounts at once

    print(a.balance)  # 210
    print(a.transactions)  # ['deposit 50', 'deposit 100 (salary)', 'deposit 10', 'deposit 20', 'deposit 30']

    try:
        a.deposit(10, -5, 20)
    except ValueError as e:
        print(e)  # your message
    print(a.balance)  # 210: nothing deposited, not even the 10

    try:
        a.deposit()
    except ValueError as e:
        print(e)  # your message: no amounts given

    print("-----------------overloading of withdraw(*args)-BankAccount class-----------------------")
    s = SavingsAccount("Mara", 500)
    s.withdraw(100, 150)
    print(s.balance, s.transactions)  # 250 ['withdraw 100', 'withdraw 150']
    try:
        s.withdraw(100, 100)  # 250 - 200 = 50, below the 100 minimum
    except ValueError as e:
        print(e)  # Below minimum balance of 100!
    print(s.balance)  # 250, unchanged