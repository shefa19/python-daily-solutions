# Problem Name: Count Vowels in a String
# Description: Count how many vowels are in the given string using a for loop.

S = input("Enter a single string: ").strip()

if not S.isalpha():
    print("Invalid input.Please enter a single string.")
else:
    coutn_vowel = 0
    for i in S:
        i = i.lower()
        match i:
            case 'a'|'e'|'i'|'o'|'u':
                coutn_vowel += 1
    print("Number of vowel: ",coutn_vowel)           