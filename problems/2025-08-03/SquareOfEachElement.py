n = int(input("Enter size of list: "))

list = [int(input("Enter number: ")) for _ in range(n)]

newList = [i**2 for i in list]

print(newList)