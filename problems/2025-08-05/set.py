mySet = {1,5,6,3,1,3,6,6,3,5}

# print type of the set
print(type(mySet))

#count unique items
print(len(mySet))

#print the set
print(mySet)

#print item with using loop
for i in mySet:
    print(i)
    
# check if 5 in the set
print(5 in mySet)

set = {"shefa", "rifa"}
list = ["robiul", "shefaly"]

# #add one item to the set
set.add("rafsan")
print(set)

#update set with list items
set.update(list)
print(set)

# #join set with list using union
set = set.union(list)
print(set)

#remove item if exists (no error if not)
set.discard("Muntaha")
print(set)

#remove a random item
set.pop()
print(set)

#clear the set
set.clear()
print(set)

set1 = {1,2,3,4}
set2 = {3,4,5,6}

#get common items from both sets
result = set1.intersection(set2)
print(result)

#get items only in set1
result = set1.difference(set2)
print(result)

#get items not common in both sets
result = set1.symmetric_difference(set2)
print(result)

#update set1 with symmetric difference
set1.symmetric_difference_update(set2)
print(set1)