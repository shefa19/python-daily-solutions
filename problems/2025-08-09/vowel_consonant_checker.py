# Problem Name: Vowel or Consonant Checker
# Description: Take a character input and determine whether it's a vowel or consonant.

character = input("Enter a single character: ")

if len(character) != 1 or not character.isalpha():
    print("Enter a single character")
else:
    character = character.lower()
    
    match character:
        case 'a'|'e'|'i'|'o'|'u':
            print("Vowel")
        case _:
            print("Consonant")