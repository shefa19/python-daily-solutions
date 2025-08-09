# Problem Name: Reverse Countdown
# Description: Take a positive integer N as input and print a countdown from N to 1 using a while loop.

try:
    N = int(input("Enter a positive integer number: ").strip())
    
    if N <= 0:
        print("Please enter a number greater than 0.")
    else:
        i = N
        while i > 0:
            print(i,end = " ")
            i -= 1
        
except ValueError:
    print("Please enter a valid positive number.")
    
