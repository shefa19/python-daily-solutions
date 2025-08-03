# Problem: Unpack & Reverse
# Description: Given a tuple with 4 elements, unpack them into four variables and print them in reverse order.

size = 4

data = tuple(input("Enter word:") for _ in range(size))

(first,second,third,fourth) = data

print(fourth,third,second,first)