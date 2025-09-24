print("Enter the value of array")
array = sorted(map(int, input().split()))

print("Enter the target value: ", end="")
target = int(input())

left, right = 0, len(array) - 1
find = False
mid = -1
while left <= right:
    mid = (left + right) // 2
    
    if array[mid] == target:
        find = True
        break
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
        
if not find:
    print("The target value is not find")
else:
    print("The target value in index : ", mid)