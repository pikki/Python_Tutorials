def mul_nums(*args):
    total = 1
    print(args)
    print(type(args))
    for i in args:
       total *= i
    return total

numbers = [2,3,4,5,6,7,8]

print(mul_nums(*numbers))



