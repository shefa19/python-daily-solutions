# Problem Name: Count Vowels and Consonants
# Description:
#   Given a string s, count and print the number of vowels and consonants.
#   Consider vowels as a, e, i, o, u (case-insensitive).


s = input("Enter a string: ").strip()

if not s.isalpha():
    print("Invalid input. Please enter alphabets only.")
else:
    total_vowels = 0
    total_consonants = 0
    for i in s:
        match i.lower():
            case 'a'|'e'|'i'|'o'|'u':
                total_vowels += 1
            case _:
                total_consonants += 1
    print(f"Vowels: {total_vowels}")
    print(f"Consonant: {total_consonants}")