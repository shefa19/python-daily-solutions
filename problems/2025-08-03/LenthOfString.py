size = int(input("Enter size of list: "))

words = [input("Enter word:") for _ in range(size)]

wordLenth = [len(word) for word in words]

print(wordLenth)