my_list = list(map(int, input("Input some list value: ").split()))

sum = 0
for n in my_list:
    if n % 2 == 0:
        sum += n
        
print("Sum of Even Numbers = ", sum)