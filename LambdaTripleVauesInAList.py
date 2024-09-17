import ast, sys

input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

greater = list(map(lambda x: x * 3, input_list))

print(greater)
