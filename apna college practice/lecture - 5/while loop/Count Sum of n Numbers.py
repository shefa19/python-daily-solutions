# WAP to find the sum of first n numbers. (using while)

try:
    n = int(input("Enter a number: ").strip())
    
    sum, i = 0, 1
    while i <= n:
        sum += i
        i += 1
    
    print(f"Sum of first {n} numbers : {sum}")
    
except ValueError:
    print("Invalid data type")
except Exception:
    print("Unexpected Error")