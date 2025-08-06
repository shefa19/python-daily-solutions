# Practice distonary all methods

myDict = {
    101: {
        "Name": "Shefa",
        "Roll": 42,
        "GPA": 3.88
    },
    102: {
        "Name": "Rifa",
        "Roll": 43,
        "GPA": 3.88
    },
    103: {
        "Name": ["Sajol", "Sakib"],
        "Roll": (2, 4),
        "GPA": {3.80, 3.50}
    }
}

# Checking the type of myDict
print(type(myDict))

# Printing the whole dictionary
print(myDict)

# Taking a key from user input
key = int(input("Enter a key: "))

# Retrieving value using get() method with a default message if key not found
print(myDict.get(key, "Not found"))

# Printing number of main keys (students)
print(len(myDict))

# Printing all values and keys
print(myDict.values())
print(myDict.keys())

# Counting how many student records (values) exist
valueCount = len(myDict.values())
print(valueCount)

# Counting total number of attributes inside all nested dictionaries
totalAttributes = sum(len(info) for info in myDict.values())
print(totalAttributes)

# Adding a new key-value pair 'Batch' to student 101 only
myDict[101]["Batch"] = 115
print(myDict)

# Adding 'Batch' key with value 115 to all students
for student in myDict.values():
    student["Batch"] = 115

# Updating name of student 101
myDict[101].update({"Name": "Shefaul"})
print(myDict)

# Removing 'Batch' key from student 101 only
myDict[101].pop("Batch")
print(myDict)

# Removing 'Batch' key from all students safely
for student in myDict.values():
    student.pop("Batch", None)
print(myDict)

# Removing last inserted item from each student's dictionary
for student in myDict.values():
    student.popitem()
print(myDict)

# Iterating through keys
for key in myDict:
    print(key)

# Iterating through values
for key in myDict:
    print(myDict[key])

# Using keys() to print all keys
for key in myDict.keys():
    print(key)

# Using values() to print all values
for value in myDict.values():
    print(value)

# Using items() to print key-value pairs
for key, value in myDict.items():
    print(key, value)

# Creating a shallow copy using copy()
newDict = myDict.copy()
print(newDict)

# Creating a new dictionary using dict()
newDict_1 = dict(myDict)
print(newDict_1)

# Nicely formatted output of all student details
for role, details in myDict.items():
    print(f"\n{role}:")
    for key, value in details.items():
        print(f"   {key}: {value}")


# Cleare all item
myDict.clear()
