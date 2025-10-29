my_list = [1, 2, 3, 4, 5]
k = 2

rotation_list  = my_list[-k:] + my_list[:len(my_list)-k]

print(rotation_list)

