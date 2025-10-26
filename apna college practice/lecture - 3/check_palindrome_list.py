my_list = [1, 2, 3, 2, 1]

rev_list = my_list.copy()
rev_list.reverse()

if my_list == rev_list:
    print("Palindrome")
else:
    print("Not Palindrome")