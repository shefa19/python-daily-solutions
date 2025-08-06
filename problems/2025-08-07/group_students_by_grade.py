# Problem: Group students based on grade category using GPA.
# description: Based on GPA, classify students as 'Excellent', 'Good', or 'Average'.

student = {}

while True:
    try:
        name = input("Enter student name or press 0 for stop: ")
        
        if name == '0':
            break
        
        gpa = float(input(f"Enter {name}'s GPA: "))
        
        student[name] = gpa
        
    except ValueError:
        print("Enter a valid name of GPA.")
        
excellent = []
good = []
average = []

for name, gpa in student.items():
    if gpa >= 3.75:
        excellent.append(name)
    elif gpa >= 3.00:
        good.append(name)
    else:
        average.append(name)
        
print("Student grade categories:")
print(f"Excellent: {excellent}")
print(f"Good: {good}")
print(f"Average: {average}")