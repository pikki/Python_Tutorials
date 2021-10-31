# Sets are unordered collection of unique elements.
# They are declared using curly brackets.
# Sets are not at all dynamic.
# We can store data types not data structures.

#set1 = {1,2,3,[5,6,7]}
# print(set1)
dict1 = {
    "names": ["alan", "mark"]
}

mylist = ['a','a','b','c']
# 'c','a','b'

set1 = {1,2,3,4,5,6,7}

# set1[2]


list1 = [1,2,3,3,4,5,5,6,7,8,9]

list2 = []
for i in list1 :
    if i not in list2:
        list2.append(i)
print(list2)


print(list(set(list1)))

set2 = {3,4,5,6,7}

set2.add(1)
set2.add(3)

print(set2)

set2.remove(6)
print(set2)
set2.discard(7)
print(set2)

set2.discard(10)
print(set2)

set3 = set2.copy()
# set2.clear()


