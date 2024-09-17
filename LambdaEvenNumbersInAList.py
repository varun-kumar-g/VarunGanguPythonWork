import ast, sys

input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

output_list = [c for c in input_list if c % 2 == 0]
print(output_list)
