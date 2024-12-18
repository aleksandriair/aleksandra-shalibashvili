class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print(f"There is not enough balance to withdraw this amount.")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance


def main():
    b = BankAccount(5000)
    b.deposit(200)
    b.withdraw(1000)
    b.withdraw(4500)
    print(b.get_balance())


if __name__ == "__main__":
    main()