def mul_nums(first_name, last_name, *args):
    total = 1
    print(args)
    print(type(args))
    for i in args:
       total *= i
    return total

print(mul_nums(1,2,3,4))

