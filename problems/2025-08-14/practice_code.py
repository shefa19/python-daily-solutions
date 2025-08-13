class student:
    def __init__(self, x, y):
        self.name = x
        self.roll = y
        
    def display_data(self):
        print(f"Name: {self.name}\nRoll: {self.roll}")
        
student1 = student("Shefaul", 42)
student1.display_data()