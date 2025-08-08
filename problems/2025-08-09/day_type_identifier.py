# Problem Name: Day Type Identifier
# Description: Accept the name of a day and determine whether it's a weekday or weekend.

day = input("Enter a name of day: ")

if len(day.split()) != 1:
    print("Enter a single name of day.")
else:
    day = day.capitalize()
    
    match day:
        case 'Saturday' | 'Sunday':
            print("Weekend")
        case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday':
            print("Weekday")
        case _:
            print("Invalid day name")