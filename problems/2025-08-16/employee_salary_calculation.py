# Problem Name: Employee Salary Calculation
# -------------------------------------------------------
# Description:
# Create a class `Person` with attributes `name` and `id`.
# Create a subclass `Employee` that inherits from `Person` and adds 
# `department` and `basic_salary`.
# Create a subclass `Manager` that inherits from `Employee` and has 
# an attribute `bonus_percent`. 
# Add a method `net_salary()` that calculates basic_salary after bonus.
#
# Input Format:
# name id department basic_salary bonus_percent
#
# Output Format:
# ID: <id>, Name: <name>, Dept: <department>, Net Salary: <net_salary>
#
# Example Input:
# Sadia E102 HR 50000 10
#
# Example Output:
# ID: E102, Name: Sadia, Dept: HR, Net Salary: 55000.00

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
class Employee(Person):
    def __init__(self, name, id, department, basic_salary):
        super().__init__(name, id)
        self.department = department
        self.basic_salary = basic_salary
        
class Manager(Employee):
    def __init__(self, name, id, department, basic_salary, bonus_percent):
        super().__init__(name, id, department, basic_salary)
        self.bonus_percent = bonus_percent
        
    def net_salary(self):
        return self.basic_salary + ((self.basic_salary * self.bonus_percent) / 100)
        
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Dept: {self.department}, Net Salary: {self.net_salary()}"
    

try:
    name, id, department, basic_salary, bonus_percent = input().split()
    basic_salary = int(basic_salary)
    bonus_percent = int(bonus_percent)
    
    obj = Manager(name, id, department, basic_salary, bonus_percent)
    print(obj)
    
except ValueError:
    print("Please enter valid data")