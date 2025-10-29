my_list = ['a', 'b', 'a', 'c', 'b', 'a']

my_dict = {}
for i in my_list:
    my_dict[i] = my_list.count(i)
    
print(my_dict)

    