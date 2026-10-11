class BankAccount:

    account_counter = 1000

    # Constructor
    def __init__(self, name):
        self.account_holder = name
        self.balance = 0

        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter

    # Deposit
    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully.")

    # Withdraw
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    # Transfer
    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print("Amount transferred successfully.")
        else:
            print("Insufficient balance.")


    def display_balance(self):
        print("Name:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    # Destructor
    def __del__(self):
        # print("\n--------")
        print("Account deleted:", self.account_number)

name1 = input("Enter first account holder name: ")
name2 = input("Enter second account holder name: ")

account1 = BankAccount(name1)
account2 = BankAccount(name2)

print("\n----Deposit----")
amount = float(input("Enter amount to deposit in first account: "))
account1.deposit(amount)

print("\n----Withdraw----")
amount = float(input("Enter amount to withdraw from first account: "))
account1.withdraw(amount)

print("\n-----Transfer----")
amount = float(input("Enter amount to transfer from first account to second account: "))
account1.transfer(amount, account2)

print("\n----Final Details----")
print("\n--- First Account ---")
account1.display_balance()

print("\n--- Second Account ---")
account2.display_balance()

print("\n--------")