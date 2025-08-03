size = int(input("Enter size of list:"))

words = [input("Enter word: ") for _ in range(size)]

reverseWord = [word[::-1] for word in words]

print(reverseWord) 