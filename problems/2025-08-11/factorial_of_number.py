# Problem Name: Factorial of a Number
# Description: Calculate the factorial of a given number N using a for loop.

try:
    N = int(input("Enter a single integer: ").strip())
    
    if N < 0:
        print("Invalid input. Please enter a positive integer.")
    else:
        factorial = 1
        for i in range(1,N + 1):
            factorial *= i
        print(f"Fatorial of {N} is = {factorial}")
        
except ValueError:
    print("Please enter a valid integer.")
        