# problem: symmetric difference of sets
# description: find elements that are in either set but not in both

# input size of set
sizeSet_A = int(input("Enter size of set A: "))
sizeSet_B = int(input("Enter size of set B: "))

#input item of set A
print(f"Enter {sizeSet_A} item of set A")
set_A = {int(input()) for _ in range(sizeSet_A)}

# input item of set B
print(f"Enter {sizeSet_B} item of set B")
set_B = {int(input()) for _ in range(sizeSet_B)}

# finding symmetric difference
symmetricDifference = set_A.symmetric_difference(set_B)

# display
print("Symmetric Difference: ",symmetricDifference)