# Print the multiplication table of a number n. 

try:
    num = int(input("Enter a number: ").strip())
    
    for n in range(1, 11):
        print(f"{num} x {n} = {num * n}")
        
except ValueError:
    print("Invalid data type")
except Exception:
    print("Unexpected Error")