# Define two variables
a = 20
b = 15

# Simple if-else comparison
if a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")  

# Using if-elif-else for more detailed comparison
if a > b:
    print(f"{a} is greater than {b}")
elif a == b:
    print(f"{a} and {b} are both equal")
else:
    print(f"{b} is greater than {a}") 

# One-liner if statement
if a > b: 
    print(f"{a} is greater than {b}")

# Ternary conditional operator
print(f"{a} is greater than {b}") if a > b else print(f"{b} is greater than {a}")

# Nested ternary for equality check
print(f"{a} is greater than {b}") if a > b else print(f"{a} and {b} are both equal") if a == b else print(f"{b} is greater than {a}")

# Division operation with logical condition
if a != 0 and b > 0:
    result = a / b
    print(f"{a} / {b} = {result}")

# Using 'or' to check if either condition is true
if a > b or b == 15:
    print(f"{a} + {b} = {a+b}")

# Using 'not' to negate a condition
if not a < b:
    print(f"{a} is not less than {b}")

if a > b:
    if b > 0:
        result =  a / b;
        print(f"{a} / {b} = {result}")
    else:
        print("Division not possible")
        

# Placeholder block using 'pass'
if a > b:
    pass  