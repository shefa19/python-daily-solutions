# Problem: Delete a student from the dictonary using roll number.
# Description: Allow the user to input a roll number and remove that entry if it exists.

student = {}

while True:
    try:
        roll = int(input("Enter student roll or press 0 for stop:"))
        
        if roll == 0:
            break
        
        name = input("Enter student name: ")
        gpa = float(input(f"Enter {name}'s GPA: "))
        
        student[roll] = {"Name": name, "GPA": gpa}
        
    except ValueError:
        print("Enter a valid name,number or Digit.")
        
try:        
    remove_roll = int(input("Enter a roll to remove: "))
    
    if remove_roll in student:
        student.pop(remove_roll)
        print(f"Student with roll {remove_roll} has been deleted.")
        
    else:
        print("Student not found.")
        
        
except ValueError:
    print("Enter a valid roll number.")
        
        