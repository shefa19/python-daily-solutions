# Problem Name: Remove Extra Spaces
# Description:
#   Given a string, that may contain extra spaces at the beginning, between words,
#   or at the end, remove all extra spaces so that only single spaces remain between words.


sentence = input("Enter a sentence: ")

print(" ".join(sentence.split()))