USD = float(input("Enter USD amount: ").strip())

def convert(usd):
    inr = usd * 90.5
    return inr

INR = convert(USD)
print("INR amount is: ", INR)