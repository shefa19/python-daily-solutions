word = "I love Python because Python is powerful"

my_dict = {}

for w in word.split():
    if not w in my_dict:
        my_dict[w] = word.count(w)

print(my_dict)