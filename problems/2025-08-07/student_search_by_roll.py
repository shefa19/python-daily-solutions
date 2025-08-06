# Problem: Search for a student's information using their roll number from a dictionary.
# description: Create a dictionary of students and allow the user to search by roll number.


student = {}

while True:
    try:
        roll = int(input("Enter roll or preass 0 for stop: "))
        
        if roll == 0:
            break
        
        name = input("Enter student name: ")
        gpa = float(input("Enter GPA: "))
        
        student[roll] = {"Name": name, "GPA": gpa}
        
    except ValueError:
        print("Enter a valid nuber or GPA.")
            
            
try:
    finding_roll = int(input("Enter roll to search: "))
    
    found = student.get(finding_roll)
    
    if found:
        print(f"Name: {found['Name']}")
        print(f"GPA: {found['GPA']}")
    else:
        print("Sorry this roll is not found.")
        
    
except ValueError:
    print("Enter a valid number")