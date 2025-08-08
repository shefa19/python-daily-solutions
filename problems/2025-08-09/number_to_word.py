# Problem Name: Number to Word
# Description: Convert a number (0-9) into its word form.

try:
    number = int(input("Enter a number (0-9): "))
    
    match number:
        case 0:
            print("Zero")
        case 1:
            print("One")
        case 2:
            print("Two")
        case 3:
            print("Three")
        case 4:
            print("Four")
        case 5:
            print("Five")
        case 6:
            print("Six")
        case 7:
            print("Seven")
        case 8:
            print("Eight")
        case 9:
            print("Nine")
        case _:
            print("Invalid number")
            
except ValueError:
        print("Inter a valid number")