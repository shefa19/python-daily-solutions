# problem: common elements in two lists
# description: find common elements using set intersection

sizeList1 = int(input("Enter size of list 1: "))
sizeList2 = int(input("Enter size of list 2: "))

print(f"Enter {sizeList1} item of List 1: ")
list1 = [int(input()) for _ in range(sizeList1)]

print(f"Enter {sizeList2} item of List 2: ")
list2 = [int(input()) for _ in range(sizeList2)]

set1 = set(list1)
set2 = set(list2)

common = set1.intersection(set2)

print("Common elements: ",common)