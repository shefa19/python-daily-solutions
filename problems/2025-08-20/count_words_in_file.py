# -------------------------------------------------------
# Problem 2: Count Words in a File
# -------------------------------------------------------
# Description:
# Write a program that reads a file and counts 
# the total number of words inside it.
#
# Input Format:
# A text file containing multiple lines of text.
#
# Output Format:
# Print the total word count.
#
# Example:
# File Content:
#   Python is fun
#   File handling is important
# Output:
#   Total Words: 7
# -------------------------------------------------------


with open("file.txt", "w") as file:
    file.write("Python is fun\n")
    file.write("File handling is important\n")
    
with open("file.txt", "r") as file:
    words = file.read().split()
    print(f"Total Words: {len(words)}")