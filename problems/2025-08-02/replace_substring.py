# Problem Name: Replace Substring
# Description: Given a sentence sentence, replace all occurrences of the word "Python" with "Java".

sentence = input("Enter a sentence: ").strip()

if "Python" in sentence:
    sentence = sentence.replace("Python","Java")
if "python" in sentence:
    sentence = sentence.replace("python","java")
    
print(sentence)


