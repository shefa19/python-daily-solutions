# Problem: Find the Index
# Description: Given a tuple of numbers, find the index of the number 50.
# If it exists, print the index. If not, print "Not found".

size = int(input("Enter size of tuple: "))

numbers = tuple(int(input("Enter number: ")) for _ in range(size))

n = int(input("Enter the number:"))

if n in numbers:
    print(numbers.index(n))
else:
    print("Not found")