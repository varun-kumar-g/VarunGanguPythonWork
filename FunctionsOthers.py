def func1(x, y=1):
    z = x * y + x + y
    return z


print(func1(2, func1(3)))


# def func2(x, y):
#     z = x * y + x + y
#     return z
#
#
# print(func2(2, func2(3)))

def func3(x=1, y=2):
    z = x * y + x + y
    return z

print(func3(2, func3(3)))
