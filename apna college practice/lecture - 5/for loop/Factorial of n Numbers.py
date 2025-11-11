#  WAP to find the factorial of first n numbers. (using for)

try:
    n = int(input("Enter a number: ").strip())
    
    fact = 1
    for num in range(1, n+1):
        fact *= num
        
    print(f"Factorial of first {n} numbers : {fact}")
    
except ValueError:
    print("Invalid data type")
except Exception:
    print("Unexpected Error")