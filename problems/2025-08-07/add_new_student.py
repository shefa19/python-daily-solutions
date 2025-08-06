# Problem: Add a new student to the dictionary using user input.
# description: Prompt the user to enter a roll, name, and GPA, and add to dictionary.

student = {}

try:
    roll = int(input("Enter a student roll: "))
    
    name = input("Enter a student name: ")
    
    gpa = float(input(f"Enter {name}'s GPA: "))
    
    student[roll] = {"name": name, "GPA": gpa}
    
except ValueError:
    print("Enter valid roll , name or GPA")
    

print(f"Student added: {student.get(roll)}")