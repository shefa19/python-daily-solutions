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
