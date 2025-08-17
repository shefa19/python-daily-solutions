# Problem Name: Multiple Inheritance Demo
# -------------------------------------------------------
# Description:
# Create a class `Teacher` with a method `teach()` that prints "Teaching students".
# Create another class `Coder` with a method `code()` that prints "Writing code".
# Create a subclass `TeacherCoder` that inherits from both `Teacher` and `Coder`,
# and has a method `display()` that calls both `teach()` and `code()`.
#
# Input Format:
# No input required.
#
# Output Format:
# First line: "Teaching students"
# Second line: "Writing code"
#
# Example Input:
# (no input)
# Example Output:
# Teaching students
# Writing code

class Teacher:
    def teach(self):
        print("Teaching students.")

class Coder():
    def code(self):
        print("Writing code.")

class TeacherCoder(Teacher, Coder):
    def display(self):
        self.teach()
        self.code()
        
    
obj = TeacherCoder()
obj.display()