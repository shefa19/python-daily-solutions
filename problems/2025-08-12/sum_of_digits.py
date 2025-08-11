# Problem Name: Sum of Digits
# Description:
#   Write a function sum_digits(n) that takes an integer n and returns the sum of its digits.
#   In the main part, take an integer input, call sum_digits, and print the result.
#   Ignore the sign for negative numbers.

 
def sum_digits(n):
    sum_of_digits = 0
    while n != 0:
        sum_of_digits += n % 10
        n = n // 10
    return sum_of_digits

   
try:
    num = int(input("Enter a single integer: ").strip())
    print(sum_digits(abs(num)))
    
except ValueError:
    print("Please enter a valid integer.")