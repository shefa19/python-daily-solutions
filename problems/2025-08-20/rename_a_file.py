# -------------------------------------------------------
# Problem 5: Rename a File
# -------------------------------------------------------
# Description:
# Write a program that renames a file to a new name.
#
# Input Format:
# Old file name and new file name.
#
# Output Format:
# Print "File renamed successfully" if operation is successful,
# otherwise print "File does not exist".
#
# Example:
# Input: old.txt new.txt
# Output: File renamed successfully

import os

old_file_name, new_file_name = input().split()

if os.path.exists(old_file_name):
    os.rename(old_file_name, new_file_name)
    
    print("File renamed successfully")
else:
    print("File does not exist")