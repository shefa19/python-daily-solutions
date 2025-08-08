# Problem Name: Season Finder
# Description: Determine the season based on the month number (1-12).

try:
    month = int(input("Enter a month number(1-12): ").strip())
    
    match month:
        case 1 | 2:
            print("Summer")
        case 3 | 4:
            print("Rainy Season")
        case 5 | 6:
            print("Autumn")
        case 7 | 8:
            print("Late Autumn")
        case 9 | 10:
            print("Winter")
        case 11 | 12:
            print("Spring")
        case _:
            print("Invalid month number.")
            
except ValueError:
    print("Enter a valid number of month.")