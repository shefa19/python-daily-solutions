# Problem Name: Sum of Natural Numbers
# Description: Calculate the sum of the first N natural numbers using a for loop.

try:
    N = int(input("Enter a positive integer: ").strip())
    
    if N <= 0:
        print("Please enter a positive integer greater than 0.")
    else:
        summation = 0
        for i in range(1,N+1):
            summation += i
        
        print(f"Summation of natural number form 1 to {N} : {summation}")
        
except ValueError:
    print("Please enter a valid positive number.")