# problem: remove duplicate and sort
# description: remove duplicates from list using set and sort the result

# input size
size = int(input("Enter size of list: "))

# input element
print(f"Enter {size} elemts of list: ")
number = [int(input()) for _ in range(size)]

# converting to set
numberSet = set(number)

# sorting and convertig to list
sortedNumber = sorted(list(numberSet))

#display
print(f"Unique sorted list: ",sortedNumber)
