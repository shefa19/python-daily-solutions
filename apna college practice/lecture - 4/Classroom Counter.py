#  You are given a list of subjects for students. Assume one classroom is required for 1
#  subject. How many classrooms are needed by all students.
#  ”python”, “java”, “C++”, “python”, “javascript”, “java”, “python”, “java”, “C++”, “C


subject = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]

my_set = set(subject)
classroom_count = len(my_set)

print("Total classrooms needed:", classroom_count)

