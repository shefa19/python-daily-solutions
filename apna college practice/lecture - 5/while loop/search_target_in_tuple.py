#  Search for a number x in this tuple using loop:
#  [1, 4, 9, 16, 25, 36, 49, 64, 81,100]


nums = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

try:
    x = int(input("Enter a number: ").strip())
    
    i, index = 0, None
    while i < len(nums):
        if nums[i] == x:
            index = i
            break
        i += 1
    
    if index:
        print("Found at index ", index)
    else:
        print("Target number not found")
    
except ValueError:
    print("Invalid data type")
except Exception:
    print("Unexpected Error")
