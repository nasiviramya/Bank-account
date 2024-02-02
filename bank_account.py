class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self.balance += amount
            print(f"Deposit of Rupees {amount} is successful. New balance: Rupees {self.balance}/-")
        else:
            print("Invalid deposit amount. Please deposit a positive numeric amount.")

    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of Rupees {amount} is successful. New balance: Rupees {self.balance}/-")
            else:
                print("Insufficient funds. Withdrawal unsuccessful.")
        else:
            print("Invalid withdrawal amount. Please withdraw a positive numeric amount.")

    def display_balance(self):
        print(f"Current balance for account {self.account_number}: Rupees {self.balance}/-")


# Create a bank account
account1 = BankAccount("Andrew", 7304785431, 12000)

# Display initial balance
account1.display_balance()

# Deposit money
account1.deposit(4000)

# Withdraw money
account1.withdraw(2000)

# Withdraw more than balance
account1.withdraw(20000)

# Display final balance
account1.display_balance()

print("\nSecond Account Holder\n")

# Creating another bank account
account2 = BankAccount("Rona", 643456789, 70000)

# Deposit and withdraw from the second account
account2.deposit(45000)
account2.withdraw(23000)
account2.withdraw(33000)

# Display final balance of the second account
account2.display_balance()
