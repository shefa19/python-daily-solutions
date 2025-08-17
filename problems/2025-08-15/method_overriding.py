# Problem Name: Method Overriding with super()
# -------------------------------------------------------
# Description:
# Create a class `Vehicle` with a method `details()` that prints "This is a vehicle".
# Create a subclass `Car` that overrides the `details()` method but also calls the parent method using `super()`,
# then prints "This is a car".
#
# Input Format:
# No input required.
#
# Output Format:
# First line: "This is a vehicle"
# Second line: "This is a car"
#
# Example Input:
# (no input)
# Example Output:
# This is a vehicle
# This is a car

class Vehicle:
    def details(self):
        print("This is a vehicle.")
        
class Car(Vehicle):
    
    def details(self):
        super().details()
        print("This is a car")
        
obj = Car()
obj.details()
    
