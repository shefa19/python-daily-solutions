# -------------------------------------------------------
# Problem 3: Append Data to a File
# -------------------------------------------------------
# Description:
# Write a program that appends a user-given string 
# to the end of an existing file.
#
# Input Format:
# A single line string from the user.
#
# Output Format:
# Print "Data appended successfully".
#
# Example:
# Input: I love programming
# Output: Data appended successfully


import os

if os.path.exists("file.txt"):
    with open("file.txt", "a") as file:
        file.write(f"{input()} \n")
        
    print("Data appended successfully")
else:
    print("File does not exist")