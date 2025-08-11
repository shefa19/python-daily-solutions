# Problem Name: Is Palindrome
# Description:
#   Write a function is_palindrome(s) that takes a string s and returns whether it is a palindrome.
#   In the main part, take a string input, call is_palindrome, and print "YES" or "NO".
#   The check should be case-insensitive.


s = input("Enter a single string: ").strip()

if not s.isalpha():
    print("Invalid input. Plese enter a correct string.")
else:
    s = s.lower()
    if s == s[::-1]:
        print("YES")
    else:
        print("NO")