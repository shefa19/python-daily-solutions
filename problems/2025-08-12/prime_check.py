# Problem Name: Prime Check
# Description:
#   Write a function is_prime(n) that returns whether n is a prime number (n > 1).
#   In the main part, take an integer input, call is_prime, and print "Prime" or "Not Prime".


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n//2):
        if n % i == 0:
            return False
    return True

try:
    n = int(input("Enter a single integer: ").strip())
    
    if is_prime(n):
        print("Prime")
    else:
        print("Not Prime")
            
except ValueError:
    print("Please enter a valid number.")