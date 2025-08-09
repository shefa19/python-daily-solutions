# Problem Name: Multiplication Table Generator
# Description: Take a number N and print its multiplication table from 1 to 10 using a while loop.

try:
    N = int(input("Enter an integer number: ").strip())
    
    if N <= 0:
        print("Enter a number greater than 0.")
    else:
        i = 1
        while i <= 10:
            print(f"{N} x {i} = {N * i}")
            i += 1
        
except ValueError:
    print("Enter a valid integer number.")