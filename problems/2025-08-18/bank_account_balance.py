# Problem Name: Bank Account Balance
# -------------------------------------------------------
# Description:
# Create a class `BankAccount` with attributes `account_number` and `balance`.
# Use a constructor to initialize them.
# Add methods:
#   - deposit(amount)
#   - withdraw(amount)  (only if balance is sufficient)
#   - display()
#
# Input Format:
# account_number initial_balance deposit_amount withdraw_amount
#
# Output Format:
# Account Number: <account_number>
# Balance: <final_balance>
#
# Example:
# Input:
# 12345 1000 500 300
#
# Output:
# Account Number: 12345
# Balance: 1200

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
    
    def display(self):
        print("Account Number: ",self.account_number)
        print("Balance: ", self.balance)
        

try:
    account_number,initial_balance, deposit_amount, withdraw_amount = map(int, input().split())
    
    b1 = BankAccount(account_number, initial_balance)
    b1.deposit(deposit_amount)
    b1.withdraw(withdraw_amount)
    b1.display()

except ValueError:
    print("Please input valid value")
    
    