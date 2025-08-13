# Problem Name: Student Registration System
# Description:
#   Create a 'Student' class with the following features:
#     1. The __init__ method should take 'name' and 'roll' as parameters and store them in the object.
#     2. Create a method 'show_info()' that prints the student's name and roll number.
#     3. Take input from the user to register multiple students.
#     4. Store all student objects in a list.
#     5. At the end, display all registered students' information using the show_info() method.


class student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")

students = []

try:
    n = int(input("How many students do you want to register: ").strip())

    for i in range(n):
        name = input("Enter student's name: ").strip()
        roll = int(input("Enter student's roll: ").strip())
        
        students.append(student(name, roll))
    
except ValueError:
    print("Please enter valid data.")
    
for s in students:
    s.show_info()

