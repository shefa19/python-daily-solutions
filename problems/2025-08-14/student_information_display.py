# Problem Name: Student Information Display
# -------------------------------------------------------
# Description:
# Create a class named `Student` with the following attributes:
#   - name (string)
#   - roll (integer)
#   - marks (float)
#
# In the class, implement the __str__() method so that when a
# Student object is printed, it shows a readable output like:
#   "Name: [name], Roll: [roll], Marks: [marks]"


class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
        
    def __str__(self):
        return f"Name: {self.name}, Roll: {self.roll}, Marks: {self.marks:.2f}"
    
    
s1 = Student("Shefa", 42, 3.88)
print(s1)