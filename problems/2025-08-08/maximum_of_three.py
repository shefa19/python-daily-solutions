# Problem: Maximum of Three
# Description: Take three integers and print the largest one using nested if-else.


try:
    num1, num2, num3 = map(int, input("Enter three integer number: ").split())
    
    if num1 > num2:
        if num1 > num3:
            print("Maximum is: ", num1)
        else:
            print("Maximum is: ", num3)
    else:
        if num2 > num3:
            print("Maximum is: ", num2)
        else:
            print("Maximum is: ", num3)
            
        
except ValueError:
        print("Enter valid integer number.")