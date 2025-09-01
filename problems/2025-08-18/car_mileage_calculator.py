# Problem Name: Car Mileage Calculator
# -------------------------------------------------------
# Description:
# Create a class `Car` with attributes `brand`, `mileage`, and `fuel`.
# Use a constructor to initialize them.
# Add a method `range()` that returns how many kilometers the car can travel 
# with the given fuel.
#
# Input Format:
# brand mileage fuel
#
# Output Format:
# Brand: <brand>
# Possible Range: <range> km
#
# Example:
# Input:
# Toyota 15 10
#
# Output:
# Brand: Toyota
# Possible Range: 150 km

class Car:
    def __init__(self, brand, mileage, fuel):
        self.brand = brand
        self.mileage = mileage
        self.fuel = fuel
        
    def range(self):
        return self.mileage * self.fuel
    

try:
    brand, mileage, fuel = input().split()
    mileage = int(mileage)
    fuel = int(fuel)
    
    c1 = Car(brand, fuel, mileage)
    
    print(f"Brand: {brand}\nPossible Range: {c1.range()} km")
    
except ValueError:
    print("Please input valid data")    