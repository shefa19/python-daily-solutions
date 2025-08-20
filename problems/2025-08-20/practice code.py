# -------------------------------
# Write to a file
# -------------------------------
myFile = open("student.txt", "w")
myFile.write("My name is Shefaul Islam")
myFile.close()

with open("student.txt", "w") as myFile:
    myFile.write("My name is Shefaul Islam")


# -------------------------------
# Read from a file
# -------------------------------
myFile = open("student.txt", "r")
content = myFile.read()
print(content)
myFile.close()

with open("student.txt", "r") as myFile:
    content = myFile.read()
    print(content)


# -------------------------------
# Append to a file
# -------------------------------
myFile = open("student.txt", "a")
myFile.write("In the long run I want to be a Data Scientist.")
myFile.close()

with open("student.txt", "a") as myFile:
    myFile.write("In the long run I want to be a Data Scientist.")


# -------------------------------
# Read specific number of characters
# -------------------------------
with open("myFile.txt") as f:
    print(f.read(5))

# -------------------------------
# Read a single line
# -------------------------------
with open("myFile.txt", "r") as myFile:
    print(myFile.readline())

# -------------------------------
# Read file line by line using loop
# -------------------------------
with open("myFile.txt") as f:
    for x in f:
        print(x)


# -------------------------------
# Delete a file
# -------------------------------
import os
os.remove("student.txt")

import os
if os.path.exists("myFile.txt"):
    os.remove("myFile.txt")
else:
    print("The file does not exist")


# -------------------------------
# Rename a file
# -------------------------------
import os
if os.path.exists("renamedFile.txt"):
    os.rename("renamedFile.txt", "myFile") 
else:
    print("The file does not exist")


# -------------------------------
# Remove a folder
# -------------------------------
import os
os.rmdir("myfolder")
