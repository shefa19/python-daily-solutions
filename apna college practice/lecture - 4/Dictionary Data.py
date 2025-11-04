# Store following word meanings in a python dictionary : 
# table : “a piece of furniture”, “list of facts & figures”
#  cat : “a small animal”


my_dict = {
    'table' : ["a piece of furniture", "list of facts & figures"],
    'cat' : "a small animal"
}

for key, val in my_dict.items():
    print(f"{key} : \n\t{val}")
    