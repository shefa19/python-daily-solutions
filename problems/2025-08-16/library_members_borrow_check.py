# Problem Name: Library Members Borrow Check
# -------------------------------------------------------
# Description:
# Create a class `Person`.
# Create a subclass `Member` that inherits from `Person` and has `member_id`, `join_year`.
# Create another subclass `StudentMember` that inherits from `Member` and has 
# `course_name` and `borrow_limit`.
# Add a method `can_borrow(requested_books)` that returns True or False.
#
# Input Format:
# name member_id join_year course_name borrow_limit requested_books
#
# Output Format:
# Member <member_id> (<name>) can borrow <requested_books>: <True/False>
#
# Example Input:
# Arif M301 2023 CSE 3 2
#
# Example Output:
# Member M301 (Arif) can borrow 2: True
class Person:
    pass

class Member(Person):
    def __init__(self, member_id, join_year):
        super().__init__()
        self.member_id = member_id
        self.join_year = join_year
        
class StudentMember(Member):
    def __init__(self,name, member_id, join_year, course_name, borrow_limit, requested_books):
        super().__init__(member_id, join_year)
        self.name = name
        self.course_name = course_name
        self.borrow_limit = borrow_limit
        self.requested_books = requested_books
        
    def can_borrow(self):
        return self.requested_books <= self.borrow_limit
    
    def __str__(self):
        return f"Member {self.member_id} ({self.name}) can borrow {self.requested_books}: {self.can_borrow()}"
    

try:
    name, member_id, join_year, course_name, borrow_limit, requested_books = input().split()
    borrow_limit = int(borrow_limit)
    requested_books = int(requested_books)
    
    if not name.isalpha() or not course_name.isalpha():
        print("Please enter string")
    else:
        obj = StudentMember(name, member_id, join_year, course_name, borrow_limit, requested_books)
        print(obj)
    
except ValueError:
    print("Please insert valid data.")