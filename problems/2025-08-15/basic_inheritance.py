# Problem Name: Basic Inheritance Example
# Description:
# Create a class `Animal` with a method `sound()` that prints "Animal makes a sound".
# Then create a subclass `Dog` that overrides the `sound()` method to print "Dog barks".
# Finally, create another subclass `Cat` that overrides the `sound()` method to print "Cat meows".
# Take the animal type as input and call the respective sound method.
#
# Input Format:
# A single string representing the animal type (e.g., "Dog" or "Cat").
#
# Output Format:
# A single line showing the sound made by that animal.
#
# Example Input:
# Dog
# Example Output:
# Dog barks

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")
        
class Cat(Animal):
    def sound(self):
        print("Cat meows")
        

animal_type = input().strip()

if not animal_type.isalpha():
    print("Please enter correct animal type")
else:
    animal_type = animal_type.capitalize()
    if animal_type == "Dog":
        obj = Dog()
    elif animal_type == "Cat":
        obj = Cat()
    else:
        obj = Animal()

obj.sound()