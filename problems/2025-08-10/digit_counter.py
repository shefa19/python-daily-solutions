# Problem Name: Digit Counter
# Description: Take a positive integer as input and count how many digits it has using a while loop.

try:
    N = int(input("Enter a positive integer number: ").strip())
    
    if N < 0:
        print("Invalid entered number.")
    else:
        count_digit = 0
        i = N
        while i != 0:
            i //= 10
            count_digit += 1
        print("Total digit: ",count_digit)
              
except ValueError:
    print("Enter a valid positive number.")