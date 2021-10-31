m = list(range(1,11))

# print(m)
#
# even_nums = []
# for i in range(1,11) :
#     if i % 2 == 0 :
#         even_nums.append(i)
# print(even_nums)
#
#
# print([i for i in m if i % 2 == 0])
#
# # List Comprehension Syntax : [append thing   loop   if condition]
#
# print([i**2 for i in range(1,100)])
#
# squares = []
# for i in range(1,101):
#     squares.append(i**2)
# print(squares)


#print([i for i in range(-1,-101,-1)])

# for i in range(0,5):
#     print(-i)

names = "kaustubh", "alan", "mark", "simone"

print([i[0] for i in names])