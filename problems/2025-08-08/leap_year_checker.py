# Problem: Leap Year Checker
# Description: Take a year as input and check if it is a leap year or not.


try:
    year = int(input("Enter a year: "))
    
    if year % 400 == 0:
        print("Leap Year")
    elif year % 4 == 0 and year % 100 != 0:
        print("Leap Year")
    else:
        print("Not Leap Year")
        
except ValueError:
    print("Enter vlid year.")
