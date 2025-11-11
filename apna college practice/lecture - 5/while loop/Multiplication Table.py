# rint the multiplication table of a number n. 

try:
    n = int(input("Enter a number: ").strip())
    
    i = 1
    while i <= 10:
        print(f"{n} X {i} = {i * n}")
        i += 1
        
except ValueError:
    print("Invalid data type")