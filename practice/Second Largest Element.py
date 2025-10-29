try:
    my_list = list(map(int, input("Enter some number: ").split()))

    my_list = list(set(my_list))
    
    if len(my_list) > 0:
        my_list.sort()
        second_l = my_list[-2]
        print("Second Largest Number is = ", second_l)
    else:
        print(my_list)
    
except ValueError:
    print("Invalid Input. Please enter valid number")