# problem: check subset
# description: check whether one set is a subset of another

# input size of set
sizeSet_A = int(input("Enter size of set A: "))
sizeSet_B = int(input("Enter size of set B: "))

# input item of set A
print(f"Enter {sizeSet_A} item of set A")
set_A = {int(input()) for _ in range(sizeSet_A)}

# input item of set B
print(f"Enter {sizeSet_B} item of set B")
set_B = {int(input()) for _ in range(sizeSet_B)}

# checking subset
subset = set_A.intersection(set_B) == set_A

# display
print("A is subset of B: ",subset)