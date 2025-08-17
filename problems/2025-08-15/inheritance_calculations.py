# Problem Name: Inheritance with Calculations
# -------------------------------------------------------
# Description:
# Create a class `Shape` with a method `area()` that returns 0.
# Create a subclass `Rectangle` that takes `length` and `width` in its constructor,
# overrides the `area()` method to return length × width.
# Input will be two integers (length and width).
#
# Input Format:
# Two integers separated by space: length width
#
# Output Format:
# A single integer showing the area.
#
# Example Input:
# 5 10
# Example Output:
# 50

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        
    def area(self):
            return self.length * self.width

try:     
    length, width = map(int, input().split())

    obj = Rectangle(length, width)
    print(obj.area())
    
except ValueError:
    print("Please enter valid value")

