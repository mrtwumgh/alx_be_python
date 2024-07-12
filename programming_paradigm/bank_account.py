class BankAccount:

    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, value):
        self.account_balance += value

    def withdraw(self, value):
        if value <= self.account_balance:
            self.account_balance -= value
            return True
        else:
            return False
            
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")