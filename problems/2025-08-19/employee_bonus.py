# Problem 4: Employee Bonus
# -------------------------------------------------------
# Description:
# Create a base class `Employee` with a method `bonus()`.
# Create subclasses `Manager`, `Developer`, and `Intern` that override `bonus()`
# to return different percentages of salary as bonus.
# Demonstrate polymorphism by calculating bonuses for different employees.
#
# Input Format:
# role salary
# (role = manager/developer/intern)
#
# Output Format:
# Print the bonus amount.
#
# Example Input:
# developer 40000
#
# Example Output:
# Bonus: 8000

class Employee:
    def __init__(self, salary):
        self.salary = salary
        
    def bonus(self):
        pass

class Manager(Employee):
    def __init__(self, salary):
        super().__init__(salary)
        
    def bonus(self):
        return self.salary * 25 // 100
        

class Developer(Employee):
    def __init__(self, salary):
        super().__init__(salary)
        
    def bonus(self):
        return self.salary * 20 // 100
        

class Intern(Employee):
    def __init__(self, salary):
        super().__init__(salary)
        
    def bonus(self):
        return self.salary * 10 // 100
    

try:
    role, salary = input("Enter role and salary: ").split()
    salary = int(salary)

    if not role.isalpha():
        print("Please enter valid role.")
    else:
        obj = None
        match role.lower():
            case "manager":
                obj = Manager(salary)
            case "developer":
                obj = Developer(salary)
            case "intern":
                obj = Intern(salary)
            case _:
                print("Unknown role")

except ValueError:
    print("Please enter valid value.")

if obj:
    print(f"Bonus: {obj.bonus()}")
