from area import triangle_area, square_area

try:
    b, h = map(int, input("Enter base and height value: ").split())
    a = int(input("Enter side value of Square: "))
    
    
    print(f"Area of Triangle is : {triangle_area(b, h)}")
    print(f"Area of Square is : {square_area(a)}")
    
except ValueError:
    print("Please enter valid values.")