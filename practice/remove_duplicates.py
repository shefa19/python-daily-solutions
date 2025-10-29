my_list = list(map(int, input("Enter some numbers: ").split()))

new_list = []
for n in my_list:
    if not n in new_list:
        new_list.append(n)

print(new_list)