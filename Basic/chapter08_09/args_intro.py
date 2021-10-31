# def add_num(a,b) :
#     return a+b
#
#
# print(add_num(2,3,6,7,8))

def add_ints(*args):
    total = 0
    print(args[2])
    print(type(args))
    print(args)
    for arg in args:
        total += arg
    return total

print(add_ints(1,2,3,4,5,6,7,8,9,10))