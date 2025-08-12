# Problem Name: Palindrome Checker
# Description:
#   Given a string txt, check if it is a palindrome.
#   Print "Yes" if it is, otherwise print "No".

txt = input("Enter a string: ").strip()
txt = txt.lower()

if txt == txt[::-1]:
    print("Yes")
else:
    print("No")
