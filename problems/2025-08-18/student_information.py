# Problem Name: Student Information
# -------------------------------------------------------
# Description:
# Create a class `Student` that has attributes `name`, `roll`, and `marks`.
# Use a constructor to initialize these attributes.
# Add a method `display()` to show the student details in a formatted way.
#
# Input Format:
# name roll marks
#
# Output Format:
# Name: <name>
# Roll: <roll>
# Marks: <marks>
#
# Example:
# Input:
# Alice 101 85
#
# Output:
# Name: Alice
# Roll: 101
# Marks: 85

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}\nRoll {self.roll}\nMarks: {self.marks}")
        

try:
    name, roll, marks = input().split()
    
    roll, marks = int(roll), int(marks)
    
    s1 = Student(name, roll, marks)
    s1.display()
    
except ValueError:
    print("Enter valid data")