import ast, sys

input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
x = int(input_list[0])
y = int(input_list[1])


def squared(a, b):
    return a ** b


# Write your code here

print(squared(x, y))
