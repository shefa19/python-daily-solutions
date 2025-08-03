size = int(input("Enter size of list: "))

list = [int(input("Enter value: ")) for _ in range(size)]

newList = [i*3 for i in list if i%2==0]

print(newList)