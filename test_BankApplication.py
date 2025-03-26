import unittest
from BankApplication import BankAccount  

class TestBankAccount(unittest.TestCase):
    # setUp method runs before each test case to initialize test data
    def setUp(self):
        self.account1 = BankAccount("Alice", 1000)
        self.account2 = BankAccount("Bob", 500)
        self.account3 = BankAccount("Raj", 0)

    # Test case for deposit functionality
    def test_deposit(self):
        self.assertEqual(self.account1.deposit(500), "Deposited: $500")
        self.assertEqual(self.account1.balance, 1500)
        self.assertEqual(self.account1.deposit(-100), "Deposit amount should be greater than 0.")

    # Test case for deposit functionality
    def test_withdraw(self):
        self.assertEqual(self.account1.withdraw(200), "Withdrew: $200")
        self.assertEqual(self.account1.balance, 800)
        self.assertEqual(self.account1.withdraw(2000), "Insufficient balance or invalid amount.")

    # Test case for money transfer between accounts
    def test_transfer(self):
        self.assertEqual(self.account1.transfer(300, self.account2), "Transferred: $300 to Bob")
        self.assertEqual(self.account1.balance, 700)
        self.assertEqual(self.account2.balance, 800)
        self.assertEqual(self.account1.transfer(10000, self.account2), "Insufficient balance or invalid amount.")

    # Test case to check balance
    def test_check_balance(self):
        self.assertEqual(self.account1.check_balance(), "Balance: $1000")
        self.assertEqual(self.account3.check_balance(), "Balance: $0")

    # Test case for adding interest to the account balance
    def test_add_interest(self):
        self.assertEqual(self.account1.add_interest(10), "Interest added: $100.0")
        self.assertEqual(self.account1.balance, 1100)
        self.assertEqual(self.account1.add_interest(-5), "Interest rate must be positive.")

    # Test case for percentage-based money transfer
    def test_transfer_percentage(self):
        # Test valid percentage transfer
        self.assertEqual(self.account1.transfer_percentage(50, self.account2), "Transferred 50% of balance: $500.0 to Bob")
        self.assertEqual(self.account1.balance, 500)
        self.assertEqual(self.account2.balance, 1000)
        
        # Test invalid percentage greater than 100
        self.assertEqual(self.account1.transfer_percentage(150, self.account2), "Invalid percentage.")
        
        # Test invalid percentage of 0
        self.assertEqual(self.account1.transfer_percentage(0, self.account2), "Invalid percentage.")
        
        # Test invalid negative percentage
        self.assertEqual(self.account1.transfer_percentage(-10, self.account2), "Invalid percentage.")

    # Test case for closing an account
    def test_close_account(self):
        self.account1.withdraw(1000)
        self.assertEqual(self.account1.close_account(), "Account Alice is closed.")
        self.assertEqual(self.account2.close_account(), "Please withdraw all balance before closing.")

    # Test case for changing the account holder's name
    def test_change_account_holder(self):
        self.assertEqual(self.account1.change_account_holder("Charlie"), "Account holder changed to Charlie.")
        self.assertEqual(self.account1.account_holder, "Charlie")

    # Test case for checking if the balance is positive
    def test_is_balance_positive(self):
        self.assertTrue(self.account1.is_balance_positive())
        self.account1.withdraw(1000)
        self.assertFalse(self.account1.is_balance_positive())

# Running the test cases
if __name__ == "__main__":
    unittest.main()