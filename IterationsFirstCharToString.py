import ast, sys

input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
capitalized_list = []
for i in input_list:
    capitalized_list.append(i.capitalize())
print(capitalized_list)
