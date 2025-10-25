try:
    
    num = int(input("Input a number: "))
    
    if num % 7 == 0:
        print(f"{num} multiple of 7")
    else:
        print(f"{num} not a multiple of 7")
    
except ValueError:
    print("Invalid input. Please input a valid number")