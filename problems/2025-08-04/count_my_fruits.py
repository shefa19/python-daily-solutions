# Problem: Count My Fruits
# Description: Given a tuple of fruits, count how many times the word "banana" appears in the tuple.
# Output the count as an integer.

numberOfFruits = int(input("Enter number of fruits:"))

fruits = tuple(input("Enter fruit name: ") for _ in range(numberOfFruits))

countFruit = input("Enter the fruit name: ")

n = fruits.count(countFruit)

print(n)
