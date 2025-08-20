# -------------------------------------------------------
# Problem Name: Append Data if File Exists
# -------------------------------------------------------
# Description:
# Write a program that checks if a file exists. 
# If it exists, append the text "Data append successfully" 
# to the file and then display the full content. 
# If the file does not exist, print "File does not exist".
#
# Input Format:
# (No direct input from the user. The program works 
# with an existing file named "file.txt".)
#
# Output Format:
# If the file exists:
#   Print the full content of the file after appending.
# If the file does not exist:
#   Print "File does not exist".
#
# Example 1:
# File Content before:
#   Hello World
# Program Output:
#   Hello WorldData append successfully
#
# Example 2:
# If "file.txt" does not exist:
# Program Output:
#   File does not exist

import os

if os.path.exists("file.txt"):
    with open("file.txt", "a") as file:
        file.write("Data append successfully")
    
    with open("file.txt", "r") as file:
        print(file.read())
else:
    print("File does not exist")