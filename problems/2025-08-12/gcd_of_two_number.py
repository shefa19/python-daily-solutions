# Problem Name: GCD of Two Numbers
# Description:
#   Write a function gcd(a, b) using the Euclidean algorithm.
#   In the main part, take two positive integers as input, call gcd, and print the result.


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

try:
    num1, num2 = map(int, input("Enter two ineger: ").split())

    if num1 < 0 or num2 < 0:
        print("Please enter ineger greater than 0.")
    else:
        print("GCD is: ",gcd(num1, num2))
        
except ValueError:
    print("Please enter valid integer.")