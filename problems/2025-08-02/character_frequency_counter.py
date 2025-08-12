# Problem Name: Character Frequency Counter
# Description: Given a string , print the frequency of each character in the order of their appearance.


txt = input("Enter a string: ").strip()

frequency = {}

for i in txt:
    n = txt.count(i)
    frequency.update({i : n})

for key, value in frequency.items():
    print(f"{key}: {value}")