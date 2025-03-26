class BankAccount:
    # Constructor to initialize account holder name and balance
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount     # Adds amount to balance
            return f"Deposited: ${amount}"
        else:
            return "Deposit amount should be greater than 0."

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount      # Deducts amount from balance
            return f"Withdrew: ${amount}"
        else:
            return "Insufficient balance or invalid amount."

    # Method to transfer money from one account to another
    def transfer(self, amount, target_account):
        if 0 < amount <= self.balance:
            self.balance -= amount               # Deducts amount from sender's balance
            target_account.balance += amount     # Adds amount to receiver's balance
            return f"Transferred: ${amount} to {target_account.account_holder}"
        else:
            return "Insufficient balance or invalid amount."

    # Method to check the current account balance
    def check_balance(self):
        return f"Balance: ${self.balance}"
    
    # Method to add interest to the account balance
    def add_interest(self, rate):
        if rate > 0:
            interest = self.balance * rate / 100     # Calculates interest amount
            self.balance += interest                 # Adds interest to balance
            return f"Interest added: ${interest}"
        return "Interest rate must be positive."

    # Method to transfer a percentage of balance to another account
    def transfer_percentage(self, percentage, target_account):
        if 0 < percentage <= 100:
            amount = self.balance * percentage / 100
            self.balance -= amount     # Deducts amount from sender
            target_account.balance += amount     # Adds amount to receiver
            return f"Transferred {percentage}% of balance: ${amount} to {target_account.account_holder}"
        return "Invalid percentage."

    # Method to close the account if balance is zero
    def close_account(self):
        if self.balance == 0:
            return f"Account {self.account_holder} is closed."
        return "Please withdraw all balance before closing."

    # Method to change the account holder's name
    def change_account_holder(self, new_account_holder):
        self.account_holder = new_account_holder     # Updates account holder name
        return f"Account holder changed to {new_account_holder}."

    # Method to check if the balance is positive
    def is_balance_positive(self):
        return self.balance > 0        # Returns True if balance is positive

    # String representation of the account
    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance}"

