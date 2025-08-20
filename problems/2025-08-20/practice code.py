# # -------------------------------
# # Write to a file
# # -------------------------------
# myFile = open("student.txt", "w")
# myFile.write("My name is Shefaul Islam")
# myFile.close()

# with open("student.txt", "w") as myFile:
#     myFile.write("My name is Shefaul Islam")


# # -------------------------------
# # Read from a file
# # -------------------------------
# myFile = open("student.txt", "r")
# content = myFile.read()
# print(content)
# myFile.close()

# with open("student.txt", "r") as myFile:
#     content = myFile.read()
#     print(content)


# # -------------------------------
# # Append to a file
# # -------------------------------
# myFile = open("student.txt", "a")
# myFile.write("In the long run I want to be a Data Scientist.")
# myFile.close()

# with open("student.txt", "a") as myFile:
#     myFile.write("In the long run I want to be a Data Scientist.")
    

# with open("myFile.txt") as f:
#   print(f.read(5))

# with open("myFile.txt", "r") as myFile:
#     print(myFile.readline())

# with open("myFile.txt") as f:
#   for x in f:
#     print(x)
  


# # -------------------------------
# # Delete a file
# # -------------------------------
# import os
# os.remove("student.txt")

    
# import os
# if os.path.exists("myFile.txt"):
#   os.remove("myFile.txt")
# else:
#   print("The file does not exist")

import os

if os.path.exists("renamedFile.txt"):
    os.rename("renamedFile.txt", "myFile")  # current name, new name
else:
    print("The file does not exist")

    
# import os
# os.rmdir("myfolder")