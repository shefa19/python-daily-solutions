# Problem 3: Payment System
# -------------------------------------------------------
# Description:
# Create a base class `Payment` with a method `pay(amount)`.
# Create subclasses `CashPayment`, `CardPayment`, and `MobilePayment`
# that override the `pay()` method to display the payment type along with the amount.
# Demonstrate polymorphism by calling `pay()` with different payment methods.
#
# Input Format:
# payment_type amount
# (where payment_type is cash/card/mobile)
#
# Output Format:
# Print the payment type and amount.
#
# Example Input:
# card 1500
#
# Example Output:
# Paid 1500 using Card Payment

class Payment:
    def pay(self, amount):
        pass

class CashPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Cash Payment"

class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Card Payment"

class MobilePayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Mobile Payment"


user_input = input("Enter payment type and amount: ").strip().lower().split()

if len(user_input) != 2:
    print("Invalid input format.")
else:
    payment_type, amount_str = user_input
    try:
        amount = float(amount_str)

        match payment_type:
            case "cash":
                obj = CashPayment()
            case "card":
                obj = CardPayment()
            case "mobile":
                obj = MobilePayment()
            case _:
                obj = None
                print("Unknown payment type")

        if obj:
            print(obj.pay(amount)) 

    except ValueError:
        print("Amount must be a number.")
