try:
    marks = int(input("Enter your marks: "))
    grade = ''
    if marks > 100 or marks < 0:
        print("Invalid marks. Please input a valid marks")
    elif marks >= 80:
        grade = "A+"
    elif marks > 70:
        grade = "A"
    elif marks > 50:
        grade = "A-"
    elif marks > 40:
        grade = 'B'
    elif marks > 32:
        grade = "C"
    else:
        grade = 'F'
    
    if grade:
        print("Your Grade : ", grade)
except ValueError:
    print("Invalid input, Please input a valid marks")