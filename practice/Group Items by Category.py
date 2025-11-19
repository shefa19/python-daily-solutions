items = [('Fruit', 'Apple'), ('Fruit', 'Banana'), ('Vegetable', 'Carrot')]

new_dict = {}

for key, val in items:
    if key not in new_dict:
        new_dict[key] = []
    new_dict[key].append(val)
print(new_dict)