size = int(input("Enter the size of list:"))

list = [int(input("Enter value:")) for _ in range(size)]

newList = [i for i in list if i%2 == 0]

print(newList)