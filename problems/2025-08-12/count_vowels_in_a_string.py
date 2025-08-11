# Problem Name: Count Vowels in a String
# Description:
#   Write a function count_vowels(s) that returns the number of vowels (a, e, i, o, u) in a given string.
#   The check should be case-insensitive.
#   In the main part, take a string input, call count_vowels, and print the result.


def count_vowels(s):
    count = 0
    for i in s:
        match i:
            case 'a'|'e'|'i'|'o'|'u':
                count += 1 
    return count        

s = input("Enter a single line string: ").strip()

if not s.isalpha():
    print("Please enter a valid string.")
else:
    print(count_vowels(s.lower()))