# Problem Name: Reverse Array Using Function
# Description:
#   Write a function reverse_array(arr) that returns the reversed array.
#   In the main part, take the size and elements of the array as input, call reverse_array, and print the reversed array.


def reverse_array(arr):
    return arr[::-1]

try:
    n = int(input("Enter of size: ").strip())
    
    arr =[int(input()) for _ in range(n)]
    
    print(*reverse_array(arr))
    
except ValueError:
    print("Please enter valid integer.")