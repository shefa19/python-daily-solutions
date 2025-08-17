# Problem Name: Constructor Inheritance
# -------------------------------------------------------
# Description:
# Create a class `Person` with a constructor that takes `name` and prints "Person: <name>".
# Create a subclass `Student` that also takes `roll` in its constructor, calls the parent constructor,
# and then prints "Roll: <roll>".
# Input will be name and roll separated by space.
#
# Input Format:
# Two values separated by space: name roll
#
# Output Format:
# First line: "Person: <name>"
# Second line: "Roll: <roll>"
#
# Example Input:
# Alice 101
# Example Output:
# Person: Alice
# Roll: 101

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person: {self.name}")
        
class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
        print(f"Roll: {self.roll}")
        
name, roll = input().split()
roll = int(roll)

student1 = Student(name,roll)

        