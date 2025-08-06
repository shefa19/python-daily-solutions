# Problem: Print all students in a formatted way.
# Description: Loop through the dictionary and print all student details nicely.

student = {}

while True:
    try:
        id = int(input("Enter a id or preass 0 for show: "))
        
        if id == 0:
            break
        
        name = input("Enter student name: ")
        roll = int(input(f"Enter {name}'s roll: "))
        gpa = float(input(f"Enter {name}'s GPA: "))
        
        student[id] = {"Name": name, "Roll": roll, "GPA": gpa}
        
    except ValueError:
        print("Enter valid Id,name,roll or GPA.")
        
for sid,details in student.items():
    print(f"\nID: {sid} :-")
    
    for key,value in details.items():
        print(f" {key} | {value}",end="")