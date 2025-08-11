# Function Examples in Python
# Author: Shefaul Islam Shefa
# Description: Demonstrating various types of Python functions with parameters, *args, **kwargs,
# default values, positional-only, keyword-only, and recursion.

# 1. Basic function without parameters
def my_function1():
    """Prints a hello message."""
    print("Hello from my function")

my_function1()


# 2. Function with one parameter
def my_function2(name):
    """Prints the given name."""
    print("Name:", name)

my_function2("Shefa")
my_function2("Rafsan")


# 3. Function with multiple parameters
def my_function3(fname, name):
    """Prints data in 'key : value' format."""
    print(fname + " : " + name)

my_function3("Email", "sishefa19")


# 4. Function that performs an action based on argument value
def my_function(args):
    """Prints a message based on the instruction given."""
    if args == "print":
        print("Hello World")
    else:
        print("Unknown instruction")

my_function("print")


# 5. Function using *args to accept multiple arguments
def my_function4(*args):
    """Prints two arguments in 'key : value' format."""
    print(args[0] + " : " + args[1])

my_function4("Email", "sishefa19")


# 6. Function using *args to print all arguments
def my_function(*args):
    """Prints all passed arguments separated by space."""
    for i in args:
        print(i, end=" ")
    print()

my_function("apple", "banana", "cherry")


# 7. Function with keyword arguments
def my_function5(child3, child2, child1):
    """Prints the youngest child's name."""
    print("The youngest child is " + child3)

my_function5(child1="Rafsan", child2="Rafit", child3="Muntaha")


# 8. Function with **kwargs (keyword arguments as dictionary)
def my_function6(**kwargs):
    """Prints the last name from keyword arguments."""
    print("His last name is " + kwargs["lname"])

my_function6(fname="Shefaul", mname="Islam", lname="Shefa")


# 9. Function with default parameter value
def my_function7(country="Canada"):
    """Prints the country name. Defaults to 'Canada'."""
    print("I am from " + country)

my_function7("Bangladesh")
my_function7()


# 10. Function taking a list as argument
def my_function8(food):
    """Prints each item in the given list."""
    for i in food:
        print(i, end=" ")
    print()

fruits = ["apple", "banana", "cherry"]
my_function8(fruits)


# 11. Function that returns a calculated value
def my_function9(x):
    """Returns three times the given number."""
    return 3 * x

print(my_function9(3))


# 12. Empty function (placeholder)
def my_function10():
    """Empty function placeholder."""
    pass


# 13. Positional-only argument (/) - must be passed by position
def my_function11(x, /):
    """Prints the value passed. Argument must be positional."""
    print(x)

my_function11(3)


# 14. Keyword-only arguments (*) - must be passed by name
def my_function12(*, a, b):
    """Prints values of a and b. Arguments must be keyword-only."""
    print(a, b)

my_function12(a=10, b=20)


# 15. Mixed: Positional-only and keyword-only
def my_function13(a, b, /, *, c, d):
    """Adds four numbers (a, b positional-only; c, d keyword-only)."""
    print(a + b + c + d)

my_function13(5, 10, c=10, d=5)


# 16. Recursive function
def my_function14(k):
    """
    Recursively sums numbers from k down to 0.
    Example: k=5 → 5+4+3+2+1+0 = 15
    """
    if k > 0:
        result = k + my_function14(k - 1)
    else:
        result = 0
    return result

results = my_function14(5)
print(results)
