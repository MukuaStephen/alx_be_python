# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add amount to account balance."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw amount from account balance if sufficient funds exist."""
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        """Display the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")
