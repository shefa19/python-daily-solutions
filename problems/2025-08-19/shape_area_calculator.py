# Problem 2: Shape Area Calculator
# -------------------------------------------------------
# Description:
# Create a base class `Shape` with a method `area()`.
# Create subclasses `Circle`, `Rectangle`, and `Triangle`, each overriding `area()`
# to calculate the respective areas.
# Demonstrate polymorphism by storing all shapes in a list and printing their areas.
#
# Input Format:
# shape_name followed by necessary dimensions
# - circle r
# - rectangle length width
# - triangle base height
#
# Output Format:
# Print the area of the given shape rounded to 2 decimals.
#
# Example Input:
# rectangle 4 6
#
# Example Output:
# 24.00


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        PI = 3.1416
        return PI * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shape_name, *values = input("Enter shape name and dimensions: ").strip().lower().split()

obj = None
try:
    match shape_name:
        case "circle":
            radius = float(values[0])
            obj = Circle(radius)
        case "rectangle":
            length, width = map(float, values)
            obj = Rectangle(length, width)
        case "triangle":
            base, height = map(float, values)
            obj = Triangle(base, height)
        case _:
            print("Unknown shape")
except (ValueError, IndexError):
    print("Invalid input")

if obj:
    print(f"{obj.area():.2f}")
