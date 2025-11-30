n = int(input("Enter a number: ").strip())

def sum_of_natural_num(n):
    sum = 0
    if n > 0:
        sum = n + sum_of_natural_num(n-1)
    return sum

result = sum_of_natural_num(n)
print(f"Sum of first {n} natural number is: {result}")
