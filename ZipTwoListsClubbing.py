import ast, sys

input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
first_name = input_list[0]
last_name = input_list[1]

name = [i + ' ' + j for i, j in zip(first_name, last_name)]
print(name)
# print(name)
