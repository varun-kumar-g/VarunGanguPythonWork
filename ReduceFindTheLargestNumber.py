import ast, sys

input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
from functools import reduce

output_list = reduce(lambda x, y: x if x > y else y, input_list)

print(output_list)
