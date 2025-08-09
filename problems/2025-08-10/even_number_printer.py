# Problem Name: Even Number Printer
# Description: Print all even numbers between 1 and a given number N using a while loop.

try:
    N = int(input("Enter an integer: ").strip())
    
    if N <= 0:
        print("Enter a positive integer.")
    else:
        i = 2
        while i <= N:
            print(i,end =" ")
            i += 2
            
except ValueError:
    print("Enter a valid integer number.")