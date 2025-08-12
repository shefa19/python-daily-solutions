# Python String Examples
# ==============================

# Basic printing
print("hello world")
print('hello world')

# Quotes inside string
print('Hi I am "Shefa"')

# Assigning a string to a variable
s = "Hello"
print(s)

# Multiline string
s = """Hi my name is Shefaul Islma Shefa. I am 22 years old.
I have completed my Diploma in Engineering and am currently pursuing a BSc.
I enjoy problem-solving, programming and aim to become a software engineer."""
print(s)

# String indexing
s = "Hello World!"
print(s[1])  # 'e'

# Looping through a string
for i in s:
    print(i, end="")
print()

# String length
print(len(s))

# Substring check
txt = "I love learning new skill"
print("love" in txt)

if "skill" in txt:
    print("Yes, 'skill' is present")

print("love" not in txt)

# String slicing
s = "Hello, World!"
print(s[2:5])
print(s[:5])
print(s[3:])
print(s[-5:-2])

# Case conversion
print(s.upper())
print(s.lower())

# Trimming
s = " Hello, World! "
print(s.strip())

# Replace characters
s = "Hello, World!"
print(s.replace('H', 'J'))

# Split
print(s.split(","))

# Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# f-string formatting
price = 59
print(f"The price is {price} dollars")
print(f"The price is {price:.2f} dollars")
print(f"The price is {20 * 59} dollars")

# Escaping quotes
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

text = "hello world"

print(text.capitalize())        
print("HELLO".casefold())        
print(text.center(20, "-"))      
print(text.count("l"))           
print(text.encode())             
print(text.endswith("world"))    
tab_text = "H\te\tl\tl\to"
print(tab_text.expandtabs(4))    
print(text.find("world"))        

name = "Shefa"
age = 24
print("My name is {} and I am {} years old".format(name, age))  

data = {"name": "Shefa", "age": 24}
print("My name is {name} and I am {age} years old".format_map(data))  

print(text.index("world"))      
print("Hello123".isalnum())      
print("Hello".isalpha())         
print("Hello".isascii())  
print("123".isdecimal())     
print("123".isdigit())        
print("myVar".isidentifier())  
print("hello".islower())       
print("123".isnumeric())       
print("Hello".isprintable())    
print("   ".isspace())           
print("Hello World".istitle())  
print("HELLO".isupper())        
print("-".join(["apple", "banana", "cherry"])) 
print(text.ljust(20, "*"))      
print("HELLO".lower())           
print("   hello   ".lstrip())    

trans_table = str.maketrans("H", "J")           
print("Hello".translate(trans_table))          

print(text.partition(" "))       
print(text.replace("world", "Shefa"))           
print(text.rfind("l"))          
print(text.rindex("l"))         
print(text.rjust(20, "*"))       
print(text.rpartition(" "))      
print(text.rsplit(" "))          
print("   hello   ".rstrip())    
print(text.split())              


multi_line = "Line1\nLine2\nLine3"
print(multi_line.splitlines())   

print(text.startswith("hello"))  
print("   hello   ".strip())     
print("Hello World".swapcase())  
print("hello world".title())     
print(text.upper())              
print("42".zfill(5))              