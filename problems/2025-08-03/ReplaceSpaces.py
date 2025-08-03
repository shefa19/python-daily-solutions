size = int(input("Enter size of list: "))

words = [input("Enter word: ") for _ in range(size)]

spaceReplace = [word.replace(" ","-") for word in words]

print(spaceReplace)