def add_numbers(a, b):
    summation= a + b
    return summation

def factorial(n):
    if n <= 1:
        return n
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact