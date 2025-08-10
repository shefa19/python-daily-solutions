# Problem Name: Reverse a String
# Description: Reverse a given string using a for loop and print it.

S = input("Enter a single string: ").strip()

if not S.isalpha():
    print("Invalid input.Please enter a single string.")
else:
    n = len(S)
    reverse_S = ""
    j = -1
    for i in range(n):
        reverse_S += S[j]
        j -= 1
    print(reverse_S)  