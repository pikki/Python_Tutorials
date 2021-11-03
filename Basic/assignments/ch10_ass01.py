# Print a list :
# [[1,2,3],[1,2,3],[1,2,3]]
#
# l = list([i for i in range(1,4)])
# print(l[1])
# for i in range(1,3):
#     l[i] = l
# print(l)
#
list1 = []
for i in range(3):
    list1.append([1,2,3])
print(list1)

print([[i for i in range(1,4)] for i in range(3)])
