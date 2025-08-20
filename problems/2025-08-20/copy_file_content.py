# -------------------------------------------------------
# Problem 4: Copy File Content
# -------------------------------------------------------
# Description:
# Create a program that copies the content of one file 
# into another file.
#
# Input Format:
# Two file names: source.txt and destination.txt
#
# Output Format:
# Print "File copied successfully".
#
# Example:
# If source.txt has:
#   Python File Handling
# Then destination.txt will also contain:
#   Python File Handling

import os

source_file , destination_file = input().split()

if os.path.exists(source_file):
    with open(source_file, "r") as file:
        content = file.read()
        
    with open(destination_file, "w") as file:
        file.write(content)
        
    print("File copied successfully")
else:
    print("File does not exist.")