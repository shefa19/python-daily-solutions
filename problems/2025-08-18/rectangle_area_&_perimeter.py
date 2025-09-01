# Problem Name: Rectangle Area and Perimeter
# -------------------------------------------------------
# Description:
# Create a class `Rectangle` with attributes `length` and `width`.
# Use a constructor to initialize them.
# Add methods `area()` and `perimeter()` to calculate area and perimeter.
#
# Input Format:
# length width
#
# Output Format:
# Area: <area>
# Perimeter: <perimeter>
#
# Example:
# Input:
# 5 3
#
# Output:
# Area: 15
# Perimeter: 16

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    

try:
    length, width = map(int, input().split())
    
    r1 = Rectangle(length, width)
    print(f"Area: {r1.area()}\nPerimeter: {r1.perimeter()}")
    
except ValueError:
    print("Please input valid value")