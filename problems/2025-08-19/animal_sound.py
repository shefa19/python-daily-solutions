# Problem 1: Animal Sounds
# -------------------------------------------------------
# Description:
# Create a base class `Animal` with a method `sound()`.
# Create subclasses `Dog`, `Cat`, and `Cow` which override the `sound()` method
# to return "Woof", "Meow", and "Moo" respectively.
# Take an animal name as input, create the corresponding object,
# and print its sound. If input is invalid, show an error message.
#
# Input Format:
# A single line containing an animal name (dog/cat/cow)
#
# Output Format:
# Print the sound of the given animal.
# If input is invalid, print an error message.
#
# Example Input 1:
# cat
#
# Example Output 1:
# Meow
#
# Example Input 2:
# tiger
#
# Example Output 2:
# Unknown animal
#
# Example Input 3:
# 123
#
# Example Output 3:
# Please input valid animal name


class Animal:
    def sound(self):
        pass
    
class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"
    
class Cow(Animal):
    def sound(self):
        return "Moo"
    

animal = input("Enter a animal name: ").strip()

if not animal.isalpha():
    print("Please input valid animal name")
else:
    obj = None
    match animal.lower():
        case "dog":
            obj = Dog()
        case "cat":
            obj = Cat()
        case "cow":
            obj = Cow()
        case _:
            print("Unknown animal")
            
if obj:
    print(obj.sound())