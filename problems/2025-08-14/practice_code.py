class person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

p1 = person("Shefa",1293063)
print(p1)
print(p1.name)


class student:
    def __init__(self, x, y):
        self.name = x
        self.roll = y
        
    def display_data(self):
        print(f"Name: {self.name}\nRoll: {self.roll}")
        
student1 = student("Shefaul", 42)
student1.display_data()


class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def __str__(self):
        return f"Name: {self.name}\nRoll: {self.id}"
        
e1 = employee("Shefa", 42)
print(e1)
        