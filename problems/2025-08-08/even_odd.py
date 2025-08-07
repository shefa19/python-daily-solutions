# Problem: Even or Odd
# Description: Check whether a given integer is even or odd using if-else.


try:
    num = int(input("Enter an integer number: "))
    
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
        
except ValueError:
    print("Please enter a valid integer number.")