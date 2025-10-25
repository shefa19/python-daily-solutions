try:
    num1, num2, num3 = map(int, input("Enter three numbers: ").split())
    greatest = 0
    
    if num1 >= num2 and num1 >= num3:
        greatest = num1
    elif num2 >= num1 and num2 >= num3:
        greatest = num2
    else:
        greatest = num3
    
    print(f"{greatest} is the greatest number")
    
except ValueError:
    print("Invalid input. Please input a valid number")