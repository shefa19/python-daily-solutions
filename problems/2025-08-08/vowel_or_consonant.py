# Problem: Vowel or Consonant
# Description: Take a single character as input. Print "Vowel" if it's a vowel (a, e, i, o, u), otherwise "Consonant".


character = input("Enter a single character: ")

if len(character) != 1 or not character.isalpha():
    print("Enter a single character.")
else:
    character = character.lower()
    
    if character in ['a','e','i','o','u']:
        print("Vowel")
    else:
        print("Consonant")