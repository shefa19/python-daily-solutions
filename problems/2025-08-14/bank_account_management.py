# Problem Name: Bank Account Management
# Description:
#   Create a 'BankAccount' class without using __init__. The class should:
#     1. Have a 'set_account()' method to set account holder's name and balance.
#     2. Have a 'deposit()' method to add money to balance.
#     3. Have a 'withdraw()' method to take out money (if balance is enough).
#     4. Have a 'show_info()' method to display account details.
#   All data should be set via set_account(), not via constructor.


class BankAccount:
    def set_account(self, name, balance):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("please deposit minimum amount")
            
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")
            
    def show_info(self):
        print(f"Account holder: {self.name}")
        print(f"Current balance: {self.balance}")
        
        
account1 = BankAccount()

account1.set_account("Shefa", 5000)
account1.deposit(1300)
account1.withdraw(3200)
account1.show_info()