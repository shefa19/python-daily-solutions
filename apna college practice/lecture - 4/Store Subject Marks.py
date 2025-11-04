'''WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with 
an empty dictionary & add one by one. Use subject name as key & marks as value'''

document = {}

try:
    for _ in range(3):
        sub,marks = input("Enter a subject name and marks: ").strip().split()
        document[sub] = int(marks)
        
    print("Final marks dictionary:", document)
    
except ValueError:
    print("Invalid data type")
except Exception:
    print("Unexpected Error")