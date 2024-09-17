import ast, sys

input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

output = list(map(lambda x: x[::-1].upper(), input_list))

print(output)
