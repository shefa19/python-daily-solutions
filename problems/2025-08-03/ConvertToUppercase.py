size = int(input("Enter size of list: "))

words = [input("Enter word: ") for _ in range(size)]

wordUppercase = [word.upper() for word in words]

print(wordUppercase)