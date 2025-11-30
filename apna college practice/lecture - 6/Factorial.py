n = int(input("Enter a number: ").strip())

def fact(n):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    
    return factorial

result = fact(n)
print("Factorial of the number is: ", result)