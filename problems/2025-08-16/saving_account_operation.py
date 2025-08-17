# Problem Name: Savings Account Operations
# -------------------------------------------------------
# Description:
# Create a class `Person`.
# Create a subclass `AccountHolder` that inherits from `Person` and has 
# `acc_no` and `balance`.
# Create another subclass `SavingsAccount` that inherits from `AccountHolder` 
# and has `interest_rate`.
# Add methods: deposit(amount), withdraw(amount), add_interest(years).
# Use simple interest formula for interest: balance += balance * rate/100 * years
#
# Input Format:
# name acc_no balance rate action val
# (action = deposit, withdraw, or interest)
#
# Output Format:
# Account <acc_no>, Holder: <name>, Balance: <balance>
#
# Example Input 1:
# Rina 201234 10000 5 deposit 2000
#
# Example Output 1:
# Account 201234, Holder: Rina, Balance: 12000.00
#
# Example Input 2:
# Rina 201234 10000 5 interest 2
#
# Example Output 2:
# Account 201234, Holder: Rina, Balance: 11000.00
