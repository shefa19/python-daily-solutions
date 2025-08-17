# Problem Name: College People Information
# -------------------------------------------------------
# Description:
# Create a class `Person` with attribute `name` and method `info()`.
# Create a subclass `Staff` that inherits from `Person`, adds `salary`, 
# and overrides `info()`.
# Create another subclass `Teacher` that inherits from `Staff`, adds `subject`, 
# and overrides `info()` to display all details.
#
# Input Format:
# name salary subject
#
# Output Format:
# Teacher Info: Name=<name>, Salary=<salary>, Subject=<subject>
#
# Example Input:
# Nusrat 42000 Mathematics
#
# Example Output:
# Teacher Info: Name=Nusrat, Salary=42000, Subject=Mathematics

class Person:
    def __init__(self, name):
        self.name = name
        
    def info(self):
        pass
    
class Staff(Person):
    def __init__(self, name, salary):
        super(). __init__(name)
        self.salary = salary
        
    def info(self):
        pass

class Teacher(Staff):
    def __init__(self, name, salary, subject):
        super().__init__(name, salary)
        self.subject = subject
        
    def info(self):
        print(f"Teacher Info: Name={self.name}, Salary={self.salary}, Subject={self.subject}")
        
try:
    name, salary, subject = input().split()
    salary = int(salary)
    
    obj = Teacher(name, salary, subject)
    obj.info()

except ValueError:
    print("Please input valid data")
