# Problem: Grade Calculator
# Description: Take a number (0-100) and print grade based on the following:
# 80-100: A+
# 70-79: A
# 60-69: A-
# 50-59: B
# 40-49: C
# 33-39: D
# 0-32: F
# For any number out of range, print "Invalid input"

try:
    mark = int(input("Enter mark (0 - 100): "))

    if mark > 100 or mark < 0:
        print("Invalid input")
    elif mark >= 80:
        print("A+")
    elif mark >= 70:
        print("A")
    elif mark >= 60:
        print("A-")
    elif mark >= 50:
        print("B")
    elif mark >= 40:
        print("C")
    elif mark >= 33:
        print("D")
    else:
        print("F")
        
except ValueError:
    print("Please enter a valid mark.")