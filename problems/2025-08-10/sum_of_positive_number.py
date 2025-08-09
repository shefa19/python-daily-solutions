# Problem Name: Sum of Positive Numbers
# Description: Continuously take integers as input and calculate their sum until the user enters a negative number.


sum_of_numbers = 0
while True:
    try:
        num = int(input("Enter positive number (Negative number for stop): ").strip())
        
        if num < 0:
            break
        else:
            sum_of_numbers += num

    except ValueError:
        print("Enter a valid number.")
        
print("Summation : ",sum_of_numbers)