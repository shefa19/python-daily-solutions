from temp_converter import *

try:
    c = float(input("Enter temperature in Celsius: "))
    f = float(input("Enter temperature in Fahrenheit: "))
    
    print(f"Celsius to Fahrenheit: {c_to_f(c)}")
    print(f"Fahrenheit to Celsius: {f_to_c(f)}")
    
except ValueError:
    print("Please enter valid value of temperature.")