my_dict = {'Math': 85, 'English': 78, 'Science': 92}

max_value = max(my_dict.values())
max_key = None

for key, val in my_dict.items():
    if val == max_value:
        max_key = key
        break
    
print(max_key)