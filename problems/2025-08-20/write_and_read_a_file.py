# -------------------------------------------------------
# Problem: Write and Read a File
# -------------------------------------------------------
# Description:
# Create a program that writes a string into a file, 
# then reads the file content and prints it.
#
# Input Format:
# A single line string from the user.
#
# Output Format:
# Print the string read from the file.
#
# Example:
# Input: Hello Python
# Output: Hello Python


with open("file.txt", "w") as file:
    file.write(input())
    
with open("file.txt", "r") as file:
    print(file.read())
    