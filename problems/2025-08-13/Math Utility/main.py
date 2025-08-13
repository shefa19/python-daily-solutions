from math_utility import *

try:
    a, b = map(int, input("Enter two numbers: ").split())
    n = int(input("Enter a number for factorial: "))
    
    print(f"Sum: {add_numbers(a, b)}")
    print(f"Factorial: {factorial(n)}")
    
except ValueError:
    print("Please enter valid number.")