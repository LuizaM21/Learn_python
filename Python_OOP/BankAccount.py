"""Creates BankAccount objects, each with its own list of transactions."""


class BankAccount:
    """A Bank Account with a balance of 0 by default .

    Attributes:
        owner (str): The owner of the Bank Account, for example "Luiza".
        balance (int): The value of the balance, for example 1000.
        transactions(list[str]): This account's own transaction history.
    """


    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        self.transactions = []


if __name__ == '__main__':
    luiza = BankAccount("Luiza", 1000)
    andrew = BankAccount("Andrew")

    luiza.transactions.append("opened")

    print(luiza.owner, luiza.balance, luiza.transactions)
    print(andrew.owner, andrew.balance, andrew.transactions)