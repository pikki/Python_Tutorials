# kwargs -> Keyword Arguments
# *args
# **kwargs

def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
    # {"a":1, "b":2}
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    # print(kwargs['a']["name"])

# func(a={'name': "Kaustubh Wankhede Arguments"}, b=2)
func(a = 1 , b = 2)

data = {'a': 1, 'b': 2}

func(**data)


