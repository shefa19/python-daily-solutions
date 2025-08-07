# Problem: Number Sign Checker
# Description: Take an integer input and print "Positive", "Negative", or "Zero".

num = int(input("Enter a integer number: "))

if num < 0:
    print("Negative")
elif num > 0:
    print("Positive")
else:
    print("Zero")