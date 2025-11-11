# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]


nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

try:
    x = int(input("Enter a value: ").strip())
    
    index = None
    for i, num in enumerate(nums):
        if num == x:
            index = i
            break
    
    if index:
        print("Target value found at index: ", index)
    else:
        print("Target value not found")
    
except ValueError:
    print("Invalid data type")
except Exception:
    print("Unexpected Error")