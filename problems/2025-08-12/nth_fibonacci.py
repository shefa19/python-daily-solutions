# Problem Name: Nth Fibonacci
# Description:
#   Write a function fib(n) that returns the nth Fibonacci number.
#   Use either iterative or recursive approach.
#   In the main part, take an integer n as input and print fib(n).



def fib(n):
    a , b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


try:
    n = int(input("Enter a single integer: ").strip())
    
    if n < 0  or  n > 90:
        print("Invalid input. Please inter a valid input.")
    else:
        print(fib(n))
        
except ValueError:
    print("Please input a valid number")