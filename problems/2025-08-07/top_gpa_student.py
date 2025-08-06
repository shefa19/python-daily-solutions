# Problem: Find the student with the highest GPA from the dictionary.
# description: Given a dictionary of students, print the name and GPA of the top student.

student = {}

highest_gpa = 0.0
top_student_name = ''

while True:
    try:
        name = input("Enter student name or press 0 for stop: ")
        
        if name == '0':
            break
        
        gpa = float(input(f"Enter {name}'s GPA: "))
        
        student[name] = {"GPA": gpa}  
        
        if gpa > highest_gpa:
            highest_gpa = gpa
            top_student_name = name
            
    except ValueError:
        print("Enter a valid name of number.")
        
if top_student_name:
    print(f"Top student: {top_student_name}")
    print(f"GPA: {highest_gpa}")
    
else:
    print("No student data entered.")
