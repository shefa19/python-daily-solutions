# Problem Name: Multiplication Table
# Description: Print the multiplication table of a given number using a for loop.

try:
    N = int(input("Enter a single integer: ").strip())
    
    if N <= 0:
        print("Please enter a positive integer greater than 0.")
    else:
        for i in range(1, 11):
            print(f"{N} x {i} = {N * i}")
            
except ValueError:
    print("Please enter a valid integer.")