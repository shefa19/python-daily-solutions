# List of fruits
fruits = ["apple", "banana", "cherry"]

# Loop through the list of fruits
for i in fruits:
    print(i)

# Loop through each character of the string "banana"
for i in "banana":
    print(i)

# Loop through the list and stop when "banana" is found (break statement)
for i in fruits:
    if i == "banana":
        break
    print(i)

# Loop through the list and skip "banana" (continue statement)
for i in fruits:
    if i == "banana":
        continue
    print(i)

# Using range() from 0 to 5
for i in range(6):
    print(i)

# Using range() from 2 to 5
for i in range(2, 6):
    print(i)

# Using range() with a step value (2 to 20, step 3)
for i in range(2, 20, 3):
    print(i)

# Using for-else: else runs if the loop finishes without break
for i in range(6):
    print(i)
else:
    print("Finally Finished!")

# for-else with break: else will NOT execute
for i in range(6):
    if i == 3:
        break
    print(i)
else:
    print("Finally Finished!")  # This won't run because of the break

# Placeholder loop with pass (used for future code)
for i in [1, 2, 3]:
    pass
