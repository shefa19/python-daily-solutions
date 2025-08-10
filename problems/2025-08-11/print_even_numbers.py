# Problem Name: Print Even Numbers
# Description: Write a program that prints all even numbers from 1 to N using a for loop.

try:
    N = int(input("Enter a single integer: ").strip())
    
    if N <= 0:
        print("Please enter a positive integer greater than 0.")
    else:
        for i in range(2, N+1, 2):
            print(i, end=" ")
            
except ValueError:
    print("Please enter a valid number.")